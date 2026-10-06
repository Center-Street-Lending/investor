import docx
import html

# -------------------------------------------------------------
# 1. GENERATE RAW PRIVACY POLICY (privacy-policy.html)
# -------------------------------------------------------------
doc_privacy = docx.Document('/Users/gregmontoya/.gemini/antigravity/brain/9d721591-535b-4651-ba85-9e6a1aa3b496/.user_uploaded/media_1791303197568.docx')

states_list = [
    ("California", "https://oag.ca.gov/contact/consumer-complaint-against-business-or-company"),
    ("Colorado", "https://coag.gov/file-complaint/"),
    ("Connecticut", "https://portal.ct.gov/AG/Common/Complaint-Form-Landing-page"),
    ("Delaware", "https://attorneygeneral.delaware.gov/fraud/cmu/complaint/"),
    ("Florida", "https://www.myfloridalegal.com/how-to-contact-us/file-a-complaint"),
    ("Indiana", "https://www.in.gov/attorneygeneral/consumer-protection-division/file-a-complaint/"),
    ("Iowa", "https://www.iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint/complaint-form"),
    ("Kentucky", "https://www.ag.ky.gov/about/Office-Divisions/OCP/Pages/default.aspx"),
    ("Maryland", "https://portal.oag.state.md.us/cpdportal/?q=Home"),
    ("Minnesota", "https://www.ag.state.mn.us/Office/Complaint.aspx"),
    ("Montana", "https://dojmt.gov/office-of-consumer-protection/consumer-complaints/"),
    ("Nebraska", "https://protectthegoodlife.nebraska.gov/data-privacy-homepage"),
    ("New Hampshire", "https://www.doj.nh.gov/consumer/complaints/"),
    ("New Jersey", "https://www.njconsumeraffairs.gov/Pages/Consumer-Complaints.aspx"),
    ("Oklahoma", "https://oklahoma.gov/oag.html"),
    ("Oregon", "https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/"),
    ("Rhode Island", "https://riag.ri.gov/forms/consumer-complaint"),
    ("Tennessee", "https://www.tn.gov/attorneygeneral/working-for-tennessee/consumer/file-a-complaint.html"),
    ("Texas", "https://consumerprotection.texasattorneygeneral.gov/consumercomplaintportal/s/"),
    ("Utah", "https://services.commerce.utah.gov/dcp-complaint/"),
    ("Virginia", "https://www.oag.state.va.us/consumer-protection/index.php/file-a-complaint")
]

table_privacy = doc_privacy.tables[0]
table_rows_privacy = []
for row in table_privacy.rows[1:]:
    cells = [cell.text.strip() for cell in row.cells]
    table_rows_privacy.append(cells)

