# Land Development Consultants: Directory Site

Static website (plain HTML, CSS, JS). No framework needed to host it.

https://salsaus.github.io/LDC-Upload/

--------NOTE BEFORE UPLOAD--------

NoIndex is set in this state prior to upload

noforward should be attached to links to company websites (IF they are to be attached)


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
