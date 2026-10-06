import os
import glob
import re

html_files = glob.glob('*.html')

target_link = 'mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace href="#" for request-access-btn with mailto link
    # Patterns: class="...request-access-btn..." href="#" or href="#" class="...request-access-btn..."
    # 1. <a href="#" class="nav-btn request-access-btn" ...>
    content_new = re.sub(
        r'href="#"(\s+class="[^"]*request-access-btn[^"]*")',
        f'href="{target_link}"\\1',
        content
    )
    content_new = re.sub(
        r'class="([^"]*request-access-btn[^"]*)"(\s+href="#")',
        f'class="\\1" href="{target_link}"',
        content_new
    )
    # Catch remaining links with text "Request Access" or "Diligence Access" or "Request Info" that have href="#"
    content_new = re.sub(
        r'href="#"([^>]*>(?:Request Access|Diligence Access|Request Info))',
        f'href="{target_link}"\\1',
        content_new
    )

    if content != content_new:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"Updated {file_path}")

# Update script.js so it doesn't preventDefault for mailto: links or .request-access-btn
if os.path.exists('script.js'):
    with open('script.js', 'r', encoding='utf-8') as f:
        script_content = f.read()

    # Comment out or remove modal logic for .request-access-btn so mailto works natively
    old_modal_code = """    // Modal Logic
    const modal = document.getElementById('investor-modal');
    const openBtns = document.querySelectorAll('.request-access-btn');
    const closeBtn = document.querySelector('.close-modal');

    if (modal && openBtns.length > 0 && closeBtn) {
        // Open Modal
        openBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('active');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            });
        });"""

    new_modal_code = """    // Modal Logic (Direct mailto handled natively)
    const modal = document.getElementById('investor-modal');
    const openBtns = document.querySelectorAll('.request-access-btn-modal-only');
    const closeBtn = document.querySelector('.close-modal');

    if (modal && openBtns.length > 0 && closeBtn) {
        // Open Modal
        openBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('active');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            });
        });"""

    if old_modal_code in script_content:
        script_content = script_content.replace(old_modal_code, new_modal_code)
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(script_content)
        print("Updated script.js")

print("Finished updating Request Access links.")
