import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
os.makedirs(OUT, exist_ok=True)
e = html.escape

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #000; }
body { font-family: Carlito, Calibri, sans-serif; font-size: var(--fs, 10.2pt); line-height: 1.22; }
.page { width: 210mm; padding: 11mm 13mm 9mm 13mm; }
h1 { font-size: 1.75em; margin: 0 0 1pt 0; font-weight: 700; }
.contact div { margin: 0; }
.target { font-weight: 700; margin: 3pt 0 4pt 0; }
h2 { font-size: 1em; font-weight: 700; text-transform: uppercase; margin: 6pt 0 3pt 0; padding-bottom: 1.5pt; border-bottom: 0.8pt solid #000; }
.row { display: flex; justify-content: space-between; align-items: baseline; }
.role { font-weight: 700; margin-top: 4pt; }
.org { text-transform: uppercase; }
.loc { font-style: italic; }
ul { margin: 1pt 0 0 0; padding-left: 22pt; }
li { margin: 0 0 0.6pt 0; }
.letter { font-size: 10.6pt; line-height: 1.32; }
.letter .page { padding: 20mm 22mm 18mm 22mm; }
.letter h1 { font-size: 1.45em; margin-bottom: 4pt; }
.letter .small { font-size: 0.92em; }
.letter .date { text-align: right; margin: 16pt 0 12pt 0; }
.letter .subject { font-weight: 700; margin-bottom: 12pt; }
.letter p { margin: 0 0 7pt 0; text-align: justify; }
"""

def entry(title, dates, org, loc, bullets):
    lis = "".join(f"<li>{e(b)}</li>" for b in bullets)
    return (f'<div class="row role"><span>{e(title)}</span><span>{e(dates)}</span></div>'
            f'<div class="row"><span class="org">{e(org)}</span><span class="loc">{e(loc)}</span></div>'
            f'<ul>{lis}</ul>')

def cv_html(c):
    body = [f'<h1>Thomas Goulard</h1><div class="contact">' + "".join(f"<div>{e(x)}</div>" for x in CONTACT + [c["location"]]) + '</div>',
            f'<div class="target">{e(c["target"])}</div>',
            '<h2>Professional experience</h2>',
            entry(c.get("bred_title", "Assistant Relationship Manager – Financial Institutions (Apprentice)"), "09/2025 - 08/2026", "BRED Banque Populaire – Groupe BPCE", "Paris, France", c["bred"]),
            entry("Relationship Manager – Private Wealth Professionals Sector (Apprentice)", "11/2024 - 08/2025", "Chambre Nationale des Conseils en Gestion de Patrimoine", "Paris, France", c["cncgp"]),
            entry("Relationship Manager – Retail Banking (Apprentice)", "09/2023 - 09/2024", "BNP Paribas", "Paris, France", BNP),
            '<h2>Education</h2>',
            entry("Master's in Management, Finance specialization – English Track", "09/2024 - 09/2026", "Grenoble École de Management", "Paris, France", [
                f"2-year Master within a 3-year Grande École programme, completed alongside the apprenticeships above; all courses validated, GPA 14/20; studies completed September 2026, diploma conferred December 2026. Selected modules: {c['modules']}.",
                "Master's thesis (graded 17.5/20, highest distinction): “Value creation or destruction in European football”, financing structures, leverage and cash flows of clubs acquired by investment funds, on a dataset built from their accounts."]),
            entry("Bachelor's Degree in Banking and Insurance", "09/2023 - 09/2024", "École Supérieure de la Banque", "Paris, France", [c["esb"]]),
            entry("Bachelor's Degree in Geography", "09/2021 - 06/2023", "University of Tours", "Tours, France", [c["tours"]]),
            '<h2>Skills, languages & certifications</h2>',
            '<ul>' + "".join(f"<li>{e(x)}</li>" for x in [c["skill1"], TOOLS, LANGS]) + '</ul>',
            '<h2>Extracurricular and leadership activities</h2>',
            '<ul>' + "".join(f"<li>{e(x)}</li>" for x in EXTRA) + '</ul>']
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CV Thomas Goulard</title><style>{CSS}</style></head><body><div class="page">{"".join(body)}</div></body></html>'

def letter_html(l):
    paras = "".join(f"<p>{e(p)}</p>" for p in l["paras"])
    sign = (f"<p>{e(l['signoff'])}</p>" if l["signoff"] else "") + "<p>Thomas Goulard</p>"
    body = (f'<h1>Thomas Goulard</h1><div class="small">{e(l["address"])}</div>'
            f'<div class="small">+33 6 64 29 38 33 | thomasgoulardpro@gmail.com</div>'
            f'<div class="date">{e(l["date"])}</div><div class="subject">{e(l["subject"])}</div>'
            f'<p>{e(l["salutation"])}</p>{paras}{sign}')
    return f'<!doctype html><html lang="{l["lang"]}"><head><meta charset="utf-8"><title>Lettre Thomas Goulard</title><style>{CSS}</style></head><body class="letter"><div class="page">{body}</div></body></html>'

for k, c in CVS.items():
    open(os.path.join(OUT, f"CV_Thomas_Goulard_{k}.html"), "w").write(cv_html(c))
for k, l in LETTERS.items():
    name = "Lettre_Motivation" if l["lang"] == "fr" else "Cover_Letter"
    open(os.path.join(OUT, f"{name}_Thomas_Goulard_{k}.html"), "w").write(letter_html(l))
print("\n".join(sorted(os.listdir(OUT))))
