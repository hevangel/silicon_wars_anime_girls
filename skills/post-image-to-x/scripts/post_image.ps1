<#
.SYNOPSIS
    Posts an image with optional text to X (Twitter) using playwright-cli.

.DESCRIPTION
    Automates opening an X session, attaching an image, inputting tweet text,
    verifying preview, and publishing via playwright-cli.

.PARAMETER ImagePath
    Path to the image file to upload (.png, .jpg, .jpeg, .webp, .gif).

.PARAMETER Text
    Optional tweet/post copy to include with the image.

.PARAMETER Session
    Name of the playwright-cli browser session (default: "x-poster").

.PARAMETER ProfileDir
    Path to a persistent user profile directory. Defaults to "$HOME\.playwright-x-profile".

.PARAMETER StateFile
    Path to a storage state JSON file exported with state-save.

.PARAMETER Headed
    Run browser in headed mode (useful for first-time login or debugging).

.PARAMETER DryRun
    Prepares post and takes a preview screenshot, but skips clicking "Post".

.EXAMPLE
    .\post_image.ps1 -ImagePath ".\c01_p01.png" -Text "Silicon Wars Chapter 1 preview!"

.EXAMPLE
    .\post_image.ps1 -ImagePath ".\poster.png" -Headed -DryRun
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$ImagePath,

    [Parameter(Mandatory = $false)]
    [string]$Text = "",

    [Parameter(Mandatory = $false)]
    [string]$Session = "x-poster",

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

# 1. Validate image path
if (-not (Test-Path -Path $ImagePath)) {
    Write-Error "Image file not found: $ImagePath"
    exit 1
}
$AbsoluteImagePath = (Resolve-Path -Path $ImagePath).ProviderPath
Write-Host "[1/7] Target image resolved: $AbsoluteImagePath" -ForegroundColor Cyan

# 2. Verify playwright-cli is available
if (-not (Get-Command "playwright-cli" -ErrorAction SilentlyContinue)) {
    Write-Error "'playwright-cli' is not found in PATH. Install with: npm install -g @playwright/cli"
    exit 1
}

# 3. Build open command
$openArgs = @("-s=$Session", "open", "https://x.com/compose/post")
if ($Headed) {
    $openArgs += "--headed"
}
if ($ProfileDir) {
    $openArgs += "--persistent"
    $openArgs += "--profile=$ProfileDir"
}

Write-Host "[2/7] Opening browser session '$Session' at https://x.com/compose/post..." -ForegroundColor Cyan
& playwright-cli @openArgs

# If StateFile is specified, load authentication state
if ($StateFile -and (Test-Path $StateFile)) {
    Write-Host "Loading storage state from $StateFile..." -ForegroundColor Cyan
    & playwright-cli "-s=$Session" state-load (Resolve-Path $StateFile).ProviderPath
    & playwright-cli "-s=$Session" goto "https://x.com/compose/post"
}

Start-Sleep -Seconds 2

# 4. Upload Image
Write-Host "[3/7] Uploading image..." -ForegroundColor Cyan
& playwright-cli "-s=$Session" upload "$AbsoluteImagePath"

Start-Sleep -Seconds 2

# 5. Enter Post Text if provided
if (-not [string]::IsNullOrWhiteSpace($Text)) {
    Write-Host "[4/7] Entering post text..." -ForegroundColor Cyan
    & playwright-cli "-s=$Session" click '[data-testid="tweetTextarea_0"]'
    & playwright-cli "-s=$Session" type "$Text"
} else {
    Write-Host "[4/7] No post text specified. Proceeding with media only." -ForegroundColor Yellow
}

Start-Sleep -Seconds 1

# 6. Preview Screenshot
Write-Host "[5/7] Capturing preview screenshot..." -ForegroundColor Cyan
& playwright-cli "-s=$Session" screenshot

if ($DryRun) {
    Write-Host "[DRY RUN] Skipping post submission. Review screenshot or headed window." -ForegroundColor Yellow
    Write-Host "Session remains open as '$Session'. Run 'playwright-cli -s=$Session close' when done."
    exit 0
}

# 7. Click Post Button
Write-Host "[6/7] Clicking Post button..." -ForegroundColor Cyan
& playwright-cli "-s=$Session" click '[data-testid="tweetButton"]'

Start-Sleep -Seconds 3

# 8. Verification & Cleanup
Write-Host "[7/7] Verifying submission..." -ForegroundColor Cyan
& playwright-cli "-s=$Session" snapshot

Write-Host "Post action complete! Closing browser session..." -ForegroundColor Green
& playwright-cli "-s=$Session" close
