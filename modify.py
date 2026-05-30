import re

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    content = f.read()

# Replace fonts
content = content.replace('family=Syne:wght@400;500;600;700;800&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600', 'family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600')
content = content.replace("'Syne'", "'Outfit'")
content = content.replace("'DM Sans'", "'Inter'")

# Replace logo
old_logo = """    <!--
    ╔═══════════════════════════════════════════════════════╗
    ║  LOGO SETUP — Replace with your image URL             ║
    ║  1. Uncomment the <img> line below                    ║
    ║  2. Replace YOUR_LOGO_URL_HERE with your image path   ║
    ║  3. Delete the .logo-fallback block below it          ║
    ╚═══════════════════════════════════════════════════════╝
    -->
    <!-- <img src="YOUR_LOGO_URL_HERE" alt="Neuro InfoTech" class="logo-img"> -->

    <!-- Default fallback (remove this block when using the img above) -->
    <div class="logo-fallback">
      <div class="logo-hex">🧠</div>
      <span class="logo-name">Neuro InfoTech</span>
    </div>"""

new_logo = """    <img src="logo.png" alt="Neuro InfoTech" class="logo-img">"""
content = content.replace(old_logo, new_logo)

# Replace Hero
old_hero = """    <div class="hero-badge">⚡ AI-Powered Data Intelligence</div>
    <h1 class="hero-title">
      Transform Data Into<br>
      <span class="grad">Intelligent Insights</span>
    </h1>
    <p class="hero-sub">
      Neuro InfoTech empowers businesses with cutting-edge neural analytics,
      data infrastructure, and intelligent automation solutions built to scale.
    </p>
    <div class="hero-btns">
      <a href="#services" class="btn-grad">Explore Services →</a>
      <a href="#contact"  class="btn-outline">Talk to Us</a>
    </div>"""

new_hero = """    <div class="hero-badge">⚡ End-to-End Digital Products</div>
    <h1 class="hero-title">
      Building Highly Scalable<br>
      <span class="grad">Production-Ready Apps</span>
    </h1>
    <p class="hero-sub">
      We are a core team of 4 Software Engineers dedicated to making end-to-end projects for clients. 
      From concept to deployment, we engineer digital products with 100% rigor.
    </p>
    <div class="hero-btns">
      <a href="#about" class="btn-grad">Explore Expertise →</a>
      <a href="#contact"  class="btn-outline">Talk to Us</a>
    </div>"""
content = content.replace(old_hero, new_hero)

# Replace About
old_about = """        <span class="s-label">Who We Are</span>
        <h2 class="s-title">Neuro InfoTech —<br><span>Intelligence Redefined</span></h2>
        <p>We are a specialized information technology company focused on delivering transformative data intelligence solutions. Our team of engineers, data scientists, and strategists work at the intersection of neuroscience-inspired algorithms and enterprise technology.</p>
        <p>Founded with a mission to make advanced analytics accessible to every business, we bridge the gap between raw data and actionable strategy — helping organisations unlock a lasting competitive edge through intelligent systems.</p>

        <div class="about-stats">
          <div class="stat-box reveal d1"><div class="stat-num">150+</div><div class="stat-lbl">Projects Delivered</div></div>
          <div class="stat-box reveal d2"><div class="stat-num">98%</div><div class="stat-lbl">Client Satisfaction</div></div>
          <div class="stat-box reveal d3"><div class="stat-num">40+</div><div class="stat-lbl">Expert Engineers</div></div>
          <div class="stat-box reveal d4"><div class="stat-num">12+</div><div class="stat-lbl">Years Experience</div></div>
        </div>"""

