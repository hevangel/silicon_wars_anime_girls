---
name: post-image-to-x
description: >-
  Post tweets with images or character art to X (formerly Twitter) using playwright-cli browser automation. Use this skill when asked to share, publish, tweet, or upload images, artwork, posters, or comic panels to X/Twitter with custom text, handle persistent authentication sessions, or verify post publication.
---

# Post Image to X (Twitter) with playwright-cli

This skill guides you through automating post creation and image uploads to X (Twitter) using `playwright-cli`.

## Table of Contents
1. [Prerequisites & Authentication](#prerequisites--authentication)
2. [Step-by-Step Interactive Workflow](#step-by-step-interactive-workflow)
3. [Automated Helper Script](#automated-helper-script)
4. [Selectors and UI Elements](#selectors-and-ui-elements)
5. [Troubleshooting & Best Practices](#troubleshooting--best-practices)

---

## Prerequisites & Authentication

`playwright-cli` is a terminal utility for Playwright browser automation.

X requires an active login session before allowing a user to compose posts. Choose one of the following session strategies:

### Strategy A: Persistent Profile (Recommended for Repeated Use)
Store the browser session directory locally so login cookies, tokens, and storage state persist across runs:
```powershell
playwright-cli -s=x open https://x.com --persistent --profile="$env:USERPROFILE\.playwright-x-profile"
```

### Strategy B: Storage State Export/Import (`state-save` / `state-load`)
If you already logged in once, save the session state:
```powershell
playwright-cli -s=x state-save "$env:USERPROFILE\.x-auth-state.json"
```
And restore it in new sessions:
```powershell
playwright-cli -s=x open https://x.com
playwright-cli -s=x state-load "$env:USERPROFILE\.x-auth-state.json"
playwright-cli -s=x goto https://x.com/compose/post
```

### Strategy C: One-Time Headed Interactive Login
If the user is not logged in:
1. Launch headed browser:
   ```powershell
   playwright-cli -s=x open https://x.com/login --headed
   ```
2. Ask the user to complete login (including 2FA if prompted) in the opened browser window.
3. Once logged in, save the state with `playwright-cli -s=x state-save` for future headless runs.

---

## Step-by-Step Interactive Workflow

Follow these steps when driving `playwright-cli` manually or in conversation:

### 1. Launch Browser Session and Navigate
Start a session (e.g., `-s=x`) with the persistent profile:
```powershell
playwright-cli -s=x open https://x.com/compose/post --persistent --profile="$env:USERPROFILE\.playwright-x-profile"
```

### 2. Verify Session State (Logged In Check)
Take a snapshot to inspect page elements:
```powershell
playwright-cli -s=x snapshot
```
- **If logged in**: You will see the tweet composer with textarea `[data-testid="tweetTextarea_0"]` or role `textbox` "Post text".
- **If redirected to login**: Pause and run the headed login flow described in [Prerequisites](#strategy-c-one-time-headed-interactive-login).

### 3. Upload Image(s)
Pass the absolute path to the image file:
```powershell
playwright-cli -s=x upload "B:\silicon_wars_anime_girls\characters\triad\renders\accepted\c01_p01_v02.png"
```
Verify the image attached successfully by taking a snapshot:
```powershell
playwright-cli -s=x snapshot
```
Look for `[data-testid="attachments"]` or an image container element in the composer.

### 4. Input Post Text
Focus the composer textarea and type your message:
```powershell
playwright-cli -s=x click '[data-testid="tweetTextarea_0"]'
playwright-cli -s=x type "Check out the latest character reveal from Silicon Wars! #SiliconWars #Anime #SciFi"
```

> [!NOTE]
> If your text contains multiple lines, special characters, or hashtags, you can also use `fill` or `run-code`:
> ```powershell
> playwright-cli -s=x run-code "async (page) => { await page.locator('[data-testid=\"tweetTextarea_0\"]').fill('Multi-line\nPost text here'); }"
> ```

### 5. Verification & Review
Always verify the preview before publishing:
```powershell
playwright-cli -s=x screenshot
```
Review the screenshot to ensure:
- The image loaded without truncation or upload errors.
- The text copy and tags are formatted correctly.
- Sensitive content flags or audience options match expectations.

### 6. Publish the Post
Click the "Post" button:
```powershell
playwright-cli -s=x click '[data-testid="tweetButton"]'
```

### 7. Confirm Publication & Close
Wait 2-3 seconds, then take a snapshot:
```powershell
playwright-cli -s=x snapshot
```
The compose modal will be closed, or a toast notification ("Your post was sent") will appear.

Save session state (optional) and close the browser:
```powershell
playwright-cli -s=x state-save "$env:USERPROFILE\.x-auth-state.json"
playwright-cli -s=x close
```

---

## Automated Helper Script

A ready-to-run helper script is included in `./scripts/post_image.ps1`.

### Usage Example:
```powershell
# Basic usage with image and text
.\skills\post-image-to-x\scripts\post_image.ps1 -ImagePath "B:\silicon_wars_anime_girls\characters\triad\renders\accepted\poster.png" -Text "Silicon Wars Chapter 1 poster reveal!"

# Interactive login mode (opens headed browser for login, then posts)
.\skills\post-image-to-x\scripts\post_image.ps1 -ImagePath "B:\path\to\art.png" -Text "New character art" -Headed

# Dry run mode (prepares post and takes screenshot without clicking Post)
.\skills\post-image-to-x\scripts\post_image.ps1 -ImagePath "B:\path\to\art.png" -Text "Preview test" -DryRun
```

---

## Selectors and UI Elements

For detailed element locators, test IDs, and fallback selectors, see [references/x_ui_selectors.md](./references/x_ui_selectors.md).

Key selectors:
- **Tweet Text Box**: `[data-testid="tweetTextarea_0"]` or `div[role="textbox"][data-testid="tweetTextarea_0"]`
- **File Input**: `input[data-testid="fileInput"][type="file"]`
- **Post Button**: `[data-testid="tweetButton"]` or `[data-testid="tweetButtonInline"]`
- **Media Preview**: `[data-testid="attachments"]`
- **Add Description / Alt Text Button**: `[data-testid="altTextButton"]` or `button:has-text("Add description")`

---

## Troubleshooting & Best Practices

1. **Upload Hangs / Spinner**:
   - Ensure the image format is supported (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`).
   - Standard image size limit is 5MB for photos on web (up to 15MB for GIFs).
2. **Post Button Remains Disabled**:
   - The button might be disabled while an image upload/compression is still processing.
   - Wait 1-2 seconds and check `playwright-cli -s=x snapshot` to ensure the media attachment has finished loading.
3. **Bot / Verification Challenges**:
   - If X presents an Arkose/CAPTCHA challenge, do NOT attempt to solve it via automated clicks.
   - Launch headed browser (`--headed`) and ask the user to complete verification manually in the browser window.
4. **Session Cleanup**:
   - If an existing session gets stuck:
     ```powershell
     playwright-cli kill-all
     ```
