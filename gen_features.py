# -*- coding: utf-8 -*-
from build import page, write

CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>'

# ============================================================ EN ============================================================
body_en = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:680px;">
        <span class="eyebrow">Features</span>
        <h1 class="display-2" style="margin-top:14px;">Everything a coaching business actually needs.</h1>
        <p class="body-lg" style="margin-top:16px;">No bloat, no modules you'll never touch — just the tools that keep athletes progressing and your day organized.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="Coach organizing the athlete roster"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">Athlete management</span>
          <h2 class="display-2" style="margin-top:14px;">Every athlete, organized.</h2>
          <p class="body-lg" style="margin-top:20px;">A single roster with full profiles, training history, and current status — so you always know who's on track and who needs a check-in.</p>
          <ul class="price-feats" style="margin-top:28px;">
            <li>{check}Full athlete profiles and training history</li>
            <li>{check}Recent sessions and activity at a glance</li>
            <li>{check}Status indicators for who needs attention</li>
            <li>{check}Fast search across your entire roster</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="reveal" style="order:2;">
          <span class="eyebrow">Progress analytics</span>
          <h2 class="display-2" style="margin-top:14px;">See progress, not just data.</h2>
          <p class="body-lg" style="margin-top:20px;">Track consistency, key performance metrics, and improvement trends over time — so you can adjust programming based on what's actually happening.</p>
          <ul class="price-feats" style="margin-top:28px;">
            <li>{check}Adherence and consistency trends</li>
            <li>{check}Performance metrics per athlete</li>
            <li>{check}Improvement trends across a training block</li>
          </ul>
        </div>
        <div class="reveal" style="order:1;">
          <div class="chart-card">
            <div class="chart-legend">
              <span class="li"><span class="sw" style="background:var(--accent-500);"></span>Session adherence</span>
              <span class="li"><span class="sw" style="background:#6b7fd7;"></span>Back squat 1RM</span>
            </div>
            <svg viewBox="0 0 400 160" width="100%" style="overflow:visible;">
              <line x1="0" y1="40" x2="400" y2="40" stroke="var(--border)" stroke-width="1"/>
              <line x1="0" y1="80" x2="400" y2="80" stroke="var(--border)" stroke-width="1"/>
              <line x1="0" y1="120" x2="400" y2="120" stroke="var(--border)" stroke-width="1"/>
              <polyline points="0,110 50,100 100,95 150,80 200,75 250,58 300,50 350,34 400,26" fill="none" stroke="var(--accent-500)" stroke-width="3" stroke-linecap="round"/>
              <polyline points="0,130 50,125 100,118 150,112 200,100 250,96 300,84 350,72 400,60" fill="none" stroke="#6b7fd7" stroke-width="3" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">The rest of the toolkit</span>
        <h2 class="heading-lg" style="margin-top:12px;">Built to support the whole coaching workflow.</h2>
      </div>
      <div class="grid-3">
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20M4 4.5A2.5 2.5 0 016.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Training programs</h3>
          <p class="body-md" style="margin-top:8px;">Build structured programs once and assign them to any athlete, then adjust week to week as they progress.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Calendar &amp; scheduling</h3>
          <p class="body-md" style="margin-top:8px;">Keep sessions, check-ins, and deadlines in one shared view instead of three different apps.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 2l3 7h7l-5.5 4.5L18.5 21 12 16.5 5.5 21l2-7.5L2 9h7z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Movement library</h3>
          <p class="body-md" style="margin-top:8px;">Reference a movement once and reuse it across every program you write, for every athlete.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Coach&ndash;athlete messaging</h3>
          <p class="body-md" style="margin-top:8px;">Keep feedback and check-ins tied to the athlete's profile, not lost in a chat app.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M9 11l3 3L22 4M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Onboarding &amp; intake</h3>
          <p class="body-md" style="margin-top:8px;">Bring every new athlete in with the same structured start, instead of improvising each time.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 20V10M18 20V4M6 20v-4"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">Coaching business tools</h3>
          <p class="body-md" style="margin-top:8px;">More of your coaching business, organized in the same workspace — coming next.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">Get started</span>
        <h2 class="display-2" style="margin-top:16px;">See it with your own athletes.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">Start free with up to 5 athletes — no credit card required.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">Start free today</a>
      </div>
    </div>
  </section>