new_about = """        <span class="s-label">Who We Are</span>
        <h2 class="s-title">Core Team of<br><span>Software Engineers</span></h2>
        <p>We are a core team of 4 passionate Software Engineers deciding to make end-to-end projects for clients. We build highly scalable, production-ready digital products tailored to your needs.</p>
        <p>Instead of bloated agencies, you get direct access to builders. We ensure 100% engineering rigor, cost-effective systems, superfast communication, and unlimited revisions.</p>

        <div class="about-stats">
          <div class="stat-box reveal d1"><div class="stat-num">100%</div><div class="stat-lbl">Engineering Rigor</div></div>
          <div class="stat-box reveal d2"><div class="stat-num">∞</div><div class="stat-lbl">Unlimited Revisions</div></div>
          <div class="stat-box reveal d3"><div class="stat-num">4</div><div class="stat-lbl">Core Experts</div></div>
          <div class="stat-box reveal d4"><div class="stat-num">24/7</div><div class="stat-lbl">Fast Communication</div></div>
        </div>"""
content = content.replace(old_about, new_about)

# Replace Services
old_services = """    <div class="srv-grid">
      <div class="srv-card reveal d1">
        <div class="srv-ico">🤖</div>
        <h3>AI &amp; Machine Learning</h3>
        <p>Custom ML models, neural networks, and intelligent automation pipelines tailored to your business workflows and data environment.</p>
        <span class="srv-tag">AI Development</span>
      </div>
      <div class="srv-card reveal d2">
        <div class="srv-ico">📊</div>
        <h3>Data Analytics &amp; BI</h3>
        <p>Advanced business intelligence dashboards, predictive analytics, and real-time reporting systems that drive smarter decisions.</p>
        <span class="srv-tag">Analytics</span>
      </div>
      <div class="srv-card reveal d3">
        <div class="srv-ico">☁️</div>
        <h3>Cloud Infrastructure</h3>
        <p>Scalable multi-cloud architectures, migration services, and DevOps pipelines built for reliability and peak performance.</p>
        <span class="srv-tag">Cloud &amp; DevOps</span>
      </div>
      <div class="srv-card reveal d1">
        <div class="srv-ico">🔒</div>
        <h3>Cybersecurity Solutions</h3>
        <p>End-to-end security audits, threat intelligence systems, and zero-trust architectures to keep your data and systems protected.</p>
        <span class="srv-tag">Security</span>
      </div>
      <div class="srv-card reveal d2">
        <div class="srv-ico">🔗</div>
        <h3>Systems Integration</h3>
        <p>Seamless API integrations, microservices architecture, and enterprise system unification for cohesive data flow across platforms.</p>
        <span class="srv-tag">Integration</span>
      </div>
      <div class="srv-card reveal d3">
        <div class="srv-ico">📱</div>
        <h3>Software Development</h3>
        <p>Full-stack web and mobile application development with modern frameworks — from ideation to deployment and maintenance.</p>
        <span class="srv-tag">Development</span>
      </div>
    </div>"""

new_services = """    <div class="srv-grid">
      <div class="srv-card reveal d1">
        <div class="srv-ico">🧠</div>
        <h3>AI Integration</h3>
        <p>Real-world ML pipelines and AI-driven features designed to make your applications smarter and more efficient.</p>
        <span class="srv-tag">Machine Learning</span>
      </div>
      <div class="srv-card reveal d2">
        <div class="srv-ico">💻</div>
        <h3>App Dev</h3>
        <p>End-to-end application development using modern stacks including MERN, Flutter, and Kotlin for robust cross-platform solutions.</p>
        <span class="srv-tag">Web & Mobile</span>
      </div>
      <div class="srv-card reveal d3">
        <div class="srv-ico">⚙️</div>
        <h3>Cost Cutting</h3>
        <p>Lean Linux and Cloud architectures optimized for performance while drastically reducing operational costs.</p>
        <span class="srv-tag">Infrastructure</span>
      </div>
      <div class="srv-card reveal d1">
        <div class="srv-ico">📈</div>
        <h3>Growth</h3>
        <p>Native SEO and SMO strategies integrated directly into the product to drive organic traffic and user acquisition.</p>
        <span class="srv-tag">Marketing</span>
      </div>
      <div class="srv-card reveal d2">
        <div class="srv-ico">🚀</div>
        <h3>100% Engineering Rigor</h3>
        <p>We write clean, maintainable, and scalable code following the best industry practices and design patterns.</p>
        <span class="srv-tag">Quality</span>
      </div>
      <div class="srv-card reveal d3">
        <div class="srv-ico">💬</div>
        <h3>Superfast Communication</h3>
        <p>Direct access to the engineers building your product. No middle-men, just transparent and rapid updates.</p>
        <span class="srv-tag">Client First</span>
      </div>
    </div>"""
