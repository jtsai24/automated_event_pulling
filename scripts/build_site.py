"""Render the newest public weekly Markdown report as a dependency-free site.

Run: python scripts/build_site.py [report.md]
Output: docs/index.html (no Notion access or runtime API required).
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

def inline(value):
    """Escape HTML and render only HTTPS links and bold text."""
    chunks = re.split(r'(\[[^\n]*?\]\(https://[^\s)]+\))', value)
    out = []
    for chunk in chunks:
        match = re.fullmatch(r'\[(.*)\]\((https://[^\s)]+)\)', chunk)
        if match:
            out.append('<a href="' + html.escape(match[2], quote=True) + '">' + html.escape(match[1].replace('\\|', '|')) + '</a>')
        else:
            text = html.escape(chunk.replace('\\|', '|'))
            out.append(re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text))
    return ''.join(out)

def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def render(text):
    lines = text.splitlines()
    output, navigation = [], []
    row_count = 0
    used_ids = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        heading = re.match(r'^(#{1,6}) (.+)$', line)
        if heading:
            level, label = len(heading[1]), heading[2]
            if level == 1:
                i += 1
                continue
            base = slug(label)
            used_ids[base] = used_ids.get(base, 0) + 1
            ident = base if used_ids[base] == 1 else base + "-" + str(used_ids[base])
            output.append(f'<h{level} id="{ident}">{inline(label)}</h{level}>')
            if level in (2, 3, 4):
                navigation.append((level, label, ident))
        elif line.startswith('|'):
            block = []
            while i < len(lines) and lines[i].startswith('|'):
                block.append(lines[i]); i += 1
            cells = lambda s: [c.strip() for c in re.split(r'(?<!\\)\|', s.strip().strip('|'))]
            header = cells(block[0])
            output.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in header) + '</tr></thead><tbody>')
            for source in block[2:]:
                row = cells(source)
                if len(row) != len(header):
                    raise ValueError('Malformed table row: ' + source)
                output.append('<tr>' + ''.join('<td data-label="' + html.escape(header[j], quote=True) + '">' + inline(c) + '</td>' for j,c in enumerate(row)) + '</tr>')
                row_count += 1
            output.append('</tbody></table></div>')
            continue
        elif line.startswith('- '):
            output.append('<p class="bullet">' + inline(line[2:]) + '</p>')
        elif line.strip():
            output.append('<p>' + inline(line) + '</p>')
        i += 1
    return '\n'.join(output), navigation, row_count

CSS = '''
:root{color-scheme:light;--ink:#162b3b;--muted:#516474;--paper:#fff;--bg:#f3f5f3;--line:#d9e2df;--accent:#176653}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:32px}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:var(--accent);text-underline-offset:3px}a:hover{text-decoration-thickness:2px}a:focus-visible{outline:3px solid #cb9227;outline-offset:4px}.skip{position:absolute;left:16px;top:-80px;background:white;padding:12px}.skip:focus{top:12px;z-index:5}.masthead{background:#153b35;color:#fff;padding:48px max(24px,calc((100vw - 1320px)/2)) 42px}.eyebrow{font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:#abd8c5;font-weight:700}.masthead h1{font-size:clamp(30px,4vw,46px);line-height:1.15;letter-spacing:-.035em;margin:14px 0}.masthead p{margin:0;color:#d4e6df}.masthead a{color:#d4e6df}.meta{display:flex;flex-wrap:wrap;gap:12px 24px;margin-top:24px!important;font-size:14px}.layout{max-width:1370px;margin:auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:40px;padding:32px 24px 80px}aside{align-self:start;position:sticky;top:24px;max-height:calc(100vh - 48px);overflow:auto;font-size:14px}aside h2{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:0 0 12px}nav a{display:block;padding:7px 10px;text-decoration:none;border-radius:6px;color:var(--ink)}nav a:hover{background:#e0eae4}nav .level-2{font-weight:750;margin-top:12px}nav .level-4{padding-left:22px;color:var(--muted)}main{min-width:0}main>p{color:var(--muted);max-width:85ch}h2{font-size:30px;letter-spacing:-.025em;margin:32px 0 12px}h3{font-size:24px;margin:42px 0 16px;border-top:1px solid var(--line);padding-top:28px}h4{font-size:21px;margin:36px 0 12px}h5{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);margin:24px 0 12px}.table-wrap{margin:0 0 24px;border:1px solid var(--line);border-radius:10px;background:var(--paper);overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;text-align:left}th{background:#e9efeb;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.07em;padding:12px 14px}td{padding:16px 14px;vertical-align:top;border-top:1px solid var(--line);overflow-wrap:anywhere}td:first-child{white-space:nowrap;color:var(--muted);font-size:12px}td:nth-child(2){min-width:125px;font-variant-numeric:tabular-nums}td:nth-child(3){min-width:250px}td:nth-child(3) a{font-weight:650}tbody tr:hover{background:#f9fbf9}.bullet{padding-left:16px;border-left:3px solid var(--line);font-size:14px}footer{border-top:1px solid var(--line);padding:24px;color:var(--muted);text-align:center;font-size:13px}.top-link{display:inline-block;margin-top:12px}
@media(max-width:1000px){.layout{grid-template-columns:180px minmax(0,1fr);gap:20px}td{padding:12px 10px}td:nth-child(3){min-width:200px}}
@media(max-width:760px){.masthead{padding:32px 20px}.layout{display:block;padding:20px 16px 48px}aside{position:static;max-height:none;margin-bottom:28px;border-bottom:1px solid var(--line);padding-bottom:20px}nav{display:flex;gap:8px;flex-wrap:wrap}nav a{padding:6px 10px;background:#e6ece7}nav .level-2{margin:0}nav .level-3{display:none}nav .level-4{padding-left:10px;font-size:12px}table,tbody,tr,td{display:block}thead{display:none}td{border:0;padding:3px 16px!important;min-width:0!important}tr{padding:16px 0;border-top:1px solid var(--line)}tr:first-child{border-top:0}td:first-child{white-space:normal}td:before{content:attr(data-label) ": ";font-weight:600;font-size:11px;text-transform:uppercase;color:var(--muted)}td:nth-child(3){margin:7px 0;font-size:16px}td:nth-child(3):before{display:none}h3{margin-top:32px}h2{font-size:26px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{aside,.skip{display:none}.layout{display:block;padding:0}.masthead{background:white;color:black;padding:0}.masthead p,.eyebrow{color:black}.table-wrap{overflow:visible}a{color:black}h3,h4,h5{break-after:avoid}tr{break-inside:avoid}}
'''

def build(source):
    text = source.read_text()
    body, nav, count = render(text)
    title = text.splitlines()[0].removeprefix('# ')
    report_url = 'https://github.com/jtsai24/automated_event_pulling/blob/main/reports/' + quote(source.name)
    nav_html = ''.join(f'<a class="level-{level}" href="#{ident}">{html.escape(label)}</a>' for level,label,ident in nav)
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Seattle career, AI and software event schedules, organized by day and time."><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body id="top"><a class="skip" href="#report">Skip to report</a>
<header class="masthead"><div class="eyebrow">Seattle · Career &amp; AI Events</div><h1>Your next conversation<br>starts here.</h1><p>{html.escape(re.sub(r'^\d{4}-\d{2}-\d{2} - ', '', title))}</p><p class="meta"><span>Report date: {html.escape(source.name[:10])}</span><span>All times: Seattle</span><a href="{report_url}">View Markdown source ↗</a></p></header>
<div class="layout"><aside><h2>Jump to a day</h2><nav aria-label="Report navigation">{nav_html}</nav><a class="top-link" href="#top">Back to top ↑</a></aside><main id="report">{body}</main></div>
<footer>Public event report · Verify current details with the organizer · <a href="https://github.com/jtsai24/automated_event_pulling">Project on GitHub</a></footer></body></html>'''
    target = ROOT / 'docs' / 'index.html'
    target.parent.mkdir(exist_ok=True)
    target.write_text(document)
    print(f'Rendered {source.name}: {count} table rows → {target}')
    return document, count

if __name__ == '__main__':
    if len(sys.argv) > 1:
        source = Path(sys.argv[1])
    else:
        reports = sorted((ROOT / 'reports').glob('* - Career AI Events for *.md'))
        if not reports:
            raise SystemExit('No weekly report found')
        source = reports[-1]
    build(source)
