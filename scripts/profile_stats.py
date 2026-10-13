#!/usr/bin/env python3
"""Render assets for the profile README's GitHub Activity section from the GitHub API.

Writes an SVG card with contributions and active days over the past year, the longest
contribution streak since the account was created, public repo count, a 52-week activity
chart, and a language breakdown limited to the repos the README features.

Standard library only. Needs a token in GITHUB_TOKEN (the Actions token is enough).

    GITHUB_TOKEN=... python3 scripts/profile_stats.py dist/activity.svg
"""
import datetime as dt
import json
import os
import sys
import urllib.request
from html import escape

USER = os.environ.get("PROFILE_USER", "Aakash553-stack")
# Languages are counted only in these repos, so generated notebook output and
# prototype scaffolding elsewhere don't drown out the code the profile is about.
LANG_REPOS = [r.strip() for r in os.environ.get(
    "LANG_REPOS",
    "aakashmunawar-site,opstrack-police-operations-platform,taskmanager,StudentGradeTracker,BankAccountSimulator",
).split(",") if r.strip()]
# Notebook output, markup and config files aren't hand-written program code.
LANG_EXCLUDE = {"Jupyter Notebook", "HTML", "CSS", "Dockerfile", "Mako", "Shell", "Batchfile"}
LANG_COLORS = {"Python": "#3B82F6", "Java": "#F59E0B", "JavaScript": "#FCD34D", "TypeScript": "#22D3EE",
               "PLpgSQL": "#8B5CF6", "SQL": "#8B5CF6"}
OTHER_COLOR = "#475569"

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"


def api(url, payload=None):
    token = os.environ["GITHUB_TOKEN"]
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-stats",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if isinstance(body, dict) and body.get("errors"):
        raise RuntimeError(body["errors"])
    return body


def graphql(query, **variables):
    return api("https://api.github.com/graphql", {"query": query, "variables": variables})["data"]


CALENDAR = """query($login:String!,$from:DateTime,$to:DateTime){user(login:$login){
  createdAt repositories(privacy:PUBLIC,ownerAffiliations:OWNER,isFork:false){totalCount}
  contributionsCollection(from:$from,to:$to){contributionCalendar{totalContributions
    weeks{contributionDays{date contributionCount}}}}}}"""


