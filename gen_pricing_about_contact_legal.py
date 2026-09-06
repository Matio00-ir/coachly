# -*- coding: utf-8 -*-
from build import page, write

CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>'

# ===================================================================== PRICING =====================================================================
pricing_en = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:640px;">
        <span class="eyebrow">Pricing</span>
        <h1 class="display-1">Start free. Grow when you're ready.</h1>
        <p class="body-lg" style="margin-top:16px;">Simple plans built around the size of your coaching business.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="pricing-grid reveal">
        <div class="price-card">
          <span class="badge" style="align-self:flex-start;">Free</span>
          <div class="price-amount"><span class="num">0</span><span class="cur">Toman</span></div>
          <p class="body-sm">Up to 5 athletes</p>
          <ul class="price-feats">
            <li>{check}Full athlete profiles</li>
            <li>{check}Progress tracking</li>
            <li>{check}Core training tools</li>
          </ul>
          <a href="#" class="btn btn-secondary btn-block">Start free</a>
        </div>
        <div class="price-card featured">
          <span class="tag">Most coaches choose this</span>
          <span class="badge badge-accent" style="align-self:flex-start;">Pro</span>
          <div class="price-amount"><span class="num font-tabular">3,200,000</span><span class="cur">Toman</span></div>
          <p class="body-sm">For growing coaching businesses</p>
          <ul class="price-feats">
            <li>{check}Everything in Free</li>
            <li>{check}Unlimited athletes</li>
            <li>{check}Full analytics suite</li>
            <li>{check}Programs &amp; calendar</li>
          </ul>
          <a href="#" class="btn btn-primary btn-block">Choose Pro</a>
        </div>
        <div class="price-card">
          <span class="badge" style="align-self:flex-start;">Max</span>
          <div class="price-amount"><span class="num font-tabular">6,800,000</span><span class="cur">Toman</span></div>
          <p class="body-sm">For established coaching teams</p>
          <ul class="price-feats">
            <li>{check}Everything in Pro</li>
            <li>{check}Priority support</li>
            <li>{check}Advanced coaching tools</li>
          </ul>
          <a href="#" class="btn btn-secondary btn-block">Choose Max</a>
        </div>
      </div>
      <p class="body-sm reveal" style="text-align:center;margin-top:40px;">Have a question about plans? <a href="contact.html" style="color:var(--accent);font-weight:600;">Get in touch</a>.</p>
    </div>
  </section>
'''.format(check=CHECK)

write("en/pricing.html", page(
    lang="en", title="Pricing — Coachly",
    desc="Coachly pricing: start free with up to 5 athletes, or upgrade to Pro or Max as your coaching business grows.",
    canonical_path="pricing.html", body=pricing_en,
))

pricing_fa = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:640px;">
        <span class="eyebrow">قیمت‌گذاری</span>
        <h1 class="display-1">رایگان شروع کنید. هر زمان آماده بودید، رشد کنید.</h1>
        <p class="body-lg" style="margin-top:16px;">پلن‌های ساده، متناسب با اندازهٔ کسب‌وکار مربی‌گری شما.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="pricing-grid reveal">
        <div class="price-card">
          <span class="badge" style="align-self:flex-start;">رایگان</span>
          <div class="price-amount"><span class="num">0</span><span class="cur">تومان</span></div>
          <p class="body-sm">تا ۵ ورزشکار</p>
          <ul class="price-feats">
            <li>{check}پروفایل کامل ورزشکار</li>
            <li>{check}پیگیری پیشرفت</li>
            <li>{check}ابزارهای اصلی تمرین</li>
          </ul>
          <a href="#" class="btn btn-secondary btn-block">شروع رایگان</a>
        </div>
        <div class="price-card featured">
          <span class="tag">انتخاب اکثر مربی‌ها</span>
          <span class="badge badge-accent" style="align-self:flex-start;">Pro</span>
          <div class="price-amount"><span class="num font-tabular">3,200,000</span><span class="cur">تومان</span></div>
          <p class="body-sm">برای کسب‌وکارهای مربی‌گری در حال رشد</p>
          <ul class="price-feats">
            <li>{check}همهٔ امکانات پلن رایگان</li>
            <li>{check}ورزشکاران نامحدود</li>
            <li>{check}مجموعهٔ کامل تحلیل‌ها</li>
            <li>{check}برنامه‌ها و تقویم</li>
          </ul>
          <a href="#" class="btn btn-primary btn-block">انتخاب Pro</a>
        </div>
        <div class="price-card">
          <span class="badge" style="align-self:flex-start;">Max</span>
          <div class="price-amount"><span class="num font-tabular">6,800,000</span><span class="cur">تومان</span></div>
          <p class="body-sm">برای تیم‌های مربی‌گری تثبیت‌شده</p>
          <ul class="price-feats">
            <li>{check}همهٔ امکانات پلن Pro</li>
            <li>{check}پشتیبانی اولویت‌دار</li>
            <li>{check}ابزارهای پیشرفتهٔ مربی‌گری</li>
          </ul>
          <a href="#" class="btn btn-secondary btn-block">انتخاب Max</a>
        </div>
      </div>
      <p class="body-sm reveal" style="text-align:center;margin-top:40px;">سؤالی دربارهٔ پلن‌ها دارید؟ <a href="contact.html" style="color:var(--accent);font-weight:600;">با ما در تماس باشید</a>.</p>
    </div>
  </section>
'''.format(check=CHECK)

