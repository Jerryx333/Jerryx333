"""Refresh the "最近在忙" block in README.md with the owner's latest public repos."""
import json, os, subprocess, sys
from datetime import datetime, timezone

OWNER = os.environ["OWNER"]
START, END = "<!-- RECENT:START -->", "<!-- RECENT:END -->"

repos = json.loads(subprocess.check_output([
    "gh", "repo", "list", OWNER, "--source", "--visibility", "public", "--limit", "20",
    "--json", "name,description,pushedAt,url",
]))
repos = [r for r in repos if r["name"].lower() != OWNER.lower()]
repos.sort(key=lambda r: r["pushedAt"], reverse=True)

lines = []
for r in repos[:5]:
    desc = (r["description"] or "").strip()
    lines.append(f"- [{r['name']}]({r['url']}) · {r['pushedAt'][:10]}" + (f"：{desc}" if desc else ""))
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
block = "\n".join([START, *lines, "", f"<sub>每天自动更新 · {today}</sub>", END])

path = "README.md"
text = open(path, encoding="utf-8").read()
head, rest = text.split(START, 1)
_, tail = rest.split(END, 1)
open(path, "w", encoding="utf-8").write(head + block + tail)
print(block)
