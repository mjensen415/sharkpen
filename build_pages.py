import os

with open("index.html", "r") as f:
    orig_html = f.read()

start_idx = orig_html.find('<!-- HERO -->')
nav_html = orig_html[:start_idx]

foot_idx = orig_html.find('<!-- FOOTER -->')
footer_html = orig_html[foot_idx:]

def make_page(filename, content):
    html = nav_html + content + '\n\n' + footer_html
    repl = [
        ('<a href="#hero"', '<a href="index.html"'),
        ('<a href="#aiml"', '<a href="ai-ml-services.html"'),
        ('<a href="#managed"', '<a href="managed-it.html"'),
        ('<a href="#about"', '<a href="about.html"'),
        ('<a href="#contact"', '<a href="contact.html"'),
        ('<li><a href="#">Case Studies</a></li>', '<li><a href="case-studies.html">Case Studies</a></li>'),
        ('<li><a href="#">Privacy Policy</a></li>', '<li><a href="privacy-policy.html">Privacy Policy</a></li>'),
        ('<li><a href="#">Terms of Service</a></li>', '<li><a href="terms-of-service.html">Terms of Service</a></li>'),
        ('<li><a href="#">Accessibility</a></li>', '<li><a href="accessibility.html">Accessibility</a></li>')
    ]
    for o, n in repl: html = html.replace(o, n)
    with open(filename, "w") as f: f.write(html)

print("Creating AI/ML page...")
aiml_start = orig_html.find('<!-- AI/ML SECTION -->')
aiml_end = orig_html.find('<!-- MANAGED IT -->')
hr_idx = orig_html.rfind('<hr class="section-rule">', aiml_start, aiml_end)
aiml_html = orig_html[aiml_start:hr_idx] if hr_idx != -1 else orig_html[aiml_start:aiml_end]
aiml_content = '''
<section id="hero" style="min-height: 400px; padding-top: 150px; padding-bottom: 80px; background: var(--off-white); border-bottom: 1px solid var(--border); text-align: center;">
  <div class="section-wrap" style="padding: 0;">
    <div class="hero-tag">AI/ML Services</div>
    <h1 class="hero-h1">Build a Smarter, More Capable Organization.</h1>
    <p class="section-lead" style="margin: 0 auto; max-width: 600px;">From executive briefings to custom model deployment, we deliver AI/ML programs with practical, measurable results across every level of your organization.</p>
  </div>
</section>
<section id="aiml" style="padding-top: 80px; padding-bottom: 80px; border-top: none;">
  <div class="section-wrap" style="padding: 0 64px;">
''' + aiml_html.strip()[aiml_html.find('<div class="services-grid'):]
make_page("ai-ml-services.html", aiml_content)

print("Creating Managed IT page...")
man_start = orig_html.find('<!-- MANAGED IT -->')
man_end = orig_html.find('<!-- ABOUT -->')
hr_idx = orig_html.rfind('<hr class="section-rule">', man_start, man_end)
man_html = orig_html[man_start:hr_idx] if hr_idx != -1 else orig_html[man_start:man_end]
man_content = '''
<section id="hero" style="min-height: 400px; padding-top: 150px; padding-bottom: 80px; background: var(--off-white); border-bottom: 1px solid var(--border); text-align: center;">
  <div class="section-wrap" style="padding: 0;">
    <div class="hero-tag">Managed IT</div>
    <h1 class="hero-h1">Proactive Infrastructure You Can Rely On.</h1>
    <p class="section-lead" style="margin: 0 auto; max-width: 600px;">Our managed services are powered by an agentic monitoring layer that doesn\\'t just alert — it analyzes, decides, and resolves.</p>
  </div>
</section>
<section id="managed" style="padding-top: 80px; padding-bottom: 80px; background: var(--white); border-top: none;">
  <div class="section-wrap" style="padding: 0 64px;">
''' + man_html.strip()[man_html.find('<div class="managed-grid'):]
make_page("managed-it.html", man_content)

print("Creating About page...")
ab_start = orig_html.find('<!-- ABOUT -->')
ab_end = orig_html.find('<!-- CONTACT -->')
ab_html = orig_html[ab_start:ab_end]
ab_content = '''
<section id="hero" style="min-height: 400px; padding-top: 150px; padding-bottom: 80px; background: var(--off-white); border-bottom: 1px solid var(--border); text-align: center;">
  <div class="section-wrap" style="padding: 0;">
    <div class="hero-tag">About Sharkpen</div>
    <h1 class="hero-h1">Precision. Speed. Partnership.</h1>
  </div>
</section>
<section id="about" style="padding-top: 80px; padding-bottom: 80px; border-top: none;">
  <div class="section-wrap" style="padding: 0 64px;">
''' + ab_html.strip()[ab_html.find('<div class="about-grid'):]
make_page("about.html", ab_content)

print("Creating Contact page...")
cont_start = orig_html.find('<!-- CONTACT -->')
cont_end = orig_html.find('<!-- FOOTER -->')
make_page("contact.html", orig_html[cont_start:cont_end].strip())