write("fa/pricing.html", page(
    lang="fa", title="قیمت‌گذاری — کوچلی",
    desc="قیمت‌گذاری کوچلی: رایگان شروع کنید تا ۵ ورزشکار، یا با رشد کسب‌وکارتان به پلن Pro یا Max ارتقا دهید.",
    canonical_path="pricing.html", body=pricing_fa,
))

# ===================================================================== ABOUT =====================================================================
about_en = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:680px;">
        <span class="eyebrow">About Coachly</span>
        <h1 class="display-1">Software for coaches, by people who respect the work.</h1>
        <p class="body-lg" style="margin-top:20px;">Coaching is a discipline. It deserves tools built with the same seriousness — not a generic dashboard with a fitness logo on it.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-3">
        <div class="card reveal">
          <h3 class="heading-md">Built around real coaching workflows</h3>
          <p class="body-md" style="margin-top:8px;">Every part of Coachly starts from how coaches actually manage athletes, not from a feature checklist.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">No feature for feature's sake</h3>
          <p class="body-md" style="margin-top:8px;">We'd rather ship fewer things that work well than a long list of things that don't.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">Growing with real feedback</h3>
          <p class="body-md" style="margin-top:8px;">Coachly is still early. What we build next is shaped by the coaches using it now.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="cta-band reveal" style="text-align:start;padding:56px;">
        <div class="grid-2" style="gap:32px;">
          <div>
            <span class="eyebrow">Built with coaches</span>
            <h2 class="heading-lg" style="margin-top:12px;">Shaped by the coaches who'll use it every day.</h2>
          </div>
          <p class="body-md">Coachly is in active development alongside real fitness coaches. Coach stories and case studies will live here as the product grows — we won't put anything in this space that isn't real.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">Get started</span>
        <h2 class="display-2" style="margin-top:16px;">See if Coachly fits how you coach.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">Start free with up to 5 athletes — no credit card required.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">Start free today</a>
      </div>
    </div>
  </section>
'''

write("en/about.html", page(
    lang="en", title="About — Coachly",
    desc="Coachly is coaching management software built around real coaching workflows, developed alongside real fitness coaches.",
    canonical_path="about.html", body=about_en,
))

about_fa = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:680px;">
        <span class="eyebrow">دربارهٔ کوچلی</span>
        <h1 class="display-1">نرم‌افزاری برای مربیان، ساخته‌شده توسط کسانی که به این حرفه احترام می‌گذارند.</h1>
        <p class="body-lg" style="margin-top:20px;">مربی‌گری یک تخصص است. سزاوار ابزارهایی‌ست که با همان جدیت ساخته شده باشند — نه یک داشبورد عمومی با یک لوگوی فیتنسی رویش.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-3">
        <div class="card reveal">
          <h3 class="heading-md">ساخته‌شده بر پایهٔ گردش‌کار واقعی مربی‌گری</h3>
          <p class="body-md" style="margin-top:8px;">هر بخش از کوچلی از روش واقعی مدیریت ورزشکاران توسط مربی‌ها شروع می‌شود، نه از یک چک‌لیست ویژگی.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">هیچ ویژگی‌ای فقط برای داشتنش نیست</h3>
          <p class="body-md" style="margin-top:8px;">ترجیح می‌دهیم چیزهای کمتری بسازیم که خوب کار می‌کنند، تا فهرست بلندی از چیزهایی که کار نمی‌کنند.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">رشد با بازخورد واقعی</h3>
          <p class="body-md" style="margin-top:8px;">کوچلی هنوز در مراحل ابتدایی است. آنچه بعد می‌سازیم را مربیانی که همین حالا از آن استفاده می‌کنند شکل می‌دهند.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="cta-band reveal" style="text-align:start;padding:56px;">
        <div class="grid-2" style="gap:32px;">
          <div>
            <span class="eyebrow">ساخته‌شده با مربی‌ها</span>
            <h2 class="heading-lg" style="margin-top:12px;">شکل‌گرفته توسط مربی‌هایی که هر روز از آن استفاده می‌کنند.</h2>
          </div>
          <p class="body-md">کوچلی در حال توسعهٔ فعال، در کنار مربی‌های واقعی بدنسازی است. تجربهٔ مربی‌ها و مطالعات موردی به‌زودی همین‌جا قرار می‌گیرند — چیزی که واقعی نباشد، اینجا نمی‌آید.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">شروع کنید</span>
        <h2 class="display-2" style="margin-top:16px;">ببینید آیا کوچلی با روش مربی‌گری شما جور در می‌آید.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">با تا ۵ ورزشکار، رایگان شروع کنید — بدون نیاز به کارت بانکی.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">همین امروز رایگان شروع کنید</a>
      </div>
    </div>
  </section>
'''

