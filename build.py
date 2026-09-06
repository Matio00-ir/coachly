# -*- coding: utf-8 -*-
"""Coachly static site generator — nav/footer/head boilerplate, hand-authored body content per page.
Run: python build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Coachly logo mark (Visual Identity V2) — inline SVG so it scales and prints crisp.
# Standalone copy: assets/brand/coachly-mark.svg
BRAND_MARK = (
    '<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="coachlyMark" x1="32" y1="4" x2="15" y2="43" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F0142E"/><stop offset=".4" stop-color="#C20E28"/><stop offset=".75" stop-color="#4E0813"/><stop offset="1" stop-color="#0F0F0F"/></linearGradient></defs><path d="M35.47 32.03 A14 14 0 1 1 35.47 15.97" fill="none" stroke="url(#coachlyMark)" stroke-width="7.6"/><path d="M34.60 7.04 A20 20 0 1 0 34.60 40.98" fill="none" stroke="url(#coachlyMark)" stroke-width="2.3" stroke-linecap="round"/></svg></span>'
)

NAV_ITEMS_EN = [
    ("features.html", "Features", "features"),
    ("for-coaches.html", "For Coaches", "for-coaches"),
    ("for-athletes.html", "For Athletes", "for-athletes"),
    ("pricing.html", "Pricing", "pricing"),
    ("blog/index.html", "Blog", "blog"),
]
NAV_ITEMS_FA = [
    ("features.html", "ویژگی‌ها", "features"),
    ("for-coaches.html", "برای مربیان", "for-coaches"),
    ("for-athletes.html", "برای ورزشکاران", "for-athletes"),
    ("pricing.html", "قیمت‌گذاری", "pricing"),
    ("blog/index.html", "وبلاگ", "blog"),
]

def rel(depth, path):
    """path is relative to the /en or /fa root (depth 0). depth=1 means we're one folder deeper (e.g. blog/)."""
    return ("../" * depth) + path

def nav(lang, active, depth):
    items = NAV_ITEMS_EN if lang == "en" else NAV_ITEMS_FA
    other_lang_path = rel(depth, "../fa/index.html") if lang == "en" else rel(depth, "../en/index.html")
    lang_label = "FA" if lang == "en" else "EN"
    lang_aria = "Switch to Persian" if lang == "en" else "Switch to English"
    home = rel(depth, "index.html")
    cta_label = "Start free" if lang == "en" else "شروع رایگان"
    menu_aria = "Open menu" if lang == "en" else "باز کردن منو"
    theme_aria = "Toggle color theme" if lang == "en" else "تغییر حالت رنگی"
    about_label = "About" if lang == "en" else "دربارهٔ ما"
    primary_links = "\n      ".join(
        '<a href="{href}"{active}>{label}</a>'.format(
            href=rel(depth, href), label=label,
            active=' class="active"' if key == active else ""
        ) for href, label, key in items
    )
    mobile_links = "\n    ".join(
        '<a href="{href}">{label}</a>'.format(href=rel(depth, href), label=label)
        for href, label, key in items
    )
    return '''<header class="nav">
  <div class="container nav-inner">
    <a href="{home}" class="brand">{mark}Coachly</a>
    <nav class="nav-links" aria-label="Primary">
      {primary_links}
    </nav>
    <div class="nav-actions">
      <a href="{other_lang_path}" class="icon-btn lang-switch" aria-label="{lang_aria}">{lang_label}</a>
      <button class="icon-btn" data-theme-toggle aria-label="{theme_aria}">
        <svg class="theme-only-dark" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
        <svg class="theme-only-light" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
      </button>
      <a href="{pricing}" class="btn btn-primary btn-sm nav-cta">{cta_label}</a>
      <button class="icon-btn menu-toggle" data-menu-toggle aria-label="{menu_aria}" aria-expanded="false">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
  <div class="mobile-menu" data-mobile-menu>
    {mobile_links}
    <a href="{about}">{about_label}</a>
    <a href="{pricing}" class="btn btn-primary btn-block">{cta_label}</a>
  </div>
</header>'''.format(
        mark=BRAND_MARK,
        home=home, primary_links=primary_links, other_lang_path=other_lang_path,
        lang_aria=lang_aria, lang_label=lang_label, theme_aria=theme_aria,
        pricing=rel(depth, "pricing.html"), cta_label=cta_label, menu_aria=menu_aria,
        mobile_links=mobile_links, about=rel(depth, "about.html"), about_label=about_label,
    )

