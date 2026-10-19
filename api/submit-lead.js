export default async function handler(req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    try {
        const {
            fullName = '',
            firstName = '',
            lastName = '',
            email = '',
            company = '',
            phone = '',
            investorType = '',
            hutk = '',
            pageUri = 'https://investor-csl.vercel.app/',
            pageName = 'Center Street Capital'
        } = req.body || {};

        const portalId = '22311313';
        const formId = '907a59ec-7731-4a37-a7e5-45068480a51c';

        // 1. Fetch live HubSpot v4 form definition to discover active fields & timestamp
        let allowedFields = ['0-1/firstname', '0-1/lastname', '0-1/email'];
        let formDefinitionUpdatedAt = 1791839158368;

        try {
            const defRes = await fetch(`https://forms.hsforms.com/embed/v4/render-definition/${portalId}/${formId}`);
            if (defRes.ok) {
                const defJson = await defRes.json();
                if (defJson?.form?.lastUpdatedAt) {
                    formDefinitionUpdatedAt = defJson.form.lastUpdatedAt;
                }
                const foundProps = [];
                const walkModules = (mods) => {
                    if (!Array.isArray(mods)) return;
                    for (const m of mods) {
                        if (m.propertyReference) foundProps.push(m.propertyReference);
                        if (m.modules) walkModules(m.modules);
                    }
                };
                walkModules(defJson?.form?.modules);
                if (foundProps.length > 0) {
                    allowedFields = foundProps;
                }
            }
        } catch (e) {
            // Use fallback definition fields
        }

        const hasCompany = allowedFields.includes('0-1/company') || allowedFields.includes('0-2/name');
        const hasPhone = allowedFields.includes('0-1/phone');
        const hasMessage = allowedFields.includes('0-1/message');

        // Build field values matching exact renderedFieldsIds on the v4 form
        const formData = new FormData();
        const renderedFieldsIds = [];

        if (allowedFields.includes('0-1/firstname')) {
            formData.append('0-1/firstname', firstName || fullName);
            renderedFieldsIds.push('0-1/firstname');
        }

        if (allowedFields.includes('0-1/lastname')) {
            // If Company/Phone/Message aren't added as separate fields on the HubSpot form yet,
            // include them cleanly in Last Name so all 5 fields are captured without HubSpot rejecting unknown fields.
            let finalLastName = lastName || '-';
            if (!hasCompany || !hasPhone || !hasMessage) {
                const extras = [];
                if (!hasCompany && company) extras.push(`Firm: ${company}`);
                if (!hasPhone && phone) extras.push(`Tel: ${phone}`);
                if (!hasMessage && investorType) extras.push(`Type: ${investorType}`);
                if (extras.length > 0) {
                    finalLastName = `${finalLastName} (${extras.join(' | ')})`;
                }
            }
            formData.append('0-1/lastname', finalLastName);
            renderedFieldsIds.push('0-1/lastname');
        }

        if (allowedFields.includes('0-1/email')) {
            formData.append('0-1/email', email);
            renderedFieldsIds.push('0-1/email');
        }

        if (allowedFields.includes('0-1/company')) {
            formData.append('0-1/company', company);
            renderedFieldsIds.push('0-1/company');
        } else if (allowedFields.includes('0-2/name')) {
            formData.append('0-2/name', company);
            renderedFieldsIds.push('0-2/name');
        }

        if (hasPhone) {
            formData.append('0-1/phone', phone);
            renderedFieldsIds.push('0-1/phone');
        }

        if (hasMessage) {
            const msg = `=== DILIGENCE ACCESS REQUEST ===\nFull Name: ${fullName}\nEmail: ${email}\nCompany / Firm: ${company}\nPhone Number: ${phone}\nInvestor Type: ${investorType}`;
            formData.append('0-1/message', msg);
            renderedFieldsIds.push('0-1/message');
        }

        const hsContext = {
            source: 'forms-embed-static',
            sourceName: 'forms-embed',
            sourceVersion: '1.0',
            sourceVersionMajor: '1',
            sourceVersionMinor: '0',
            locale: 'en',
            formDefinitionUpdatedAt,
            pageUrl: pageUri,
            pageTitle: pageName,
            renderedFieldsIds,
            captchaStatus: 'NOT_APPLICABLE',
            emailResubscribeStatus: 'NOT_APPLICABLE',
            shouldProcess: true
        };

        if (hutk) {
            hsContext.hutk = hutk;
        }

        formData.append('hs_context', JSON.stringify(hsContext));

        const submitUrl = `https://forms.hsforms.com/submissions/v3/public/submit/formsnext/multipart/${portalId}/${formId}`;
        const hsResponse = await fetch(submitUrl, {
            method: 'POST',
            headers: {
                'Origin': 'https://js.hsforms.net',
                'Referer': 'https://js.hsforms.net/ui-forms-embed-components-app/frame.html'
            },
            body: formData
        });

        const responseText = await hsResponse.text();
        const accepted = responseText.includes('"accepted":true');

        return res.status(accepted ? 200 : 400).json({
            accepted,
            raw: responseText
        });
    } catch (err) {
        return res.status(500).json({ error: String(err) });
    }
}
