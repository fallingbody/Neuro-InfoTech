with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    content = f.read()

# Replace Hero Canvas with Stock Image
hero_canvas = """<canvas id="neural-canvas"></canvas>"""
hero_img = """<img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=2072&q=80" alt="Software Engineering" class="hero-bg-img">"""
content = content.replace(hero_canvas, hero_img)

# Add CSS for hero-bg-img if not present
if "hero-bg-img" not in content:
    css_insert = """    .hero-bg-img {
      position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.15; z-index: 0;
    }"""
    content = content.replace("#neural-canvas {", f"{css_insert}\n    #neural-canvas {{")

# Replace about-visual content with a stock image
old_about_visual = """      <div class="about-visual reveal d2">
        <div class="av-row"><div class="av-ico">🧠</div><div class="av-info"><h4>Neural-Inspired Architecture</h4><p>Systems modelled on brain-like pattern recognition</p></div></div>
        <div class="av-row"><div class="av-ico">⚡</div><div class="av-info"><h4>Real-Time Processing</h4><p>Sub-millisecond data ingestion &amp; analysis pipelines</p></div></div>
        <div class="av-row"><div class="av-ico">🔒</div><div class="av-info"><h4>Enterprise Security</h4><p>ISO 27001 certified, end-to-end encrypted infrastructure</p></div></div>
        <div class="av-row"><div class="av-ico">🌐</div><div class="av-info"><h4>Global Scalability</h4><p>Multi-cloud deployment across 15+ data centres worldwide</p></div></div>
        <div class="av-row"><div class="av-ico">📊</div><div class="av-info"><h4>Predictive Analytics</h4><p>Forward-looking insights with 94% forecast accuracy</p></div></div>
      </div>"""

new_about_visual = """      <div class="about-visual reveal d2" style="padding: 0; display: flex;">
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80" alt="Engineering Team" style="width: 100%; height: 100%; object-fit: cover; border-radius: 22px; opacity: 0.9;">
      </div>"""
content = content.replace(old_about_visual, new_about_visual)

# Replace srv-ico emojis with SVGs
svg_ai = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z"/></svg>"""
svg_app = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>"""
svg_cost = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline></svg>"""
svg_growth = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>"""
svg_quality = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>"""
svg_msg = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path><line x1="9" y1="9" x2="15" y2="15"></line><line x1="15" y1="9" x2="9" y2="15"></line></svg>"""

content = content.replace('<div class="srv-ico">🧠</div>', f'<div class="srv-ico">{svg_ai}</div>')
content = content.replace('<div class="srv-ico">💻</div>', f'<div class="srv-ico">{svg_app}</div>')
content = content.replace('<div class="srv-ico">⚙️</div>', f'<div class="srv-ico">{svg_cost}</div>')
content = content.replace('<div class="srv-ico">📈</div>', f'<div class="srv-ico">{svg_growth}</div>')
content = content.replace('<div class="srv-ico">🚀</div>', f'<div class="srv-ico">{svg_quality}</div>')
content = content.replace('<div class="srv-ico">💬</div>', f'<div class="srv-ico">{svg_msg}</div>')

with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'w') as f:
    f.write(content)
