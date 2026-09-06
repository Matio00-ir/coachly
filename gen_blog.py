# -*- coding: utf-8 -*-
from build import page, write

# ===================================================================== BLOG INDEX — EN =====================================================================
blog_index_en = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:640px;">
        <span class="eyebrow">Blog</span>
        <h1 class="display-1">Reading for serious coaches.</h1>
        <p class="body-lg" style="margin-top:16px;">Notes on coaching, athlete management, and running a training business — written for coaches, not marketers.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <a href="tracking-progress-without-spreadsheets.html" class="blog-feature reveal" style="display:grid;">
        <div class="media-frame" data-caption="Editorial — coach with notebook"></div>
        <div>
          <div class="blog-meta"><span>Coaching</span><span>&middot;</span><span>6 min read</span></div>
          <h2 class="display-2" style="margin-top:12px;">How to Track Athlete Progress Without Spreadsheets</h2>
          <p class="body-lg" style="margin-top:16px;">Why most tracking systems fall apart after week three — and what to use instead.</p>
          <span class="btn btn-secondary" style="margin-top:24px;">Read the article</span>
        </div>
      </a>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);padding-top:0;">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">More on the way</span>
        <h2 class="heading-lg" style="margin-top:12px;">Coming soon</h2>
      </div>
      <div class="grid-3">
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>Coaching Business</span><span>&middot;</span><span>5 min read</span></div>
          <h3 class="heading-md">Building a Repeatable Onboarding Process for New Athletes</h3>
          <p class="body-sm">A simple intake structure that saves hours in your first month with any athlete.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">Coming soon</span>
        </div>
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>Analytics</span><span>&middot;</span><span>7 min read</span></div>
          <h3 class="heading-md">What Coaches Should Actually Measure Every Week</h3>
          <p class="body-sm">Fewer metrics, tracked consistently, beat a dashboard full of numbers nobody checks.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">Coming soon</span>
        </div>
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>Programming</span><span>&middot;</span><span>6 min read</span></div>
          <h3 class="heading-md">Writing Training Programs That Survive Real Life</h3>
          <p class="body-sm">How to build in flexibility without losing structure.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">Coming soon</span>
        </div>
      </div>
    </div>
  </section>
'''

write("en/blog/index.html", page(
    lang="en", title="Blog — Coachly",
    desc="Notes on coaching, athlete management, and running a training business — from the team building Coachly.",
    canonical_path="blog/index.html", body=blog_index_en, depth=1,
))

# ===================================================================== BLOG INDEX — FA =====================================================================
blog_index_fa = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head center reveal" style="max-width:640px;">
        <span class="eyebrow">وبلاگ</span>
        <h1 class="display-1">خواندنی‌هایی برای مربی‌های جدی.</h1>
        <p class="body-lg" style="margin-top:16px;">یادداشت‌هایی دربارهٔ مربی‌گری، مدیریت ورزشکاران و ادارهٔ یک کسب‌وکار تمرینی — نوشته‌شده برای مربی‌ها، نه بازاریاب‌ها.</p>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <a href="tracking-progress-without-spreadsheets.html" class="blog-feature reveal" style="display:grid;">
        <div class="media-frame" data-caption="ادیتوریال — مربی با دفترچه یادداشت"></div>
        <div>
          <div class="blog-meta"><span>مربی‌گری</span><span>&middot;</span><span>۶ دقیقه مطالعه</span></div>
          <h2 class="display-2" style="margin-top:12px;">چطور بدون اکسل، پیشرفت ورزشکار را دنبال کنیم</h2>
          <p class="body-lg" style="margin-top:16px;">چرا بیشتر سیستم‌های پیگیری بعد از هفتهٔ سوم از هم می‌پاشند — و باید به‌جایش از چه استفاده کرد.</p>
          <span class="btn btn-secondary" style="margin-top:24px;">مطالعهٔ مقاله</span>
        </div>
      </a>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);padding-top:0;">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">به‌زودی بیشتر</span>
        <h2 class="heading-lg" style="margin-top:12px;">در راه است</h2>
      </div>
      <div class="grid-3">
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>کسب‌وکار مربی‌گری</span><span>&middot;</span><span>۵ دقیقه مطالعه</span></div>
          <h3 class="heading-md">ساخت یک فرآیند پذیرش تکرارپذیر برای ورزشکاران جدید</h3>
          <p class="body-sm">یک ساختار ساده برای شروع کار که در همان ماه اول با هر ورزشکار، ساعت‌ها زمان شما را ذخیره می‌کند.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">به‌زودی</span>
        </div>
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>تحلیل داده</span><span>&middot;</span><span>۷ دقیقه مطالعه</span></div>
          <h3 class="heading-md">مربی‌ها واقعاً باید هر هفته چه چیزی را اندازه بگیرند؟</h3>
          <p class="body-sm">شاخص‌های کمتر، اما پیگیری‌شده به‌طور مداوم، بهتر از یک داشبورد پر از عددهایی است که کسی نگاهشان نمی‌کند.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">به‌زودی</span>
        </div>
        <div class="blog-card card reveal" style="opacity:0.6;">
          <div class="blog-meta"><span>برنامه‌نویسی تمرین</span><span>&middot;</span><span>۶ دقیقه مطالعه</span></div>
          <h3 class="heading-md">نوشتن برنامه‌های تمرینی که در زندگی واقعی دوام می‌آورند</h3>
          <p class="body-sm">چطور بدون از دست دادن ساختار، انعطاف‌پذیری را در برنامه بگنجانیم.</p>
          <span class="badge" style="margin-top:8px;align-self:flex-start;">به‌زودی</span>
        </div>
      </div>
    </div>
  </section>
'''