'''.format(check=CHECK)

write("en/features.html", page(
    lang="en",
    title="Features — Coachly",
    desc="Athlete management, progress analytics, training programs, and the rest of the Coachly coaching toolkit.",
    canonical_path="features.html",
    body=body_en,
))

# ============================================================ FA ============================================================
body_fa = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:680px;">
        <span class="eyebrow">ویژگی‌ها</span>
        <h1 class="display-2" style="margin-top:14px;">هر چیزی که یک کسب‌وکار مربی‌گری واقعاً لازم دارد.</h1>
        <p class="body-lg" style="margin-top:16px;">بدون اضافه‌بار، بدون ماژول‌هایی که هرگز لمس‌شان نمی‌کنید — فقط ابزارهایی که پیشرفت ورزشکاران و نظم روزتان را تضمین می‌کنند.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="grid-2">
        <div class="hero-media reveal">
          <div class="media-frame" data-caption="مربی در حال سازمان‌دهی فهرست ورزشکاران"></div>
        </div>
        <div class="reveal">
          <span class="eyebrow">مدیریت ورزشکاران</span>
          <h2 class="display-2" style="margin-top:14px;">هر ورزشکار، منظم و در دسترس.</h2>
          <p class="body-lg" style="margin-top:20px;">یک فهرست واحد با پروفایل کامل، سابقهٔ تمرینی و وضعیت فعلی هر ورزشکار؛ تا همیشه بدانید چه کسی در مسیر درست است و چه کسی نیاز به پیگیری دارد.</p>
          <ul class="price-feats" style="margin-top:28px;">
            <li>{check}پروفایل کامل و سابقهٔ تمرینی ورزشکاران</li>
            <li>{check}جلسات و فعالیت‌های اخیر در یک نگاه</li>
            <li>{check}نشانگر وضعیت برای شناسایی سریع ورزشکاران نیازمند پیگیری</li>
            <li>{check}جست‌وجوی سریع در کل فهرست ورزشکاران</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="grid-2">
        <div class="reveal" style="order:2;">
          <span class="eyebrow">تحلیل پیشرفت</span>
          <h2 class="display-2" style="margin-top:14px;">پیشرفت را ببینید، نه فقط داده را.</h2>
          <p class="body-lg" style="margin-top:20px;">پایبندی به تمرین، شاخص‌های کلیدی عملکرد و روند بهبود را در طول زمان دنبال کنید؛ تا برنامه‌ریزی را بر اساس واقعیت تنظیم کنید.</p>
          <ul class="price-feats" style="margin-top:28px;">
            <li>{check}روند پایبندی و تداوم تمرین</li>
            <li>{check}شاخص‌های عملکرد برای هر ورزشکار</li>
            <li>{check}روند بهبود در طول یک بلوک تمرینی</li>
          </ul>
        </div>
        <div class="reveal" style="order:1;">
          <div class="chart-card">
            <div class="chart-legend">
              <span class="li"><span class="sw" style="background:var(--accent-500);"></span>پایبندی به جلسات</span>
              <span class="li"><span class="sw" style="background:#6b7fd7;"></span>رکورد اسکات پشت</span>
            </div>
            <svg viewBox="0 0 400 160" width="100%" style="overflow:visible;">
              <line x1="0" y1="40" x2="400" y2="40" stroke="var(--border)" stroke-width="1"/>
              <line x1="0" y1="80" x2="400" y2="80" stroke="var(--border)" stroke-width="1"/>
              <line x1="0" y1="120" x2="400" y2="120" stroke="var(--border)" stroke-width="1"/>
              <polyline points="0,110 50,100 100,95 150,80 200,75 250,58 300,50 350,34 400,26" fill="none" stroke="var(--accent-500)" stroke-width="3" stroke-linecap="round"/>
              <polyline points="0,130 50,125 100,118 150,112 200,100 250,96 300,84 350,72 400,60" fill="none" stroke="#6b7fd7" stroke-width="3" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">بقیهٔ جعبه‌ابزار</span>
        <h2 class="heading-lg" style="margin-top:12px;">ساخته‌شده برای کل گردش‌کار مربی‌گری.</h2>
      </div>
      <div class="grid-3">
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20M4 4.5A2.5 2.5 0 016.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">برنامه‌های تمرینی</h3>
          <p class="body-md" style="margin-top:8px;">برنامه‌های ساختاریافته را یک‌بار بسازید و به هر ورزشکاری اختصاص دهید، سپس هفته‌به‌هفته با پیشرفت او تنظیمش کنید.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">تقویم و زمان‌بندی</h3>
          <p class="body-md" style="margin-top:8px;">جلسات، پیگیری‌ها و مهلت‌ها را در یک نمای مشترک نگه دارید، نه در سه اپ مختلف.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 2l3 7h7l-5.5 4.5L18.5 21 12 16.5 5.5 21l2-7.5L2 9h7z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">کتابخانهٔ حرکات</h3>
          <p class="body-md" style="margin-top:8px;">هر حرکت را یک‌بار تعریف کنید و در همهٔ برنامه‌ها، برای هر ورزشکاری، دوباره استفاده کنید.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">پیام‌رسانی مربی و ورزشکار</h3>
          <p class="body-md" style="margin-top:8px;">بازخوردها و پیگیری‌ها را به پروفایل ورزشکار متصل نگه دارید، نه گم‌شده در یک اپ چت.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M9 11l3 3L22 4M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">شروع به کار و پذیرش</h3>
          <p class="body-md" style="margin-top:8px;">هر ورزشکار جدید را با فرآیندی یکسان و ساختاریافته وارد کار کنید، نه با بداهه‌پردازی هر بار.</p>
        </div>
        <div class="card reveal">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M12 20V10M18 20V4M6 20v-4"/></svg>
          <h3 class="heading-md" style="margin-top:16px;">ابزارهای کسب‌وکار مربی‌گری</h3>
          <p class="body-md" style="margin-top:8px;">بخش بیشتری از کسب‌وکار مربی‌گری‌تان، در همین فضای کاری — به‌زودی.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="cta-band reveal">
        <span class="eyebrow">شروع کنید</span>
        <h2 class="display-2" style="margin-top:16px;">با ورزشکاران واقعی خودتان امتحانش کنید.</h2>
        <p class="body-lg" style="margin:20px auto 32px;max-width:46ch;">با تا ۵ ورزشکار، رایگان شروع کنید — بدون نیاز به کارت بانکی.</p>
        <a href="pricing.html" class="btn btn-primary btn-lg">همین امروز رایگان شروع کنید</a>
      </div>
    </div>
  </section>
'''.format(check=CHECK)

write("fa/features.html", page(
    lang="fa",
    title="ویژگی‌ها — کوچلی",
    desc="مدیریت ورزشکاران، تحلیل پیشرفت، برنامه‌های تمرینی و بقیهٔ جعبه‌ابزار مربی‌گری کوچلی.",
    canonical_path="features.html",
    body=body_fa,
))
