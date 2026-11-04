"""
LDC Directory: static site generator
====================================
Run:  python3 build.py
Output: writes the finished website into the folder named OUT (LDC-Directory/).
Needs (in the same folder): dir_data.py (directory firms), dir_pages.py (directory pages).
Static assets (css/, js/, images/) are copied in by hand, not generated here.

How it works
  1. Content lives in Python lists below (SERV = services, LOC = locations).
  2. page() wraps any body HTML in the shared header, footer, SEO tags and schema.org data.
  3. Each page() call writes one folder/index.html. A sitemap.xml and robots.txt are made at the end.

Common edits
  - Domain change: edit SITE and BASE just below, then re-run.
  - New service or location: add a line to SERV or LOC; pages, menus and links update automatically.
  - Directory firms: edit dir_data.py. Contact form address: edit form().
"""
import os,json,datetime,html
# --- Site settings -------------------------------------------------------
# SITE = full public address with no trailing slash (used in canonical links, sitemap, schema).
SITE="https://salsaus.github.io/LDC-Directory"   # change to custom domain later
# BASE = placeholder for the link prefix. With RELATIVE_LINKS it is swapped for ./ or ../ in w() below.
# RELATIVE_LINKS = True makes every internal link and file path relative to the page it is on
# (e.g. ../services/), so the site works from ANY address or folder: a GitHub project page,
# a sub-folder, or a custom domain. Leave it True unless you have a reason not to.
# (Set the environment variable LDC_ABS=1 to use absolute /LDC-Directory/... links instead.)
RELATIVE_LINKS=not os.environ.get("LDC_ABS")
BASE="@@" if RELATIVE_LINKS else "/LDC-Directory"                              # set "" if using a custom domain
# NAME and EMAIL appear in the header, footer and structured data.
NAME="Land Development Consultants"
EMAIL="services@blueweta.com"
# TODAY is stamped into the sitemap as the last-modified date.
TODAY=datetime.date.today().isoformat()
# OUT = folder the finished site is written to.
OUT=os.environ.get("LDC_OUT","LDC-Directory")
# pages collects (url, priority) for every indexable page, to build sitemap.xml at the end.
pages=[]
# w(): write a file (creating folders as needed) inside OUT.
def w(path,content):
    # Swap the "@@/" link placeholder for a real prefix: "../" per folder level (relative links).
    # 404.html is served from whatever address was mistyped, so it uses the full SITE address instead.
    if path.endswith(".html"):
        rel=SITE+"/" if path=="404.html" else ("../"*path.count("/") or "./")
        content=content.replace("@@/",rel)
    p=os.path.join(OUT,path);os.makedirs(os.path.dirname(p) or OUT,exist_ok=True)
    open(p,"w",encoding="utf-8").write(content)
