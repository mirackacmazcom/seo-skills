#!/usr/bin/env python3
"""LLM Patents search tool (client).

The archive lives on seoskills.io. This script sends its arguments to the search API and prints the answer,
exactly as the search tool on the server prints it. Standard library only.

    python3 scripts/patent.py --help
    python3 scripts/patent.py <command> [options]

Your search terms are sent to api.seoskills.io only to run the search. They are not logged or linked to you;
results are cached for up to an hour so repeat searches are fast.
Set SEOSKILLS_API to use another server.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

SKILL = "llm-patents"
API = os.environ.get("SEOSKILLS_API", "https://api.seoskills.io").rstrip("/")


def main():
    args = sys.argv[1:] or ["--help"]
    req = urllib.request.Request(
        f"{API}/v1/{SKILL}",
        data=json.dumps({"args": args}).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": f"seoskills-skill/1.2.0 ({SKILL})"},
        method="POST",
    )
    try:
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                body = r.read()
        except urllib.error.HTTPError:
            raise
        except (urllib.error.URLError, ConnectionError):
            # A dropped connection is usually the search engine restarting. Try once more before giving up.
            time.sleep(4)
            with urllib.request.urlopen(req, timeout=90) as r:
                body = r.read()
        result = json.loads(body.decode("utf-8"))
        if not isinstance(result, dict):
            raise ValueError("unexpected response")
    except urllib.error.HTTPError as e:
        try:
            message = json.load(e).get("error", "")
        except Exception:
            message = ""
        if e.code == 429:
            sys.exit("Too many searches in a short time. Wait a minute and run the command again.")
        sys.exit(f"The search API returned an error ({e.code}). {message}".strip())
    except ValueError:
        sys.exit(
            f"{API} sent a response this script could not read. It may be a temporary block or outage.\n"
            "Wait a minute and run the command again, or use the SEO Skills MCP server: https://seoskills.io/install/"
        )
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        sys.exit(
            f"Could not reach {API} ({e}).\n"
            "If this was a one-off, run the command again in a few seconds. The skill needs internet access; if\n"
            "your agent runs in a sandbox without it, connect the SEO Skills MCP server: https://seoskills.io/install/"
        )
    # Write UTF-8 bytes: the output has characters such as § ¶ → that a Windows console code page cannot encode.
    for stream, key in ((sys.stdout, "stdout"), (sys.stderr, "stderr")):
        text = result.get(key)
        if text:
            stream.flush()
            raw = getattr(stream, "buffer", None)
            if raw is None:
                stream.write(str(text))
            else:
                raw.write(str(text).encode("utf-8"))
                raw.flush()
    code = result.get("exit", 0)
    sys.exit(code if isinstance(code, int) else 1)


if __name__ == "__main__":
    main()
