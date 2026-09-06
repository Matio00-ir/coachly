# -*- coding: utf-8 -*-
from build import page, write

CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>'
CROSS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M18 6L6 18M6 6l12 12"/></svg>'

# ===================================================================== FOR COACHES — EN =====================================================================
coaches_en = '''
  <section class="hero" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head reveal" style="max-width:680px;">
        <span class="eyebrow">For coaches</span>
        <h1 class="display-1">Built for the way you already coach.</h1>
        <p class="body-lg" style="margin-top:20px;">Coachly doesn't ask you to change how you coach. It gives the roster, the programming, and the progress tracking you're already doing a proper home.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-2">
        <div class="card reveal" style="padding:32px;">
          <span class="badge" style="margin-bottom:20px;">Without Coachly</span>
          <ul class="price-feats">
            <li style="color:var(--text-tertiary);">{cross}Athlete data spread across spreadsheets and chat apps</li>
            <li style="color:var(--text-tertiary);">{cross}Progress you have to reconstruct from memory</li>
            <li style="color:var(--text-tertiary);">{cross}A different process for every new athlete</li>
            <li style="color:var(--text-tertiary);">{cross}Check-ins that fall through the cracks</li>
          </ul>
        </div>
        <div class="card reveal" style="padding:32px;border-color:var(--accent);">
          <span class="badge badge-accent" style="margin-bottom:20px;">With Coachly</span>
          <ul class="price-feats">
            <li>{check}One roster, one source of truth for every athlete</li>
            <li>{check}Progress you can actually see, tracked automatically</li>
            <li>{check}A consistent, repeatable onboarding process</li>
            <li>{check}Status indicators that surface who needs you</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="Coach building a training program"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">Your workflow, not a new one</span>
          <h2 class="display-2" style="margin-top:14px;">Write programs once. Reuse them for years.</h2>
          <p class="body-lg" style="margin-top:20px;">Build a program, assign it to an athlete, and adjust it week to week as they progress — without starting from a blank page every time.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">Made for coaches who take it seriously</span>
        <h2 class="heading-lg" style="margin-top:12px;">Whether you coach 5 athletes or 150.</h2>
      </div>
      <div class="grid-3">
        <div class="card reveal">
          <h3 class="heading-md">Independent coaches</h3>
          <p class="body-md" style="margin-top:8px;">Start free, keep every athlete organized without hiring an assistant to manage spreadsheets.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">Growing coaching businesses</h3>
          <p class="body-md" style="margin-top:8px;">Scale past the point where memory and group chats stop working.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">Coaching teams</h3>
          <p class="body-md" style="margin-top:8px;">Keep every coach on the same system, with the same standard for every athlete.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">Get started</span>
        <h2 class="display-2" style="margin-top:16px;">Bring your athletes into one place.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">Start free with up to 5 athletes — no credit card required.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">Start free today</a>
      </div>
    </div>
  </section>
'''.format(check=CHECK, cross=CROSS)

write("en/for-coaches.html", page(
    lang="en", title="For Coaches — Coachly",
    desc="Coachly gives fitness coaches one place to manage their roster, run training programs, and track athlete progress.",
    canonical_path="for-coaches.html", body=coaches_en,
))