# --- Content data ----------------------------------------------------------
# SERV: one tuple per service. Fields, in order:
#   (url-slug, short name, SEO page heading, intro paragraph, [what is included], FAQ question, FAQ answer)
# Each tuple becomes a page at /services/<slug>/ and appears in menus, dropdowns and footers.
SERV=[
("land-subdivision","Land Subdivision","Subdivision surveyors in Victoria","Splitting a lot into two or into a large estate needs a licensed surveyor to prepare the plan of subdivision, work with council and lodge it with Land Use Victoria.",["Plan of subdivision preparation","Council and referral authority liaison","Statement of compliance support","Staged and multi-lot estates"],"How long does a subdivision take in Victoria?","Simple two-lot subdivisions commonly take several months from planning permit to new titles. Complexity, council workload and servicing requirements all affect timing."),
("boundary-marking-disputes","Boundary Marking & Re-establishment","Boundary survey and title re-establishment","A re-establishment survey locates your legal boundaries from title and survey records and marks them on the ground, helping before you build a fence, or when neighbours disagree.",["Boundary pegging and re-establishment","Fence and encroachment checks","Identification surveys for building","Evidence reports for boundary disputes"],"When do I need a boundary survey?","Before building near a boundary, fencing, buying a property with unclear boundaries, or when a neighbour disputes where the line is."),
("easements","Easements: Create or Remove","Easement surveys and variations","Easements give others rights over your land, for drainage, access or services. A surveyor can prepare plans to create, vary or remove them.",["Easement creation plans","Removal and variation applications","Drainage and services easements","Liaison with authorities and owners"],"Can an easement be removed?","Sometimes. It usually needs the consent of the party that benefits from it and the correct application through the right authority, supported by a survey plan."),
("title-amendments","Title Amendments","Title amendment and re-consolidation surveys","Merging lots, correcting titles or amending plans requires survey plans lodged with Land Use Victoria.",["Consolidation of lots","Plan amendments","Title boundary corrections","Lodgement with Land Use Victoria"],"What is a title consolidation?","Combining two or more adjoining titles into one, often to build across a former boundary."),
("feature-and-level-survey","Feature & Level Surveys","Feature and level survey Victoria","A feature and level survey records ground levels, buildings, trees, services and boundaries. It is the base for architects, engineers and planners.",["Contours and spot levels","Buildings, fences, trees and services","Boundary relationships","CAD and PDF deliverables"],"Who needs a feature and level survey?","Architects, builders, designers and engineers use it before designing a house, extension or development."),
("flood-level-survey","Flood Level Surveys","Flood level surveys for building permits","Many Victorian sites need a flood level survey to confirm floor levels relative to council or authority flood levels.",["Ground and floor level certification","Relating levels to flood data","Support for permit applications","Existing building level checks"],"Do I need a flood level survey?","Possibly, if your site is in a flood overlay. Check with your council or building surveyor."),
("building-set-out","Building Set-out","Building set-out surveyors","A set-out survey marks where a building, slab or structure goes, so it is built in the right location and at the right level.",["Slab and footing set-out","Boundary offsets","Level control","As-built checks"],"Why does set-out matter?","Errors in location or height can breach permits and setbacks and are expensive to fix after construction."),
("laser-scanning-3d-modelling","Laser Scanning & 3D Modelling","3D laser scanning and modelling","Laser scanning captures millions of measurements to produce accurate point clouds and 3D models of buildings, sites and structures.",["Point cloud capture","3D models for design and heritage","Building and façade documentation","Volume and clash analysis"],"What is laser scanning used for?","Renovations, heritage records, industrial sites, and as a high-detail base for design work."),
("aerial-drone-survey","Aerial Drone Survey","Drone surveys and aerial mapping","Drone surveys cover large or hard-to-reach sites quickly, producing orthophotos, contours and 3D surface models.",["Orthophotos and contours","Stockpile and volume surveys","Progress monitoring","Large rural and development sites"],"Are drone surveys accurate?","With ground control, they can deliver accuracy suitable for many design and volume uses. Your professional will advise on suitability."),
("volume-surveys","Volume Surveys","Stockpile and earthworks volume surveys","Volume surveys measure stockpiles, cut and fill or excavations for payment, compliance and planning.",["Stockpile volumes","Cut and fill calculations","Quarry and earthworks","Drone or ground-based methods"],"How are volumes calculated?","By comparing surveyed surfaces against a base or design surface to compute cut and fill volumes."),
("retaining-wall-design","Retaining Wall Design","Retaining wall engineers","Retaining walls hold back soil and are safety-critical. An engineer designs them for loads, drainage and ground conditions.",["Structural design and drawings","Drainage detailing","Geotechnical coordination","Permit documentation"],"Do retaining walls need engineering?","Walls above certain heights, or those near boundaries and structures, commonly need engineering and a permit. Confirm with your building surveyor."),
("driveway-roading-services-design","Driveway, Roading & Services Design","Civil engineering driveway and roading design","Civil design covers driveways, roads, stormwater, sewer and water layouts required for permits and subdivisions.",["Driveway grades and access","Road and drainage design","Services layout plans","Engineering plan approval support"],"What does civil design include?","Typically levels, grading, stormwater, and road or accessway details prepared to meet council and authority standards."),
("town-planning-permits","Town Planning & Permits","Town planners and planning permits Victoria","Town planners assess your site against the planning scheme and prepare permit applications for subdivision, development and use.",["Planning feasibility advice","Permit applications","Overlay and zoning review","VCAT and objection support"],"Do I need a planning permit?","It depends on zoning, overlays and what you propose. A planner can confirm before you spend on design."),
("geotechnical-testing","Geotechnical Testing","Geotechnical engineers and soil testing","Geotechnical testing identifies soil type, reactivity and bearing capacity to guide foundations and retaining walls.",["Soil classification","Bearing capacity","Slope stability","Reports for building permits"],"Why test the soil?","Soil behaviour determines foundation design. Poor information can lead to cracking and costly rectification."),
]
# LOC: one tuple per location: (url-slug, display name, local blurb). Each becomes /locations/<slug>/.
LOC=[("melbourne","Melbourne","Inner and outer Melbourne: infill subdivisions, townhouse developments and unit sites across metropolitan councils."),
("geelong","Geelong & Surf Coast","Geelong, Surf Coast and Bellarine growth areas, plus coastal planning overlays."),
("ballarat","Ballarat","Ballarat and surrounding Central Highlands towns, including growing residential estates."),
("bendigo","Bendigo","Bendigo and Loddon Mallee, covering residential, rural living and regional development."),
("mornington-peninsula","Mornington Peninsula","Peninsula sites with coastal, bushfire and environmental overlays that affect subdivision and design."),
("gippsland","Gippsland","Latrobe Valley and wider Gippsland: rural subdivisions, boundary work and flood-prone land."),
("shepparton","Shepparton & Goulburn Valley","Goulburn Valley rural and urban sites, with significant flood and irrigation considerations."),
("werribee","Werribee & Melbourne West","Fast-growing western growth corridor sites in Wyndham and Melton."),
("casey-cardinia","Casey & Cardinia","South-east growth areas covering Cranbourne, Pakenham and Officer."),
("wodonga","Wodonga & North East Victoria","Border and north-east Victoria sites, including rural and alpine fringe land."),]
# --- Helpers -------------------------------------------------------------
# esc(): escape text so it is safe inside HTML attributes.
def esc(s): return html.escape(s,quote=True)
# nav(): the skip link plus sticky header (logo, menu button, main menu). Classes match css/styles.css; the menu button is wired up in js/main.js.
def nav():
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap bar"><a class="logo" href="{BASE}/" aria-label="{NAME} home"><img src="{BASE}/images/BlueWeta.png" alt="{NAME}" height="48"> {NAME}</a><button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" class="nav" aria-label="Main"><a href="{BASE}/directory/">Directory</a><a href="{BASE}/services/">Services</a><a href="{BASE}/locations/">Locations</a><a href="{BASE}/about/">About</a><a href="{BASE}/faq/">FAQ</a><a class="btn btn-small" href="{BASE}/contact/">Get matched</a></nav></div></header>'''
# foot(): the site footer (about blurb, service and location links, company links) and the current year, which js/main.js keeps updated.
def foot():
    s="".join(f'<li><a href="{BASE}/services/{x[0]}/">{x[1]}</a></li>' for x in SERV[:7])
    l="".join(f'<li><a href="{BASE}/locations/{x[0]}/">{x[1]}</a></li>' for x in LOC[:7])
    return f'''<footer class="site-footer"><div class="wrap foot"><div><strong>{NAME}</strong><p class="small">Victoria, Australia<br>Connecting clients to licensed professionals.</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div><div><strong>Services</strong><ul>{s}</ul></div><div><strong>Locations</strong><ul>{l}</ul></div><div><strong>Company</strong><ul><li><a href="{BASE}/directory/">Directory</a></li><li><a href="{BASE}/list-your-business/">List your business</a></li><li><a href="{BASE}/about/">About</a></li><li><a href="{BASE}/faq/">FAQ</a></li><li><a href="{BASE}/contact/">Contact</a></li><li><a href="{BASE}/privacy/">Privacy</a></li></ul></div></div><p class="wrap copy small">&copy; <span id="year">{datetime.date.today().year}</span> {NAME}. Connecting clients to licensed professionals.</p></footer>'''
# form(): the enquiry form. Posts to Formspree (emails you). js/main.js validates it and shows messages. Change the action URL here to use another form service.
#   pre = text pre-filled in the message box; heading = the form's title.
def form(pre="",heading="What do you need help with?"):
    opts="".join(f'<option>{x[1]}</option>' for x in SERV)+"<option>Other</option>"
    return f'''<form class="quote" id="quote" action="https://formspree.io/f/xwllwjvz" method="POST" novalidate><h2>{heading}</h2><label for="service">Service</label><select id="service" name="service" required><option value="">Choose a service…</option>{opts}</select><label for="suburb">Address of your site</label><input id="suburb" name="suburb" type="text" autocomplete="postal-code" placeholder="e.g. Ballarat 3350" required><label for="email">Your email</label><input id="email" name="email" type="email" autocomplete="email" placeholder="you@example.com" required><label for="details">Tell us what you want</label><textarea id="details" name="details" rows="3">{esc(pre)}</textarea><button class="btn" type="submit">Get matched with a professional</button><p class="form-msg" id="form-msg" role="status" aria-live="polite"></p></form>'''
# crumbs(): builds BreadcrumbList structured data so Google can show breadcrumb trails in results.
def crumbs(items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(items)]}
# page(): the core template. Every page goes through here.
#   path = output folder ("" for home), title/desc = <title> and meta description,
#   body = main HTML, schema = extra schema.org items, crumb = breadcrumb list,
#   prio = sitemap priority, noindex = True hides the page from search engines and the sitemap.
def page(path,title,desc,body,schema=None,crumb=None,og="website",prio="0.7",noindex=False):
    url=SITE+"/"+path
    g=[{"@type":"Organization","@id":SITE+"/#org","name":NAME,"url":SITE+"/","logo":SITE+"/images/BlueWeta.png","email":EMAIL,"areaServed":{"@type":"State","name":"Victoria"}}]
    if crumb: g.append(crumbs(crumb))
    if schema: g+=schema
    ld=json.dumps({"@context":"https://schema.org","@graph":g},ensure_ascii=False)
    h=f'''<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}<meta name="geo.region" content="AU-VIC"><meta property="og:type" content="{og}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/images/BlueWeta.png"><meta property="og:locale" content="en_AU"><meta name="twitter:card" content="summary"><link rel="icon" href="{BASE}/images/favicon.svg" type="image/svg+xml"><link rel="icon" href="{BASE}/images/Logo.png" type="image/png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="{BASE}/css/styles.css"><script type="application/ld+json">{ld}</script></head><body>
