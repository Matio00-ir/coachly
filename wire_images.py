# -*- coding: utf-8 -*-
"""One-off script: replace media-frame placeholders with real <img> tags."""
import re, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def save(p, s):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        f.write(s)
    print("updated", p)

def replace_simple(content, caption, img_path, alt, path):
    """Replace <div class="media-frame" data-caption="CAPTION"></div> (any class order/extra classes)."""
    pattern = re.compile(
        r'<div class="media-frame([^"]*)" data-caption="' + re.escape(caption) + r'"></div>'
    )
    def repl(m):
        extra = m.group(1)
        return '<div class="media-frame{extra} has-photo" data-caption="{caption}"><img src="{img}" alt="{alt}" loading="lazy"></div>'.format(
            extra=extra, caption=caption, img=img_path, alt=alt
        )
    new_content, n = pattern.subn(repl, content)
    if n == 0:
        raise SystemExit("NOT FOUND (simple): {} :: {}".format(path, caption))
    return new_content

def replace_hero(content, caption, img_path, alt, path):
    """Hero media-frame has an inner <div class="scrim"></div>."""
    pattern = re.compile(
        r'(<div class="media-frame" data-caption="' + re.escape(caption) + r'">)\s*<div class="scrim"></div>'
    )
    def repl(m):
        return '<div class="media-frame has-photo" data-caption="{caption}"><img src="{img}" alt="{alt}" loading="eager"><div class="scrim"></div>'.format(
            caption=caption, img=img_path, alt=alt
        )
    new_content, n = pattern.subn(repl, content)
    if n == 0:
        raise SystemExit("NOT FOUND (hero): {} :: {}".format(path, caption))
    return new_content

def replace_styled(content, caption, img_path, alt, path):
    """Article hero media-frame with an inline style attribute, self-closing."""
    pattern = re.compile(
        r'<div class="media-frame reveal" data-caption="' + re.escape(caption) + r'" style="([^"]*)"></div>'
    )
    def repl(m):
        style = m.group(1)
        return '<div class="media-frame reveal has-photo" data-caption="{caption}" style="{style}"><img src="{img}" alt="{alt}" loading="lazy"></div>'.format(
            caption=caption, style=style, img=img_path, alt=alt
        )
    new_content, n = pattern.subn(repl, content)
    if n == 0:
        raise SystemExit("NOT FOUND (styled): {} :: {}".format(path, caption))
    return new_content


# ---- EN ----
EN_ALT = {
    "hero-coach-snatch": "Coach performing a dumbbell snatch in a premium CrossFit gym",
    "coach-reviewing-roster": "Coach reviewing athlete profiles on a tablet",
    "coach-building-program": "Coach building a training program at a desk",
    "athlete-kettlebell-swing": "Athlete mid-kettlebell swing in a premium gym",
    "blog-coach-notebook": "Coach writing notes in a notebook",
    "blog-coach-onboarding": "Coach welcoming a new athlete",
    "blog-analytics-closeup": "Close-up of a coach reviewing analytics on a tablet",
}
# ---- FA ----
FA_ALT = {
    "hero-coach-snatch": "مربی در حال اجرای اسنچ دمبل در یک باشگاه کراسفیت پرمیوم",
    "coach-reviewing-roster": "مربی در حال بررسی پروفایل ورزشکاران روی تبلت",
    "coach-building-program": "مربی در حال ساخت یک برنامهٔ تمرینی پشت میز",
    "athlete-kettlebell-swing": "ورزشکار در حال اجرای کتل‌بل سوینگ در یک باشگاه پرمیوم",
    "blog-coach-notebook": "مربی در حال یادداشت‌برداری در دفترچه",
    "blog-coach-onboarding": "مربی در حال خوش‌آمدگویی به ورزشکار جدید",
    "blog-analytics-closeup": "نمای نزدیک مربی در حال بررسی تحلیل‌ها روی تبلت",
}

def img_path(name, depth):
    return ("../" * depth) + "assets/img/{}.jpg".format(name)

