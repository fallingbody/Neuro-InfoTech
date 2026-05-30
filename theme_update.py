import re

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    content = f.read()

# 1. CSS Variables
old_vars = """    :root {
      --bg:      #05080f;
      --bg2:     #08101e;
      --bg3:     #0e1829;
      --card:    #111d30;
      --border:  rgba(34,211,238,.1);
      --cyan:    #22d3ee;
      --purple:  #818cf8;
      --grad:    linear-gradient(135deg, #22d3ee 0%, #818cf8 100%);
      --text:    #dde6f0;
      --muted:   #5a7393;
      --white:   #f4f9ff;
    }"""
new_vars = """    :root {
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
content = content.replace(old_vars, new_vars)

# 2. RGB Replacements (Cyan -> Green, Purple -> Dark Green)
content = content.replace('34,211,238', '45,181,82')
content = content.replace('129,140,248', '30,150,64')

# 3. Nav backgrounds
content = content.replace('rgba(5,8,15,.92)', 'rgba(255,255,255,.92)')
content = content.replace('rgba(5,8,15,.97)', 'rgba(255,255,255,.97)')

# 4. Fonts
old_font_link = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
if old_font_link in content:
    content = content.replace(old_font_link, new_font_link)
else:
    # Fallback if the link was slightly different
    content = re.sub(r'<link href="https://fonts.googleapis.com/css2[^"]+" rel="stylesheet">', new_font_link, content)

content = content.replace("'Inter'", "'Poppins'")
content = content.replace("'Outfit'", "'Poppins'")

# 5. Some light-theme tweaks
content = content.replace('rgba(255,255,255,.02)', 'rgba(0,0,0,.02)')
content = content.replace('color: var(--white);', 'color: var(--white);') # Unchanged, but noting --white is now dark

# 6. Add shadows for light theme
shadow_css = """
    .stat-box, .about-visual, .srv-card, .price-card, .test-card, .c-form {
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    }
    .srv-card:hover, .price-card:hover, .test-card:hover {
      box-shadow: 0 12px 30px rgba(45,181,82,0.12);
      border-color: rgba(45,181,82,0.4);
    }
    .av-row { background: #f4f9f6; border-color: rgba(45,181,82,0.15); }
    .av-row:hover { background: rgba(45,181,82,0.08); border-color: rgba(45,181,82,0.3); }
    .hero-title { color: #0f1f17; } /* Force hero title to dark */
  </style>"""
content = content.replace('</style>', shadow_css)

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'w') as f:
    f.write(content)

