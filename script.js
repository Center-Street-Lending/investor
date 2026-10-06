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

    // Modal Logic (Direct mailto handled natively)
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
        });

        // Close Modal via X button
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        });

        // Close Modal via clicking outside
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
        
        // Escape key to close
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // Bio Modal Trigger Handling
    const bioModal = document.getElementById('bio-modal');
    const bioTriggers = document.querySelectorAll('.bio-trigger');
    const closeBioBtn = document.querySelector('.close-bio-modal');

    if (bioModal && bioTriggers.length > 0) {
        bioTriggers.forEach(card => {
            card.style.cursor = 'pointer';
            card.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const name = card.getAttribute('data-bio-name');
                const title = card.getAttribute('data-bio-title');
                const image = card.getAttribute('data-bio-image');
                const text = card.getAttribute('data-bio-text');
                const highlights = card.getAttribute('data-bio-highlights');

                document.getElementById('bio-modal-name').textContent = name;
                document.getElementById('bio-modal-title').textContent = title;
                document.getElementById('bio-modal-image').src = image;
                document.getElementById('bio-modal-image').alt = name;
                document.getElementById('bio-modal-text').textContent = text;
                document.getElementById('bio-modal-highlights').innerHTML = highlights;

                bioModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        if (closeBioBtn) {
            closeBioBtn.addEventListener('click', () => {
                bioModal.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        window.addEventListener('click', (e) => {
            if (e.target === bioModal) {
                bioModal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && bioModal.classList.contains('active')) {
                bioModal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // Cookie Banner Logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesBtn = document.getElementById('accept-cookies');
    const rejectCookiesBtn = document.getElementById('reject-cookies');
    const openCookieSettingsBtn = document.getElementById('open-cookie-settings');

    if (cookieBanner) {
        const consent = localStorage.getItem('csc_cookie_consent');
        if (!consent) {
            cookieBanner.style.display = 'block';
        }

        if (acceptCookiesBtn) {
            acceptCookiesBtn.addEventListener('click', () => {
                localStorage.setItem('csc_cookie_consent', 'accepted');
                cookieBanner.style.display = 'none';
            });
        }

        if (rejectCookiesBtn) {
            rejectCookiesBtn.addEventListener('click', () => {
                localStorage.setItem('csc_cookie_consent', 'rejected');
                cookieBanner.style.display = 'none';
            });
        }

        if (openCookieSettingsBtn) {
            openCookieSettingsBtn.addEventListener('click', (e) => {
                e.preventDefault();
                cookieBanner.style.display = 'block';
            });
        }
    }
});

