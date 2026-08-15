# RevivaCatch

Marketing site for **RevivaCatch** — missed-call recovery, automated booking, and reputation tools for med spas and aesthetic clinics.

Static site (no build step). Hosted on GitHub Pages, served at https://revivacatch.com.

## Pages
- `index.html` — landing page (hero, calculator, guarantee, audit CTA)
- `privacy-policy.html` — privacy policy incl. SMS/A2P consent language
- `terms-of-service.html` — terms of service

### Tablet signage
Full-screen signs for a tablet at the delivery point. Not linked from the site; open them
directly and use the corner arrow to flip between the two.
- `packages.html` — "PLACE PACKAGES HERE" with a drop arrow
- `carriers.html` — UPS, FedEx, Amazon and USPS marks

## Deploy
Push to `main`; GitHub Pages serves from the repo root. Custom domain set via the `CNAME` file.