write("fa/blog/index.html", page(
    lang="fa", title="وبلاگ — کوچلی",
    desc="یادداشت‌هایی دربارهٔ مربی‌گری، مدیریت ورزشکاران و ادارهٔ یک کسب‌وکار تمرینی — از تیم سازندهٔ کوچلی.",
    canonical_path="blog/index.html", body=blog_index_fa, depth=1,
))

# ===================================================================== ARTICLE — EN =====================================================================
article_en = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="article-prose reveal" style="text-align:center;max-width:720px;">
        <div class="blog-meta" style="justify-content:center;"><span>Coaching</span><span>&middot;</span><span>6 min read</span><span>&middot;</span><span>Coachly Team</span><span>&middot;</span><span>September 2026</span></div>
        <h1 class="display-1" style="margin-top:16px;">How to Track Athlete Progress Without Spreadsheets</h1>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="media-frame reveal" data-caption="Editorial — coach reviewing notes" style="max-width:900px;margin:0 auto 48px;aspect-ratio:16/9;"></div>
      <div class="article-prose reveal">
        <p>Almost every coach starts the same way: a spreadsheet. It's free, it's flexible, and for the first five or six athletes, it works fine. Then it doesn't.</p>
        <p>The failure point is rarely dramatic. It's a missed update here, a duplicated tab there, a column that meant one thing in March and something else by June. By the time you notice, you're not tracking progress anymore — you're maintaining a spreadsheet, which is a different job entirely.</p>
        <h2>Why spreadsheets break down around week three</h2>
        <p>Spreadsheets are built for structured, static data. Athlete progress is neither. It changes shape as a training block evolves, it needs context a cell can't hold, and it has to be updated consistently by someone who is usually mid-session, not sitting at a desk.</p>
        <ul>
          <li>There's no single view of "who needs my attention today."</li>
          <li>History gets overwritten instead of preserved.</li>
          <li>Nothing alerts you when an athlete goes quiet.</li>
        </ul>
        <h2>What to track instead</h2>
        <p>The fix isn't a more complicated spreadsheet. It's tracking fewer things, more consistently, in a system built for the job:</p>
        <ul>
          <li><strong>Adherence</strong> — did the athlete train when the program said they would?</li>
          <li><strong>Key lifts or benchmarks</strong> — the two or three numbers that actually matter for their goal.</li>
          <li><strong>Recent activity</strong> — a simple, current view of who trained, who didn't, and who needs a check-in.</li>
        </ul>
        <p>That's it. Not every metric available — the ones that change how you coach next week.</p>
        <h2>The real cost of losing track</h2>
        <p>When progress tracking breaks down, the athlete usually feels it before the coach does — a program that stops adjusting, a check-in that never comes, a plateau nobody notices. The tool matters less than the discipline of tracking a few things consistently. But the right tool makes that discipline a lot easier to keep.</p>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Keep reading</span>
        <h2 class="heading-lg" style="margin-top:12px;">More from the blog</h2>
      </div>
      <p class="body-md reveal"><a href="index.html" style="color:var(--accent);font-weight:600;">Back to all articles &rarr;</a></p>
    </div>
  </section>
