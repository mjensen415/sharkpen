import re

def update_form(filename):
    with open(filename, "r") as f:
        html = f.read()

    # The block we want to replace
    old_form_start = html.find('<form class="contact-form-wrap"')
    if old_form_start == -1:
        return False
        
    old_form_end = html.find('</form>', old_form_start)
    if old_form_end == -1:
        return False
    
    # We want to keep the wrapping structure but change the inner form
    old_block = html[old_form_start:old_form_end + 7] # pull the closing </form>
    
    new_block = '''<form class="contact-form-wrap" action="https://formsubmit.co/dskarpnes@sharkpenconsulting.com" method="POST" autocomplete="off">
          <div class="form-title">Request a Consultation</div>
          <div class="form-subtitle">We respond to all inquiries within one business day.</div>
          <div class="form-row">
            <div class="form-group">
              <label>First Name</label>
              <input type="text" name="First Name" placeholder="Alex" required>
            </div>
            <div class="form-group">
              <label>Last Name</label>
              <input type="text" name="Last Name" placeholder="Johnson" required>
            </div>
          </div>
          <div class="form-group">
            <label>Work Email</label>
            <input type="email" name="Email" placeholder="alex@yourcompany.com" required>
          </div>
          <div class="form-group">
            <label>Company</label>
            <input type="text" name="Company" placeholder="Your Organization">
          </div>
          <div class="form-group">
            <label>Area of Interest</label>
            <select name="Interest">
              <option value="" disabled selected>Select a service area</option>
              <option value="AI/ML Training & Enablement">AI/ML Training & Enablement</option>
              <option value="Custom Model Development">Custom Model Development</option>
              <option value="Managed Cloud Operations">Managed Cloud Operations</option>
              <option value="Cybersecurity & Compliance">Cybersecurity & Compliance</option>
              <option value="Agentic IT Monitoring">Agentic IT Monitoring</option>
              <option value="AI Readiness Assessment">AI Readiness Assessment</option>
              <option value="Full Partnership / All Services">Full Partnership / All Services</option>
            </select>
          </div>
          <div class="form-group">
            <label>Tell us about your challenge</label>
            <textarea name="Message" placeholder="Briefly describe your current environment and what you're looking to achieve..." required></textarea>
          </div>
          <button type="submit" class="submit-btn" onclick="handleSubmit(this)">Send Message</button>
        </form>'''
        
    html = html.replace(old_block, new_block)
    
    with open(filename, "w") as f:
        f.write(html)
    return True

print("Updating index.html:", update_form("index.html"))
print("Updating contact.html:", update_form("contact.html"))