content = content.replace(old_services, new_services)

# Remove Analytics
old_analytics = """<!-- ╔══════════════════════════════════════ GRAPH ANALYTICS ═════════╗ -->
<section id="analytics">
  <div class="container">
    <div class="an-layout">

      <div class="reveal">
        <span class="s-label">Data Intelligence</span>
        <h2 class="s-title">Graph <span>Analytics</span></h2>
        <p class="s-sub">Our proprietary analytics engine processes millions of data points in real time, surfacing patterns invisible to conventional BI tools.</p>

        <div class="an-metrics">
          <div class="metric reveal d1"><div class="met-val">2.4M</div><div class="met-lbl">Events / Second</div><div class="met-chg">↑ 18% this month</div></div>
          <div class="metric reveal d2"><div class="met-val">99.9%</div><div class="met-lbl">System Uptime</div><div class="met-chg">↑ SLA Met</div></div>
          <div class="metric reveal d3"><div class="met-val">0.4ms</div><div class="met-lbl">Avg Query Time</div><div class="met-chg">↓ 34% faster</div></div>
          <div class="metric reveal d4"><div class="met-val">94%</div><div class="met-lbl">Forecast Accuracy</div><div class="met-chg">↑ 7% vs baseline</div></div>
        </div>
      </div>

      <div class="reveal d2">
        <div class="chart-wrap">
          <div class="chart-hdr">
            <div class="chart-ttl">Performance Analytics — 2024</div>
            <div class="chart-leg">
              <div class="leg-item"><div class="leg-dot" style="background:#22d3ee"></div><span>Data Processed</span></div>
              <div class="leg-item"><div class="leg-dot" style="background:#818cf8"></div><span>Insights Generated</span></div>
            </div>
          </div>
          <canvas id="analyticsChart" height="210"></canvas>
        </div>
      </div>

    </div>
  </div>
</section>

"""
content = content.replace(old_analytics, "")

# Remove Analytics Nav Link
content = content.replace('<li><a href="#analytics">Analytics</a></li>\n    ', '')
content = content.replace('<a href="#analytics"     onclick="closeNav()">Analytics</a>\n  ', '')