# ===================================================================== FOR COACHES — FA =====================================================================
coaches_fa = '''
  <section class="hero" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head reveal" style="max-width:680px;">
        <span class="eyebrow">برای مربیان</span>
        <h1 class="display-1">ساخته‌شده برای همان روشی که همین حالا مربی‌گری می‌کنید.</h1>
        <p class="body-lg" style="margin-top:20px;">کوچلی از شما نمی‌خواهد روش مربی‌گری‌تان را عوض کنید. فقط به فهرست ورزشکاران، برنامه‌نویسی و پیگیری پیشرفتی که همین حالا انجام می‌دهید، یک خانهٔ درست می‌دهد.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-2">
        <div class="card reveal" style="padding:32px;">
          <span class="badge" style="margin-bottom:20px;">بدون کوچلی</span>
          <ul class="price-feats">
            <li style="color:var(--text-tertiary);">{cross}اطلاعات ورزشکاران پخش‌شده در اکسل‌ها و اپ‌های چت</li>
            <li style="color:var(--text-tertiary);">{cross}پیشرفتی که باید از حافظه‌تان بازسازی کنید</li>
            <li style="color:var(--text-tertiary);">{cross}فرآیندی متفاوت برای هر ورزشکار جدید</li>
            <li style="color:var(--text-tertiary);">{cross}پیگیری‌هایی که از دست می‌روند</li>
          </ul>
        </div>
        <div class="card reveal" style="padding:32px;border-color:var(--accent);">
          <span class="badge badge-accent" style="margin-bottom:20px;">با کوچلی</span>
          <ul class="price-feats">
            <li>{check}یک فهرست، یک منبع واحد برای هر ورزشکار</li>
            <li>{check}پیشرفتی که واقعاً می‌بینید، به‌صورت خودکار پیگیری‌شده</li>
            <li>{check}یک فرآیند پذیرش یکسان و تکرارپذیر</li>
            <li>{check}نشانگرهای وضعیت که نشان می‌دهند چه کسی به شما نیاز دارد</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="مربی در حال ساخت یک برنامهٔ تمرینی"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">گردش‌کار خودتان، نه یک روش تازه</span>
          <h2 class="display-2" style="margin-top:14px;">برنامه‌ها را یک‌بار بنویسید. سال‌ها استفاده کنید.</h2>
          <p class="body-lg" style="margin-top:20px;">یک برنامه بسازید، به یک ورزشکار اختصاص دهید و هفته‌به‌هفته با پیشرفت او تنظیمش کنید — بدون شروع دوباره از صفحهٔ خالی هر بار.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">ساخته‌شده برای مربیانی که جدی‌اند</span>
        <h2 class="heading-lg" style="margin-top:12px;">چه ۵ ورزشکار مربی‌گری کنید، چه ۱۵۰ تا.</h2>
      </div>
      <div class="grid-3">
        <div class="card reveal">
          <h3 class="heading-md">مربیان مستقل</h3>
          <p class="body-md" style="margin-top:8px;">رایگان شروع کنید و بدون استخدام دستیار برای مدیریت اکسل، همه‌چیز را منظم نگه دارید.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">کسب‌وکارهای مربی‌گری در حال رشد</h3>
          <p class="body-md" style="margin-top:8px;">از نقطه‌ای که حافظه و گروه‌های چت دیگر جواب نمی‌دهند، عبور کنید.</p>
        </div>
        <div class="card reveal">
          <h3 class="heading-md">تیم‌های مربی‌گری</h3>
          <p class="body-md" style="margin-top:8px;">همهٔ مربی‌ها را روی یک سیستم و با یک استاندارد یکسان برای هر ورزشکار نگه دارید.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">شروع کنید</span>
        <h2 class="display-2" style="margin-top:16px;">ورزشکارانتان را در یک جا جمع کنید.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">با تا ۵ ورزشکار، رایگان شروع کنید — بدون نیاز به کارت بانکی.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">همین امروز رایگان شروع کنید</a>
      </div>
    </div>
  </section>
'''.format(check=CHECK, cross=CROSS)

write("fa/for-coaches.html", page(
    lang="fa", title="برای مربیان — کوچلی",
    desc="کوچلی به مربیان بدنسازی یک فضای واحد برای مدیریت ورزشکاران، اجرای برنامه‌های تمرینی و پیگیری پیشرفت می‌دهد.",
    canonical_path="for-coaches.html", body=coaches_fa,
))

