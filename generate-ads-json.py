#!/usr/bin/env python3
"""Parse the creative briefing markdown and generate ADS JS array for index.html."""

import re
import json
from pathlib import Path

BRIEFING_PATH = Path("/Users/derickcarneiro/Documents/Claude/Projects/Balls&Brains/10-research-pipeline/2026-W17-batch-13/04-creative-briefing.md")
HTML_PATH = Path("/tmp/tmc-ads-review/index.html")

DAY_META = {
    1: {"label": "Segunda", "date": "20/04/26", "cluster": "Cluster 3 Cognitive Decline"},
    2: {"label": "Terça", "date": "21/04/26", "cluster": "Cluster 4 Belly Fat / Man Boobs"},
    3: {"label": "Quarta", "date": "22/04/26", "cluster": "Cluster 4 High Blood Sugar"},
    4: {"label": "Quinta", "date": "23/04/26", "cluster": "Cluster 6 Joint & Knee Pain"},
    5: {"label": "Sexta", "date": "24/04/26", "cluster": "Cluster 1 Weak Erections"},
}

# Day ranges by ID
def get_day(ad_id):
    if 1 <= ad_id <= 12: return 1
    if 13 <= ad_id <= 24: return 2
    if 25 <= ad_id <= 36: return 3
    if 37 <= ad_id <= 48: return 4
    if 49 <= ad_id <= 60: return 5
    return None

def get_type(title):
    if "OVERRIDE" in title or "[OVERRIDE" in title:
        return "override"
    if "Winner Variation" in title:
        return "winner"
    return "fill"

text = BRIEFING_PATH.read_text()

# Split by ## AD #N headings
sections = re.split(r'\n## AD #(\d+) — ', text)
# sections[0] = preamble, then alternating: id, body, id, body...

ads = []
for i in range(1, len(sections), 2):
    ad_id = int(sections[i])
    body = sections[i+1]

    # First line of body is the title (before the newline)
    first_newline = body.find('\n')
    title = body[:first_newline].strip()
    rest = body[first_newline:]

    # Extract fields (ignoring the header section)
    def extract(field_name):
        # Match "- **FieldName:** value" until end of line or next "- **" at start
        pattern = rf'- \*\*{re.escape(field_name)}:\*\*\s+(.+?)(?=\n- \*\*|\n## |\n---|\Z)'
        m = re.search(pattern, rest, re.DOTALL)
        if m:
            # Clean multi-line values
            val = m.group(1).strip()
            val = re.sub(r'\s+', ' ', val)
            return val
        return ""

    angle = extract("Ângulo")
    hook_copy = extract("Copy Hook")
    hook_visual = extract("Visual Hook")
    format_field = extract("Formato")
    speaker = extract("Speaker")
    execution = extract("Execução")

    day = get_day(ad_id)
    meta = DAY_META[day]

    ads.append({
        "id": ad_id,
        "day": day,
        "dayLabel": meta["label"],
        "date": meta["date"],
        "cluster": meta["cluster"],
        "type": get_type(title),
        "title": title,
        "angle": angle,
        "hookCopy": hook_copy,
        "hookVisual": hook_visual,
        "format": format_field,
        "speaker": speaker,
        "execution": execution,
    })

# Sort by id
ads.sort(key=lambda a: a["id"])
print(f"Parsed {len(ads)} ads")

# Generate JS array with compact formatting (one ad per line)
js_lines = []
for ad in ads:
    # Use JSON stringify with proper escaping
    line_dict = {
        "id": ad["id"],
        "day": ad["day"],
        "dayLabel": ad["dayLabel"],
        "date": ad["date"],
        "cluster": ad["cluster"],
        "type": ad["type"],
        "title": ad["title"],
        "angle": ad["angle"],
        "hookCopy": ad["hookCopy"],
        "hookVisual": ad["hookVisual"],
        "format": ad["format"],
        "speaker": ad["speaker"],
        "execution": ad["execution"],
    }
    # Emit as JS object literal (same as JSON but without quoting keys that are safe)
    js_lines.append("  " + json.dumps(line_dict, ensure_ascii=False) + ",")

new_ads_js = "const ADS = [\n" + "\n".join(js_lines) + "\n];"

# Read HTML, replace ADS array
html = HTML_PATH.read_text()

# Find start and end of current ADS array
start_marker = "const ADS = ["
end_marker = "];"

start_idx = html.find(start_marker)
if start_idx == -1:
    raise ValueError("Could not find ADS array start")

# Find the matching closing bracket — we look for the next "];\n\n" after start
# Let's find the line after which the comment "// ============ STATE MANAGEMENT" appears
state_marker = "// ============ STATE MANAGEMENT"
state_idx = html.find(state_marker, start_idx)
if state_idx == -1:
    raise ValueError("Could not find STATE MANAGEMENT marker")

# The closing "];" is on the line before state_marker
end_search = html.rfind("];", start_idx, state_idx)
if end_search == -1:
    raise ValueError("Could not find end of ADS array")

# Replace
new_html = html[:start_idx] + new_ads_js + "\n\n" + html[state_idx:]

HTML_PATH.write_text(new_html)
print(f"Updated {HTML_PATH}")
print(f"ADS array size: {len(new_ads_js)} chars")