# Replace Pricing
old_pricing = """<!-- ╔══════════════════════════════════════════ PRICING ═════════════╗ -->
<section id="pricing">
  <div class="container">
    <div class="sec-head reveal">
      <span class="s-label">Plans &amp; Pricing</span>
      <h2 class="s-title">Transparent <span>Pricing</span></h2>
      <p class="s-sub">Choose a plan that fits your scale. All plans include onboarding, 24/7 monitoring, and dedicated support.</p>
    </div>

    <div class="price-grid">

      <!-- Starter -->
      <div class="price-card reveal d1">
        <div class="plan-name">Starter</div>
        <div class="plan-price"><span class="p-sym">$</span><span class="p-amt">299</span><span class="p-per">/month</span></div>
        <p class="plan-desc">Perfect for small teams and startups exploring data-driven decisions.</p>
        <ul class="plan-feats">
          <li><div class="chk">✓</div>Up to 5 team members</li>
          <li><div class="chk">✓</div>3 analytics dashboards</li>
          <li><div class="chk">✓</div>50 GB data storage</li>
          <li><div class="chk">✓</div>Standard API access</li>
          <li><div class="chk">✓</div>Email support</li>
          <li class="dim"><div class="chk">—</div>Custom ML models</li>
          <li class="dim"><div class="chk">—</div>Advanced integrations</li>
        </ul>
        <a href="#contact" class="plan-btn ghost">Get Started</a>
      </div>

      <!-- Pro (Featured) -->
      <div class="price-card featured reveal d2">
        <div class="pop-badge">Most Popular</div>
        <div class="plan-name">Professional</div>
        <div class="plan-price"><span class="p-sym">$</span><span class="p-amt">799</span><span class="p-per">/month</span></div>
        <p class="plan-desc">For growing businesses that need powerful analytics and automation at scale.</p>
        <ul class="plan-feats">
          <li><div class="chk">✓</div>Up to 20 team members</li>
          <li><div class="chk">✓</div>Unlimited dashboards</li>
          <li><div class="chk">✓</div>500 GB data storage</li>
          <li><div class="chk">✓</div>Full API access + webhooks</li>
          <li><div class="chk">✓</div>Priority support (24 / 7)</li>
          <li><div class="chk">✓</div>5 custom ML models</li>
          <li class="dim"><div class="chk">—</div>Dedicated infrastructure</li>
        </ul>
        <a href="#contact" class="plan-btn solid">Get Started</a>
      </div>

      <!-- Enterprise -->
      <div class="price-card reveal d3">
        <div class="plan-name">Enterprise</div>
        <div class="plan-price"><span class="p-amt" style="font-size:2.1rem">Custom</span></div>
        <p class="plan-desc">Tailored solutions for large organisations with complex requirements and compliance needs.</p>
        <ul class="plan-feats">
          <li><div class="chk">✓</div>Unlimited team members</li>
          <li><div class="chk">✓</div>Custom dashboards &amp; reports</li>
          <li><div class="chk">✓</div>Unlimited data storage</li>
          <li><div class="chk">✓</div>Private API deployment</li>
          <li><div class="chk">✓</div>Dedicated account manager</li>
          <li><div class="chk">✓</div>Unlimited ML models</li>
          <li><div class="chk">✓</div>Dedicated infrastructure</li>
        </ul>
        <a href="#contact" class="plan-btn ghost">Contact Sales</a>
      </div>

    </div>
  </div>
</section>"""

new_pricing = """<!-- ╔══════════════════════════════════════════ WHY CHOOSE US ═══════════╗ -->
<section id="pricing">
  <div class="container">
    <div class="sec-head reveal">
      <span class="s-label">Our Approach</span>
      <h2 class="s-title">Why <span>Choose Us?</span></h2>
      <p class="s-sub">We don't do illogical pricing tiers. Every project is unique, and we price based on value, scope, and engineering hours.</p>
    </div>

    <div class="price-grid" style="grid-template-columns: repeat(2, 1fr); max-width: 800px; margin: 0 auto;">
      
      <!-- Value Proposition -->
      <div class="price-card reveal d1">
        <div class="plan-name">The Agency Way</div>
        <p class="plan-desc">Bloated teams, slow communication, and hidden fees.</p>
        <ul class="plan-feats">
          <li class="dim"><div class="chk">—</div>Paying for account managers</li>
          <li class="dim"><div class="chk">—</div>Rigid processes</li>
          <li class="dim"><div class="chk">—</div>Limited revisions</li>
          <li class="dim"><div class="chk">—</div>Slow turnaround times</li>
        </ul>
      </div>

      <!-- Our Way -->
      <div class="price-card featured reveal d2">
        <div class="pop-badge">Our Team</div>
        <div class="plan-name">The Core Team Way</div>
        <p class="plan-desc">Direct partnership with 4 dedicated software engineers.</p>
        <ul class="plan-feats">
          <li><div class="chk">✓</div>100% Engineering Rigor</li>
          <li><div class="chk">✓</div>Cost-Effective Systems</li>
          <li><div class="chk">✓</div>Superfast Communication</li>
          <li><div class="chk">✓</div>Unlimited Revisions</li>
        </ul>
        <a href="#contact" class="plan-btn solid" style="margin-top: 1rem;">Contact us now for your project! CHEERS!</a>
      </div>

    </div>
  </div>
</section>"""
content = content.replace(old_pricing, new_pricing)

# Nav Link
content = content.replace('<li><a href="#pricing">Pricing</a></li>', '<li><a href="#pricing">Approach</a></li>')
content = content.replace('<a href="#pricing"       onclick="closeNav()">Pricing</a>', '<a href="#pricing"       onclick="closeNav()">Approach</a>')

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'w') as f:
    f.write(content)
