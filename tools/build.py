#!/usr/bin/env python3
"""Składa samodzielny index.html z src/game.html (fragment strony bez <html>/<head>).
Uruchom: python3 tools/build.py"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
src = (root / "src" / "game.html").read_text(encoding="utf-8")
cut = src.index('<canvas id="gl">')
head, body = src[:cut], src[cut:]
html = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Szuter Rally – przeglądarkowa gra rajdowa na szutrze w 3D.">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}</style>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html:", len(html), "bajtów")
