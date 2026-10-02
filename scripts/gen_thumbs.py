#!/usr/bin/env python3
"""Generate -thumb.webp thumbnails for all images in static/images/.
Thumbnails are 400px wide (aspect preserved), WebP q72 — for use in
listing cards. Full-size images stay for article hero.
Idempotent: skips thumbnails that are newer than the source.
Usage: python3 scripts/gen_thumbs.py [site_dir]
"""
import os, sys
from PIL import Image

site = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
imgdir = os.path.join(site, 'static', 'images')
THUMB_W = 400

count = 0
for root, _, files in os.walk(imgdir):
    for f in files:
        if not f.lower().endswith('.webp') or f.endswith('-thumb.webp'):
            continue
        src = os.path.join(root, f)
        dst = os.path.join(root, f[:-5] + '-thumb.webp')
        if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
            continue
        try:
            im = Image.open(src).convert('RGB')
            w, h = im.size
            if w > THUMB_W:
                im = im.resize((THUMB_W, int(h * THUMB_W / w)), Image.LANCZOS)
            im.save(dst, 'WEBP', quality=72, method=6)
            count += 1
        except Exception as e:
            print(f"skip {src}: {e}")
print(f"thumbnails generated: {count}")
