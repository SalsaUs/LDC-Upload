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
("sample-survey-group","Sample Survey Group","Surveying",["land-subdivision","boundary-marking-disputes","easements","title-amendments"],["melbourne","casey-cardinia","werribee"],"Placeholder listing. Replace with a real firm's description of its subdivision and boundary survey work."),
("example-cadastral-partners","Example Cadastral Partners","Surveying",["boundary-marking-disputes","feature-and-level-survey","building-set-out","flood-level-survey"],["geelong","ballarat","melbourne"],"Placeholder listing. Replace with a real firm's description of its cadastral and level survey work."),
("placeholder-geospatial","Placeholder Geospatial","Surveying",["aerial-drone-survey","laser-scanning-3d-modelling","volume-surveys","feature-and-level-survey"],["bendigo","shepparton","melbourne"],"Placeholder listing. Replace with a real firm's description of its drone, scanning and volume survey work."),
("demo-civil-engineering","Demo Civil Engineering","Engineering",["driveway-roading-services-design","retaining-wall-design","geotechnical-testing"],["melbourne","mornington-peninsula","casey-cardinia"],"Placeholder listing. Replace with a real firm's description of its civil and structural design work."),
("sample-geotech-and-structures","Sample Geotech & Structures","Engineering",["geotechnical-testing","retaining-wall-design"],["gippsland","wodonga","shepparton"],"Placeholder listing. Replace with a real firm's description of its geotechnical and structural work."),
("example-land-studio","Example Land Studio","Surveying & Engineering",["town-planning-permits","land-subdivision"],["melbourne","mornington-peninsula","geelong"],"Placeholder listing. Replace with a real firm's description of its planning permit and subdivision work."),
("placeholder-land-development","Placeholder Land Development Co","Surveying",["land-subdivision","town-planning-permits","easements"],["ballarat","bendigo","wodonga"],"Placeholder listing. Replace with a real firm's description of its project management and feasibility work."),
("demo-regional-survey","Demo Regional Survey","Surveying",["land-subdivision","boundary-marking-disputes","title-amendments","building-set-out"],["gippsland","wodonga","shepparton","bendigo"],"Placeholder listing. Replace with a real firm's description of its regional survey work."),
("sample-boundary-surveys","Sample Boundary Surveys","Surveying",['boundary-marking-disputes', 'title-amendments', 'easements'],['melbourne', 'werribee', 'casey-cardinia'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-level-and-contour","Example Level & Contour Co","Surveying",['feature-and-level-survey', 'flood-level-survey', 'building-set-out'],['melbourne', 'mornington-peninsula'],"Placeholder listing. Replace with a real firm's description of its work."),
("demo-subdivision-surveyors","Demo Subdivision Surveyors","Surveying & Engineering",['land-subdivision', 'title-amendments', 'easements'],['geelong', 'ballarat', 'bendigo'],"Placeholder listing. Replace with a real firm's description of its work."),
("placeholder-cadastral-group","Placeholder Cadastral Group","Surveying",['boundary-marking-disputes', 'land-subdivision'],['gippsland', 'casey-cardinia', 'mornington-peninsula'],"Placeholder listing. Replace with a real firm's description of its work."),
("sample-title-and-easement","Sample Title & Easement Surveys","Surveying",['title-amendments', 'easements', 'land-subdivision'],['melbourne', 'wodonga'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-flood-and-feature","Example Flood & Feature Surveys","Surveying & Engineering",['flood-level-survey', 'feature-and-level-survey'],['shepparton', 'bendigo', 'wodonga'],"Placeholder listing. Replace with a real firm's description of its work."),
("demo-drone-mapping","Demo Drone Mapping","Surveying",['aerial-drone-survey', 'volume-surveys', 'feature-and-level-survey'],['melbourne', 'geelong', 'ballarat'],"Placeholder listing. Replace with a real firm's description of its work."),
("placeholder-scanning-services","Placeholder 3D Scanning Services","Surveying",['laser-scanning-3d-modelling', 'feature-and-level-survey'],['melbourne', 'werribee'],"Placeholder listing. Replace with a real firm's description of its work."),
("sample-set-out-specialists","Sample Set-out Specialists","Surveying & Engineering",['building-set-out', 'feature-and-level-survey', 'boundary-marking-disputes'],['casey-cardinia', 'mornington-peninsula', 'gippsland'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-volume-surveys","Example Volume Surveys","Surveying",['volume-surveys', 'aerial-drone-survey'],['ballarat', 'bendigo', 'shepparton'],"Placeholder listing. Replace with a real firm's description of its work."),
("sample-civil-design","Sample Civil Design","Engineering",['driveway-roading-services-design', 'retaining-wall-design'],['melbourne', 'werribee', 'casey-cardinia'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-structural-partners","Example Structural Partners","Engineering & Surveying",['retaining-wall-design', 'geotechnical-testing'],['geelong', 'melbourne'],"Placeholder listing. Replace with a real firm's description of its work."),
("demo-geotechnical","Demo Geotechnical Services","Engineering",['geotechnical-testing'],['melbourne', 'gippsland', 'mornington-peninsula'],"Placeholder listing. Replace with a real firm's description of its work."),
("placeholder-drainage-engineers","Placeholder Drainage Engineers","Engineering & Surveying",['driveway-roading-services-design', 'flood-level-survey'],['geelong', 'ballarat', 'bendigo'],"Placeholder listing. Replace with a real firm's description of its work."),
("sample-roads-and-services","Sample Roads & Services Design","Engineering & Surveying",['driveway-roading-services-design', 'land-subdivision'],['shepparton', 'wodonga', 'bendigo'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-retaining-walls","Example Retaining Wall Engineers","Engineering",['retaining-wall-design', 'driveway-roading-services-design'],['mornington-peninsula', 'casey-cardinia', 'melbourne'],"Placeholder listing. Replace with a real firm's description of its work."),
("demo-permit-engineering","Demo Permit Engineering","Engineering",['town-planning-permits'],['melbourne', 'werribee', 'casey-cardinia'],"Placeholder listing. Replace with a real firm's description of its work."),
("placeholder-urban-development","Placeholder Urban Development","Surveying & Engineering",['town-planning-permits', 'land-subdivision'],['geelong', 'ballarat'],"Placeholder listing. Replace with a real firm's description of its work."),
("sample-subdivision-surveys","Sample Subdivision Surveys","Surveying",['town-planning-permits', 'land-subdivision', 'easements'],['gippsland', 'wodonga', 'shepparton'],"Placeholder listing. Replace with a real firm's description of its work."),
("example-development-engineers","Example Development Engineers","Engineering & Surveying",['land-subdivision', 'town-planning-permits'],['melbourne', 'mornington-peninsula'],"Placeholder listing. Replace with a real firm's description of its work."),
("demo-site-survey-partners","Demo Site Survey Partners","Surveying",['land-subdivision', 'title-amendments', 'easements'],['bendigo', 'ballarat', 'geelong'],"Placeholder listing. Replace with a real firm's description of its work."),
("placeholder-site-engineering","Placeholder Site Engineering","Engineering",['land-subdivision', 'driveway-roading-services-design', 'town-planning-permits'],['casey-cardinia', 'werribee', 'melbourne'],"Placeholder listing. Replace with a real firm's description of its work."),
]
# FIRMS tuple: (slug, name, discipline, services, locations, description).
# discipline is shown on the card as "Specialisation": Surveying, Engineering, or both written in the firm's priority order
# (for example "Engineering & Surveying" for an engineering-led firm).

# Every firm is Surveying, Engineering, or both (in priority order). Town planning and other work are services, not firm types.
assert all(f[2] in ("Surveying","Engineering","Surveying & Engineering","Engineering & Surveying") for f in FIRMS), "A firm has an invalid discipline: use Surveying, Engineering, Surveying & Engineering or Engineering & Surveying"

# SN / LN: look up a service or location display name from its slug.
SN={x[0]:x[1] for x in SERV};LN={x[0]:x[1] for x in LOC}
# ==========================================================================
# TIERS AND CARDS
# Every firm in FIRMS gets a card on the directory, service and location pages.
# Clicking a card opens the Get Matched page ("Request a quote from <firm>").
# Only firms listed in CLAIMED also get their own profile page (the firm supplies this
# extra data through the "List your business" form), so unfinished firms never create thin pages.
# ==========================================================================
CLAIMED={
 "example-cadastral-partners":{
  "years":18,"licence":"Licensed surveyor (sample number)",
  "bio":"Sample text: a bio written or approved by the firm, covering the jobs they do most, the councils they know, and who you will deal with.",
  "projects":["Sample project: 4-lot subdivision, Newtown","Sample project: boundary re-establishment, Ocean Grove","Sample project: flood level survey, Belmont"],
  "reviews":[("Sample review: clear quote up front and the plan was lodged ahead of schedule.","Subdivision client")]},
}
def claimed(f): return f[0] in CLAIMED

# SCROLL_AT: a list of more than this many cards scrolls inside a box with a fade along the bottom.
SCROLL_AT=12
def scrollwrap(inner,n,label="Firm list"):
    if n<=SCROLL_AT: return inner
    return '<div class="scroll-wrap"><div class="scroll-frame"><div class="scrollbox" tabindex="0" role="region" aria-label="'+label+'">'+inner+'</div></div><p class="scroll-hint small" aria-hidden="true">Scroll for more firms &darr;</p></div>'

# fcard(): one firm card. Top to bottom: firm name, specialisation, locations, services (click to open), then
# "View profile" (claimed firms only) above "Request a quote".
# The whole card links to the quote page (rel=nofollow keeps crawlers off the ?firm= links); the services toggle and
# the profile link sit above that link (see .firm-tile in css/styles.css).
# svc (optional) is the service slug of the page it appears on, so the quote form can pre-select it.
def fcard(f,svc=None):
    q=BASE+"/contact/?firm="+f[0]+("&amp;service="+svc if svc else "")
    locs=", ".join(LN[l] for l in f[4][:3])+((" +"+str(len(f[4])-3)+" more") if len(f[4])>3 else "")
    sm="<p class=small>Sample listing</p>" if PLACEHOLDER else ""
    prof='<a class="firm-profile" href="'+BASE+'/directory/'+f[0]+'/">View profile &rarr;</a>' if claimed(f) else ""
    svcs="".join("<li>"+SN[x]+"</li>" for x in f[3])
    return ('<div class="tile firm-tile"><h3><a href="'+q+'" rel="nofollow">'+f[1]+'</a></h3>'
            +'<p class="firm-spec">'+f[2]+'</p>'
            +'<p class="firm-loc">'+locs+'</p>'
            +'<details class="firm-services"><summary>Services</summary><ul>'+svcs+'</ul></details>'
            +sm+prof+'<p class="small firm-cta">Request a quote &rarr;</p></div>')

# firmsec(): a "Firms offering X" / "Firms servicing Y" block (claimed firms first). Scrolls when there are many.
def firmsec(svc=None,loc=None):
    m=[f for f in FIRMS if (svc in f[3] if svc else loc in f[4])]
    if not m: return ""
    m.sort(key=lambda f: not claimed(f))
    t=("Firms offering "+SN[svc]) if svc else ("Firms servicing "+LN[loc])
    g='<div class="grid">'+"".join(fcard(f,svc) for f in m)+'</div>'
    return '<h2>'+t+'</h2>'+scrollwrap(g,len(m),t)+'<p><a href="'+BASE+'/directory/">Browse the full directory →</a></p>'

# claimedextra(): extra sections on a claimed firm's profile page.
def claimedextra(f):
    c=CLAIMED[f[0]]
    pr="".join("<li>"+p+"</li>" for p in c["projects"])
    rv="".join("<blockquote><p>"+t+"</p><p class=small>"+w+"</p></blockquote>" for t,w in c["reviews"])
    return '<p class="small"><strong>Licence:</strong> '+c["licence"]+' · <strong>Operating:</strong> '+str(c["years"])+' years</p><h2>Recent projects</h2><ul class="ticks">'+pr+'</ul><h2>Client reviews</h2>'+rv