# EN pages (depth 0)
p = "en/index.html"; c = load(p)
c = replace_hero(c, "Hero — Coach performing a dumbbell snatch, premium CrossFit gym", img_path("hero-coach-snatch", 0), EN_ALT["hero-coach-snatch"], p)
c = replace_simple(c, "Coach reviewing athlete profiles on a tablet", img_path("coach-reviewing-roster", 0), EN_ALT["coach-reviewing-roster"], p)
c = replace_simple(c, "Editorial — coach with notebook", img_path("blog-coach-notebook", 0), EN_ALT["blog-coach-notebook"], p)
c = replace_simple(c, "Editorial — coach onboarding athlete", img_path("blog-coach-onboarding", 0), EN_ALT["blog-coach-onboarding"], p)
c = replace_simple(c, "Editorial — analytics close-up", img_path("blog-analytics-closeup", 0), EN_ALT["blog-analytics-closeup"], p)
save(p, c)

p = "en/features.html"; c = load(p)
c = replace_simple(c, "Coach organizing the athlete roster", img_path("coach-reviewing-roster", 0), EN_ALT["coach-reviewing-roster"], p)
save(p, c)

p = "en/for-coaches.html"; c = load(p)
c = replace_simple(c, "Coach building a training program", img_path("coach-building-program", 0), EN_ALT["coach-building-program"], p)
save(p, c)

p = "en/for-athletes.html"; c = load(p)
c = replace_simple(c, "Athlete mid-kettlebell swing, premium gym", img_path("athlete-kettlebell-swing", 0), EN_ALT["athlete-kettlebell-swing"], p)
save(p, c)

p = "en/blog/index.html"; c = load(p)
c = replace_simple(c, "Editorial — coach with notebook", img_path("blog-coach-notebook", 1), EN_ALT["blog-coach-notebook"], p)
save(p, c)

p = "en/blog/tracking-progress-without-spreadsheets.html"; c = load(p)
c = replace_styled(c, "Editorial — coach reviewing notes", img_path("blog-coach-notebook", 1), EN_ALT["blog-coach-notebook"], p)
save(p, c)

# FA pages (depth 0)
p = "fa/index.html"; c = load(p)
c = replace_hero(c, "هیرو — مربی در حال اجرای اسنچ دمبل، باشگاه کراسفیت پرمیوم", img_path("hero-coach-snatch", 0), FA_ALT["hero-coach-snatch"], p)
c = replace_simple(c, "مربی در حال بررسی پروفایل ورزشکاران روی تبلت", img_path("coach-reviewing-roster", 0), FA_ALT["coach-reviewing-roster"], p)
c = replace_simple(c, "ادیتوریال — مربی با دفترچه یادداشت", img_path("blog-coach-notebook", 0), FA_ALT["blog-coach-notebook"], p)
c = replace_simple(c, "ادیتوریال — پذیرش ورزشکار جدید", img_path("blog-coach-onboarding", 0), FA_ALT["blog-coach-onboarding"], p)
c = replace_simple(c, "ادیتوریال — نمای نزدیک تحلیل داده", img_path("blog-analytics-closeup", 0), FA_ALT["blog-analytics-closeup"], p)
save(p, c)

p = "fa/features.html"; c = load(p)
c = replace_simple(c, "مربی در حال سازمان‌دهی فهرست ورزشکاران", img_path("coach-reviewing-roster", 0), FA_ALT["coach-reviewing-roster"], p)
save(p, c)

p = "fa/for-coaches.html"; c = load(p)
c = replace_simple(c, "مربی در حال ساخت یک برنامهٔ تمرینی", img_path("coach-building-program", 0), FA_ALT["coach-building-program"], p)
save(p, c)

p = "fa/for-athletes.html"; c = load(p)
c = replace_simple(c, "ورزشکار در حال اجرای کتل‌بل سوینگ، باشگاه پرمیوم", img_path("athlete-kettlebell-swing", 0), FA_ALT["athlete-kettlebell-swing"], p)
save(p, c)

p = "fa/blog/index.html"; c = load(p)
c = replace_simple(c, "ادیتوریال — مربی با دفترچه یادداشت", img_path("blog-coach-notebook", 1), FA_ALT["blog-coach-notebook"], p)
save(p, c)

p = "fa/blog/tracking-progress-without-spreadsheets.html"; c = load(p)
c = replace_styled(c, "ادیتوریال — مربی در حال بررسی یادداشت‌ها", img_path("blog-coach-notebook", 1), FA_ALT["blog-coach-notebook"], p)
save(p, c)

print("ALL DONE")
