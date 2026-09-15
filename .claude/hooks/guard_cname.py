import json
import sys

try:
    data = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
except Exception:
    sys.exit(0)

fp = ((data.get("tool_input") or {}).get("file_path") or "").replace("\\", "/")
if fp.rstrip("/").endswith("/CNAME") or fp == "CNAME":
    print("Blocked: CNAME holds the custom domain for revivacatch.com. "
          "Changing or deleting it takes the live site down. "
          "If this is really intended, the user must edit it manually.", file=sys.stderr)
    sys.exit(2)
