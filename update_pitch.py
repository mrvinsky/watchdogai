import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific sentence in slide 7
content = content.replace(
    "real incremental revenue</strong> — calculated on the next slide.</p></div>",
    "real incremental game volume</strong> — calculated on the next slide.</p></div>"
)

# Define the new slide 8
new_slide = """<!-- ═══════════════════════════════════════════
     SLIDE 8 — VELOCITY IMPACT
═══════════════════════════════════════════ -->
<section class="slide" id="velocity">
  <div class="orb" style="width:700px;height:700px;background:var(--g);top:-250px;left:-250px"></div>

  <div class="eyebrow">Velocity & Game Volume</div>
  <h2 class="slide-title">Those 18 recovered days<br>translate directly into massive game volume.</h2>
  <p class="slide-body">
    An average fast-paced game round takes a dealer approximately <strong>0.6 seconds</strong> to process. Every recovered second is a round that gets played. Here is the operational impact when you remove badge-scanning friction.
  </p>

  <div class="grid g3" style="max-width:900px;margin-bottom:2.5rem">
    <div class="card" style="text-align:center;padding:1.5rem">
      <p style="font-size:.75rem;color:var(--muted);margin-bottom:.5rem">Avg. Dealer Speed / Round</p>
      <p style="font-size:1.6rem;font-weight:800;color:var(--b)">0.6 seconds</p>
    </div>
    <div class="card" style="text-align:center;padding:1.5rem">
      <p style="font-size:.75rem;color:var(--muted);margin-bottom:.5rem">Saved per Rotation</p>
      <p style="font-size:1.6rem;font-weight:800;color:var(--g)">2.0 seconds</p>
    </div>
    <div class="card" style="text-align:center;padding:1.5rem">
      <p style="font-size:.75rem;color:var(--muted);margin-bottom:.5rem">Extra Rounds per Rotation</p>
      <p style="font-size:1.6rem;font-weight:800;color:var(--gold)">~3.3 rounds</p>
    </div>
  </div>

  <p style="font-size:.72rem;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--muted);text-align:center;margin-bottom:1rem">Result: 3.3 extra rounds per rotation · 48 rotations per day · 45 tables</p>

  <div class="roi-wrap" style="margin-bottom:3.5rem">
    <div class="roi-r head">
      <div class="roi-c">Period</div>
      <div class="roi-c">Recovered Time</div>
      <div class="roi-c">Extra Games Dealt</div>
    </div>
    <div class="roi-r">
      <div class="roi-c period">Daily</div>
      <div class="roi-c">1.2 hours</div>
      <div class="roi-c eur" style="color:var(--b)">+7,200 games</div>
    </div>
    <div class="roi-r">
      <div class="roi-c period">Weekly</div>
      <div class="roi-c">8.4 hours</div>
      <div class="roi-c eur" style="color:var(--b)">+50,400 games</div>
    </div>
    <div class="roi-r">
      <div class="roi-c period">Monthly</div>
      <div class="roi-c">36 hours</div>
      <div class="roi-c eur" style="color:var(--b)">+216,000 games</div>
    </div>
    <div class="roi-r hl">
      <div class="roi-c" style="color:var(--g);font-weight:800;font-size:1.05rem">Annually</div>
      <div class="roi-c" style="font-size:1rem;font-weight:700">18 days</div>
      <div class="roi-c eur" style="font-size:1.25rem;color:var(--g)">+2,628,000 games</div>
    </div>
  </div>

  <div class="bign">2.6M+</div>
  <p style="font-size:1rem;color:var(--muted);margin-top:1.25rem;text-align:center;max-width:540px;line-height:1.7">
    Extra games per year. From just 45 tables.<br>
    <strong style="color:#fff">Zero new tables. Zero new dealers. Zero new hardware.</strong><br>
    <span style="color:var(--b);font-size:.9rem">If rolled out to all 360 tables → <strong style="color:var(--b)">~21M+ extra games / year</strong></span>
  </p>
</section>"""

# Using regex to replace the whole slide 8 section
pattern = re.compile(r"<!-- ═══════════════════════════════════════════\s*SLIDE 6 — REVENUE IMPACT.*?</section>", re.DOTALL)
new_content = pattern.sub(new_slide, content)

# Also fix the disclaimer at the bottom
disclaimer_pattern = re.compile(r"<div class=\"disc\">.*?</div>", re.DOTALL)
new_disclaimer = """<div class="disc">
    <strong style="color:rgba(255,255,255,.7)">Assumptions used in calculations:</strong>
    0.6 seconds per round · 2 seconds saved per rotation · 48 rotations per day per table · 45 active tables · 24/7 operation.
    All figures represent conservative minimums based on time saved from physical badge scanning and authentication delays.
  </div>"""
new_content = disclaimer_pattern.sub(new_disclaimer, new_content)

# Oh wait, the section was `id="revenue"`. The new is `id="velocity"`.
# Let's check the navigation dots on the left.
nav_pattern = re.compile(r'<a href="#revenue" class="n-dot" title="Revenue"></a>')
new_content = new_content.replace(
    '<a href="#revenue" class="n-dot" title="Revenue"></a>',
    '<a href="#velocity" class="n-dot" title="Game Volume"></a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Update complete")