privacy_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Security & Privacy Meta Tags -->
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy | Center Street Capital</title>
    <meta name="description" content="Privacy Policy and U.S. State Privacy Notice for Center Street Capital. How we collect, use, disclose, and protect personal information.">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles.css?v=5.20">
    <style>
        body {{
            background-color: #ffffff !important;
            color: #0f172a !important;
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            line-height: 1.8;
        }}
        .legal-content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 5% 100px;
            color: #334155;
            font-size: 1.02rem;
            background-color: #ffffff;
        }}
        .legal-content h1 {{
            font-size: 2.35rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }}
        .legal-date {{
            color: #64748b;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 36px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 16px;
        }}
        
        /* Clean Raw Table of Contents */
        .toc-wrapper {{
            margin-bottom: 44px;
            padding-bottom: 24px;
            border-bottom: 1px solid #e2e8f0;
        }}
        .toc-title {{
            font-size: 1rem;
            font-weight: 700;
            color: #0f172a;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
        }}
        .toc-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .toc-list a {{
            color: #4683b3;
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
        }}
        .toc-list a:hover {{
            color: #0f172a;
            text-decoration: underline;
        }}

        .legal-content h2 {{
            font-size: 1.35rem;
            font-weight: 700;
            color: #0f172a;
            margin-top: 44px;
            margin-bottom: 16px;
            padding-top: 16px;
            border-top: 1px solid #f1f5f9;
            scroll-margin-top: 90px;
        }}
        .legal-content h2:first-of-type {{
            border-top: none;
            padding-top: 0;
        }}
        .legal-content p {{
            margin-bottom: 20px;
            color: #334155;
        }}
        .legal-content strong {{
            color: #0f172a;
        }}
        .legal-content ul {{
            margin: 0 0 24px 24px;
            padding: 0;
            color: #334155;
        }}
        .legal-content li {{
            margin-bottom: 10px;
        }}
        .legal-content a {{
            color: #4683b3;
            text-decoration: underline;
        }}

        /* Clean Raw Table Styling */
        .table-responsive {{
            overflow-x: auto;
            margin: 28px 0 36px 0;
            border: 1px solid #e2e8f0;
        }}
        .privacy-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            text-align: left;
            min-width: 750px;
        }}
        .privacy-table th {{
            background-color: #f8fafc;
            color: #0f172a;
            font-weight: 700;
            padding: 14px 16px;
            border-bottom: 2px solid #cbd5e1;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}
        .privacy-table td {{
            padding: 14px 16px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
            color: #334155;
            line-height: 1.6;
        }}
        .privacy-table tr:last-child td {{
            border-bottom: none;
        }}

        /* Clean State AG List */
        .ag-list {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px 24px;
            margin: 16px 0 24px 0;
        }}
        @media (max-width: 640px) {{
            .ag-list {{
                grid-template-columns: 1fr;
            }}
        }}
        .ag-list div {{
            font-size: 0.92rem;
            color: #334155;
        }}

        /* Header Navigation */
        .header-wrapper {{
            background-color: #ffffff;
            border-bottom: 1px solid #e2e8f0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
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
                <a href="csl-rtf-fund.html" class="nav-link" style="color: #334155; text-decoration: none; font-weight: 500; font-size: 0.9rem; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">CSL-RTF Fund</a>
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
            <a href="csl-rtf-fund.html" class="mobile-nav-link">CSL-RTF Fund <span>&rarr;</span></a>
            <a href="mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request" class="nav-btn request-access-btn mobile-cta-btn">Request Access</a>
        </div>
    </div>

    <!-- Main Content Container -->
    <main class="legal-content">
        <h1>Privacy Policy</h1>
        <div class="legal-date">Updated: October 6, 2026</div>

        <!-- Clean Raw Table of Contents -->
        <div class="toc-wrapper">
            <div class="toc-title">Table of Contents</div>
            <div class="toc-list">
                <a href="#section-1">1. Introduction</a>
                <a href="#section-2">2. Scope</a>
                <a href="#section-3">3. Notice at Collection</a>
                <a href="#section-4">4. Sources of Collected Personal Information</a>
                <a href="#section-5">5. How We Use Personal Information (Purposes for Collection and Processing)</a>
                <a href="#section-6">6. Cookies and Other Technologies</a>
                <a href="#section-7">7. How We Disclose Personal Information</a>
                <a href="#section-8">8. Your U.S. State Privacy Rights</a>
                <a href="#section-9">9. Opt-Out Preference Signals</a>
                <a href="#section-10">10. Children and Individuals Under the Age of Eighteen</a>
                <a href="#section-11">11. Newsletters and Emails</a>
                <a href="#section-12">12. Security of Your Information</a>
                <a href="#section-13">13. Retention of Personal Information</a>
                <a href="#section-14">14. Linked Materials</a>
                <a href="#section-15">15. Changes to Our Privacy Policy</a>
                <a href="#section-16">16. Reasonable Fees</a>
                <a href="#section-17">17. How to Contact Us</a>
            </div>
        </div>

        <!-- Section 1 -->
        <h2 id="section-1">1. Introduction</h2>
        <p>Center Street Capital, LLC ("Center Street Capital," "we," "us," and "our") recognizes the importance of protecting the privacy of the personal information you provide to us.</p>
        <p>"Personal information" means information that identifies, relates to, describes, is capable of being associated with, or could reasonably be linked, directly or indirectly, with a particular consumer or household. "Personal information" does not include publicly available information (e.g., information from government records or information lawfully made available to the general public), deidentified information, or aggregate consumer information. If we process deidentified information, we publicly commit to maintain and use deidentified information only in deidentified form, not to attempt to re-identify it, and to contractually obligate recipients to do the same.</p>
        <p>We have developed this Privacy Policy (the "Policy") so that you can make educated and informed decisions about the personal information that you entrust to us when you use <a href="./">www.centerstreetcapital.com</a> and any other website, mobile website, our official pages on third-party social media platforms (to the extent permitted by those platforms' terms), email communications you exchange with us, and any other digital platform, including any services, features, pages, and functions contained or offered therein, that are owned, operated, or provided by Center Street Capital (collectively, the "Site"), and so you understand how we collect, use, disclose, and otherwise manage this information.</p>
        <p>This Policy is incorporated into our <a href="terms-of-use.html">Terms of Service</a>. If there are any terms in this Policy or in our Terms of Service to which you do not agree, you must discontinue your use of the Site. <strong>PLEASE READ THIS PRIVACY POLICY CAREFULLY. BY USING OUR SITE, YOU ACKNOWLEDGE THAT YOU HAVE READ, UNDERSTAND, AND AGREE TO THE TERMS OF THIS PRIVACY POLICY.</strong> If you do not agree with this Policy, do not use the Site or provide personal information to us.</p>
        <p>This Policy is written in the English language. We do not guarantee the accuracy of any translated versions of this Policy. To the extent any translated versions conflict with the English language version, the English language version shall control. Our Site is intended for United States residents only.</p>

        <!-- Section 2 -->
        <h2 id="section-2">2. Scope</h2>
        <p>This Policy applies to personal information collected through the Site.</p>

        <!-- Section 3 -->
        <h2 id="section-3">3. Notice at Collection</h2>
        <p>We collect the following categories of personal information:</p>

        <div class="table-responsive">
            <table class="privacy-table">
                <thead>
                    <tr>
                        <th style="width: 18%;">Category</th>
                        <th style="width: 22%;">Examples We Collect</th>
                        <th style="width: 22%;">Purposes</th>
                        <th style="width: 20%;">Sold or Shared?</th>
                        <th style="width: 18%;">Retention</th>
                    </tr>
                </thead>
                <tbody>
"""

for row in table_rows_privacy:
    cat, ex, purp, sold, ret = row
    privacy_html += f"""                    <tr>
                        <td><strong>{html.escape(cat)}</strong></td>
                        <td>{html.escape(ex)}</td>
                        <td>{html.escape(purp)}</td>
                        <td>{html.escape(sold)}</td>
                        <td>{html.escape(ret)}</td>
                    </tr>
"""

privacy_html += """                </tbody>
            </table>
        </div>

        <p>In the preceding 12 months, we disclosed Identifiers, Internet/network activity, Professional information, Customer-records information, and Commercial information to service providers that provide website hosting, analytics, and email/form processing on our behalf.</p>
        <p>For more information on retention of Personal Information for all Categories see Section 13 (Retention of Personal Information).</p>
        <p>We do <strong>not</strong> sell personal information. We do not share personal information for cross-context behavioral advertising, and we do not use advertising or retargeting pixels. We do not engage in automated decision-making or profiling to make decisions that produce legal or similarly significant effects about individuals. If these practices change, we will update this Policy and provide a "Do Not Sell or Share" link.</p>
        <p><strong>Non-personal information.</strong> Even if you do not provide any personal information to Center Street Capital, we collect non-personal information about your use of the Site — information that we cannot use to identify or contact you, such as aggregate statistics. If you do not want us to collect such information, please do not use the Site.</p>

        <!-- Section 4 -->
        <h2 id="section-4">4. Sources of Collected Personal Information</h2>
        <p>Center Street Capital collects personal information from the following sources.</p>
        <p><strong>Information you provide to us directly.</strong> Center Street Capital collects personal information from you directly when you interact with the Site, contact us, submit a diligence-access request, sign up to receive emails from us, or otherwise communicate with us. When you use the Site, we may collect your name, firm, title, email address, phone number, and the content of the messages you send us, including diligence-access requests. Please do not submit Social Security numbers, government IDs, or wire instructions through the public Site.</p>
        <p><strong>Information we obtain indirectly.</strong> We may receive publicly available professional information about you, and information from service providers who host or analyze the Site. We may combine this with information we have already collected, such as your contact details and prior inquiry history, to respond to your requests and to improve the Site.</p>
        <p><strong>Information collected automatically.</strong> When you use our Site, we collect certain information automatically through cookies and similar technologies, including your IP address, device and browser type, the referring URL, the pages you view, the dates and times of your visits, and cookie identifiers, to allow us to operate and provide the Site and to understand how you interact with it. To learn more, see the Cookies and Other Technologies section below.</p>

        <!-- Section 5 -->
        <h2 id="section-5">5. How We Use Personal Information (Purposes for Collection and Processing)</h2>
        <p>Center Street Capital only collects and processes the minimum amount of personal information necessary for the purposes of our information processing activities and retains such information only as required to fulfill such purposes, including to:</p>
        <ul>
            <li>Operate, secure, and improve the Site;</li>
            <li>Respond to general inquiries and diligence-access requests, and keep professional records of those communications;</li>
            <li>Send you a newsletter or other communications you have requested;</li>
            <li>Protect against fraud, abuse, and security incidents;</li>
            <li>Comply with law and respond to lawful requests; and</li>
            <li>Enforce our agreements.</li>
        </ul>
        <p>In some circumstances, we may collect aggregated data or anonymize your personal information (so that it can no longer be associated with you) for research or statistical purposes. Aggregated or anonymized information is not considered personal information under this Policy. Where applicable, if Center Street Capital intends to further process your personal information for a purpose other than that for which it was initially collected, Center Street Capital shall, prior to such processing, provide you with relevant information on such additional purpose and, to the extent required by applicable law, obtain your consent. To the extent you provide consent to Center Street Capital for any purpose, you may withdraw such consent at any time by contacting us at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>. We do not use your personal information to train artificial intelligence or machine-learning models, including large language models.</p>
        <p>Through the Site, Center Street Capital does not request or intentionally collect any category of 'sensitive personal information' as defined under applicable state privacy law, including without limitation government identifiers, account credentials, precise geolocation, health, biometric, or neural data, or information revealing racial or ethnic origin, religious beliefs, sexual orientation, citizenship, or union membership. We ask that you not send nor disclose any sensitive personal information that we do not explicitly collect for the purposes outlined in this Policy or to provide our Site to you.</p>

        <!-- Section 6 -->
        <h2 id="section-6">6. Cookies and Other Technologies</h2>
        <p>A "cookie" is a small file created by a web server that can be stored on a user's device for use either during a particular browsing session (a "session" cookie) or a future browsing session (a "persistent" cookie). We may use cookies, analytics software, log files, or similar technologies (collectively, "Cookies") to collect certain information about your online activity on the Site. This information allows us to keep track of analytics and enables Center Street Capital to operate, secure, and improve the Site. We do not use advertising or retargeting pixels. We use strictly necessary Cookies to operate the Site and analytics Cookies to understand Site usage. You are free to decline our Cookies, but if you do, some parts of the Site may not work properly for you. You may manage preferences via <a href="cookie-policy.html">Cookie Settings</a>, and you may disallow Cookies at any time through your web browser. We do not permit third parties to collect personal information about your online activities over time and across different websites when you use the Site.</p>
        <p>If you would like more detailed information about first-party and third-party Cookies in use on the Site, please contact us using the information below.</p>

        <!-- Section 7 -->
        <h2 id="section-7">7. How We Disclose Personal Information</h2>
        <p>We may share or disclose your personal information for the following limited purposes:</p>
        <p><strong>Third parties providing services on our behalf.</strong> We may share information with vendors and suppliers (collectively, "Service Providers") who perform services and functions on our behalf, such as website hosting, analytics, and email or form processing. Service Providers do not have the right to use personal information we share with them beyond what is necessary to assist us, and we contractually require that they (1) protect the privacy of your personal information consistent with this Policy and (2) not use or disclose it for any purpose other than providing the limited service or function for Center Street Capital.</p>
        <p><strong>Aggregate information.</strong> We may share non-identifying information, such as aggregate statistics or usage information, with third parties. Any aggregated information shared in this way will not contain personal information.</p>
        <p><strong>With your consent.</strong> Center Street Capital may share personal information with third parties when we have your consent to do so. If you agree to have your personal information shared with a third party, it will be subject to that third party's privacy policy and business practices.</p>
        <p><strong>Legal disclosure.</strong> We may disclose information to comply with a legal obligation; when we believe in good faith that the law requires it; at the request of governmental authorities conducting an investigation; to verify or enforce our agreements or policies; to respond to an emergency; or otherwise to protect the rights, property, safety, or security of third parties, visitors to our Site, or the public.</p>
        <p><strong>Transfer in the event of sale or change of control.</strong> If the ownership of all or substantially all of our business changes, or we otherwise transfer assets relating to our business or the Site to a third party (such as by merger, acquisition, or bankruptcy proceeding), we may transfer personal information to the new owner. Unless prohibited by applicable law, your information would remain subject to the privacy policy applicable at the time of such transfer.</p>
        <p><strong>Emergencies.</strong> We may disclose personal information to appropriate law enforcement or other emergency response professionals in response to a physical threat to you or others.</p>
        <p>We do not disclose personal information to third parties for their own direct marketing.</p>

        <!-- Section 8 -->
        <h2 id="section-8">8. Your U.S. State Privacy Rights</h2>
        <p>Depending on your state of residence, you may have some or all of the following rights with respect to your personal information, subject to the conditions, exceptions, and limitations of the law of your state:</p>
        <p><strong>Right to confirm whether we process, and know/access</strong> the personal information we have collected about you (including categories, sources, purposes, and third parties to whom it was disclosed).</p>
        <p><strong>Request to Access.</strong> You may submit a request to obtain a copy of or access to the personal information that we have collected on you.</p>
        <p><strong>Request to Know.</strong> You may request information on the categories of personal information we have collected about you; the categories of sources; our business or commercial purpose for collecting, selling, or sharing personal information; the categories of third parties to whom we have disclosed personal information; and the specific pieces of personal information we have collected about you. You may also request the categories of personal information we have sold or shared and the categories of third parties to whom it was sold or shared, and the categories disclosed for a business purpose and the categories of persons to whom it was disclosed. The categories, sources, and disclosures will not exceed what is contained in this Policy. We are not required to retain information used only for a one-time transaction, to re-identify personal information not stored in that manner, or to provide personal information to you more than twice in a twelve-month period.</p>
        <p><strong>Right to correct inaccurate personal information.</strong> You may correct or update your personal information at any time by contacting us.</p>
        <p><strong>Right to delete personal information.</strong> You may request that we delete personal information we have collected from you. Subject to certain exceptions, we will, on receipt of a verifiable request, delete your personal information from our records, direct our service providers to do the same, and notify third parties with whom we have shared it to delete it unless this proves impossible or involves disproportionate effort. To the extent permitted or required by applicable law in your state, we may not delete your personal information if it is necessary to: complete a transaction you requested; protect security and prevent fraud; identify and fix technical errors; comply with legal obligations; conduct internal uses reasonably compatible with the context in which the information was collected; and establish, exercise, or defend legal claims.</p>
        <p><strong>Right to data portability</strong> (a copy in a portable format). You may request that we transfer your personal information to another entity, to the extent technically feasible.</p>
        <p><strong>Right to opt out</strong> of the sale or sharing of personal information and of processing for targeted advertising or profiling. We do not sell personal information, we do not share personal information for targeted advertising, and we do not use profiling in furtherance of decisions that produce legal or similarly significant effects. If these practices change, we will update this Policy and provide a "Do Not Sell or Share" link, and you may submit a request to opt out, including via a GPC signal.</p>
        <p><strong>Right to limit the use of sensitive personal information.</strong> We do not seek sensitive personal information through the public Site, and we only receive sensitive personal information that you voluntarily provide in inquiries or diligence-access requests. We use such information solely to respond to and service your requests. We do not sell or share your sensitive personal information, and we do not use sensitive personal information collected from the public Site to infer characteristics or for advertising. You may withdraw your consent to any use or disclosure of your sensitive personal information.</p>
        <p><strong>Right to Access Information About Automated Decision-Making.</strong> We do not currently engage in automated individual decision-making. In the event we ever do so, we will inform you of such change and you may request information about and opt out of such automated decision-making.</p>
        <p><strong>Right to a list of specific third parties.</strong> Residents of certain states may request a list of the specific third parties to which we have disclosed personal information.</p>
        <p><strong>Right to Appeal (in certain states).</strong> If we notify you that no action is to be taken in response to your request, you may appeal by contacting us within 30 days with the reason why you believe further action should be taken. We will respond within the period required by your state law (e.g., 45 or 60 days). If you are not satisfied with the result of the appeal and are a resident of one of the states listed below, you may contact the Attorney General of your state:</p>

        <div class="ag-list">
"""

for st_name, st_url in states_list:
    privacy_html += f"""            <div>{st_name}: <a href="{st_url}" target="_blank" rel="noopener">State Attorney General</a></div>\n"""

privacy_html += """        </div>

        <p>If you would like to exercise your rights as a resident of one of these states, submit requests by calling (949) 244-1090 or sending an email to <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>, providing enough information to identify you and enough specificity on the requested data. We will verify your request as required by law and respond within statutory time-frames (generally 45 days, extendable). To verify your identity we may ask you to confirm information we already hold (e.g., email address used to contact us). An authorized agent may submit a request on your behalf by providing signed written permission.</p>
        <p><strong>Non-discrimination for exercising your rights.</strong> We may not, and will not, treat you differently for exercising your privacy rights.</p>

        <!-- Section 9 -->
        <h2 id="section-9">9. Opt-Out Preference Signals</h2>
        <p>Because we do not sell or share personal information, opt-out preference signals do not currently affect our practices. Nevertheless, our Site recognizes Global Privacy Control (GPC) opt-out preference signals and displays a confirmation once your signal has been processed. Should our practices change, we will treat a GPC signal as a valid opt-out for the applicable browser. Apart from Global Privacy Control signals, the Site does not currently respond to browser “Do Not Track“ signals.</p>

        <!-- Section 10 -->
        <h2 id="section-10">10. Children and Individuals Under the Age of Eighteen</h2>
        <p>We are committed to protecting the privacy of children. Our Site is not intended for or directed to persons under eighteen (18) years of age. <strong>IF YOU ARE UNDER THE AGE OF EIGHTEEN (18) YOU ARE NOT AUTHORIZED TO USE OUR SITE, EVEN IF YOU HAVE OBTAINED PARENTAL CONSENT TO DO SO.</strong> We do not knowingly collect, request, process, or disclose data of persons under eighteen (18). Upon notice that a person under eighteen (18) has provided us with personal information, or that another party has otherwise provided us with the personal information of a person under eighteen (18), we will delete that personal information from our records. If you are a parent or guardian and believe we have collected personal information of a person under eighteen (18), please contact us at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a> and we will remove such data.</p>

        <!-- Section 11 -->
        <h2 id="section-11">11. Newsletters and Emails</h2>
        <p><strong>Newsletters and emails.</strong> At various times during your use of the Site, you may be given the option of opting in to recurring informational or promotional newsletters via email from Center Street Capital. When you provide your email address or sign up for one of our mailing lists, you may at any time choose to opt out of receiving additional informational or promotional newsletters by following the unsubscribe directions included at the bottom of each email or by contacting us at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>. We will process unsubscribe requests within ten (10) business days. When you communicate with us, we may retain your communications to process and respond to them and to improve our services.</p>

        <!-- Section 12 -->
        <h2 id="section-12">12. Security of Your Information</h2>
        <p>The security of your personal information is important to us. We follow generally accepted industry standards to protect the personal information submitted to us, both during transmission and once we receive it. However, no method of transmission over the Internet, or method of electronic storage, is 100% secure, and Center Street Capital cannot promise or guarantee that hackers, cybercriminals, or other unauthorized third parties will not be able to defeat our security. If a breach of security involving personal information occurs, we will comply with all applicable breach-notification laws. If you believe you have identified a security vulnerability in the Site, please report it to us at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>. Do not access, modify, or delete data belonging to others or disrupt the Site when investigating or reporting a potential vulnerability. If you believe any personal information you have submitted to us is insecure, please notify us immediately at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>.</p>

        <!-- Section 13 -->
        <h2 id="section-13">13. Retention of Personal Information</h2>
        <p>We retain inquiry and diligence-request records for as long as necessary to respond to them and to meet applicable record-keeping and legal obligations, and then delete or de-identify them when they are no longer needed. Website logs are typically retained for a shorter operational period. To determine the appropriate retention period, we consider: the amount, nature, and sensitivity of the information; the potential risk of harm from unauthorized use or disclosure; the purposes for which we obtained the information and whether we can achieve those purposes through other means; whether the information is needed to provide and improve our services and respond to your inquiries; the need to maintain appropriate business and accounting records; compliance with our legal, regulatory, and contractual obligations; and our rights to establish, exercise, or defend legal claims. When personal information is no longer needed, we will delete, destroy, de-identify, or anonymize it in accordance with standard retention practices, subject to legal hold, backup retention, or other legal, regulatory, contractual, or operational obligations.</p>

        <!-- Section 14 -->
        <h2 id="section-14">14. Linked Materials</h2>
        <p>The Site may contain links to third-party owned or operated websites, including social media websites and publications hosted on such third-party websites (each a "Linked Materials"), as a convenient method of accessing information that may be useful to you. When you click on a link to a Linked Material, you will leave the Site, and another entity may collect personal information or anonymous data from you. This Policy does not apply to Linked Materials; they have their own privacy and data collection practices, and we have no responsibility or liability relating to them.</p>

        <!-- Section 15 -->
        <h2 id="section-15">15. Changes to Our Privacy Policy</h2>
        <p>We reserve the right to change or modify this Policy at any time. Any nonmaterial changes are effective upon being posted unless we advise otherwise. If we make any material changes to this Policy, we will notify you by email or post notice on the Site before the change becomes effective. Material changes will be effective thirty (30) days after we provide notice, except changes relating to new features or required by law, which are effective immediately. Use of information we collect is subject to the Policy in effect at the time such information is used. If we make a material change that would allow us to use previously collected personal information in a materially different manner, we will obtain your consent where required by applicable law before doing so. We encourage you to frequently review this Policy.</p>

        <!-- Section 16 -->
        <h2 id="section-16">16. Reasonable Fees</h2>
        <p>Subject to applicable law, Center Street Capital may charge a reasonable fee for the administrative costs of any request that is manifestly unfounded or excessive.</p>

        <!-- Section 17 -->
        <h2 id="section-17">17. How to Contact Us</h2>
        <p>If you have any questions about this Policy, you may contact us by email at <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>, or by mail at:</p>
        <p style="padding-left: 16px; border-left: 3px solid #4683b3; color: #0f172a;">
            <strong>Privacy Officer</strong><br>
            Center Street Capital, LLC<br>
            18201 Von Karman Ave STE 400, Irvine, CA 92612<br>
            (949) 244-1090
        </p>
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
                        <li style="margin-bottom: 12px;"><a href="csl-rtf-fund.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">CSL-RTL Fund (Real Estate Debt)</a></li>
                        <li><a href="riviera-capital.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Center Street Riviera Direct Corporate Lending</a></li>
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
                        <li style="margin-bottom: 12px;"><a href="terms-of-use.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Terms of Service</a></li>
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
        if (hamburgerBtn && mobileMenu) {{
            hamburgerBtn.addEventListener('click', () => {{
                hamburgerBtn.classList.toggle('active');
                mobileMenu.classList.toggle('active');
            }});
        }}
    </script>
</body>
</html>
"""

with open('/Users/gregmontoya/AntiGravity Workspaces/CSLCompanies.com/privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_html)


# -------------------------------------------------------------
# 2. GENERATE RAW TERMS OF SERVICE (terms-of-use.html)
# -------------------------------------------------------------

terms_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Security & Privacy Meta Tags -->
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service | Center Street Capital</title>
    <meta name="description" content="Terms of Service for Center Street Capital. Legal agreement governing website use, intellectual property, disclaimers, liability limitations, and arbitration.">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles.css?v=5.20">
    <style>
        body {
            background-color: #ffffff !important;
            color: #0f172a !important;
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            line-height: 1.8;
        }
        .legal-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 5% 100px;
            color: #334155;
            font-size: 1.02rem;
            background-color: #ffffff;
        }
        .legal-content h1 {
            font-size: 2.35rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }
        .legal-date {
            color: #64748b;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 36px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 16px;
        }
        
        /* Clean Raw Table of Contents */
        .toc-wrapper {
            margin-bottom: 44px;
            padding-bottom: 24px;
            border-bottom: 1px solid #e2e8f0;
        }
        .toc-title {
            font-size: 1rem;
            font-weight: 700;
            color: #0f172a;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
        }
        .toc-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .toc-list a {
            color: #4683b3;
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
        }
        .toc-list a:hover {
            color: #0f172a;
            text-decoration: underline;
        }

        .legal-content h2 {
            font-size: 1.35rem;
            font-weight: 700;
            color: #0f172a;
            margin-top: 44px;
            margin-bottom: 16px;
            padding-top: 16px;
            border-top: 1px solid #f1f5f9;
            scroll-margin-top: 90px;
        }
        .legal-content h2:first-of-type {
            border-top: none;
            padding-top: 0;
        }
        .legal-content p {
            margin-bottom: 20px;
            color: #334155;
        }
        .legal-content strong {
            color: #0f172a;
        }
        .legal-content ul {
            margin: 0 0 24px 24px;
            padding: 0;
            color: #334155;
        }
        .legal-content li {
            margin-bottom: 10px;
        }
        .legal-content a {
            color: #4683b3;
            text-decoration: underline;
        }

        /* Header Navigation */
        .header-wrapper {
            background-color: #ffffff;
            border-bottom: 1px solid #e2e8f0;
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
                <a href="csl-rtf-fund.html" class="nav-link" style="color: #334155; text-decoration: none; font-weight: 500; font-size: 0.9rem; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">CSL-RTF Fund</a>
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
            <a href="csl-rtf-fund.html" class="mobile-nav-link">CSL-RTF Fund <span>&rarr;</span></a>
            <a href="mailto:ir@centerstreetcapital.com?subject=Diligence%20Access%20Request" class="nav-btn request-access-btn mobile-cta-btn">Request Access</a>
        </div>
    </div>

    <!-- Main Content Container -->
    <main class="legal-content">
        <h1>Terms of Service</h1>
        <div class="legal-date">Updated: October 6, 2026</div>

        <!-- Clean Raw Table of Contents -->
        <div class="toc-wrapper">
            <div class="toc-title">Table of Contents</div>
            <div class="toc-list">
                <a href="#section-1">1. Introduction</a>
                <a href="#section-2">2. Eligibility</a>
                <a href="#section-3">3. No Offer, Solicitation, or Advice</a>
                <a href="#section-4">4. Communications Consent</a>
                <a href="#section-5">5. Permitted Use and Prohibited Conduct</a>
                <a href="#section-6">6. Intellectual Property Rights and Ownership</a>
                <a href="#section-7">7. Linked Material</a>
                <a href="#section-8">8. Disclaimers</a>
                <a href="#section-9">9. Limitation of Liability</a>
                <a href="#section-10">10. Indemnification</a>
                <a href="#section-11">11. Dispute Resolution — Binding Arbitration and Class Action Waiver</a>
                <a href="#section-12">12. Governing Law and Venue</a>
                <a href="#section-13">13. Additional Terms</a>
                <a href="#section-14">14. Contact</a>
            </div>
        </div>

        <!-- Section 1 -->
        <h2 id="section-1">1. Introduction</h2>
        <p><strong>PLEASE READ THESE TERMS OF SERVICE (THE "TERMS") CAREFULLY</strong> before using our Site or submitting any information through it. These Terms are a binding agreement between you and Center Street Capital, LLC ("Center Street Capital," "we," "us," or "our") and apply to and govern your access to and use of <a href="./">www.centerstreetcapital.com</a> and any other website, mobile website, our official pages on third-party social media platforms (to the extent permitted by those platforms' terms), email communications you exchange with us, and any other digital platform, including any services, features, pages, and functions contained or offered therein, that are owned, operated, or provided by Center Street Capital (collectively, the "Site"). By visiting or otherwise using the Site in any manner, you acknowledge, accept, and agree to be bound and abide by these Terms. You also acknowledge, agree, and consent to the terms of our <a href="privacy-policy.html">Privacy Policy</a>, which is incorporated herein by reference. If for any reason you do not accept and agree to these Terms or the Privacy Policy, accessing the Site is strictly prohibited and you must immediately exit.</p>
        <p><strong>THESE TERMS AFFECT YOUR LEGAL RIGHTS, RESPONSIBILITIES, AND OBLIGATIONS, GOVERN YOUR USE OF THE SITE, ARE LEGALLY BINDING, LIMIT CENTER STREET CAPITAL'S LIABILITY TO YOU, AND REQUIRE YOU TO INDEMNIFY CENTER STREET CAPITAL AND TO SETTLE CERTAIN DISPUTES THROUGH ARBITRATION (SECTION 11), INCLUDING A CLASS ACTION WAIVER. IF YOU DO NOT WISH TO BE BOUND BY THESE TERMS OR ANY FUTURE MODIFICATIONS, DO NOT USE THE SITE.</strong></p>
        <p>We reserve the right to change these Terms at any time in our sole discretion. Any nonmaterial changes will be effective upon posting, and you agree to the new posted Terms by continuing your use of the Site. Material changes will be effective thirty (30) days after we provide notice by posting the revised Terms and, if provided, by email to the address you provided, except changes relating to new features or required by law, which are effective immediately. It is your responsibility to check periodically for changes.</p>
        <p>These Terms are written in the English language; to the extent any translated versions conflict with the English language version, the English language version shall control.</p>

        <!-- Section 2 -->
        <h2 id="section-2">2. Eligibility</h2>
        <p>The Site is intended for U.S. residents. By using the Site, you represent and agree that you are at least the legal age of majority in the jurisdiction in which you reside. The Site is not targeted for use by children under the age of 18. <strong>IF YOU ARE UNDER THE AGE OF EIGHTEEN (18), OR HAVE NOT REACHED THE AGE OF MAJORITY IN YOUR JURISDICTION, YOU ARE NOT AUTHORIZED TO USE THE SITE, TO SUBMIT ANY INFORMATION THROUGH IT, OR TO AGREE TO THESE TERMS, AND YOUR USE OF THE SITE IS STRICTLY PROHIBITED.</strong></p>

        <!-- Section 3 -->
        <h2 id="section-3">3. No Offer, Solicitation, or Advice</h2>
        <p>Content on the Site is provided for general informational purposes only. Nothing on the Site constitutes (a) an offer to sell, or a solicitation of an offer to buy, any security or interest in any private investment fund or vehicle managed or advised by Center Street Capital or its affiliates; or (b) investment, legal, tax, or accounting advice.</p>
        <p>Center Street Capital does not provide personalized investment advice to visitors to this Site or to prospective or actual investors through this Site, and use of this Site does not create an advisory or fiduciary relationship with you.</p>
        <p>You agree that you will not rely on the Site in making any investment decision.</p>
        <p><strong>Eligible Investors.</strong> Investment opportunities are not offered publicly on the Site and are available only to persons who meet applicable eligibility requirements, which may include qualification as an accredited investor under Rule 501(a) of Regulation D and/or a qualified purchaser under the Investment Company Act of 1940. Offering materials are made available only through non-public, access-controlled channels after eligibility verification.</p>
        <p><strong>Performance Statements.</strong> The Site does not present fund performance or target returns. Any performance information is provided only in confidential offering materials to eligible persons.</p>
        <p><strong>Risk of Loss.</strong> Investment in private credit and other alternative strategies involves substantial risk, including illiquidity, lack of a secondary market, leverage, credit and default risk, real-estate market risk, and the possible loss of the entire investment. Such investments are not bank deposits and are not insured by the FDIC or any other governmental agency.</p>

        <!-- Section 4 -->
        <h2 id="section-4">4. Communications Consent</h2>
        <p><strong>(a) Calls and messages:</strong> Center Street Capital may use your phone number that you provide to us to respond to your inquiries, including via phone call or text message. We will not send you marketing and promotional communications unless we obtain your express consent. You recognize and acknowledge that text messaging is an inherently less secure method of communication and agree to receive text messages regardless of the level of security associated with them. Message and data rates may apply.</p>
        <p><strong>(b) Email:</strong> By providing your email address and opting in, you consent to receive marketing and promotional emails from Center Street Capital regarding informational updates, market insights, and firm news, which may be sent using automated email systems or third-party email service providers on Center Street Capital’s behalf. You recognize and acknowledge that email is an inherently less secure method of communication and agree to receive emails regardless of the level of security associated with them.</p>
        <p>You may unsubscribe from marketing emails at any time by clicking the “unsubscribe” link contained in any marketing email you receive from us, or by sending an email to <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a> requesting to unsubscribe from marketing emails. Please allow a reasonable period of time for Center Street Capital to process your unsubscribe request.</p>

        <!-- Section 5 -->
        <h2 id="section-5">5. Permitted Use and Prohibited Conduct</h2>
        <p>You may use the Site only for lawful purposes and in accordance with these Terms. You agree not to use the Site:</p>
        <ul>
            <li>In any way that violates any applicable federal, state, local, or international law or regulation (including, without limitation, any laws regarding the export of data or software to and from the US or other countries);</li>
            <li>For the purpose of exploiting, harming, or attempting to exploit or harm minors in any way by exposing them to inappropriate content, asking for personally identifiable information, or otherwise;</li>
            <li>To transmit, or procure the sending of, any advertising or promotional material without our prior written consent, including any "junk mail," "chain letter," "spam," or any other similar solicitation;</li>
            <li>To impersonate or attempt to impersonate Center Street Capital, a Center Street Capital employee, another user, or any other person or entity (including, without limitation, by using email addresses or screen names associated with any of the foregoing);</li>
            <li>To submit any information that is untruthful, inaccurate, or misleading; or</li>
            <li>To engage in any other conduct that restricts or inhibits anyone's use or enjoyment of the Site, or which, as determined by us, may harm Center Street Capital or users of the Site, or expose them to liability.</li>
        </ul>
        <p>Additionally, you agree not to:</p>
        <ul>
            <li>Use the Site in any manner that could disable, overburden, damage, or impair the Site or interfere with any other party's use of the Site;</li>
            <li>Use or cause the use of the Site or its Content to train artificial intelligence, including large language models, through any means including data scraping;</li>
            <li>Use any robot, spider, or other automatic device, process, or means to access the Site for any purpose, including monitoring or copying any of the material on the Site;</li>
            <li>Use any manual process to monitor or copy any of the material on the Site, or for any other purpose not expressly authorized in these Terms, without our prior written consent;</li>
            <li>Use any device, software, or routine that interferes with the proper working of the Site;</li>
            <li>Introduce any viruses, Trojan horses, worms, logic bombs, or other material that is malicious or technologically harmful;</li>
            <li>Attempt to gain unauthorized access to, interfere with, damage, or disrupt any parts of the Site, the server on which the Site is stored, or any server, computer, or database connected to the Site;</li>
            <li>Attack the Site via a denial-of-service attack or a distributed denial-of-service attack; or</li>
            <li>Otherwise attempt to interfere with the proper working of the Site.</li>
        </ul>
        <p>We reserve the right to determine whether or not your use of the Site is acceptable and to immediately revoke or block your access to the Site at our sole discretion.</p>

        <!-- Section 6 -->
        <h2 id="section-6">6. Intellectual Property Rights and Ownership</h2>
        <p>The Site, all of its content, and any associated intellectual property, including without limitation all copyrights, patents, trademarks, service marks, and trade names, as well as all logos, text, design, graphics, icons, images, audio clips, downloads, interfaces, code, and software, as well as the selection and arrangement thereof (collectively, the "Content"), are proprietary and owned or controlled by Center Street Capital, our licensors, and certain other third parties. All right, title, and interest in and to the Content is the exclusive property of Center Street Capital, our licensors, or certain other third parties, and is protected by United States and international copyright, trademark, trade dress, patent, or other intellectual property and unfair competition rights and laws to the fullest extent possible.</p>
        <p>These Terms permit you to use the Site and Content for evaluation purposes only. A limited, revocable, nontransferable license is granted to temporarily download one copy of the Content for transitory viewing only, for use in strict accordance with these Terms. This is not a transfer of title, right, or interest in the Site or Content. The license does not give you the right to, and you are strictly prohibited from, otherwise copying the Content, modifying the Content, using the Content for any commercial purpose (other than evaluating Center Street Capital's services), publicly displaying the Content, attempting to decompile or reverse engineer the Content, removing any copyright, trademark, or other proprietary notations from the Content, or otherwise infringing upon the intellectual property rights of Center Street Capital or its licensors. This license shall automatically terminate if you violate any of these restrictions and may be terminated by Center Street Capital at its sole discretion at any time. Upon termination of this license, you must destroy any downloaded materials in your possession, whether in electronic or printed format. Except for the limited license expressly provided in these Terms, no license of intellectual property is granted by Center Street Capital in these Terms, and no assignment of intellectual property is granted by Center Street Capital in these Terms.</p>
        <p>By submitting information or materials through the Site, you grant Center Street Capital a non-exclusive, royalty-free license to use, store, and reproduce such submissions for the purposes described in the Privacy Policy and these Terms.</p>
        <p>Confidential offering materials made available to you by email or other means are subject to the confidentiality terms or non-disclosure agreement accompanying those materials, which control over this Section 6.</p>
        <p>Center Street Capital owns and uses trademarks on or in relation to the Site, including but not limited to Center Street Capital and related designs and logos. You must not use such marks without Center Street Capital's prior written permission. All other names, logos, product and service names, designs, and slogans on the Site are the trademarks of their respective owners. Nothing contained in the Site should be construed as granting any license or right to use any trademark displayed on the Site without the express written permission of Center Street Capital or such third party that may own the trademark.</p>

        <!-- Section 7 -->
        <h2 id="section-7">7. Linked Material</h2>
        <p>The Site may provide links to third-party websites and publications ("Linked Material"). Center Street Capital has not necessarily reviewed the information in the Linked Material, does not maintain them, and cannot control the completeness, accuracy, or security of their content. The content of any Linked Material is solely the responsibility of its provider, and the inclusion of any link does not imply endorsement by Center Street Capital. If you decide to access any Linked Material, you do so entirely at your own risk, and you agree that Center Street Capital shall not be responsible or liable, directly or indirectly, for any damage or loss caused or alleged to be caused by or in connection with use of or reliance on any third-party content, products, or services available on or through any link provided by Center Street Capital.</p>

        <!-- Section 8 -->
        <h2 id="section-8">8. Disclaimers</h2>
        <p><strong>YOUR USE OF THE SITE IS AT YOUR RISK. THE SITE AND ALL SERVICES, INFORMATION, AND MATERIALS MADE AVAILABLE THROUGH THE SITE ARE PROVIDED TO YOU "AS IS" AND "AS AVAILABLE" WITHOUT ANY EXPRESS REPRESENTATIONS OR WARRANTIES OF ANY KIND, AND WE DISCLAIM ALL STATUTORY OR IMPLIED REPRESENTATIONS, WARRANTIES, TERMS, AND CONDITIONS, INCLUDING THE REPRESENTATIONS AND WARRANTIES OF SATISFACTORY QUALITY, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, AND TITLE. WE MAKE NO REPRESENTATION OR WARRANTY THAT THE SITE (OR ANY PART THEREOF) WILL BE ACCURATE, COMPLETE, ERROR-FREE, AVAILABLE, UNINTERRUPTED, OR FREE OF VIRUSES OR OTHER HARMFUL COMPONENTS. THE MATERIALS ON THE SITE MAY BE OUT OF DATE, AND CENTER STREET CAPITAL MAKES NO COMMITMENT AND ASSUMES NO DUTY TO UPDATE SUCH MATERIALS. YOU AGREE THAT YOU MUST EVALUATE, AND THAT YOU BEAR ALL RISKS ASSOCIATED WITH, THE USE OF THE SITE, INCLUDING ANY RELIANCE ON THE ACCURACY, COMPLETENESS, TIMELINESS, OR USEFULNESS OF ANY INFORMATION OR MATERIALS MADE AVAILABLE THROUGH THE SITE. THE FOREGOING EXCLUSIONS DO NOT APPLY TO THE EXTENT PROHIBITED BY LAW.</strong></p>

        <!-- Section 9 -->
        <h2 id="section-9">9. Limitation of Liability</h2>
        <p><strong>TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT WILL CENTER STREET CAPITAL, ITS MEMBERS, OFFICERS, DIRECTORS, EMPLOYEES, AFFILIATES, AGENTS, SUCCESSORS, OR ASSIGNS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, EXEMPLARY, OR PUNITIVE DAMAGES OF ANY KIND IN CONNECTION WITH THE SITE, OR FOR ANY DAMAGES FOR LOSS OF PROFITS, LOSS OF USE, LOSS OF DATA, BUSINESS INTERRUPTION, LOSS OF SECURITY OF INFORMATION YOU HAVE PROVIDED IN CONNECTION WITH YOUR USE OF THE SITE, OR UNAUTHORIZED INTERCEPTION OF ANY SUCH INFORMATION BY THIRD PARTIES, EVEN IF ADVISED IN ADVANCE OF SUCH DAMAGES OR LOSSES. IN THE EVENT OF ANY PROBLEM WITH THE SITE OR ANY CONTENT, YOU AGREE THAT YOUR SOLE AND EXCLUSIVE REMEDY IS TO STOP USING THE SITE. OUR MAXIMUM LIABILITY FOR ALL DAMAGES, LOSSES, AND CAUSES OF ACTION, WHETHER IN CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, SHALL BE THE HIGHER OF ONE HUNDRED DOLLARS ($100) OR THE TOTAL AMOUNT, IF ANY, PAID BY YOU TO US TO ACCESS AND USE THE SITE AND ANY RELATED SERVICES. IT IS POSSIBLE THAT APPLICABLE LAW MAY NOT ALLOW FOR LIMITATIONS ON CERTAIN IMPLIED WARRANTIES OR EXCLUSIONS OR LIMITATIONS OF CERTAIN DAMAGES; SOLELY TO THE EXTENT SUCH LAW APPLIES TO YOU, SOME OR ALL OF THE ABOVE DISCLAIMERS, EXCLUSIONS, OR LIMITATIONS MAY NOT APPLY TO YOU. NOTHING HEREIN LIMITS LIABILITY FOR DEATH OR PERSONAL INJURY CAUSED BY A PARTY'S NEGLIGENCE, FRAUD, OR ANY OTHER MATTER TO THE EXTENT SUCH LIMITATION IS PROHIBITED BY APPLICABLE LAW.</strong></p>
        <p>Nothing in this Section limits any right or remedy that cannot be limited under applicable law, including the California Consumer Privacy Act.</p>

        <!-- Section 10 -->
        <h2 id="section-10">10. Indemnification</h2>
        <p>Except to the extent prohibited under applicable law, you agree to indemnify, defend, and hold harmless Center Street Capital and its officers, directors, employees, and agents from and against any claims, losses, liabilities, damages, costs, or expenses, including attorneys' fees and costs, that may arise from or in connection with (a) your use of, or activities in connection with, the Site; (b) your violation of these Terms, including any misrepresentations made by you in connection with your use of the Site or any information submitted through it; or (c) your violation of any law or the rights of a third party. Center Street Capital reserves the right, at its own expense, to assume the exclusive defense and control of any matter otherwise subject to your indemnification.</p>

        <!-- Section 11 -->
        <h2 id="section-11">11. Dispute Resolution — Binding Arbitration and Class Action Waiver</h2>
        <p><strong>(a) Informal resolution first:</strong> Before initiating arbitration or any other proceeding, you and Center Street Capital each agree to first attempt to resolve any dispute informally and in good faith. To begin this process, the party asserting a claim must send a written notice (“Notice”) to the other party describing: (i) the nature and basis of the claim or dispute; (ii) the specific relief sought; and (iii) contact information for the party providing the Notice. Notice to Center Street Capital must be sent to <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>. Notice to you will be sent to the most recent email address or physical address Center Street Capital has on file for you. Following receipt of the Notice, the parties agree to negotiate in good faith to resolve the dispute for a period of thirty (30) days (the “Cure Period”). This informal resolution process is nonbinding, and neither party is obligated to accept any resolution proposed during the Cure Period. If the dispute is not resolved to the mutual satisfaction of both parties within the Cure Period, either party may proceed to initiate binding arbitration as set forth below. Completion of this informal resolution process is a condition precedent to filing any arbitration demand or lawsuit, and either party may seek to have a court or arbitrator stay any such proceeding until this condition has been satisfied.</p>
        <p><strong>(b) Arbitration:</strong> We will make reasonable efforts to informally resolve any complaints, disputes, or disagreements that you may have with us. If those efforts fail, by using the Site, you agree that any complaint, dispute, or disagreement you may have against us, and any claim that we may have against you, arising out of, relating to, or connected in any way with these Terms, the Privacy Policy, or the Site shall be resolved exclusively by final, confidential and binding arbitration (“Arbitration”) before a single arbitrator administered by JAMS or its successor (“JAMS”) and conducted in accordance with the JAMS Streamlined Arbitration Rules And Procedures in effect at the time the Arbitration is initiated or, if the amount in controversy exceeds $100,000, in accordance with the JAMS Comprehensive Arbitration Rules and Procedures then in effect (respectively, the “Applicable Rules”). The Applicable Rules can be found at <a href="https://www.jamsadr.com" target="_blank" rel="noopener">www.jamsadr.com</a>. If JAMS is no longer in existence, the Arbitration shall be administered by the American Arbitration Association or its successor (the “AAA”) instead, and conducted in accordance with the AAA Commercial Arbitration Rules in effect at that time (which shall be the “Applicable Rules” in such circumstances). If JAMS (or, if applicable, AAA) at the time the arbitration is filed has Minimum Standards of Procedural Fairness for Consumer Arbitrations in effect that would be applicable to the matter in dispute, we agree to provide the benefit of such Minimum Standards to you to the extent they are more favorable than the comparable arbitration provisions set forth in this section. Furthermore, this section shall not prevent any party from seeking provisional remedies (that is, a temporary restraining order or preliminary injunction) from a court of appropriate jurisdiction. You further agree that: If a court decides that any part of this agreement to arbitrate is invalid or unenforceable, the other parts of this Section shall still apply. Specifically, if a court decides that applicable law precludes enforcement of any of this section’s limitations as to a particular claim or a particular request for a remedy (such as a request for public injunctive relief), then that claim or that remedy request (and only that claim or that remedy request) may be severed from the arbitration and may be brought in court, subject to your and Center Street Capital’s right to appeal the court’s decision. All other claims shall be arbitrated.</p>
        <p><strong>(c) Single Arbitrator.</strong> The Arbitration shall be conducted before a single arbitrator selected in accordance with the Applicable Rules or by mutual agreement between you and us (the “Arbitrator”).</p>
        <p><strong>(d) Arbitrator Will Interpret This Agreement.</strong> The Arbitrator, and not any federal, state, or local court or agency, shall have the exclusive authority to resolve any dispute arising under or relating to the validity, interpretation, applicability, enforceability or formation of these Terms or these arbitration provisions, including but not limited to any claim that all or any part of these Terms is void or voidable, except that a court shall decide any dispute regarding the enforceability of the class action waiver in subsection (g) or the severance of public injunctive relief under subsection (m).</p>
        <p><strong>(e) Location of Arbitration.</strong> The arbitration shall be held (i) in Orange County, California (if permitted by the applicable rules); (ii) at such other location as may be mutually agreed upon by you and us; or (iii) if the only claims in the arbitration are asserted by you and are for less than $10,000 in aggregate, at a location of your election, by telephone or written submission.</p>
        <p><strong>(f) Governing Law.</strong> The Arbitrator (i) shall apply internal laws of the State of California consistent with the Federal Arbitration Act and applicable statutes of limitations, or, to the extent (if any) that federal law prevails, shall apply the law of the U.S., irrespective of any conflict of law principles; (ii) shall entertain any motion to dismiss, motion to strike, motion for judgment on the pleadings, motion for complete or partial summary judgment, motion for summary adjudication, or any other dispositive motion consistent with California or federal rules of procedure, as applicable; (iii) shall honor claims of privilege recognized at law; and (iv) shall have authority to award any form of legal or equitable relief.</p>
        <p><strong>(g) No Class Relief.</strong> The Arbitration can resolve only your or our individual claims, and the Arbitrator shall have no authority to entertain or arbitrate any claims on a class or representative basis, or to consolidate or join the claims of other persons or parties who may be similarly situated.<br><br><strong>YOU AND WE AGREE TO WAIVE ANY AND ALL RIGHTS TO A JURY TRIAL, EXCEPT AS PROVIDED IN SUBSECTION (m) (California Public Injunctive Relief) BELOW. ADDITIONALLY, UNLESS YOU AND WE AGREE OTHERWISE, EACH PARTY MAY BRING CLAIMS AGAINST THE OTHER ONLY ON AN INDIVIDUAL BASIS AND NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY PURPORTED CLASS, REPRESENTATIVE ACTION OR PRIVATE ATTORNEY GENERAL PROCEEDING. ALSO, TO THE EXTENT AVAILABLE BY LAW, AND SUBJECT TO THE DAMAGE LIMITATIONS DISCUSSED HEREIN, THE ARBITRATOR MAY AWARD RELIEF ONLY IN FAVOR, AND FOR THE BENEFIT OF, THE INDIVIDUAL PARTY SEEKING RELIEF.</strong></p>
        <p><strong>(h) Written Award.</strong> The Arbitrator shall issue a written award supported by a statement of decision setting forth the Arbitrator’s complete determination of the dispute and the factual findings and legal conclusions relevant to it (an “Award”). Judgment upon the Award may be entered by any court having jurisdiction thereof or having jurisdiction over the relevant party or its assets.</p>
        <p><strong>(i) Arbitration Costs.</strong> In the event that you are able to demonstrate that the costs of Arbitration will be prohibitive as compared to the costs of litigation, we will pay as much of your filing and hearing fees in connection with the Arbitration as the Arbitrator deems necessary to prevent the arbitration from being cost-prohibitive, regardless of the outcome of the Arbitration, unless the Arbitrator determines that your claim(s) were frivolous or asserted in bad faith.</p>
        <p><strong>(j) Reasonable Attorney’s Fees.</strong> Except where prohibited by applicable law or in conflict with the Minimum Standards, in the event you recover an Award greater than our last written settlement offer, the Arbitrator shall also have the right to include in the Award our reimbursement of your reasonable and actual out-of-pocket attorneys’ fees associated with the Arbitration. In the event you recover an Award less than our last written settlement offer, or you are found to not be entitled to any Award, the Arbitrator shall also have the right to entitle Center Street Capital to the reimbursement, by you, of our reasonable and actual out-of-pocket attorneys’ fees associated with the Arbitration.</p>
        <p><strong>(k) Small Claims Matters are Excluded. No Class Relief or Joinder of Claims.</strong> Notwithstanding the foregoing arbitration provisions, at your option, you may bring any claim for damages you have against us in your local small claims court within the U.S., if your claim is within such court’s jurisdictional limit; provided that such court does not have the authority to entertain any claims on a class or representative basis, or to consolidate or join the claims of other persons or parties who may be similarly situated in such proceeding.</p>
        <p><strong>(l) Confidentiality of Arbitration.</strong> You and we agree to maintain the confidential nature of the Arbitration and shall not disclose the facts of the Arbitration, any documents exchanged as part of the Arbitration, proceedings of the Arbitration, the Arbitrator’s decision and the existence or amount of any Award, except as may be necessary to prepare for or conduct the Arbitration (in which case anyone becoming privy to such confidential information must undertake to preserve its confidentiality), or except as may be necessary in connection with a court application for a provisional remedy, a judicial challenge to an Award or its enforcement, or unless otherwise required by applicable law or court order. Nothing in this subsection prevents either party from reporting to or cooperating with any governmental or regulatory authority.</p>
        <p><strong>(m) California Public Injunctive Relief.</strong> Notwithstanding anything to the contrary in this Section 11, if and only to the extent that applicable California law governs a claim and, under such law, the claim or remedy cannot lawfully be waived or compelled to arbitration on an individual basis, nothing in these Terms shall be construed to waive your right to seek public injunctive relief within the meaning of McGill v. Citibank, N.A., 2 Cal. 5th 945 (2017). Any such non-waivable request for public injunctive relief (and only that remedy request) may be severed from the Arbitration, consistent with the severability provisions of subsection (b) above, and brought in a court of competent jurisdiction as set forth in Section 12 (Governing Law and Venue). All other claims, remedies, and requests for relief, including any request for relief other than public injunctive relief, shall remain subject to Arbitration on an individual basis as set forth in this Section 11, and, to the fullest extent permitted by applicable law, any claim or remedy request proceeding in court under this subsection shall be stayed pending completion of the Arbitration of all arbitrable claims. This subsection applies only to the extent required by applicable California law and shall not be construed to expand any right to bring claims on a class, collective, or representative basis, or to seek public injunctive relief, beyond what applicable California law provides and does not permit to be waived.</p>

        <!-- Section 12 -->
        <h2 id="section-12">12. Governing Law and Venue</h2>
        <p>These Terms are governed by California law (excluding conflict rules) and venue for non-arbitrable matters is in Orange County, California. If it is determined that arbitration is not permitted, has been waived, or is otherwise unavailable, the sole and exclusive jurisdiction and venue for any action arising out of or related to these Terms or the Site shall be an appropriate state or federal court located in Orange County, California, and you hereby submit and irrevocably consent to the personal jurisdiction and venue of said courts. You agree that such courts are a convenient forum and that you will not seek to transfer an action or proceeding to any other forum or jurisdiction, under the doctrine of forum non conveniens or otherwise. You further agree that the laws of the United States and the state of California, without regard to the principles of conflict of laws principles, shall govern these Terms and all matters relating to the Site. This paragraph shall not be read to conflict with the mandatory arbitration provision.</p>

        <!-- Section 13 -->
        <h2 id="section-13">13. Additional Terms</h2>
        <p>The failure of Center Street Capital to enforce any term or condition of these Terms shall not be deemed a waiver of such term or condition or of any other term or condition. If any provision of these Terms is held by a court or other tribunal of competent jurisdiction to be invalid, illegal, or unenforceable for any reason, such provision shall be eliminated or limited to the minimum extent such that the remaining provisions will continue in full force and effect. All provisions which by their nature should survive termination shall survive, including provisions regarding ownership, warranty disclaimers, indemnification, and limitations of liability.</p>
        <p>These Terms (including the Privacy Policy, to the extent incorporated) constitute the sole and entire agreement between you and Center Street Capital regarding the Site and supersede all prior and contemporaneous understandings, agreements, representations, and warranties regarding the Site. Nothing in these Terms modifies or supersedes any confidentiality agreement, confidential private placement memorandum or similar offering document, subscription agreement, or other written agreement between you and Center Street Capital, each of which controls in the event of conflict. We may assign these Terms, in whole or in part, at any time without notice to you; you may not assign or transfer these Terms without our prior written consent.</p>
        <p>You agree that, regardless of any statute or law establishing a different limitations period, to the maximum extent permitted under applicable law, any claim or cause of action arising out of, related to, or connected with the use of the Site or these Terms must be filed within one (1) year after such claim or cause of action arose or be forever barred.</p>
        <p>We may provide you with information regarding the Site in electronic form only, and you agree that such notices satisfy any legal requirement that communications be in writing.</p>

        <!-- Section 14 -->
        <h2 id="section-14">14. Contact</h2>
        <p>Please direct any questions about the Site or these Terms to: <a href="mailto:hello@centerstreetcapital.com">hello@centerstreetcapital.com</a>.</p>
        <p>Although Center Street Capital will in most circumstances be able to receive your communications, Center Street Capital does not guarantee that it will receive them timely and accurately and shall not be legally obligated to read, act on, or respond to any such email except for privacy rights requests, Notices stated in these Terms, or communications we are legally required to receive or respond to.</p>
        <p>Email is not a secure medium; please do not send Social Security numbers, account numbers, or bank or payment information by email. We handle personal information you send us in accordance with our Privacy Policy. Unsolicited ideas or materials you send us (other than personal information and diligence requests) are not treated as confidential and you agree that Center Street Capital may use any such unsolicited ideas or materials without obligation or compensation to you.</p>
        <p style="padding-left: 16px; border-left: 3px solid #4683b3; color: #0f172a;">
            Center Street Capital, LLC<br>
            18201 Von Karman Ave STE 400, Irvine, CA 92612<br>
            (949) 244-1090
        </p>
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
                        <li style="margin-bottom: 12px;"><a href="csl-rtf-fund.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">CSL-RTL Fund (Real Estate Debt)</a></li>
                        <li><a href="riviera-capital.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Center Street Riviera Direct Corporate Lending</a></li>
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
                        <li style="margin-bottom: 12px;"><a href="terms-of-use.html" style="color: #cbd5e1; text-decoration: none; font-size: 0.85rem; transition: color 0.2s;">Terms of Service</a></li>
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
    f.write(terms_html)

print("Generated both raw privacy-policy.html and raw terms-of-use.html successfully!")
