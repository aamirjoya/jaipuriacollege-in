# Jaipuria College — jaipuriacollege.in

Independent English education-news portal (Google Discover traffic play):
college admission alerts, exam results / admit cards, scholarships, education news.

## Stack

- Hugo static site (no theme, no JS frameworks, single CSS file)
- Builds with stock Hugo — no Node, no Python, no submodules

## Cloudflare Pages dashboard settings

When connecting the GitHub repo in Pages (rifabulhasan@gmail.com account):

| Setting            | Value          |
|--------------------|----------------|
| Framework preset   | None           |
| Build command      | `hugo --minify`|
| Build output dir   | `public`       |
| Environment var    | `HUGO_VERSION = 0.147.4` |

Then Pages → Custom domains → add `jaipuriacollege.in` (and `www` if wanted).

## Local build

```sh
~/workspace/blog-lexx/bin/hugo --minify   # must exit 0
```

## Content

- Articles: `content/<admissions|results|scholarships|education-news>/*.md`
- Featured images: `static/images/<slug>.webp` — real photos only, exactly
  1200x675 WebP q~82. After adding/removing images, regenerate
  `data/imagemeta.json` (maps `images/x.webp` → bytes; used for RSS enclosures):

```sh
python3 -c "
import os, json
json.dump({('images/'+f): os.path.getsize('static/images/'+f) for f in sorted(os.listdir('static/images'))}, open('data/imagemeta.json','w'), indent=1)
"
```

- Frontmatter per article: `title`, `date`, `description`, `author: "Editorial Desk"`,
  `featured_image: "/images/<slug>.webp"`, `featured_image_alt`, `faq:` list.

## Notes / gotchas found while building

- Go's html/template treats `<script type="application/ld+json">` as a JSON
  context: plain `{{ .Title }}` interpolation is auto-quoted/escaped correctly,
  but `{{ .Title | jsonify }}` DOUBLE-encodes (jsonify output gets JSON-escaped
  again). So: never use `jsonify` on individual values inside ld+json blocks —
  interpolate raw values and let the escaper do its job (same pattern as
  blog-lexx's schema_json.html).
- `{{ with .Params.featured_image }}` rebinds `.` to the string — capture the
  page in a `$p` variable before `with` when you need `.Permalink` etc. inside.
