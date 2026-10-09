document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar') || document.querySelector('.header-wrapper');
    
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Mobile Menu Toggle
    const menuBtn = document.querySelector('.mobile-menu-btn') || document.querySelector('.hamburger-btn');
    const navLinks = document.querySelector('.nav-links') || document.querySelector('.mobile-menu');

    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            menuBtn.classList.toggle('active');
            navLinks.classList.toggle('open');
            navLinks.classList.toggle('active');
            
            // Toggle hamburger animation
            const spans = menuBtn.querySelectorAll('span');
            if (spans.length >= 3) {
                if (navLinks.classList.contains('open') || navLinks.classList.contains('active')) {
                    spans[0].style.transform = 'rotate(45deg) translate(6px, 6px)';
                    spans[1].style.opacity = '0';
                    spans[2].style.transform = 'rotate(-45deg) translate(6px, -6px)';
                } else {
                    spans[0].style.transform = 'none';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = 'none';
                }
            }
        });

        // Close mobile menu on click outside
        document.addEventListener('click', (e) => {
            if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
                menuBtn.classList.remove('active');
                navLinks.classList.remove('open');
                navLinks.classList.remove('active');
            }
        });
    }

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (!targetId || targetId === '#' || targetId === '#!') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                
                // Close mobile menu if open
                if (navLinks && navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                }

                const headerOffset = 70; // height of navbar offset
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Cookie Banner Logic Removed
});

// Direct Email Action for Request Access
window.openInvestorModal = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    window.location.href = "mailto:ir@centerstreetcapital.com?subject=" + encodeURIComponent("Diligence Access Request - Center Street Capital");
    return false;
};

window.closeInvestorModal = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const modal = document.getElementById('investorModal') || document.getElementById('investor-modal');
    if (modal) {
        modal.classList.remove('active');
        modal.style.display = 'none';
        modal.style.opacity = '0';
        modal.style.pointerEvents = 'none';
        document.body.style.overflow = '';
    }
};

window.handleDiligenceFormSubmit = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    
    const name = (document.getElementById('req-name')?.value || '').trim();
    const email = (document.getElementById('req-email')?.value || '').trim();
    const company = (document.getElementById('req-company')?.value || '').trim() || 'N/A';
    const phone = (document.getElementById('req-phone')?.value || '').trim() || 'N/A';
    
    const typeEl = document.querySelector('input[name="investor_type"]:checked');
    const investorType = typeEl ? typeEl.value : 'General Investor';

    const subject = `Diligence Access Request - ${investorType} - ${name}`;
    const bodyText = `Full Name: ${name}\nEmail: ${email}\nCompany/Firm: ${company}\nPhone: ${phone}\nInvestor Type: ${investorType}\n\nRequesting diligence materials for Center Street Capital.`;

    const mailtoUrl = `mailto:ir@centerstreetcapital.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyText)}`;
    
    window.location.href = mailtoUrl;
    
    setTimeout(() => {
        window.closeInvestorModal();
    }, 400);

    return false;
};

// Global Bio Modal Functions
window.getOrCreateBioModal = function() {
    let modal = document.getElementById('bio-modal') || document.getElementById('bioModal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'bio-modal';
        modal.className = 'modal';
        modal.style.cssText = 'display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(15, 23, 42, 0.8); z-index: 100000; overflow-y: auto; align-items: center; justify-content: center; backdrop-filter: blur(6px);';
        modal.innerHTML = `
            <div class="modal-content" style="max-width: 680px; width: 90%; padding: 36px; border-radius: 16px; position: relative; background-color: #ffffff; margin: 40px auto; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); text-align: left;">
                <span class="close-bio-modal close-modal" onclick="window.closeBioModal(event)" style="position: absolute; top: 20px; right: 24px; font-size: 28px; cursor: pointer; color: #94a3b8; line-height: 1;">&times;</span>
                <div style="display: flex; gap: 20px; align-items: center; margin-bottom: 24px;" class="bio-header-flex">
                    <div style="width: 90px; height: 90px; border-radius: 50%; overflow: hidden; border: 2px solid #e2e8f0; flex-shrink: 0;">
                        <img id="bio-modal-image" src="" alt="" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div>
                        <h3 id="bio-modal-name" style="font-size: 1.5rem; font-weight: 700; color: #0f172a; margin: 0 0 4px 0; line-height: 1.2;"></h3>
                        <div id="bio-modal-title" style="color: #4683b3; font-size: 0.9rem; font-weight: 600; line-height: 1.4; margin-bottom: 8px;"></div>
                        <div id="bio-modal-highlights" style="font-size: 0.78rem; color: #64748b; background-color: #f8fafc; padding: 4px 10px; border-radius: 6px; border: 1px solid #e2e8f0; display: inline-block;"></div>
                    </div>
                </div>
                <div style="border-top: 1px solid #e2e8f0; padding-top: 20px;">
                    <p id="bio-modal-text" style="font-size: 0.95rem; color: #475569; line-height: 1.65; margin: 0; white-space: pre-line;"></p>
                </div>
            </div>
        `;
        document.body.appendChild(modal);

        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                window.closeBioModal(e);
            }
        });
    }
    return modal;
};