write("fa/about.html", page(
    lang="fa", title="دربارهٔ ما — کوچلی",
    desc="کوچلی نرم‌افزار مدیریت مربی‌گری است که بر پایهٔ گردش‌کار واقعی مربی‌ها و در کنار مربیان واقعی بدنسازی ساخته می‌شود.",
    canonical_path="about.html", body=about_fa,
))

# ===================================================================== CONTACT =====================================================================
contact_en = '''
  <section class="section-pad">
    <div class="container">
      <div class="section-head center reveal" style="max-width:600px;">
        <span class="eyebrow">Contact</span>
        <h1 class="display-1">Talk to us.</h1>
        <p class="body-lg" style="margin-top:20px;">Questions about Coachly, your plan, or whether it fits your coaching business — we read every message.</p>
      </div>
      <div class="reveal" style="max-width:480px;margin:48px auto 0;">
        <div class="card" style="text-align:center;padding:40px;">
          <span class="eyebrow">General inquiries</span>
          <p class="heading-md" style="margin-top:14px;"><a href="mailto:hello@coachly.app" style="color:var(--accent);">hello@coachly.app</a></p>
          <p class="body-sm" style="margin-top:12px;">We typically reply within one business day.</p>
        </div>
      </div>
    </div>
  </section>
'''

write("en/contact.html", page(
    lang="en", title="Contact — Coachly",
    desc="Get in touch with the Coachly team about your plan, your coaching business, or a question about the product.",
    canonical_path="contact.html", body=contact_en,
))

contact_fa = '''
  <section class="section-pad">
    <div class="container">
      <div class="section-head center reveal" style="max-width:600px;">
        <span class="eyebrow">تماس با ما</span>
        <h1 class="display-1">با ما صحبت کنید.</h1>
        <p class="body-lg" style="margin-top:20px;">سؤال دربارهٔ کوچلی، پلن‌تان، یا اینکه آیا با کسب‌وکار مربی‌گری‌تان جور در می‌آید — همهٔ پیام‌ها را می‌خوانیم.</p>
      </div>
      <div class="reveal" style="max-width:480px;margin:48px auto 0;">
        <div class="card" style="text-align:center;padding:40px;">
          <span class="eyebrow">پرسش‌های عمومی</span>
          <p class="heading-md" style="margin-top:14px;direction:ltr;"><a href="mailto:hello@coachly.app" style="color:var(--accent);">hello@coachly.app</a></p>
          <p class="body-sm" style="margin-top:12px;">معمولاً ظرف یک روز کاری پاسخ می‌دهیم.</p>
        </div>
      </div>
    </div>
  </section>
'''

write("fa/contact.html", page(
    lang="fa", title="تماس با ما — کوچلی",
    desc="با تیم کوچلی دربارهٔ پلن‌تان، کسب‌وکار مربی‌گری‌تان یا سؤالی دربارهٔ محصول در تماس باشید.",
    canonical_path="contact.html", body=contact_fa,
))

# ===================================================================== PRIVACY / TERMS =====================================================================
def legal_body_en(title, lead, paragraphs):
    ps = "\n        ".join('<p>{}</p>'.format(p) for p in paragraphs)
    return '''
  <section class="section-pad">
    <div class="container">
      <div class="article-prose reveal">
        <span class="eyebrow">Legal</span>
        <h1 class="display-2" style="margin-top:14px;">{title}</h1>
        <p class="body-lg" style="margin-top:16px;">{lead}</p>
        {ps}
      </div>
    </div>
  </section>
'''.format(title=title, lead=lead, ps=ps)