print("Creating standard pages...")
make_page("case-studies.html", '''
<section id="hero" style="min-height: 400px; padding-top: 150px; padding-bottom: 80px; background: var(--off-white); border-bottom: 1px solid var(--border); text-align: center;">
  <div class="section-wrap" style="padding: 0;">
    <div class="hero-tag">Case Studies</div>
    <h1 class="hero-h1">Our Work In Action.</h1>
  </div>
</section>
<section style="padding: 100px 64px; background: var(--white);">
  <div class="section-wrap" style="max-width: 800px; margin: 0 auto; padding: 0;">
    <h2 class="section-title">Case Study 1: Logistics Agentic Dispatch</h2>
    <p style="font-size: 16px; color: var(--text2); line-height: 1.8;">By implementing a custom LLM orchestration workflow, we reduced manual dispatch errors by 80% for a Fortune 500 logistics provider. Agents automated route generation while keeping human-in-the-loop oversight on anomalies.</p>
    <hr style="margin: 40px 0; border: none; border-top: 1px solid var(--border);">
    <h2 class="section-title">Case Study 2: Healthcare Data Strategy</h2>
    <p style="font-size: 16px; color: var(--text2); line-height: 1.8;">Built a GDPR-compliant data lake and fine-tuned a medical LLM to assist practitioners. Information retrieval time for patient history plummeted by 30%, increasing hands-on care focus.</p>
  </div>
</section>
''')

make_page("privacy-policy.html", '''
<section style="padding: 150px 64px 100px; background: var(--white); min-height: 60vh;">
  <div class="section-wrap" style="max-width: 800px; margin: 0 auto; padding: 0;">
    <h1 class="hero-h1">Privacy Policy</h1>
    <p style="font-size: 15px; color: var(--text2); line-height: 1.8;">Your privacy is important to us. We only collect the minimal amount of information needed to provide our services. We do not sell your personal data to third parties.</p>
  </div>
</section>
''')

make_page("terms-of-service.html", '''
<section style="padding: 150px 64px 100px; background: var(--white); min-height: 60vh;">
  <div class="section-wrap" style="max-width: 800px; margin: 0 auto; padding: 0;">
    <h1 class="hero-h1">Terms of Service</h1>
    <p style="font-size: 15px; color: var(--text2); line-height: 1.8;">By using our services, you agree to our standard terms and conditions. These terms govern the use of Sharkpen Consulting\\'s platform and IT advisory engagements.</p>
  </div>
</section>
''')

make_page("accessibility.html", '''
<section style="padding: 150px 64px 100px; background: var(--white); min-height: 60vh;">
  <div class="section-wrap" style="max-width: 800px; margin: 0 auto; padding: 0;">
    <h1 class="hero-h1">Accessibility Statement</h1>
    <p style="font-size: 15px; color: var(--text2); line-height: 1.8;">We are committed to making our website accessible to all users, regardless of ability. If you have any difficulty navigating our site, please contact us for assistance.</p>
  </div>
</section>
''')

# Update index.html
repl = [
    ('<a href="#hero"', '<a href="index.html"'),
    ('<a href="#aiml"', '<a href="ai-ml-services.html"'),
    ('<a href="#managed"', '<a href="managed-it.html"'),
    ('<a href="#about"', '<a href="about.html"'),
    ('<a href="#contact"', '<a href="contact.html"'),
    ('<li><a href="#">Case Studies</a></li>', '<li><a href="case-studies.html">Case Studies</a></li>'),
    ('<li><a href="#">Privacy Policy</a></li>', '<li><a href="privacy-policy.html">Privacy Policy</a></li>'),
    ('<li><a href="#">Terms of Service</a></li>', '<li><a href="terms-of-service.html">Terms of Service</a></li>'),
    ('<li><a href="#">Accessibility</a></li>', '<li><a href="accessibility.html">Accessibility</a></li>')
]
for o, n in repl:
    orig_html = orig_html.replace(o, n)

def insert_btn(html, section_id, btn_html):
    start = html.find(f'id="{section_id}"')
    if start == -1: return html
    sec_end = html.find('</section>', start)
    if sec_end == -1: return html
    inner_div_end = html.rfind('</div>', start, sec_end)
    return html[:inner_div_end] + btn_html + "\\n  " + html[inner_div_end:]

orig_html = insert_btn(orig_html, 'aiml', '\\n    <div style="text-align: center; margin-top: 48px;">\\n      <a href="ai-ml-services.html" class="btn-primary">View All AI/ML Services</a>\\n    </div>')
orig_html = insert_btn(orig_html, 'managed', '\\n    <div style="text-align: center; margin-top: 48px;">\\n      <a href="managed-it.html" class="btn-primary">Explore Managed IT Services</a>\\n    </div>')
orig_html = insert_btn(orig_html, 'about', '\\n    <div style="text-align: center; margin-top: 48px;">\\n      <a href="about.html" class="btn-primary">Learn More About Us</a>\\n    </div>')

with open("index.html", "w") as f:
    f.write(orig_html)
