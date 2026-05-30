import random

def generate_stars(n):
    stars = []
    for _ in range(n):
        x = random.randint(0, 2000)
        y = random.randint(0, 2000)
        stars.append(f"{x}px {y}px #FFF")
    return ", ".join(stars)

stars1 = generate_stars(300)
stars2 = generate_stars(100)
stars3 = generate_stars(50)

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    content = f.read()

css = f"""
    .space-bg {{
      position: absolute; inset: 0; width: 100%; height: 100%; 
      background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
      z-index: 0; overflow: hidden;
    }}
    .star-layer {{
      position: absolute; top: 0; left: 0; width: 2px; height: 2px; background: transparent;
    }}
    .stars1 {{
      width: 1px; height: 1px; box-shadow: {stars1}; animation: animStar 50s linear infinite;
    }}
    .stars1:after {{
      content: " "; position: absolute; top: 0; left: 2000px; width: 1px; height: 1px; box-shadow: {stars1};
    }}
    .stars2 {{
      width: 2px; height: 2px; box-shadow: {stars2}; animation: animStar 100s linear infinite;
    }}
    .stars2:after {{
      content: " "; position: absolute; top: 0; left: 2000px; width: 2px; height: 2px; box-shadow: {stars2};
    }}
    .stars3 {{
      width: 3px; height: 3px; box-shadow: {stars3}; animation: animStar 150s linear infinite;
    }}
    .stars3:after {{
      content: " "; position: absolute; top: 0; left: 2000px; width: 3px; height: 3px; box-shadow: {stars3};
    }}
    @keyframes animStar {{
      from {{ transform: translateX(0px); }}
      to {{ transform: translateX(-2000px); }}
    }}
    .imposter-wrapper {{
      position: absolute;
      top: 30%; left: -100px;
      width: 80px; height: 80px;
      animation: floatImposter 25s linear infinite;
      z-index: 1;
    }}
    .imposter-svg {{
      width: 100%; height: 100%;
      animation: rotateImposter 10s linear infinite;
    }}
    @keyframes floatImposter {{
      0% {{ transform: translate(0, 0); }}
      25% {{ transform: translate(600px, 150px); }}
      50% {{ transform: translate(1200px, -50px); }}
      75% {{ transform: translate(1800px, 100px); }}
      100% {{ transform: translate(2400px, 0); }}
    }}
    @keyframes rotateImposter {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    .hero-content h1, .hero-content p {{
       color: #ffffff !important;
       text-shadow: 0 0 10px rgba(0,0,0,0.5);
    }}
"""

old_css = """    .hero-bg-img {
      position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.15; z-index: 0;
    }"""
content = content.replace(old_css, css)

old_html = """  <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=2072&q=80" alt="Software Engineering" class="hero-bg-img">"""
new_html = """  <div class="space-bg">
    <div class="star-layer stars1"></div>
    <div class="star-layer stars2"></div>
    <div class="star-layer stars3"></div>
    <div class="imposter-wrapper">
      <svg viewBox="0 0 100 100" class="imposter-svg">
        <path d="M 25 40 h -10 a 5 5 0 0 0 -5 5 v 20 a 5 5 0 0 0 5 5 h 10" fill="#c62828" />
        <path d="M 30 50 v 30 a 10 10 0 0 0 10 10 h 5 a 10 10 0 0 0 10 -10 v -10 h 10 v 10 a 10 10 0 0 0 10 10 h 5 a 10 10 0 0 0 10 -10 v -30 c 0 -25 -25 -35 -30 -35 s -30 10 -30 35 z" fill="#e53935" />
        <path d="M 45 30 h 30 a 15 15 0 0 1 15 15 v 5 a 15 15 0 0 1 -15 15 h -30 a 15 15 0 0 1 -15 -15 v -5 a 15 15 0 0 1 15 -15 z" fill="#81d4fa" />
        <ellipse cx="65" cy="40" rx="15" ry="5" fill="#e1f5fe" transform="rotate(-15 65 40)" />
      </svg>
    </div>
  </div>"""

content = content.replace(old_html, new_html)

# The gradient in hero-title is using var(--grad), we should ensure it looks okay on dark bg.
# But hero-glow is still there:
#    .hero-glow { ... }
# Let's remove hero-glow since we have a space background
content = content.replace('<div class="hero-glow"></div>', '')

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'w') as f:
    f.write(content)