window.openBioModal = function(element, e) {
    if (e && e.preventDefault) e.preventDefault();
    if (e && e.stopPropagation) e.stopPropagation();

    const trigger = element || (e ? e.currentTarget : null);
    if (!trigger) return false;

    const name = trigger.getAttribute('data-bio-name') || '';
    const title = trigger.getAttribute('data-bio-title') || '';
    const image = trigger.getAttribute('data-bio-image') || '';
    const text = trigger.getAttribute('data-bio-text') || '';
    const highlights = trigger.getAttribute('data-bio-highlights') || '';

    const modal = window.getOrCreateBioModal();
    const nameEl = document.getElementById('bio-modal-name');
    const titleEl = document.getElementById('bio-modal-title');
    const imageEl = document.getElementById('bio-modal-image');
    const textEl = document.getElementById('bio-modal-text');
    const highlightsEl = document.getElementById('bio-modal-highlights');

    if (nameEl) nameEl.textContent = name;
    if (titleEl) titleEl.textContent = title;
    if (imageEl) { imageEl.src = image; imageEl.alt = name; }
    if (textEl) textEl.textContent = text;
    if (highlightsEl) {
        if (highlights) {
            highlightsEl.innerHTML = highlights;
            highlightsEl.style.display = 'inline-block';
        } else {
            highlightsEl.style.display = 'none';
        }
    }

    modal.classList.add('active');
    modal.style.display = 'flex';
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
    document.body.style.overflow = 'hidden';
    return false;
};

window.closeBioModal = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const modal = document.getElementById('bio-modal') || document.getElementById('bioModal');
    if (modal) {
        modal.classList.remove('active');
        modal.style.display = 'none';
        modal.style.opacity = '0';
        modal.style.pointerEvents = 'none';
        document.body.style.overflow = '';
    }
    return false;
};

// Global Click Delegation for Diligence Modal and Bio Modals
document.addEventListener('click', function(e) {

    // Check Request Access trigger (direct email action)
    const triggerAccess = e.target.closest('.request-access-btn, .request-access-link');
    if (triggerAccess && !triggerAccess.closest('.exec-card-item') && !triggerAccess.closest('.bio-trigger')) {
        e.preventDefault();
        window.openInvestorModal(e);
        return;
    }

    // Check Close Diligence Modal
    if (e.target.closest('.close-modal') && !e.target.closest('.close-bio-modal')) {
        window.closeInvestorModal(e);
        return;
    }

    // Check Close Bio Modal
    if (e.target.closest('.close-bio-modal')) {
        window.closeBioModal(e);
        return;
    }

    // Check Executive Bio Modal trigger
    const bioTrigger = e.target.closest('.bio-trigger, [data-bio-name]');
    if (bioTrigger) {
        window.openBioModal(bioTrigger, e);
        return;
    }

    // Close Diligence Modal via backdrop click
    const invModal = document.getElementById('investorModal') || document.getElementById('investor-modal');
    if (e.target === invModal) {
        window.closeInvestorModal(e);
    }
    
    // Close Bio Modal via backdrop click
    const bioModal = document.getElementById('bio-modal') || document.getElementById('bioModal');
    if (e.target === bioModal) {
        window.closeBioModal(e);
    }
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        window.closeInvestorModal(e);
        window.closeBioModal(e);
    }
});