'''

write("en/blog/tracking-progress-without-spreadsheets.html", page(
    lang="en", title="How to Track Athlete Progress Without Spreadsheets — Coachly Blog",
    desc="Why most athlete tracking spreadsheets fall apart after week three, and the few things worth tracking instead.",
    canonical_path="blog/tracking-progress-without-spreadsheets.html", body=article_en, depth=1,
    extra_head='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"How to Track Athlete Progress Without Spreadsheets","author":{"@type":"Organization","name":"Coachly Team"},"datePublished":"2026-09-01","publisher":{"@type":"Organization","name":"Coachly"}}</script>\n',
))

# ===================================================================== ARTICLE — FA =====================================================================
article_fa = '''
  <section class="section-pad" style="padding-bottom:0;">
    <div class="container">
      <div class="article-prose reveal" style="text-align:center;max-width:720px;">
        <div class="blog-meta" style="justify-content:center;"><span>مربی‌گری</span><span>&middot;</span><span>۶ دقیقه مطالعه</span><span>&middot;</span><span>تیم کوچلی</span><span>&middot;</span><span>شهریور ۱۴۰۵</span></div>
        <h1 class="display-1" style="margin-top:16px;">چطور بدون اکسل، پیشرفت ورزشکار را دنبال کنیم</h1>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="container">
      <div class="media-frame reveal" data-caption="ادیتوریال — مربی در حال بررسی یادداشت‌ها" style="max-width:900px;margin:0 auto 48px;aspect-ratio:16/9;"></div>
      <div class="article-prose reveal">
        <p>تقریباً هر مربی‌ای همین‌طور شروع می‌کند: یک فایل اکسل. رایگان است، انعطاف‌پذیر است، و برای پنج یا شش ورزشکار اول، خوب کار می‌کند. بعد دیگر کار نمی‌کند.</p>
        <p>نقطهٔ شکست معمولاً دراماتیک نیست. یک به‌روزرسانی از قلم‌افتاده اینجا، یک تب تکراری آنجا، ستونی که در فروردین یک معنی داشت و تا تیر معنی دیگری پیدا کرده. تا وقتی متوجه شوید، دیگر پیشرفت را دنبال نمی‌کنید — دارید یک فایل اکسل را نگه‌داری می‌کنید، که کاری کاملاً متفاوت است.</p>
        <h2>چرا اکسل‌ها حوالی هفتهٔ سوم از هم می‌پاشند</h2>
        <p>فایل‌های اکسل برای داده‌های ساختاریافته و ثابت ساخته شده‌اند. پیشرفت ورزشکار نه ساختاریافته است و نه ثابت. با پیشرفت یک بلوک تمرینی شکل عوض می‌کند، به زمینه‌ای نیاز دارد که یک سلول نمی‌تواند در خود جای دهد، و باید به‌طور مداوم توسط کسی به‌روزرسانی شود که معمولاً وسط یک جلسه است، نه پشت میز.</p>
        <ul>
          <li>هیچ نمای واحدی از «امروز چه کسی به توجه من نیاز دارد» وجود ندارد.</li>
          <li>سابقه به‌جای حفظ شدن، بازنویسی می‌شود.</li>
          <li>هیچ‌چیز به شما هشدار نمی‌دهد وقتی ورزشکاری بی‌خبر می‌شود.</li>
        </ul>
        <h2>به‌جایش چه چیزی را دنبال کنیم</h2>
        <p>راه‌حل، یک اکسل پیچیده‌تر نیست. دنبال‌کردن چیزهای کمتر است، اما به‌طور مداوم‌تر، در سیستمی که برای همین کار ساخته شده:</p>
        <ul>
          <li><strong>پایبندی</strong> — آیا ورزشکار همان‌طور که برنامه گفته بود تمرین کرده؟</li>
          <li><strong>حرکات یا شاخص‌های کلیدی</strong> — همان دو یا سه عددی که واقعاً برای هدفش اهمیت دارند.</li>
          <li><strong>فعالیت اخیر</strong> — یک نمای ساده و به‌روز از اینکه چه کسی تمرین کرده، چه کسی نکرده، و چه کسی نیاز به پیگیری دارد.</li>
        </ul>
        <p>همین. نه هر شاخص موجود — فقط آن‌هایی که هفتهٔ بعد را در مربی‌گری‌تان تغییر می‌دهند.</p>
        <h2>هزینهٔ واقعی از دست دادن ردِ پیشرفت</h2>
        <p>وقتی پیگیری پیشرفت از هم می‌پاشد، معمولاً ورزشکار زودتر از مربی متوجهش می‌شود — برنامه‌ای که دیگر تنظیم نمی‌شود، پیگیری‌ای که هرگز نمی‌رسد، سکویی که کسی متوجهش نمی‌شود. ابزار کمتر از انضباطِ دنبال‌کردن مداوم چند چیز اهمیت دارد. اما ابزار درست، حفظ آن انضباط را بسیار ساده‌تر می‌کند.</p>
      </div>
    </div>
  </section>

  <section class="section-pad" style="background:var(--surface-2);">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">ادامهٔ مطالعه</span>
        <h2 class="heading-lg" style="margin-top:12px;">بیشتر از وبلاگ</h2>
      </div>
      <p class="body-md reveal"><a href="index.html" style="color:var(--accent);font-weight:600;">&larr; بازگشت به همهٔ مقالات</a></p>
    </div>
  </section>
'''

write("fa/blog/tracking-progress-without-spreadsheets.html", page(
    lang="fa", title="چطور بدون اکسل، پیشرفت ورزشکار را دنبال کنیم — وبلاگ کوچلی",
    desc="چرا بیشتر فایل‌های اکسل پیگیری ورزشکار بعد از هفتهٔ سوم از هم می‌پاشند، و چند چیزی که واقعاً ارزش دنبال‌کردن دارند.",
    canonical_path="blog/tracking-progress-without-spreadsheets.html", body=article_fa, depth=1,
    extra_head='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"چطور بدون اکسل، پیشرفت ورزشکار را دنبال کنیم","author":{"@type":"Organization","name":"تیم کوچلی"},"datePublished":"2026-09-01","publisher":{"@type":"Organization","name":"کوچلی"}}</script>\n',
))
