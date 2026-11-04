# ==========================================================================
# dir_data.py: directory data and helper functions (loaded by build.py)
# Edit FIRMS below to add, change or remove listed firms, then run build.py.
# ==========================================================================

# PLACEHOLDER: True while FIRMS are sample names. While True, directory pages are hidden from search engines
# (noindex), left out of the sitemap, and marked with a "sample listing" banner. Set False for real listings.
PLACEHOLDER=True   # set False once real, consenting firms replace the samples below
# FIRMS: one tuple per firm. Fields, in order:
#   (url-slug, business name, type, [service slugs from SERV], [location slugs from LOC], description)
# Slugs must match entries in build.py or the build will fail.
FIRMS=[
("sample-survey-group","Sample Survey Group","Land surveying",["land-subdivision","boundary-marking-disputes","easements","title-amendments"],["melbourne","casey-cardinia","werribee"],"Placeholder listing. Replace with a real firm's description of its subdivision and boundary survey work."),
("example-cadastral-partners","Example Cadastral Partners","Land surveying",["boundary-marking-disputes","feature-and-level-survey","building-set-out","flood-level-survey"],["geelong","ballarat","melbourne"],"Placeholder listing. Replace with a real firm's description of its cadastral and level survey work."),
("placeholder-geospatial","Placeholder Geospatial","Land surveying",["aerial-drone-survey","laser-scanning-3d-modelling","volume-surveys","feature-and-level-survey"],["bendigo","shepparton","melbourne"],"Placeholder listing. Replace with a real firm's description of its drone, scanning and volume survey work."),
("demo-civil-engineering","Demo Civil Engineering","Engineering",["driveway-roading-services-design","retaining-wall-design","geotechnical-testing"],["melbourne","mornington-peninsula","casey-cardinia"],"Placeholder listing. Replace with a real firm's description of its civil and structural design work."),
("sample-geotech-and-structures","Sample Geotech & Structures","Engineering",["geotechnical-testing","retaining-wall-design"],["gippsland","wodonga","shepparton"],"Placeholder listing. Replace with a real firm's description of its geotechnical and structural work."),
("example-planning-studio","Example Planning Studio","Town planning",["town-planning-permits","land-subdivision"],["melbourne","mornington-peninsula","geelong"],"Placeholder listing. Replace with a real firm's description of its planning permit and subdivision work."),
("placeholder-land-development","Placeholder Land Development Co","Development support",["land-subdivision","town-planning-permits","easements"],["ballarat","bendigo","wodonga"],"Placeholder listing. Replace with a real firm's description of its project management and feasibility work."),
("demo-regional-survey","Demo Regional Survey","Land surveying",["land-subdivision","boundary-marking-disputes","title-amendments","building-set-out"],["gippsland","wodonga","shepparton","bendigo"],"Placeholder listing. Replace with a real firm's description of its regional survey work."),
]
# SN / LN: look up a service or location display name from its slug.
SN={x[0]:x[1] for x in SERV};LN={x[0]:x[1] for x in LOC}
# fcard(): one clickable firm card (used on the directory and on service/location pages).
def fcard(f):
    return f'<a class="tile" href="{BASE}/directory/{f[0]}/"><h3>{f[1]}</h3><p><strong>{f[2]}</strong><br>{", ".join(LN[l] for l in f[4][:3])}</p>{"<p class=small>Sample listing</p>" if PLACEHOLDER else ""}</a>'
# firmsec(): a "Firms offering X" or "Firms servicing Y" block for a service page (svc=) or location page (loc=).
# Returns nothing if no firm matches.
def firmsec(svc=None,loc=None):
    m=[f for f in FIRMS if (svc in f[3] if svc else loc in f[4])]
    if not m: return ""
    t=("Firms offering "+SN[svc]) if svc else ("Firms servicing "+LN[loc])
    return f'<h2>{t}</h2><div class="grid">{"".join(fcard(f) for f in m)}</div><p><a href="{BASE}/directory/">Browse the full directory →</a></p>'