def footer(lang, depth):
    home = rel(depth, "index.html")
    other = rel(depth, "../fa/index.html") if lang == "en" else rel(depth, "../en/index.html")
    if lang == "en":
        return '''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <a href="{home}" class="brand">{mark}Coachly</a>
        <p class="body-sm" style="margin-top:16px;max-width:32ch;">Coaching management software for fitness coaches — built to grow with your athletes.</p>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul>
          <li><a href="{features}">Features</a></li>
          <li><a href="{coaches}">For Coaches</a></li>
          <li><a href="{athletes}">For Athletes</a></li>
          <li><a href="{pricing}">Pricing</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="{about}">About</a></li>
          <li><a href="{blog}">Blog</a></li>
          <li><a href="{contact}">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="{privacy}">Privacy</a></li>
          <li><a href="{terms}">Terms</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Coachly. All rights reserved.</span>
      <a href="{other}">فارسی</a>
    </div>
  </div>
</footer>'''.format(mark=BRAND_MARK, home=home, features=rel(depth,"features.html"), coaches=rel(depth,"for-coaches.html"),
                     athletes=rel(depth,"for-athletes.html"), pricing=rel(depth,"pricing.html"),
                     about=rel(depth,"about.html"), blog=rel(depth,"blog/index.html"), contact=rel(depth,"contact.html"),
                     privacy=rel(depth,"privacy.html"), terms=rel(depth,"terms.html"), other=other)
    else:
        return '''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <a href="{home}" class="brand">{mark}Coachly</a>
        <p class="body-sm" style="margin-top:16px;max-width:32ch;">نرم‌افزار مدیریت مربی‌گری برای مربیان بدنسازی — ساخته‌شده برای رشد همراه با ورزشکاران شما.</p>
      </div>
      <div class="footer-col">
        <h4>محصول</h4>
        <ul>
          <li><a href="{features}">ویژگی‌ها</a></li>
          <li><a href="{coaches}">برای مربیان</a></li>
          <li><a href="{athletes}">برای ورزشکاران</a></li>
          <li><a href="{pricing}">قیمت‌گذاری</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>شرکت</h4>
        <ul>
          <li><a href="{about}">دربارهٔ ما</a></li>
          <li><a href="{blog}">وبلاگ</a></li>
          <li><a href="{contact}">تماس با ما</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>قوانین</h4>
        <ul>
          <li><a href="{privacy}">حریم خصوصی</a></li>
          <li><a href="{terms}">شرایط استفاده</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; ۲۰۲۶ کوچلی. تمامی حقوق محفوظ است.</span>
      <a href="{other}">English</a>
    </div>
  </div>
</footer>'''.format(mark=BRAND_MARK, home=home, features=rel(depth,"features.html"), coaches=rel(depth,"for-coaches.html"),
                     athletes=rel(depth,"for-athletes.html"), pricing=rel(depth,"pricing.html"),
                     about=rel(depth,"about.html"), blog=rel(depth,"blog/index.html"), contact=rel(depth,"contact.html"),
                     privacy=rel(depth,"privacy.html"), terms=rel(depth,"terms.html"), other=other)

def page(lang, title, desc, canonical_path, body, depth=0, og_title=None, og_desc=None, extra_head=""):
    dir_attr = "ltr" if lang == "en" else "rtl"
    other_lang = "fa" if lang == "en" else "en"
    css = rel(depth, "../assets/css/styles.css")
    js = rel(depth, "../assets/js/main.js")
    skip_label = "Skip to content" if lang == "en" else "رفتن به محتوا"
    font_link = (
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
        if lang == "en" else
        '<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet">'
    )
    og_title = og_title or title
    og_desc = og_desc or desc
    locale = "en_US" if lang == "en" else "fa_IR"
    alt_locale = "fa_IR" if lang == "en" else "en_US"
    return '''<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://coachly.app/{lang}/{canonical_path}">
<link rel="alternate" hreflang="en" href="https://coachly.app/en/{canonical_path}">
<link rel="alternate" hreflang="fa" href="https://coachly.app/fa/{canonical_path}">
<link rel="alternate" hreflang="x-default" href="https://coachly.app/en/{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="https://coachly.app/{lang}/{canonical_path}">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{alt_locale}">
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%2048%2048%27%3E%3Crect%20width%3D%2748%27%20height%3D%2748%27%20rx%3D%2711%27%20fill%3D%27%23141414%27%2F%3E%3ClinearGradient%20id%3D%27coachlyMark%27%20x1%3D%2732%27%20y1%3D%274%27%20x2%3D%2715%27%20y2%3D%2743%27%20gradientUnits%3D%27userSpaceOnUse%27%3E%3Cstop%20offset%3D%270%27%20stop-color%3D%27%23F0142E%27%2F%3E%3Cstop%20offset%3D%27.4%27%20stop-color%3D%27%23C20E28%27%2F%3E%3Cstop%20offset%3D%27.75%27%20stop-color%3D%27%234E0813%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%230F0F0F%27%2F%3E%3C%2FlinearGradient%3E%3Cpath%20d%3D%27M35.47%2032.03%20A14%2014%200%201%201%2035.47%2015.97%27%20fill%3D%27none%27%20stroke%3D%27url%28%23coachlyMark%29%27%20stroke-width%3D%277.6%27%2F%3E%3Cpath%20d%3D%27M34.60%207.04%20A20%2020%200%201%200%2034.60%2040.98%27%20fill%3D%27none%27%20stroke%3D%27url%28%23coachlyMark%29%27%20stroke-width%3D%272.3%27%20stroke-linecap%3D%27round%27%2F%3E%3C%2Fsvg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{font_link}
<link rel="stylesheet" href="{css}">
{extra_head}</head>
<body>
<a class="skip-link" href="#main">{skip_label}</a>
{nav}
<main id="main">
{body}
</main>
{footer}
<script src="{js}"></script>
</body>
</html>
'''.format(lang=lang, dir_attr=dir_attr, title=title, desc=desc, canonical_path=canonical_path,
           og_title=og_title, og_desc=og_desc, locale=locale, alt_locale=alt_locale,
           font_link=font_link, css=css, extra_head=extra_head, skip_label=skip_label,
           nav=nav(lang, canonical_path.split(".")[0].split("/")[0] if canonical_path != "index.html" else "", depth),
           body=body, footer=footer(lang, depth), js=js)

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)
