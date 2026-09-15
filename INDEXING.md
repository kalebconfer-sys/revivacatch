# Why nobody can find this site, and the two steps that fix it

**Measured 2026-09-15: zero indexed pages on Google, Bing AND DuckDuckGo.**

That triple zero is the useful part. It rules out the things people usually blame:

| checked | result |
|---|---|
| `robots.txt` | `User-agent: * / Allow: /` — allows everything |
| `sitemap.xml` | valid XML, now 11 URLs |
| `noindex` meta tag | none on any page |
| `X-Robots-Tag` header | none |
| pages served to a Googlebot user agent | all `200`, with real `<title>` and `<meta description>` |

Nothing is blocking the crawl. The site is simply **undiscovered** — a new domain
with no inbound links gives a crawler no reason to ever visit. Publishing a sitemap
does not summon anybody; something has to point at it.

---

## Step 1 — Bing and DuckDuckGo. No login, already built.

```bash
python submit_indexnow.py
```

IndexNow lets a site tell Bing, Yandex, Seznam and Naver "here are my URLs" with no
account. The key file `33d12d999159b8a73b588d669f7d774b.txt` at the site root is
what proves the domain is yours; it has to be live, so this only works **after the
next push**.

DuckDuckGo results come from Bing, so this covers both.

**Google does not participate in IndexNow.** A `200` from that script says nothing
whatsoever about Google. Check with a `site:revivacatch.com` query, never by
assuming.

---

## Step 2 — Google. 4 minutes, and it needs your login.

This is the actual bottleneck, and it has been the top pending item for days.

1. Open https://search.google.com/search-console and sign in as kalebconfer@gmail.com
2. Add property → choose the **URL prefix** box on the right → `https://revivacatch.com`
   (URL prefix, not Domain — Domain needs a DNS record at Porkbun and is slower)
3. Pick the **HTML file** verification method and download the file it gives you.
   It is named something like `google1a2b3c4d5e6f.html`.
4. Drop that file into `C:\Users\kaleb\revivacatch\`, then commit and push it.
   Tell Claude and it will do the commit; the push needs your go.
5. Back in Search Console, click **Verify**. Then Sitemaps → enter `sitemap.xml` → Submit.

Then use **URL Inspection** on `https://revivacatch.com/pdf-check/` and click
**Request Indexing**. That one page is the whole inbound bet: it is the free tool a
stranger with a rejected PDF would search for.

Expect days to weeks, not hours.

---

## Why this is worth four minutes

The only real buyer this business has ever had — `packaged_heat`, a US agency with a
rejected remediated PDF and a deadline — arrived **inbound**, through a marketplace
listing, and was able to pay by card without a purchase order. Roughly 700 cold
emails across six projects produced one warm reply and no money.

The free checker at `/pdf-check/` is built to catch exactly that person at exactly
that moment. Right now it cannot be found by anyone who is not already holding the
link.
