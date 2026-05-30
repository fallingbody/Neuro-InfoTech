with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    content = f.read()

# 1. Update root variables to Dark Theme
old_vars = """    :root {
      --bg:      #ffffff;
      --bg2:     #f4f9f6;
      --bg3:     #ffffff;
      --card:    #ffffff;
      --border:  rgba(45, 181, 82, 0.2);
      --cyan:    #2db552;
      --purple:  #1e9640;
      --grad:    linear-gradient(135deg, #2db552 0%, #1e9640 100%);
      --text:    #4a5568;
      --muted:   #718096;
      --white:   #0f1f17;
    }"""
new_vars = """    :root {
      --bg:      transparent;
      --bg2:     transparent;
      --bg3:     rgba(15, 23, 42, 0.6);
      --card:    rgba(15, 23, 42, 0.6);
      --border:  rgba(45, 181, 82, 0.2);
      --cyan:    #2db552;
      --purple:  #1e9640;
      --grad:    linear-gradient(135deg, #2db552 0%, #1e9640 100%);
      --text:    #dde6f0;
      --muted:   #94a3b8;
      --white:   #ffffff;
    }"""
content = content.replace(old_vars, new_vars)

# 2. Update .space-bg CSS to be fixed and cover the viewport
old_space_css = """    .space-bg {
      position: absolute; inset: 0; width: 100%; height: 100%; 
      background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
      z-index: 0; overflow: hidden;
    }"""
new_space_css = """    .space-bg {
      position: fixed; inset: 0; width: 100vw; height: 100vh; 
      background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
      z-index: -1; overflow: hidden;
    }"""
content = content.replace(old_space_css, new_space_css)

# 3. Remove Imposter CSS
imposter_css = """    .imposter-wrapper {
      position: absolute;
      top: 30%; left: -100px;
      width: 80px; height: 80px;
      animation: floatImposter 25s linear infinite;
      z-index: 1;
    }
    .imposter-svg {
      width: 100%; height: 100%;
      animation: rotateImposter 10s linear infinite;
    }
    @keyframes floatImposter {
      0% { transform: translate(0, 0); }
      25% { transform: translate(600px, 150px); }
      50% { transform: translate(1200px, -50px); }
      75% { transform: translate(1800px, 100px); }
      100% { transform: translate(2400px, 0); }
    }
    @keyframes rotateImposter {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }"""
content = content.replace(imposter_css, "")

# 4. Remove Imposter HTML
imposter_html = """    <div class="imposter-wrapper">
      <svg viewBox="0 0 100 100" class="imposter-svg">
        <path d="M 25 40 h -10 a 5 5 0 0 0 -5 5 v 20 a 5 5 0 0 0 5 5 h 10" fill="#c62828" />
        <path d="M 30 50 v 30 a 10 10 0 0 0 10 10 h 5 a 10 10 0 0 0 10 -10 v -10 h 10 v 10 a 10 10 0 0 0 10 10 h 5 a 10 10 0 0 0 10 -10 v -30 c 0 -25 -25 -35 -30 -35 s -30 10 -30 35 z" fill="#e53935" />
        <path d="M 45 30 h 30 a 15 15 0 0 1 15 15 v 5 a 15 15 0 0 1 -15 15 h -30 a 15 15 0 0 1 -15 -15 v -5 a 15 15 0 0 1 15 -15 z" fill="#81d4fa" />
        <ellipse cx="65" cy="40" rx="15" ry="5" fill="#e1f5fe" transform="rotate(-15 65 40)" />
      </svg>
    </div>"""
content = content.replace(imposter_html, "")

# 5. Move space-bg to right after <body>
# First, extract space-bg HTML
space_bg_html_full = """  <div class="space-bg">
    <div class="star-layer stars1"></div>
    <div class="star-layer stars2"></div>
    <div class="star-layer stars3"></div>
    
  </div>"""

# Wait, the replace string for removing imposter might have left blank lines. Let's use regex to extract and remove space-bg from #hero
import re
space_bg_match = re.search(r'(\s*<div class="space-bg">.*?</div>\s*</div>)', content, flags=re.DOTALL)
if space_bg_match:
    extracted_space_bg = space_bg_match.group(1)
    content = content.replace(extracted_space_bg, "")
    
    # Clean up the extracted HTML (remove the extra div if the regex caught it, wait, the regex above `.*?</div>\s*</div>` is a bit risky)
    # Let's just do it explicitly.
else:
    # Fallback exact match without imposter
    exact_space = """  <div class="space-bg">
    <div class="star-layer stars1"></div>
    <div class="star-layer stars2"></div>
    <div class="star-layer stars3"></div>
    
  </div>"""
    if exact_space in content:
        content = content.replace(exact_space, "")
        extracted_space_bg = exact_space
    else:
        # If it failed to remove imposter or something changed
        pass

# Actually, the safest way is to just find `<section id="hero">` and the space-bg inside it.
import re
new_space_bg = """
<!-- Space Background -->
<div class="space-bg">
  <div class="star-layer stars1"></div>
  <div class="star-layer stars2"></div>
  <div class="star-layer stars3"></div>
</div>
"""
# Remove old space-bg using a generic regex
content = re.sub(r'\s*<div class="space-bg">.*?</div>\s*(?:</div>\s*)?(?=<div class="hero-content">)', '', content, flags=re.DOTALL)
content = content.replace('<body>', '<body>' + new_space_bg)

# 6. Ensure background colors of sections are transparent (they should be since var(--bg) is transparent, 
# but let's check nav background. 
# nav.scrolled has `background: rgba(255,255,255,.92);`. We need to change that to a dark version.
content = content.replace("background: rgba(255,255,255,.92);", "background: rgba(9, 10, 15, 0.92);")
content = content.replace("background: rgba(255,255,255,.02);", "background: rgba(255,255,255,.05);") # for av-row if it exists
content = content.replace("background: #f4f9f6;", "background: rgba(15, 23, 42, 0.6);") # leftover light bg
content = content.replace("background: var(--bg);", "background: transparent;")
content = content.replace("background: var(--bg2);", "background: transparent;")

# Fix text colors explicitly forced
content = content.replace("color: #ffffff !important;", "")
content = content.replace("text-shadow: 0 0 10px rgba(0,0,0,0.5);", "")

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'w') as f:
    f.write(content)
