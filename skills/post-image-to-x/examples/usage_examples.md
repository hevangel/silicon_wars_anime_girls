# Usage Examples: Posting Images to X

This document provides sample workflows and commands for posting artwork and chapter panels from the Silicon Wars repository to X (Twitter).

---

## Example 1: Posting a Newly Accepted Character Render

```powershell
# Using the helper script with a caption and hashtags
.\skills\post-image-to-x\scripts\post_image.ps1 `
    -ImagePath "B:\silicon_wars_anime_girls\characters\triad\renders\accepted\c01_p01_v02.png" `
    -Text "First look at the Triad front reference card for Silicon Wars! #SiliconWars #ConceptArt #IndieManga"
```

---

## Example 2: Interactive Login & First-Time Setup

When setting up on a new machine or when existing cookies expire:

```powershell
# 1. Open headed browser to log in manually
playwright-cli -s=x-auth open https://x.com/login --headed

# 2. Complete the login, pass 2FA or security check in the opened browser window

# 3. Save the session state to file for reuse
playwright-cli -s=x-auth state-save "$env:USERPROFILE\.x-auth-state.json"

# 4. Close the interactive setup session
playwright-cli -s=x-auth close
```

Afterward, subsequent posts can load this state directly:
```powershell
.\skills\post-image-to-x\scripts\post_image.ps1 `
    -ImagePath "B:\silicon_wars_anime_girls\characters\intel\renders\c01_p02.png" `
    -Text "Intel - The Blue Empress. Silicon Wars." `
    -StateFile "$env:USERPROFILE\.x-auth-state.json"
```

---

## Example 3: Step-by-Step Interactive CLI Workflow

For fine-grained control or troubleshooting:

```powershell
# 1. Open the post composer with persistent profile
playwright-cli -s=x open https://x.com/compose/post --persistent --profile="$env:USERPROFILE\.playwright-x-profile"

# 2. Inspect element tree
playwright-cli -s=x snapshot

# 3. Attach image
playwright-cli -s=x upload "B:\silicon_wars_anime_girls\characters\amd\renders\accepted\poster.png"

# 4. Fill text
playwright-cli -s=x click '[data-testid="tweetTextarea_0"]'
playwright-cli -s=x type "AMD - The Crimson Challenger takes the stage."

# 5. Review preview screenshot
playwright-cli -s=x screenshot

# 6. Post
playwright-cli -s=x click '[data-testid="tweetButton"]'

# 7. Close session
playwright-cli -s=x close
```
