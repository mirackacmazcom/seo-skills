#!/usr/bin/env python3
"""Google Search Docs search tool (client).

The archive lives on seoskills.io. This script sends its arguments to the search API and prints the answer,
exactly as the search tool on the server prints it. Standard library only.

    python3 scripts/gdocs.py --help
    python3 scripts/gdocs.py <command> [options]

Your search terms are sent to api.seoskills.io to run the search. They are not stored.
Set SEOSKILLS_API to use another server.
"""
import json
import os
import sys
import urllib.error
import urllib.request

SKILL = "google-search-docs"
API = os.environ.get("SEOSKILLS_API", "https://api.seoskills.io").rstrip("/")


def main():
    args = sys.argv[1:] or ["--help"]
    req = urllib.request.Request(
        f"{API}/v1/{SKILL}",
        data=json.dumps({"args": args}).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "seoskills-skill/1.0 ({SKILL})"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            result = json.load(r)
    except urllib.error.HTTPError as e:
        try:
            message = json.load(e).get("error", "")
        except Exception:
            message = ""
        if e.code == 429:
            sys.exit("Too many searches in a short time. Wait a minute and run the command again.")
        sys.exit(f"The search API returned an error ({e.code}). {message}".strip())
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        sys.exit(
            f"Could not reach {API} ({e}).\n"
            "This skill needs internet access to run its searches. If your agent runs in a sandbox without it,\n"
            "connect the SEO Skills MCP server instead: https://seoskills.io/install/"
        )
    if result.get("stdout"):
        sys.stdout.write(result["stdout"])
    if result.get("stderr"):
        sys.stderr.write(result["stderr"])
    sys.exit(result.get("exit", 0))


if __name__ == "__main__":
    main()