write("en/privacy.html", page(
    lang="en", title="Privacy Policy — Coachly",
    desc="How Coachly collects, uses, and protects coach and athlete data.",
    canonical_path="privacy.html",
    body=legal_body_en(
        "Privacy Policy",
        "Coachly is still in active development. This page will describe in full how we collect, use, and protect the data coaches and athletes share with us.",
        [
            "In short: we collect only the information needed to run the product — account details, athlete records you enter, and basic usage data to keep Coachly reliable.",
            "We do not sell coach or athlete data to third parties.",
            "A complete, detailed privacy policy will be published here before Coachly is generally available. If you have questions in the meantime, contact us directly.",
        ],
    ),
))

def legal_body_fa(title, lead, paragraphs):
    ps = "\n        ".join('<p>{}</p>'.format(p) for p in paragraphs)
    return '''
  <section class="section-pad">
    <div class="container">
      <div class="article-prose reveal">
        <span class="eyebrow">قوانین</span>
        <h1 class="display-2" style="margin-top:14px;">{title}</h1>
        <p class="body-lg" style="margin-top:16px;">{lead}</p>
        {ps}
      </div>
    </div>
  </section>
'''.format(title=title, lead=lead, ps=ps)

write("fa/privacy.html", page(
    lang="fa", title="حریم خصوصی — کوچلی",
    desc="کوچلی چگونه داده‌های مربیان و ورزشکاران را جمع‌آوری، استفاده و محافظت می‌کند.",
    canonical_path="privacy.html",
    body=legal_body_fa(
        "حریم خصوصی",
        "کوچلی هنوز در حال توسعهٔ فعال است. این صفحه به‌طور کامل توضیح خواهد داد که چگونه داده‌هایی را که مربیان و ورزشکاران با ما به اشتراک می‌گذارند جمع‌آوری، استفاده و محافظت می‌کنیم.",
        [
            "به‌طور خلاصه: فقط اطلاعاتی را جمع‌آوری می‌کنیم که برای اجرای محصول لازم است — جزئیات حساب کاربری، سوابق ورزشکارانی که وارد می‌کنید، و داده‌های پایهٔ استفاده برای پایدار نگه‌داشتن کوچلی.",
            "ما داده‌های مربیان یا ورزشکاران را به هیچ شخص ثالثی نمی‌فروشیم.",
            "یک سیاست حریم خصوصی کامل و دقیق، پیش از در دسترس قرار گرفتن عمومی کوچلی، همین‌جا منتشر خواهد شد. در همین حین، برای هر سؤالی مستقیماً با ما در تماس باشید.",
        ],
    ),
))

write("en/terms.html", page(
    lang="en", title="Terms of Service — Coachly",
    desc="The terms governing use of Coachly.",
    canonical_path="terms.html",
    body=legal_body_en(
        "Terms of Service",
        "Coachly is still in active development. A complete terms of service will be published here before general availability.",
        [
            "Using Coachly today means using an early-stage product that is actively changing based on coach feedback.",
            "Detailed terms covering accounts, billing, and acceptable use will be finalized and posted here as the product matures.",
            "Questions about current terms? Contact us directly and we'll answer them plainly.",
        ],
    ),
))

write("fa/terms.html", page(
    lang="fa", title="شرایط استفاده — کوچلی",
    desc="شرایط حاکم بر استفاده از کوچلی.",
    canonical_path="terms.html",
    body=legal_body_fa(
        "شرایط استفاده",
        "کوچلی هنوز در حال توسعهٔ فعال است. شرایط استفادهٔ کامل، پیش از در دسترس قرار گرفتن عمومی محصول، همین‌جا منتشر خواهد شد.",
        [
            "استفاده از کوچلی امروز به‌معنای استفاده از محصولی در مرحلهٔ ابتدایی‌ست که بر اساس بازخورد مربیان به‌طور فعال در حال تغییر است.",
            "شرایط دقیق دربارهٔ حساب‌های کاربری، صورت‌حساب و استفادهٔ مجاز، هم‌زمان با بلوغ محصول نهایی و همین‌جا منتشر خواهد شد.",
            "سؤالی دربارهٔ شرایط فعلی دارید؟ مستقیماً با ما تماس بگیرید تا شفاف پاسخ دهیم.",
        ],
    ),
))
