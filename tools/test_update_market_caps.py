"""Offline checks for currency conversion and safe market-cap updates."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

from update_market_caps import fetch_snapshot, update_characters, write_json_atomic


class MarketCapTests(unittest.TestCase):
    def test_usd_quote_is_not_converted(self):
        ticker = Mock(return_value=Mock(get_info=Mock(return_value={
            "symbol": "INTC", "marketCap": 100, "currency": "USD", "regularMarketTime": 1,
        })))
        result = fetch_snapshot("INTC", ticker, {}, "now")
        self.assertEqual(result["marketCapUsd"], 100)
        self.assertEqual(result["marketCapQuote"]["usdExchangeRate"], 1)
        ticker.assert_called_once_with("INTC")

    def test_foreign_quotes_share_a_cached_usd_rate(self):
        closes = Mock()
        closes.empty = False
        closes.iloc = {-1: 0.001}
        closes.index = {-1: datetime(2026, 11, 6, tzinfo=timezone.utc)}
        column = Mock()
        column.dropna.return_value = closes
        tickers = {
            "005930.KS": Mock(get_info=Mock(return_value={"symbol": "005930.KS", "marketCap": 900000, "currency": "KRW"})),
            "000660.KS": Mock(get_info=Mock(return_value={"symbol": "000660.KS", "marketCap": 500000, "currency": "KRW"})),
            "KRWUSD=X": Mock(history=Mock(return_value={"Close": column})),
        }
        factory = Mock(side_effect=tickers.__getitem__)
        cache = {}
        self.assertEqual(fetch_snapshot("005930.KS", factory, cache, "now")["marketCapUsd"], 900)
        self.assertEqual(fetch_snapshot("000660.KS", factory, cache, "now")["marketCapUsd"], 500)
        tickers["KRWUSD=X"].history.assert_called_once()

    def test_failure_preserves_last_good_value_and_timestamp(self):
        data = {"characters": [{"name": "Intel", "sort": {
            "yahooSymbol": "INTC", "marketCapUsd": 123, "marketCapUpdatedAt": "yesterday",
        }}, {"name": "Private company", "sort": {"yahooSymbol": None, "marketCapUsd": None}}]}
        before = copy.deepcopy(data)
        factory = Mock(side_effect=RuntimeError("Yahoo unavailable"))
        self.assertEqual(update_characters(data, factory, retries=0, delay=0), (0, ["INTC"]))
        self.assertEqual(data, before)
        factory.assert_called_once_with("INTC")

    def test_invalid_quotes_do_not_become_zero_market_caps(self):
        for amount in [None, 0, -5, float("nan"), float("inf"), True]:
            with self.subTest(amount=amount):
                factory = Mock(return_value=Mock(get_info=Mock(return_value={
                    "symbol": "INTC", "currency": "USD", "marketCap": amount,
                })))
                with self.assertRaises(ValueError):
                    fetch_snapshot("INTC", factory, {}, "now")

    def test_unlisted_estimates_survive_public_quote_updates(self):
        estimate = {"yahooSymbol": None, "marketCapUsd": 250000000000,
                    "marketCapBasis": "acquisition_price", "marketCapUpdatedAt": "previous check",
                    "valuationEstimate": {"eventDate": "2026-02-02", "source": "https://example.com/deal"}}
        data = {"characters": [{"sort": copy.deepcopy(estimate)}, {"sort": {"yahooSymbol": "INTC"}}]}
        factory = Mock(return_value=Mock(get_info=Mock(return_value={
            "symbol": "INTC", "marketCap": 100, "currency": "USD",
        })))
        self.assertEqual(update_characters(data, factory, retries=0, delay=0), (1, []))
        self.assertEqual(data["characters"][0]["sort"], estimate)
        self.assertEqual(data["characters"][1]["sort"]["marketCapBasis"], "public_market_cap")
        factory.assert_called_once_with("INTC")

    def test_atomic_write_preserves_metadata_and_leaves_no_temp_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "characters.json"
            data = {"characters": [{"name": "Intel", "sort": {"curatedOrder": 1, "foundedYear": 1968}}]}
            write_json_atomic(path, data)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), data)
            self.assertEqual([p.name for p in path.parent.iterdir()], ["characters.json"])


if __name__ == "__main__":
    unittest.main()
