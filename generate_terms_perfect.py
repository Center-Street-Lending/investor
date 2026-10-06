import html

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Security & Privacy Meta Tags -->
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Use | Center Street Capital</title>
    <meta name="description" content="Terms of Use for Center Street Capital. Conditions of website access, intellectual property, disclaimers, and governing law.">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles.css?v=5.00">
    <style>
        :root {
            --primary-navy: #0f172a;
            --secondary-navy: #1e293b;
            --brand-blue: #4683b3;
            --brand-blue-hover: #346892;
            --accent-orange: #f26522;
            --text-dark: #0f172a;
            --text-muted: #334155;
            --text-light: #64748b;
            --bg-light: #f8fafc;
            --border-light: #e2e8f0;
            --border-subtle: #cbd5e1;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #ffffff !important;
            color: var(--text-dark) !important;
            line-height: 1.75;
            -webkit-font-smoothing: antialiased;
        }

        /* Hero Header Styling */
        .terms-hero {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #ffffff;
            padding: 64px 5% 54px;
            border-bottom: 4px solid var(--brand-blue);
        }
        .terms-hero-container {
            max-width: 960px;
            margin: 0 auto;
        }
        .terms-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(70, 131, 179, 0.22);
            color: #7dd3fc;
            border: 1px solid rgba(125, 211, 252, 0.35);
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 18px;
        }
        .terms-hero h1 {
            font-size: 2.75rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.025em;
            margin: 0 0 12px 0;
            line-height: 1.2;
        }
        .terms-hero-subtitle {
            font-size: 1.12rem;
            color: #cbd5e1;
            max-width: 760px;
            margin: 0 0 24px 0;
            line-height: 1.6;
        }
        .terms-hero-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            font-size: 0.9rem;
            color: #94a3b8;
        }
        .terms-hero-meta strong {
            color: #ffffff;
        }

        /* Main Content Container */
        .legal-container {
            max-width: 960px;
            margin: 0 auto;
            padding: 54px 5% 90px;
        }

        /* Table of Contents Card */
        .toc-card {
            background: var(--bg-light);
            border: 1px solid var(--border-light);
            border-radius: 12px;
            padding: 30px 34px;
            margin-bottom: 54px;
            box-shadow: 0 2px 5px rgba(15, 23, 42, 0.03);
        }
        .toc-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 22px;
            padding-bottom: 14px;
            border-bottom: 2px solid var(--border-light);
        }
        .toc-card-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--primary-navy);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .toc-grid {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .toc-link {
            color: var(--brand-blue);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: color 0.15s ease;
        }
        .toc-link:hover {
            color: var(--primary-navy);
            text-decoration: underline;
        }

        /* Typography & Section Styling */
        .legal-section {
            margin-bottom: 48px;
            scroll-margin-top: 100px;
        }
        .legal-section h2 {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-navy);
            margin: 0 0 20px 0;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--border-light);
            letter-spacing: -0.01em;
        }
        .legal-section p {
            color: var(--text-muted);
            font-size: 1.02rem;
            margin-bottom: 20px;
            line-height: 1.78;
        }
        .legal-section strong {
            color: var(--primary-navy);
            font-weight: 700;
        }
        .legal-section a {
            color: var(--brand-blue);
            text-decoration: underline;
            text-underline-offset: 3px;
            transition: color 0.15s;
        }
        .legal-section a:hover {
            color: var(--brand-blue-hover);
        }

        .disclaimer-box {
            background: #fff7ed;
            border-left: 4px solid var(--accent-orange);
            border: 1px solid #ffedd5;
            border-left-width: 4px;
            border-radius: 8px;
            padding: 24px;
            margin: 24px 0;
        }
        .disclaimer-box p {
            color: #9a3412 !important;
            font-weight: 600;
            margin-bottom: 0 !important;
        }

        /* Contact Box Styling */
        .contact-card {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border: 1px solid var(--border-light);
            border-left: 4px solid var(--brand-blue);
            border-radius: 10px;
            padding: 30px;
            margin-top: 24px;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
        }
        .contact-card p {
            margin-bottom: 8px !important;
            color: var(--primary-navy) !important;
        }
        .contact-detail {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-top: 14px;
            font-size: 0.98rem;
            color: var(--text-muted);
        }
        .contact-detail-icon {
            color: var(--brand-blue);
            font-weight: 700;
            font-size: 1.1rem;
        }

        /* Header Navigation Sticky Fix */
        .header-wrapper {
            background-color: #ffffff;
            border-bottom: 1px solid var(--border-light);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
    </style>
</head>
<body>

    <!-- Unified Navigation Header -->
    <header class="header-wrapper">
        <div class="nav-container" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 5%; max-width: 1200px; margin: 0 auto;">
            <!-- Left: Logo -->
            <a href="./" class="logo" style="display: flex; align-items: center; text-decoration: none;">
                <img src="CS-Capital_Horiz_OnLight.svg" alt="Center Street Capital Logo" class="logo-image" style="height: 32px; width: auto; object-fit: contain;">
            </a>
            
            <!-- Right: Navigation Links (Desktop) -->
            <div class="desktop-nav" style="display: flex; align-items: center; gap: 20px;">
                <a href="who-we-are.html" class="nav-link" style="color: #334155; text-decoration: none; font-weight: 500; font-size: 0.9rem; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">Who we are</a>
                <a href="csl-rtf.html" class="nav-link" style="color: #334155; text-decoration: none; font-weight: 500; font-size: 0.9rem; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">CSL-RTF Fund</a>
                <a href="mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request" class="nav-btn request-access-btn" style="background-color: #f26522; color: #ffffff; padding: 10px 22px; border-radius: 4px; font-weight: 600; font-size: 0.9rem; text-decoration: none; transition: background-color 0.2s;">Request Access</a>
            </div>

            <!-- Hamburger Button (Mobile) -->
            <button class="hamburger-btn" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-menu">
        <div class="mobile-menu-inner">
            <a href="who-we-are.html" class="mobile-nav-link">Who we are <span>&rarr;</span></a>
            <a href="csl-rtf.html" class="mobile-nav-link">CSL-RTF Fund <span>&rarr;</span></a>
            <a href="mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request" class="nav-btn request-access-btn mobile-cta-btn">Request Access</a>
        </div>
    </div>

    <!-- Hero Header Banner -->
    <section class="terms-hero">
        <div class="terms-hero-container">
            <div class="terms-badge">Legal Terms &bull; Website Governance</div>
            <h1>Terms of Use</h1>
            <div class="terms-hero-subtitle">Conditions of access, intellectual property rights, disclaimers, and legal agreements for Center Street Capital.</div>
            <div class="terms-hero-meta">
                <span><strong>Last Updated:</strong> October 6, 2026</span>
                <span><strong>Organization:</strong> Center Street Capital</span>
            </div>
        </div>
    </section>

    <!-- Main Content Container -->
    <main class="legal-container">

        <!-- Table of Contents Card -->
        <div class="toc-card">
            <div class="toc-card-header">
                <div class="toc-card-title">Table of Contents</div>
            </div>
            <div class="toc-grid">
                <a href="#section-1" class="toc-link">1. Agreement</a>
                <a href="#section-2" class="toc-link">2. The Site is an introduction only</a>
                <a href="#section-3" class="toc-link">3. Eligibility</a>
                <a href="#section-4" class="toc-link">4. License and intellectual property</a>
                <a href="#section-5" class="toc-link">5. Acceptable use</a>
                <a href="#section-6" class="toc-link">6. Submissions</a>
                <a href="#section-7" class="toc-link">7. Third-party links</a>
                <a href="#section-8" class="toc-link">8. Disclaimer of warranties</a>
                <a href="#section-9" class="toc-link">9. Limitation of liability</a>
                <a href="#section-10" class="toc-link">10. Indemnity</a>
                <a href="#section-11" class="toc-link">11. Governing law and venue</a>
                <a href="#section-12" class="toc-link">12. Changes</a>
                <a href="#section-13" class="toc-link">13. Contact</a>
            </div>
        </div>

        <!-- Section 1 -->
        <div class="legal-section" id="section-1">
            <h2>1. Agreement</h2>
            <p>These Terms of Use (the “Terms”) govern access to and use of <a href="./">www.centerstreetcapital.com</a> and any related pages we operate (the “Site”). The Site is operated by Center Street Capital (“Center Street Capital,” “we,” “us,” or “our”). By accessing the Site, you agree to these Terms, our <a href="legal-notice.html">Important Legal Notice</a>, <a href="privacy-policy.html">Privacy Policy</a>, and <a href="cookie-policy.html">Cookie Policy</a>. If you do not agree, do not use the Site.</p>
        </div>

        <!-- Section 2 -->
        <div class="legal-section" id="section-2">
            <h2>2. The Site is an introduction only</h2>
            <p>The Site is a general introduction to Center Street Capital. It is not an offer to sell or a solicitation of an offer to buy any security. We manage or co-manage private credit and private equity funds. We do not provide investment advice to individual clients through the Site. Visiting the Site does not make you our client or an investor in any fund.</p>
        </div>

        <!-- Section 3 -->
        <div class="legal-section" id="section-3">
            <h2>3. Eligibility</h2>
            <p>The Site is intended for persons 18 years of age or older. You may not use the Site where such use is prohibited by law.</p>
        </div>

        <!-- Section 4 -->
        <div class="legal-section" id="section-4">
            <h2>4. License and intellectual property</h2>
            <p>We grant you a limited, revocable, non-exclusive, non-transferable license to view the Site for your personal or internal professional use. All content, trademarks, logos, and design — including the name “Center Street Capital” — are owned by us or our licensors. You may not copy, scrape, crawl, harvest, republish, commercially exploit, or use Site content to train machine-learning models without our prior written consent. You may not frame the Site or impersonate the firm.</p>
        </div>

        <!-- Section 5 -->
        <div class="legal-section" id="section-5">
            <h2>5. Acceptable use</h2>
            <p>You agree not to: (a) attempt unauthorized access to any portal, server, or data; (b) interfere with the security or operation of the Site; (c) upload malware; (d) use the Site to send unsolicited promotional messages; (e) misrepresent your identity or affiliation; or (f) use the Site in violation of applicable law.</p>
        </div>

        <!-- Section 6 -->
        <div class="legal-section" id="section-6">
            <h2>6. Submissions</h2>
            <p>Do not send Social Security numbers, account credentials, wire instructions, or material nonpublic information through a public form. Except as described in our Privacy Policy, information you submit through the Site is treated as non-confidential. You grant us a non-exclusive license to use submissions as needed to operate the Site and respond to you.</p>
        </div>

        <!-- Section 7 -->
        <div class="legal-section" id="section-7">
            <h2>7. Third-party links</h2>
            <p>The Site may link to third-party websites. We do not control or endorse those sites and are not responsible for their content, policies, or practices.</p>
        </div>

        <!-- Section 8 -->
        <div class="legal-section" id="section-8">
            <h2>8. Disclaimer of warranties</h2>
            <div class="disclaimer-box">
                <p>THE SITE IS PROVIDED “AS IS” AND “AS AVAILABLE.” TO THE MAXIMUM EXTENT PERMITTED BY LAW, WE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. WE DO NOT WARRANT THAT THE SITE WILL BE UNINTERRUPTED, ERROR-FREE, OR FREE OF HARMFUL COMPONENTS.</p>
            </div>
        </div>

        <!-- Section 9 -->
        <div class="legal-section" id="section-9">
            <h2>9. Limitation of liability</h2>
            <div class="disclaimer-box">
                <p>TO THE MAXIMUM EXTENT PERMITTED BY LAW, CENTER STREET CAPITAL AND ITS AFFILIATES, AND THEIR RESPECTIVE MEMBERS, MANAGERS, OFFICERS, EMPLOYEES, AND AGENTS, WILL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES, OR ANY LOSS OF PROFITS, DATA, OR GOODWILL, ARISING OUT OF OR RELATED TO YOUR USE OF THE SITE.</p>
            </div>
            <p>This Section limits liability arising from use of a public website. It does not waive any right that cannot be waived under the federal securities laws or under the California Consumer Privacy Act, and it does not limit liability for fraud or willful misconduct.</p>
        </div>

        <!-- Section 10 -->
        <div class="legal-section" id="section-10">
            <h2>10. Indemnity</h2>
            <p>You agree to indemnify and hold harmless Center Street Capital and its affiliates, and their respective members, managers, officers, employees, and agents, from claims, damages, losses, and expenses (including reasonable attorneys’ fees) arising out of your misuse of the Site or your violation of these Terms.</p>
        </div>

        <!-- Section 11 -->
        <div class="legal-section" id="section-11">
            <h2>11. Governing law and venue</h2>
            <p>These Terms are governed by the laws of the State of California, without regard to conflict-of-law rules. Exclusive venue for disputes arising out of the Site lies in the state or federal courts located in Orange County, California, except where a non-waivable statute requires otherwise.</p>
        </div>

        <!-- Section 12 -->
        <div class="legal-section" id="section-12">
            <h2>12. Changes</h2>
            <p>We may revise these Terms by posting an updated version on the Site with a new “Last updated” date. Continued use of the Site after posting constitutes acceptance. If you do not agree, stop using the Site.</p>
        </div>

        <!-- Section 13 -->
        <div class="legal-section" id="section-13">
            <h2>13. Contact</h2>
            <p>If you have questions regarding these Terms, you may contact us at:</p>
            <div class="contact-card">
                <p style="font-size: 1.05rem; font-weight: 700; color: var(--primary-navy);">Center Street Capital</p>
                <div class="contact-detail">
                    <span class="contact-detail-icon">&bull;</span>
                    <span>18201 Von Karman Ave STE 400, Irvine, CA 92612</span>
                </div>
                <div class="contact-detail">
                    <span class="contact-detail-icon">&bull;</span>
                    <span>General Inquiries: <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a></span>
                </div>
                <div class="contact-detail">
                    <span class="contact-detail-icon">&bull;</span>
                    <span>Diligence Requests: <a href="mailto:ir@centerstreetcapital.com">ir@centerstreetcapital.com</a></span>
                </div>
                <div class="contact-detail">
                    <span class="contact-detail-icon">&bull;</span>
                    <span>Phone: (949) 244-1090</span>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer style="background-color: #0f172a; color: #cbd5e1; padding: 70px 0 40px; border-top: 1px solid #1e293b;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 5%;">
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px; margin-bottom: 50px;">
                <!-- Column 1 -->
                <div>
                    <a href="./" style="display: flex; align-items: center; text-decoration: none; margin-bottom: 20px;">
                        <img src="CS-Capital_Horiz_OnDark.svg" alt="Center Street Capital Logo" style="height: 32px; width: auto; object-fit: contain;">
                    </a>
                    <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; margin: 0 0 16px 0; max-width: 380px;">We manage and co-manage private credit and private equity funds, built on rigorous underwriting and GP capital in every strategy.</p>
                    <p style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6; margin: 0;">Center Street Capital<br>18201 Von Karman Ave, Suite 400, Irvine, CA 92612<br>Diligence requests: <a href="mailto:ir@centerstreetcapital.com" style="color: #cbd5e1; text-decoration: none;">ir@centerstreetcapital.com</a><br>(949) 244-1090</p>
                </div>
                <!-- Column 2 -->
                <div>
                    <h4 style="color: #ffffff; font-weight: 700; margin: 0 0 20px 0; font-size: 0.95rem;">Strategies</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 12px;"><a href="csl-rtf.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">CSL-RTL Fund (Real Estate Debt)</a></li>
                        <li><a href="riviera-capital-partners.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Center Street Riviera Direct Corporate Lending</a></li>
                    </ul>
                </div>
                <!-- Column 3 -->
                <div>
                    <h4 style="color: #ffffff; font-weight: 700; margin: 0 0 20px 0; font-size: 0.95rem;">Firm</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 12px;"><a href="who-we-are.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Who We Are</a></li>
                        <li style="margin-bottom: 12px;"><a href="./#who-we-serve" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Who We Serve</a></li>
                        <li><a href="mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request" class="request-access-btn" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Diligence Access</a></li>
                    </ul>
                </div>
                <!-- Column 4 -->
                <div>
                    <h4 style="color: #ffffff; font-weight: 700; margin: 0 0 20px 0; font-size: 0.95rem;">Legal & Disclosures</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 12px;"><a href="legal-notice.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Important Legal Notice</a></li>
                        <li style="margin-bottom: 12px;"><a href="terms-of-use.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Terms of Use</a></li>
                        <li><a href="privacy-policy.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Privacy Policy</a></li>
                    </ul>
                </div>
            </div>
            <div style="border-top: 1px solid #1e293b; padding-top: 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <p style="color: #64748b; font-size: 0.8rem; margin: 0;">&copy; 2026 Center Street Capital. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Mobile Menu JS -->
    <script>
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        const mobileMenu = document.querySelector('.mobile-menu');
        if (hamburgerBtn && mobileMenu) {
            hamburgerBtn.addEventListener('click', () => {
                hamburgerBtn.classList.toggle('active');
                mobileMenu.classList.toggle('active');
            });
        }
    </script>
</body>
</html>
"""

with open('/Users/gregmontoya/AntiGravity Workspaces/CSLCompanies.com/terms-of-use.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated terms-of-use.html successfully!")