<!-- Header and navigation -->{nav()}
<!-- Page content -->
<main id="main">{body if body.startswith("<section") else "<div class=inner>"+body+"</div>"}</main>
<!-- Footer -->{foot()}
<!-- Menu toggle, form handling and footer year -->
<script src="{BASE}/js/main.js"></script></body></html>'''
    w(path+("index.html" if path.endswith("/") or path=="" else ""),h)
    if not noindex: pages.append((url,prio))
# bc(): breadcrumb list starting from Home (used for schema data).
def bc(*items): return [("Home","/")]+list(items)
# faqld(): turns (question, answer) pairs into FAQPage structured data (can earn rich results).
def faqld(qs): return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qs]}
# crumbhtml(): the visible breadcrumb links shown above page headings.
def crumbhtml(items): return '<nav class="crumbs" aria-label="Breadcrumb"><a href="'+BASE+'/">Home</a>'+"".join(f' › <a href="{BASE}{u}">{n}</a>' for n,u in items)+'</nav>'
# ==========================================================================
# HOME PAGE: hero + enquiry form, services grid, how it works, who we are, FAQ, Victoria
# (hf = the home page FAQ, also used as FAQ schema)
# ==========================================================================
# HOME
cards="".join(f'<a class="tile" href="{BASE}/services/{x[0]}/"><h3>{x[1]}</h3><p>{x[3][:92]}…</p></a>' for x in SERV)
hf=[("Do I need a surveyor, engineer or planner?","Tell us your goal. Surveyors measure and define land, engineers design, and planners handle approvals. We point you to the right discipline."),("Is it free to enquire?","Yes. Enquiries are free and carry no obligation."),("Are the professionals licensed?","We only introduce licensed Victorian surveyors and engineers.")]
locs=" · ".join(f'<a href="{BASE}/locations/{l[0]}/">{l[1]}</a>' for l in LOC)
home=f'''<section class="hero" id="top"><div class="wrap hero-grid"><div><h1>Land surveyors &amp; engineers in Victoria, found fast.</h1><p class="lead">Tell us about your development needs. We connect you with licensed Victorian land surveyors and engineering firms who do exactly that work.</p><ul class="ticks"><li>Free to enquire, no obligation</li><li>Licensed surveyors and engineers only</li><li>One enquiry, the right introductions</li></ul></div>{form()}</div></section>
<section class="section" id="services"><div class="wrap"><h2 class="section-title">Surveying, engineering and development help in one place</h2><p class="section-intro">Not sure who you need? Start here. We know which discipline solves which problem, and who in Victoria is licensed to do it.</p><div class="grid svc-cards">{cards}</div></div></section>
<section class="section tint" id="how"><div class="wrap"><h2 class="section-title">How it works</h2><ol class="steps"><li><h3>Tell us what you need</h3><p>Not sure whether you need a surveyor, an engineer or a planner? Just tell us your goal and we will take it from there.</p></li><li><h3>We find the right people</h3><p>We match your job to licensed surveyors and engineers who handle it regularly.</p></li><li><h3>Professionals do the work</h3><p>Your selected professionals will handle the job with expertise and care.</p></li></ol></div></section>
<section class="section" id="who"><div class="wrap split"><div><h2 class="section-title">Who we are</h2><p class="big">15+ years across surveying and engineering.</p></div><div class="prose"><p>We have worked on both sides of the land development process, in surveying and in civil engineering, across projects from single-lot title fixes to staged subdivisions.</p><p>That experience taught us one thing above all: the right licensed professional matters. In Australia, cadastral surveying and engineering sign-off are regulated for good reason. The wrong person can cost you months, a failed council or title submission, or a boundary you have to redo.</p><p>So we do not guess. We ask the right questions up front and point you to someone qualified for that specific job.</p></div></div></section>
<section class="section tint" id="faq"><div class="wrap narrow"><h2 class="section-title">Frequently asked questions</h2>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in hf)}<p><a href="{BASE}/faq/">More questions answered →</a></p></div></section>
<section class="section victoria" id="victoria"><div class="wrap split"><div><h2 class="section-title">A Victorian company, built to make this easy</h2></div><div class="prose"><p>We are based in Victoria and know how things work here: council planning schemes, water authority requirements, Land Use Victoria titles and the realities of regional and metropolitan sites.</p><p class="links">Areas we cover: {locs}</p><a class="btn" href="#quote">Start your enquiry</a></div></div></section>'''
page("","Land Surveyors & Engineers Victoria | Land Development Consultants","Find licensed land surveyors and civil engineers in Victoria for subdivisions, boundary surveys, easements, level surveys and planning. Free to enquire.",home,[{"@type":"WebSite","@id":SITE+"/#site","url":SITE+"/","name":NAME,"inLanguage":"en-AU"},{"@type":"ProfessionalService","name":NAME,"url":SITE+"/","email":EMAIL,"areaServed":"Victoria, Australia","description":"Directory connecting clients with licensed surveyors and land development engineers in Victoria."},faqld(hf)],prio="1.0")
# Load directory data and helper functions (FIRMS, fcard, firmsec). Must run before the service and location pages, which list firms.
exec(open("dir_data.py").read())
# ==========================================================================
# SERVICE PAGES: an index page, then one page per entry in SERV (with listed firms, FAQ and related services)
# ==========================================================================
# SERVICES
page("services/","Land Surveying & Engineering Services in Victoria",
"Browse surveying, engineering and planning services for Victorian land development, from subdivisions to geotechnical testing.",
f'<div class="wrap">{crumbhtml([("Services","/services/")])}<h1>Land Development Services in Victoria</h1><div class="grid">{cards}</div></div>',crumb=bc(("Services","/services/")),prio="0.9")
for i,s in enumerate(SERV):
    slug,name,kw,intro,inc,q,a=s
    rel="".join(f'<li><a href="{BASE}/services/{r[0]}/">{r[1]}</a></li>' for r in SERV if r[0]!=slug)[:0]
    rel="".join(f'<li><a href="{BASE}/services/{SERV[(i+k)%len(SERV)][0]}/">{SERV[(i+k)%len(SERV)][1]}</a></li>' for k in (1,2,3))
    locs="".join(f'<a href="{BASE}/locations/{l[0]}/">{l[1]}</a> · ' for l in LOC[:6])
    b=f'<div class="wrap pg">{""}<article>{crumbhtml([("Services","/services/"),(name,"/services/"+slug+"/")])}<h1>{kw}</h1><p class="lead">{intro}</p><h2>What is included</h2><ul class="ticks">{"".join(f"<li>{x}</li>" for x in inc)}</ul><h2>Why use a licensed professional?</h2><p>In Australia, cadastral surveying and engineering sign-off are regulated. Using the wrong person can mean failed council or title submissions and costly rework. We match you with someone qualified for this specific job.</p><h2>Available across Victoria</h2><p>{locs}<a href="{BASE}/locations/">all locations</a></p>{firmsec(svc=slug)}<h2>FAQ</h2><details open><summary>{q}</summary><p>{a}</p></details><h2>Related services</h2><ul>{rel}</ul></article><aside>{form("I need help with: "+name)}</aside></div>'
    page(f"services/{slug}/",f"{kw} | {NAME}",f"{intro[:140].rstrip()}… Get matched with licensed Victorian professionals."[:158],b,[{"@type":"Service","name":name,"serviceType":name,"provider":{"@id":SITE+"/#org"},"areaServed":"Victoria, Australia","description":intro},faqld([(q,a)])],bc(("Services","/services/"),(name,"/services/"+slug+"/")),prio="0.9")
# ==========================================================================
# LOCATION PAGES: an index page, then one page per entry in LOC
# ==========================================================================
# LOCATIONS
page("locations/","Surveyors & Engineers Across Victoria",
"Find licensed land surveyors, engineers and town planners across Melbourne and regional Victoria.",
f'<div class="wrap">{crumbhtml([("Locations","/locations/")])}<h1>Surveyors &amp; Engineers Across Victoria</h1><div class="grid">{"".join(f"<a class=tile href={BASE}/locations/{l[0]}/><h3>{l[1]}</h3><p>{l[2]}</p></a>" for l in LOC)}</div></div>',crumb=bc(("Locations","/locations/")),prio="0.8")
for slug,name,blurb in LOC:
    sl="".join(f'<li><a href="{BASE}/services/{s[0]}/">{s[1]} in {name}</a></li>' for s in SERV)
    q=f"Do you cover {name}?"; a=f"Yes. We match {name} projects with licensed surveyors and engineers who work in the area."
    b=f'<div class="wrap pg"><article>{crumbhtml([("Locations","/locations/"),(name,"/locations/"+slug+"/")])}<h1>Land Surveyors &amp; Engineers in {name}</h1><p class="lead">{blurb}</p><p>Local knowledge matters: council planning schemes, overlays and servicing authorities differ across Victoria. We introduce you to professionals who know your area.</p><h2>Services in {name}</h2><ul>{sl}</ul>{firmsec(loc=slug)}<h2>FAQ</h2><details open><summary>{q}</summary><p>{a}</p></details></article><aside>{form("Site in "+name+". ")}</aside></div>'
    page(f"locations/{slug}/",f"Land Surveyors & Engineers in {name} | {NAME}",f"Licensed land surveyors, engineers and planners in {name}, Victoria. Subdivisions, boundary and level surveys, easements and more. Free to enquire.",b,[faqld([(q,a)])],bc(("Locations","/locations/"),(name,"/locations/"+slug+"/")),prio="0.8")
# Build the directory index, every firm profile page and the "List your business" page.
exec(open("dir_pages.py").read())
# ==========================================================================
# GENERAL PAGES: FAQ, About, Contact, Privacy, then the 404 page
# ==========================================================================
# FAQ
FQ=[("How much does a land survey cost in Victoria?","Cost depends on site size, complexity and survey type. Describe your project and professionals can quote."),("Do I need a surveyor to subdivide?","Yes. A licensed surveyor prepares the plan of subdivision and lodges it for title."),("What is the difference between a surveyor and an engineer?","Surveyors measure and define land. Engineers design infrastructure and structures."),("Can you help if my neighbour disputes the boundary?","A re-establishment survey is the usual first step."),("Do you service regional Victoria?","Yes, across Victoria."),("How quickly will I hear back?","Submit an enquiry and we aim to respond promptly with next steps.")]+hf
page("faq/","FAQ: Surveying & Land Development in Victoria","Answers to common questions about land surveys, subdivisions, boundaries, engineers and costs in Victoria.",
f'<div class="wrap narrow">{crumbhtml([("FAQ","/faq/")])}<h1>Frequently Asked Questions</h1>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in FQ)}</div>',[faqld(FQ)],bc(("FAQ","/faq/")))
page("about/","About Us | Land Development Consultants","15+ years across surveying and civil engineering. We connect Victorian landowners with the right licensed professionals.",
f'<div class="wrap narrow">{crumbhtml([("About","/about/")])}<h1>About {NAME}</h1><p class="lead">15+ years across surveying and engineering.</p><p>We have worked on both sides of land development, from single-lot title fixes to staged subdivisions. We know that the right licensed professional matters, and we ask the right questions up front.</p><p>Based in Victoria, we understand council planning schemes, water authority requirements and Land Use Victoria titles.</p><p><a class="btn" href="{BASE}/contact/">Start your enquiry</a></p></div>',crumb=bc(("About","/about/")),prio="0.5")
page("contact/","Get Matched with a Surveyor or Engineer | Contact","Send one enquiry and get introduced to licensed Victorian surveyors and engineers. Free, no obligation.",
f'<div class="wrap narrow"><h1>Get Matched with a Licensed Professional</h1>{form()}<p>Or email <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>',crumb=bc(("Contact","/contact/")),prio="0.8")
page("privacy/","Privacy Policy",f"Privacy policy for {NAME}.",f'<div class="wrap narrow"><h1>Privacy Policy</h1><p>We collect the details you submit (email, site address, project description) only to match you with professionals and respond to your enquiry. We share them with matched professionals for that purpose. Contact {EMAIL} to request access or deletion.</p><p class="small">Replace with a full policy reviewed for the Privacy Act 1988 (Cth).</p></div>',prio="0.2")
# 404 page: GitHub Pages shows this automatically for missing addresses (noindex so it is not listed).
w("404.html",f'<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found</title><meta name="robots" content="noindex"><link rel="stylesheet" href="{BASE}/css/styles.css"></head><body>{nav()}<main class="inner narrow"><h1>Page not found</h1><p><a href="{BASE}/">Back to home</a> or <a href="{BASE}/services/">browse services</a>.</p></main></body></html>')
# --- Search engine files ---------------------------------------------------
# sitemap.xml lists every indexable page. Submit it to Google Search Console and Bing Webmaster Tools.
w("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>" for u,p in pages)+"</urlset>")
# robots.txt allows crawling and points to the sitemap.
w("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
# README for the generated site.
w("README.md","""# Land Development Consultants: Directory Site

Static website (plain HTML, CSS, JS). No framework needed to host it.

## Structure
- `index.html`, `services/`, `locations/`, `directory/`, `faq/`, `about/`, `contact/`, `list-your-business/`, `privacy/`: generated pages
- `css/styles.css`: all styling (colours are variables at the top)
- `js/main.js`: mobile menu, enquiry form, footer year
- `images/`: logo, favicon, hero contours
- `build.py`, `dir_data.py`, `dir_pages.py`: the generator (optional, only needed to regenerate)

## Regenerate pages
`python3 build.py` (keep the three .py files in the same folder).

## Go live
1. Upload everything to the repo root and enable GitHub Pages.
2. Custom domain: add a `CNAME` file, set `SITE` and `BASE` in build.py, rebuild.
3. Directory: replace the sample firms in `dir_data.py`, set `PLACEHOLDER=False`, rebuild.
4. Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools.
""")
# Report how many pages were written.
print(len(pages),"pages")
