---
name: preview-site
description: Serve the RevivaCatch site locally and open it in the browser for visual verification. Use before any push - file:// URLs do not work with the browser extension.
---

# Preview Site

Serve locally (file:// URLs fail in the Chrome extension — learned the hard way):

```powershell
Start-Process python -ArgumentList '-m','http.server','8642' -WorkingDirectory 'C:\Users\kaleb\revivacatch'
Start-Process 'http://localhost:8642'
```

Check all three pages: `/`, `/privacy-policy.html`, `/terms-of-service.html` —
desktop and mobile widths. When done, stop the server:

```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8642 -State Listen).OwningProcess -Confirm:$false
```

Remember: **pushing to main deploys the live site** (GitHub Pages). Preview
first, push only after approval.
