<#
.SYNOPSIS
    Posts one or more images with optional text to X (Twitter) using playwright-cli.

.DESCRIPTION
    Automates opening an X session, attaching up to 20 images, inputting tweet text,
    verifying preview, clicking Post, and closing the session cleanly.

.PARAMETER ImagePath
    Path(s) to the image file(s) to upload (.png, .jpg, .jpeg, .webp, .gif).

.PARAMETER Text
    Optional tweet/post copy to include with the image(s).

.PARAMETER Session
    Name of the playwright-cli browser session (default: "x").

.PARAMETER ProfileDir
    Path to a persistent user profile directory. Defaults to "$env:USERPROFILE\.playwright-x-profile".

.PARAMETER StateFile
    Path to a storage state JSON file exported with state-save.

.PARAMETER Headed
    Run browser in headed mode (useful for first-time login or debugging).

.PARAMETER DryRun
    Prepares post and takes a preview screenshot, but skips clicking "Post".

.EXAMPLE
    .\post_image.ps1 -ImagePath ".\c01_p01.png" -Text "Silicon Wars preview! #what_if_ai_companies_are_anime_girls"

.EXAMPLE
    .\post_image.ps1 -ImagePath @(".\ms.png", ".\arm.jpg", ".\tsmc.webp", ".\bc.webp") -Text "Day 2: Paper Collage — Microsoft, ARM, TSMC & Broadcom #what_if_ai_companies_are_anime_girls"
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string[]]$ImagePath,

    [Parameter(Mandatory = $false)]
    [string]$Text = "",

    [Parameter(Mandatory = $false)]
    [string]$Session = "x",

    [Parameter(Mandatory = $false)]
    [string]$ProfileDir = "$env:USERPROFILE\.playwright-x-profile",

    [Parameter(Mandatory = $false)]
    [string]$StateFile = "",

    [Parameter(Mandatory = $false)]
    [switch]$Headed,

    [Parameter(Mandatory = $false)]
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# 1. Validate and resolve all image paths
$AbsoluteImagePaths = @()
foreach ($p in $ImagePath) {
    if (-not (Test-Path -Path $p)) {
        Write-Error "Image file not found: $p"
        exit 1
    }
    $AbsoluteImagePaths += (Resolve-Path -Path $p).ProviderPath
}
Write-Host "[1/6] Resolved $($AbsoluteImagePaths.Count) image(s)." -ForegroundColor Cyan

# 2. Verify playwright-cli is available
if (-not (Get-Command "playwright-cli" -ErrorAction SilentlyContinue)) {
    Write-Error "'playwright-cli' is not found in PATH. Install with: npm install -g @playwright/cli"
    exit 1
}

# 3. Open browser session
$openArgs = @("-s=$Session", "open", "https://x.com/compose/post")
if ($Headed) {
    $openArgs += "--headed"
}
if ($ProfileDir) {
    $openArgs += "--persistent"
    $openArgs += "--profile=$ProfileDir"
}

Write-Host "[2/6] Opening browser session '$Session' at https://x.com/compose/post..." -ForegroundColor Cyan
& playwright-cli @openArgs

if ($StateFile -and (Test-Path $StateFile)) {
    Write-Host "Loading storage state from $StateFile..." -ForegroundColor Cyan
    & playwright-cli "-s=$Session" state-load (Resolve-Path $StateFile).ProviderPath
    & playwright-cli "-s=$Session" goto "https://x.com/compose/post"
}

# 4. Generate temporary Playwright script (avoids PowerShell inline quoting issues)
$imgsJson = ConvertTo-Json -InputObject @($AbsoluteImagePaths) -Compress
$textJson = ConvertTo-Json -InputObject $Text -Compress
$dryRunJs = if ($DryRun) { "true" } else { "false" }

$jsContent = @"
async (page) => {
  await page.waitForTimeout(3000);
  const currentUrl = page.url();
  if (currentUrl.includes('login') || currentUrl.includes('onboarding')) {
    throw new Error('AUTH_REQUIRED: Redirected to ' + currentUrl + '. Run with -Headed and sign in first.');
  }

  const modal = page.locator('[role="dialog"]').filter({ has: page.locator('[data-testid="tweetTextarea_0"]') }).last();
  await modal.waitFor({ state: 'visible', timeout: 15000 });

  const fileInput = modal.locator('input[data-testid="fileInput"]').first();
  await fileInput.setInputFiles($imgsJson);

  const text = $textJson;
  const textarea = modal.locator('[data-testid="tweetTextarea_0"]').first();
  if (text && text.trim().length > 0) {
    await textarea.click();
    await textarea.fill(text);
  }

  const postBtn = modal.locator('[data-testid="tweetButton"]').first();
  await postBtn.waitFor({ state: 'visible', timeout: 15000 });
  for (let i = 0; i < 30; i++) {
    const disabled = await postBtn.getAttribute('aria-disabled');
    if (!disabled || disabled === 'false') break;
    await page.waitForTimeout(1000);
  }

  if ($dryRunJs) {
    return { dryRun: true, url: page.url() };
  }

  await postBtn.click({ force: true });
  await page.waitForTimeout(3000);
  if (await postBtn.isVisible().catch(() => false)) {
    await textarea.focus();
    await page.keyboard.press('Control+Enter');
    await page.waitForTimeout(4000);
  }

  const afterUrl = page.url();
  const statusLinks = await page.locator('a[href*="/status/"]').evaluateAll(
    els => els.slice(0, 5).map(e => e.href)
  );
  return { ok: true, afterUrl, statusLinks };
}
"@

$tempJs = Join-Path $env:TEMP ("post_x_" + [guid]::NewGuid().ToString("N") + ".js")
Set-Content -Path $tempJs -Value $jsContent -Encoding UTF8

try {
    Write-Host "[3/6] Uploading media, entering text, and submitting..." -ForegroundColor Cyan
    & playwright-cli "-s=$Session" run-code "--filename=$tempJs"

    Write-Host "[4/6] Capturing screenshot..." -ForegroundColor Cyan
    & playwright-cli "-s=$Session" screenshot

    if ($DryRun) {
        Write-Host "[DRY RUN] Skipped clicking Post. Session '$Session' left open for inspection." -ForegroundColor Yellow
        exit 0
    }

    Write-Host "[5/6] Post submitted! Closing browser session..." -ForegroundColor Green
    & playwright-cli "-s=$Session" close
}
finally {
    if (Test-Path $tempJs) {
        Remove-Item $tempJs -Force -ErrorAction SilentlyContinue
    }
}
