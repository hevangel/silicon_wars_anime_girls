"""Refresh character sorting metadata from Yahoo Finance using yfinance.

Install: python -m pip install -r tools/requirements-market-cap.txt
Run:     python tools/update_market_caps.py
"""
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "website" / "data" / "characters.json"


def positive_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def fetch_snapshot(symbol, ticker_factory, fx_cache, fetched_at):
    info = ticker_factory(symbol).get_info()
    amount = info.get("marketCap")
    currency = info.get("currency")
    if not positive_number(amount) or not isinstance(currency, str) or len(currency) != 3:
        raise ValueError(f"{symbol}: missing valid marketCap/currency")
    if info.get("symbol", "").upper() != symbol.upper():
        raise ValueError(f"{symbol}: Yahoo returned an unexpected symbol")
    currency = currency.upper()
    rate, rate_date = 1.0, None
    if currency != "USD":
        if currency not in fx_cache:
            history = ticker_factory(f"{currency}USD=X").history(period="5d", auto_adjust=False)
            closes = history["Close"].dropna()
            if closes.empty or not positive_number(float(closes.iloc[-1])):
                raise ValueError(f"{currency}: no valid USD exchange rate")
            fx_cache[currency] = (float(closes.iloc[-1]), closes.index[-1].isoformat())
        rate, rate_date = fx_cache[currency]
    usd = amount * rate
    if not positive_number(usd):
        raise ValueError(f"{symbol}: invalid converted market cap")
    market_time = info.get("regularMarketTime")
    return {
        "marketCapUsd": round(usd),
        "marketCapBasis": "public_market_cap",
        "marketCapUpdatedAt": fetched_at,
        "marketCapQuote": {
            "amount": amount,
            "currency": currency,
            "usdExchangeRate": rate,
            "exchangeRateDate": rate_date,
            "marketTime": datetime.fromtimestamp(market_time, timezone.utc).isoformat() if positive_number(market_time) else None,
            "source": f"https://finance.yahoo.com/quote/{symbol}/",
        },
    }


def update_characters(data, ticker_factory, symbols=None, retries=2, delay=0.5):
    """Update public quotes; preserve unlisted estimates and failed snapshots."""
    fx_cache = {}
    updated = 0
    failures = []
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for character in data["characters"]:
        metadata = character.get("sort", {})
        symbol = metadata.get("yahooSymbol")
        if not symbol or (symbols and symbol not in symbols):
            continue
        for attempt in range(retries + 1):
            try:
                snapshot = fetch_snapshot(symbol, ticker_factory, fx_cache, fetched_at)
                metadata.update(snapshot)
                updated += 1
                print(f"{symbol}: USD {snapshot['marketCapUsd']:,}", flush=True)
                break
            except Exception as error:
                if attempt == retries:
                    failures.append(symbol)
                    print(f"{symbol}: retained previous data ({error})", file=sys.stderr, flush=True)
                else:
                    time.sleep(min(2 ** attempt, 8))
        if delay:
            time.sleep(delay)
    return updated, failures


def write_json_atomic(path, data):
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, suffix=".tmp", delete=False) as temporary:
            temporary_path = Path(temporary.name)
            json.dump(data, temporary, indent=2, ensure_ascii=False, allow_nan=False)
            temporary.write("\n")
        os.replace(temporary_path, path)
    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--symbols", nargs="+", help="Update only these configured Yahoo symbols")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report without writing JSON")
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between companies")
    args = parser.parse_args()
    if args.retries < 0 or not math.isfinite(args.delay) or args.delay < 0:
        parser.error("retries and delay must be nonnegative")
    try:
        import yfinance as yf
    except ImportError:
        parser.error("Install dependencies: python -m pip install -r tools/requirements-market-cap.txt")
    data = json.loads(args.data.read_text(encoding="utf-8"))
    if args.symbols:
        configured = {c.get("sort", {}).get("yahooSymbol") for c in data["characters"]}
        unknown = set(args.symbols) - configured
        if unknown:
            parser.error(f"Unconfigured symbols: {', '.join(sorted(unknown))}")
    # Keep Yahoo's cookie/timezone SQLite caches writable, including in sandboxes.
    cache = Path(tempfile.gettempdir()) / "silicon-wars-yahoo-cache"
    cache.mkdir(parents=True, exist_ok=True)
    yf.set_tz_cache_location(str(cache))
    updated, failures = update_characters(data, yf.Ticker, set(args.symbols or []), args.retries, args.delay)
    if updated and not args.dry_run:
        write_json_atomic(args.data, data)
    print(f"Updated {updated}; failed {len(failures)}; " + ("dry run, no file changes" if args.dry_run else str(args.data)))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
