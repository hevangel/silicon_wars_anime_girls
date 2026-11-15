# X (Twitter) UI Selectors Reference

This document catalogs the DOM selectors, test IDs, and accessibility attributes for X's web interface used by `playwright-cli`.

## Composer Elements

| Element | Primary Selector (`data-testid`) | Fallback CSS / Role Selector | Notes |
| :--- | :--- | :--- | :--- |
| **Compose Modal Textarea** | `[data-testid="tweetTextarea_0"]` | `div[role="textbox"][contenteditable="true"]` | Primary input for post copy |
| **Inline Home Feed Textarea** | `[data-testid="tweetTextarea_0_Inline"]` | `div[role="textbox"]` | When composing from `/home` without opening modal |
| **File / Media Input** | `input[data-testid="fileInput"]` | `input[type="file"][accept*="image"]` | Hidden input used for file uploads |
| **Media Attachments Container** | `[data-testid="attachments"]` | `div[aria-label="Media"]` | Contains uploaded image cards |
| **Remove Attachment Button** | `[data-testid="removeMedia"]` | `button[aria-label="Remove media"]` | Clears an attached image |
| **Alt Text / Tag Button** | `[data-testid="altTextButton"]` | `button:has-text("Add description")` | Adds accessibility alt text |
| **Post Button (Modal)** | `[data-testid="tweetButton"]` | `button:has-text("Post")` | Submit button in compose dialog |
| **Post Button (Inline)** | `[data-testid="tweetButtonInline"]` | `button[data-testid="tweetButtonInline"]` | Submit button on home timeline composer |
| **Close / Dismiss Modal** | `[data-testid="app-bar-close"]` | `button[aria-label="Close"]` | Discards post draft |

## Navigation & Authentication

| Page / Component | URL / Test ID | Fallback Selector | Purpose |
| :--- | :--- | :--- | :--- |
| **Compose Direct URL** | `https://x.com/compose/post` | - | Opens direct modal composer |
| **Home Timeline** | `https://x.com/home` | - | Main dashboard |
| **Login Page** | `https://x.com/login` | - | Authentication page |
| **Username Input** | `input[autocomplete="username"]` | `input[name="text"]` | Initial login step |
| **Password Input** | `input[type="password"]` | `input[name="password"]` | Password entry step |
| **Account Navigation / Menu** | `[data-testid="SideNav_AccountSwitcher_Button"]` | `button[aria-label*="Account menu"]` | Used to verify active user login |
| **Toast Notifications** | `[data-testid="toast"]` | `div[role="status"]` | "Your post was sent" confirmation |

## Working with Selectors in playwright-cli

### Example: Uploading Image
Using `playwright-cli` native `upload` command targets active file inputs:
```powershell
playwright-cli -s=x upload "C:\path\to\render.png"
```
If targeting explicitly via `run-code`:
```powershell
playwright-cli -s=x run-code "async (page) => {
  const fileInput = await page.locator('input[data-testid=\"fileInput\"]').first();
  await fileInput.setInputFiles('C:/path/to/render.png');
}"
```

### Example: Checking Post Status
```powershell
playwright-cli -s=x eval "() => {
  const btn = document.querySelector('[data-testid=\"tweetButton\"]');
  return btn ? !btn.disabled : false;
}"
```