def collect():
    now = dt.datetime.now(dt.timezone.utc)
    user = graphql(CALENDAR, login=USER)["user"]  # no range: the past year, as on the profile page
    cal = user["contributionsCollection"]["contributionCalendar"]
    year_days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    weeks = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]][-52:]

    # Longest streak needs every day since the account was created, one year per query.
    counts = {}
    start = dt.datetime.fromisoformat(user["createdAt"].replace("Z", "+00:00"))
    while start < now:
        end = min(start + dt.timedelta(days=365), now)
        c = graphql(CALENDAR, login=USER, **{"from": start.isoformat(), "to": end.isoformat()})
        for w in c["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]:
            for d in w["contributionDays"]:
                counts[d["date"]] = d["contributionCount"]
        start = end
    longest = run = 0
    for day in sorted(counts):
        run = run + 1 if counts[day] > 0 else 0
        longest = max(longest, run)

    langs = {}
    for repo in LANG_REPOS:
        full = repo if "/" in repo else f"{USER}/{repo}"
        for name, size in api(f"https://api.github.com/repos/{full}/languages").items():
            if name not in LANG_EXCLUDE:
                langs[name] = langs.get(name, 0) + size

    return {
        "total": cal["totalContributions"],
        "active": sum(1 for d in year_days if d["contributionCount"] > 0),
        "longest": longest,
        "repos": user["repositories"]["totalCount"],
        "weeks": weeks,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


def text(x, y, s, size, fill, cls="mono", anchor="start", weight=None, ls=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    w = f' font-weight="{weight}"' if weight else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    return f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}{w}{l}>{escape(str(s))}</text>'


def render(s):
    W, H = 840, 236
    out = [f'<rect width="{W}" height="{H}" fill="#0A0F1E"/><rect width="{W}" height="2" fill="url(#spec)" opacity=".8"/>',
           text(32, 36, "GITHUB.ACTIVITY", 11, "#22D3EE", weight=700, ls=2.5),
           text(808, 36, "// regenerated daily by GitHub Actions from the GitHub API", 10, "#64748B", anchor="end")]

    def plural(n, word):
        return f"{word}{'' if n == 1 else 's'}"

    tiles = [(f"{s['total']:,}", plural(s["total"], "contribution"), "past 12 months", "#22D3EE"),
             (f"{s['active']}", plural(s["active"], "active day"), "past 12 months", "#3B82F6"),
             (f"{s['longest']}", f"{plural(s['longest'], 'day')} longest streak", "since joining GitHub", "#8B5CF6"),
             (f"{s['repos']}", plural(s["repos"], "public repo"), "original, not forks", "#94A3B8")]
    for i, (num, label, sub, col) in enumerate(tiles):
        x = 20 + i * 202
        out.append(f'<rect x="{x}" y="52" width="192" height="70" rx="10" fill="#0D1426" stroke="#1E293B"/>'
                   f'<rect x="{x}" y="64" width="3" height="46" rx="1.5" fill="{col}"/>'
                   + text(x + 18, 90, num, 26, "#F8FAFC", weight=800)
                   + text(x + 18, 108, label, 10.5, "#CBD5E1")
                   + text(x + 182, 72, sub, 8.5, "#64748B", anchor="end"))

    # weekly activity
    out.append(f'<rect x="20" y="132" width="490" height="88" rx="10" fill="#0D1426" stroke="#1E293B"/>'
               + text(34, 150, "WEEKLY CONTRIBUTIONS · 52 WEEKS", 9, "#64748B", ls=1.5))
    peak = max(s["weeks"] + [1])
    bw = 450 / 52
    css = []
    for i, n in enumerate(s["weeks"]):
        h = 3 if n == 0 else 6 + 48 * n / peak
        col = "#22D3EE" if n == peak and n > 0 else ("#3B82F6" if n else "#1E293B")
        out.append(f'<rect class="w" x="{34 + i * bw:.1f}" y="{208 - h:.1f}" width="{bw - 2.4:.1f}" height="{h:.1f}" rx="1.5" fill="{col}" style="animation-delay:{i * 0.03:.2f}s"/>')

    # languages
    total = sum(v for _, v in s["langs"]) or 1
    top = s["langs"][:4]
    rest = total - sum(v for _, v in top)
    parts = top + ([("Other", rest)] if rest > 0 else [])
    out.append(f'<rect x="520" y="132" width="300" height="88" rx="10" fill="#0D1426" stroke="#1E293B"/>'
               + text(534, 150, "LANGUAGES · FEATURED REPOS", 9, "#64748B", ls=1.5))
    x = 534.0
    for name, size in parts:
        w = 272 * size / total
        out.append(f'<rect x="{x:.1f}" y="160" width="{max(w - 2, 1):.1f}" height="8" rx="2" fill="{LANG_COLORS.get(name, OTHER_COLOR)}"/>')
        x += w
    for i, (name, size) in enumerate(parts):
        lx, ly = 534 + (i % 2) * 140, 185 + (i // 2) * 15
        out.append(f'<circle cx="{lx + 4}" cy="{ly - 3.5}" r="3.5" fill="{LANG_COLORS.get(name, OTHER_COLOR)}"/>'
                   + text(lx + 12, ly, f"{name} {100 * size / total:.0f}%", 10, "#CBD5E1"))

    css = (f".mono{{font-family:{MONO}}}.sans{{font-family:{SANS}}}"
           ".w{transform-box:fill-box;transform-origin:bottom;animation:grow 1.2s ease-out both}"
           "@keyframes grow{from{transform:scaleY(0)}}"
           "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
    lang_desc = ", ".join(f"{n} {100 * v / total:.0f}%" for n, v in parts)
    desc = (f"{s['total']} contributions and {s['active']} active days in the past 12 months; longest streak "
            f"{s['longest']} days; {s['repos']} public repositories. Languages in featured repos by code size: {lang_desc}.")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">GitHub activity for {USER}</title>
  <desc id="d">{escape(desc)}</desc>
  <defs><clipPath id="clip"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  <linearGradient id="spec" x1="0" x2="1"><stop offset="0" stop-color="#3B82F6"/><stop offset=".5" stop-color="#22D3EE"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient></defs>
  <style>{css}</style>
  <g clip-path="url(#clip)">{"".join(out)}</g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="13.5" fill="none" stroke="#1E293B"/>
</svg>
'''


def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} OUTPUT.svg")
    stats = collect()
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[1])), exist_ok=True)
    with open(sys.argv[1], "w") as f:
        f.write(render(stats))
    print(json.dumps({k: v for k, v in stats.items() if k != "weeks"}))


if __name__ == "__main__":
    main()
