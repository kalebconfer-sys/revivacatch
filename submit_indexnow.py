"""Tell Bing the site exists. Google does not accept IndexNow.

revivacatch.com had ZERO indexed pages on Google, Bing AND DuckDuckGo as of
2026-09-15, while robots.txt allowed everything, sitemap.xml was valid, no page
carried a noindex, and every page returned 200 to a Googlebot user agent. The
site is crawlable and simply undiscovered: a new domain with no inbound links
gives a crawler no reason to visit.

IndexNow fixes exactly half of that. Bing, Yandex, Seznam and Naver accept a
direct "here are my URLs" ping with no account and no login. **Google does not
participate.** A 200 from this script means Bing, not Google - see
~/.claude/.../memory/reference_indexnow_not_google.md. Google still needs
Search Console, which is Kaleb's step.

Usage:  python submit_indexnow.py
"""
import json
import urllib.request

KEY = "33d12d999159b8a73b588d669f7d774b"
HOST = "revivacatch.com"
URLS = [
    "https://revivacatch.com/",
    "https://revivacatch.com/pdf-check/",
    "https://revivacatch.com/why-pdfs-come-back-rejected/",
    "https://revivacatch.com/proofs/",
    "https://revivacatch.com/proofs/pennsylvania/",
    "https://revivacatch.com/proofs/mn-dhs-4740-spa.html",
    "https://revivacatch.com/proofs/mn-dhs-3418-spa.html",
    "https://revivacatch.com/proofs/mn-dhs-3182-spa.html",
    "https://revivacatch.com/proofs/wa-lni-f700-074-909.html",
]


def main():
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": "https://%s/%s.txt" % (HOST, KEY),
        "urlList": URLS,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow", data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print("HTTP %s - %d URLs submitted to Bing/Yandex" % (r.status, len(URLS)))
        print("Google is NOT covered by this. Verify indexing with a site: query,")
        print("never by assuming a 200 here means anything about Google.")


if __name__ == "__main__":
    main()
