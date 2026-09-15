# RevivaCatch Site

Static marketing site for RevivaCatch LLC. The site sells **document
accessibility remediation** (PDF/UA-1, veraPDF-measured) for government and
agency documents. It was originally a med-spa HighLevel reseller site; that
offer is dead and only the HighLevel chat widget remains from it.
**LIVE at https://revivacatch.com via GitHub Pages — pushing to main IS
deploying.** Never push without explicit approval; preview locally first
with `/preview-site`.

## Files
- `index.html`, `privacy-policy.html`, `terms-of-service.html` — the core site
- `proofs/` — published before/after remediation measurements. `proofs/index.html`
  (translated MN/NC/WA documents) and `proofs/pennsylvania/` (13 PA documents,
  3 of them at veraPDF 106/106 PASS). These are the only sales proof that exists.
- `why-pdfs-come-back-rejected/` — the inbound article. Targets the query a real
  buyer types. Every number in it traces to a measurement in
  `~/remediation-samples`; do not add a claim that is not measured there.
- `robots.txt`, `sitemap.xml` — added 2026-09-14. The site had NEITHER before
  that and `site:revivacatch.com` returned zero indexed pages.
- `CNAME` — custom-domain binding; a hook blocks edits (deleting it kills
  the domain). DNS lives at Porkbun.

## Rules
- Legal pages name the entity RevivaCatch LLC (PA) — keep entity details
  consistent across all three pages.
- The HighLevel chat widget on the site is part of an approved A2P
  compliance submission — do not remove it.
- No build step, no frameworks. Plain HTML/CSS only.

## Indexing
`site:revivacatch.com` returned **zero** results on 2026-09-14 — Google had not
indexed a single page. `robots.txt` and `sitemap.xml` now exist, but a sitemap
alone does not get a new domain crawled, and IndexNow does not reach Google
(see the `reference_indexnow_not_google` memory). Getting indexed needs Google
Search Console verification plus a sitemap submission, which is Kaleb's step.
Re-check with a `site:` query, never by assuming the sitemap was enough.

## Never claim on this site
No accessibility certification, no VPAT authorship, no assistive-technology or
screen-reader testing, and never that a document is "ADA compliant" or
"certified". Conformance to PDF/UA-1 is measurable and may be stated; legal
compliance is not ours to assert.
