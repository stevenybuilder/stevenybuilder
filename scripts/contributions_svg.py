#!/usr/bin/env python3
"""Render a GitHub-style contribution graph (from a fixed start date to today) as SVG.

Usage: GITHUB_TOKEN=... python3 scripts/contributions_svg.py > contributions.svg
"""
import datetime as dt
import json
import os
import sys
import urllib.request

LOGIN = "stevenybuilder"
START = dt.date(2026, 3, 1)
COLORS = ["#EEEEEE", "#7cd2a7", "#62b88d", "#2f855a", "#266a48"]  # NONE..FOURTH_QUARTILE
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, "
        "'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'")
CELL, STEP, LEFT, TOP = 10, 12, 27, 20


def fetch(start: dt.date, end: dt.date):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is required")
    query = """
    query($login:String!, $from:DateTime!, $to:DateTime!) {
      user(login:$login) { contributionsCollection(from:$from, to:$to) {
        contributionCalendar { weeks { contributionDays { date contributionCount contributionLevel } } } } } }"""
    body = json.dumps({"query": query, "variables": {
        "login": LOGIN, "from": f"{start}T00:00:00Z", "to": f"{end}T23:59:59Z"}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        sys.exit(json.dumps(data["errors"]))
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]


def render(weeks) -> str:
    width = LEFT + STEP * len(weeks) - (STEP - CELL)
    height = TOP + STEP * 7
    out = [f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">']
    text = f"fill:#767676;font-family:{FONT};font-size:9px;"
    for i, name in enumerate(["Mon", "Wed", "Fri"]):
        out.append(f'<text style="{text}" x="0" y="{TOP + STEP * (1 + 2 * i) + 8}">{name}</text>')
    last_month = None
    for wi, week in enumerate(weeks):
        x = LEFT + STEP * wi
        for day in week["contributionDays"]:
            d = dt.date.fromisoformat(day["date"])
            if d.month != last_month:
                if last_month is not None or d.day <= 7:
                    out.append(f'<text style="{text}" x="{x}" y="{TOP - 6}">{d.strftime("%b")}</text>')
                last_month = d.month
            y = TOP + STEP * (d.isoweekday() % 7)
            color = COLORS[LEVELS[day["contributionLevel"]]]
            out.append(f'<rect style="fill:{color};shape-rendering:crispedges;" data-date="{d}" '
                       f'data-count="{day["contributionCount"]}" x="{x}" y="{y}" width="{CELL}" height="{CELL}"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    print(render(fetch(START, dt.date.today())))