# ===================================================================== FOR ATHLETES — EN =====================================================================
athletes_en = '''
  <section class="hero" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head reveal" style="max-width:680px;">
        <span class="eyebrow">For athletes</span>
        <h1 class="display-1">Training that's actually organized.</h1>
        <p class="body-lg" style="margin-top:20px;">Coachly is software your coach uses — but you're the one who feels the difference: clearer programs, visible progress, and a coach who always knows where you're at.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-3">
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20M4 4.5A2.5 2.5 0 016.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">A program you can actually follow</h3>
          <p class="body-md" style="margin-top:8px;">No more guessing what today's session is from a screenshot of a screenshot.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 20V10M18 20V4M6 20v-4"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Progress you can see</h3>
          <p class="body-md" style="margin-top:8px;">Your consistency and performance tracked over time, not just remembered.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Feedback that doesn't get lost</h3>
          <p class="body-md" style="margin-top:8px;">Check-ins and notes tied to your profile, not buried in an old chat thread.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="Athlete mid-kettlebell swing, premium gym"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">Why it matters</span>
          <h2 class="display-2" style="margin-top:14px;">A coach who's organized coaches better.</h2>
          <p class="body-lg" style="margin-top:20px;">When your coach isn't reconstructing your training history from memory, they can spend that time actually coaching you.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">Know a coach who needs this?</span>
        <h2 class="display-2" style="margin-top:16px;">Tell your coach about Coachly.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">Coachly is built for coaches. If yours is still working from spreadsheets, send them this page.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">See plans for coaches</a>
      </div>
    </div>
  </section>
'''

write("en/for-athletes.html", page(
    lang="en", title="For Athletes — Coachly",
    desc="What Coachly means for the athletes of a coach who uses it: clearer programs, visible progress, and feedback that doesn't get lost.",
    canonical_path="for-athletes.html", body=athletes_en,
))

# ===================================================================== FOR ATHLETES — FA =====================================================================
athletes_fa = '''
  <section class="hero" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head reveal" style="max-width:680px;">
        <span class="eyebrow">برای ورزشکاران</span>
        <h1 class="display-1">تمرینی که واقعاً منظم است.</h1>
        <p class="body-lg" style="margin-top:20px;">کوچلی نرم‌افزاری‌ست که مربی شما استفاده می‌کند — اما این شمایید که تفاوتش را حس می‌کنید: برنامه‌های شفاف‌تر، پیشرفت قابل مشاهده، و مربی‌ای که همیشه می‌داند شما کجای مسیر هستید.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-3">
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20M4 4.5A2.5 2.5 0 016.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">برنامه‌ای که واقعاً می‌شود دنبالش کرد</h3>
          <p class="body-md" style="margin-top:8px;">دیگر نیازی نیست حدس بزنید تمرین امروز چیست، آن‌هم از روی یک اسکرین‌شات از یک اسکرین‌شات.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 20V10M18 20V4M6 20v-4"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">پیشرفتی که می‌بینید</h3>
          <p class="body-md" style="margin-top:8px;">پایبندی و عملکردتان در طول زمان پیگیری می‌شود، نه فقط به خاطر سپرده.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">بازخوردی که گم نمی‌شود</h3>
          <p class="body-md" style="margin-top:8px;">پیگیری‌ها و یادداشت‌ها به پروفایل شما متصل‌اند، نه دفن‌شده در یک تاپیک چت قدیمی.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="ورزشکار در حال اجرای کتل‌بل سوینگ، باشگاه پرمیوم"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">چرا اهمیت دارد</span>
          <h2 class="display-2" style="margin-top:14px;">مربی‌ای که منظم است، بهتر مربی‌گری می‌کند.</h2>
          <p class="body-lg" style="margin-top:20px;">وقتی مربی‌تان مجبور نیست سابقهٔ تمرینی‌تان را از حافظه بازسازی کند، آن زمان را صرف مربی‌گری واقعی شما می‌کند.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">مربی‌ای می‌شناسید که به این نیاز دارد؟</span>
        <h2 class="display-2" style="margin-top:16px;">کوچلی را به مربی‌تان معرفی کنید.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">کوچلی برای مربی‌ها ساخته شده. اگر مربی شما هنوز با اکسل کار می‌کند، این صفحه را برایش بفرستید.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">مشاهدهٔ پلن‌ها برای مربیان</a>
      </div>
    </div>
  </section>
'''

write("fa/for-athletes.html", page(
    lang="fa", title="برای ورزشکاران — کوچلی",
    desc="کوچلی برای ورزشکارانِ مربی‌ای که از آن استفاده می‌کند چه معنایی دارد: برنامه‌های شفاف‌تر، پیشرفت قابل مشاهده و بازخوردی که گم نمی‌شود.",
    canonical_path="for-athletes.html", body=athletes_fa,
))
