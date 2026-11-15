# Content of the 5 tailored CVs and 5 cover letters (same text as the Claude Doc tabs).

CONTACT = ["(+33) 6 64 29 38 33 | thomasgoulardpro@gmail.com", "linkedin.com/in/thomas-goulard"]

CNCGP = [
    "Managed relationships with 100+ institutional partners, including asset managers and insurers, in direct contact with senior executives, and a network of 4,000+ independent wealth managers (CGPI), family offices and IAS/IOBSP brokers.",
    "Produced documents for members and governance bodies; verified members' regulatory files (25+ a month).",
]
CNCGP_PB = [
    "Managed relationships with a network of 4,000+ independent wealth managers (CGPI), family offices and IAS/IOBSP brokers, and 100+ institutional partners including asset managers and insurers, in direct contact with senior executives.",
    "Verified members' regulatory files (25+ a month); produced documents for members and governance bodies.",
]
BNP = ["Managed a portfolio of ~300 clients under monthly targets: high-volume prospecting (40+ calls a day, 8–10 qualified meetings a week), sale of savings and investment products."]

GEM_MODULES = "Corporate Finance, Financial Markets, International Financial Management"
ESB_STD = "Financial Mathematics, Taxation, Banking Compliance, Private Banking: 15/20 in every module. Obtained with honors, direct entry into the final year."
ESB_PB = "Private Banking, Banking Compliance, Taxation, Financial Mathematics: 15/20 in every module. Obtained with honors, direct entry into the final year."
TOURS_MKT = "Economic Geography, Political Geography, Geopolitics: emerging markets, resources and trade flows. Licence 1 & 2 validated."
TOURS_STD = "Economic Geography, Political Geography, Geopolitics. Licence 1 & 2 validated."

TOOLS = "Advanced Excel and VBA • PowerPoint (client presentations) • Word • Python • AI tools used daily, every output checked against the source • AMF Certification (French financial-markets regulation)"
LANGS = "French (mother tongue), English (C1), Spanish (B1)"

EXTRA = [
    "Selected for the SEO Europe France Finance Programme (2025–2026), a selective programme promoting social mobility, with technical workshops across leading financial institutions.",
    "Outside linebacker (American football), Pioneers de Touraine, six competitive seasons (2017–2023): French D2 champion in 2022, D1 semi-finalist in 2023.",
    "Entrepreneur: run an Amazon FBA business: sourcing and supplier negotiation, pricing and margins, inventory and logistics.",
]

TAIL = "Master's in Management, Finance, Grenoble École de Management, diploma December 2026 | Internship agreement through a university diploma (DU), Université Paris Nanterre"

CVS = {
    "Natixis_FIG": dict(
        location="Malakoff | France",
        target="Applying to the Financial Analyst Internship – Advisory & Coverage FIG, Natixis CIB, Paris, 6 months from January 2027 | " + TAIL + " | French native, English C1",
        bred=[
            "Prepared client presentations and meeting materials for the senior bankers covering financial institutions in Latin America, the Middle East and Asia-Pacific; country notes and market research on client markets.",
            "Prepared credit applications for counterparty banks, defended in committee; ran KYC onboarding and periodic reviews with Compliance until files were complete.",
            "Built and maintained the team's Excel/VBA client database tracking activity, revenues and limits by client (multi-source consolidation, data checks).",
            "Placed BRED's NEU CP and EMTN with correspondent banks, prices and orders through the dealing platform; prepared the team's meeting programme for Sibos 2026 (Miami); coordinated client requests with BIC-BRED teams in Dubai and Geneva.",
        ],
        cncgp=CNCGP, modules=GEM_MODULES, esb=ESB_STD, tours=TOURS_MKT,
        skill1="FIG analysis: banks (profitability, asset quality, CET1, LCR/NSFR, Basel III) and insurers (Solvency II); credit applications and counterparty reviews; pitch materials and client presentations; CRM reporting automated in Excel/VBA.",
    ),
    "Natixis_Commodities": dict(
        location="Malakoff | France",
        target="Applying to the Assistant Sales Internship – Commodities Markets, Natixis CIB, Paris, 6 months from January 2027 | " + TAIL + " | French native, English C1",
        bred=[
            "Placed BRED's NEU CP and EMTN with correspondent banks: prices and orders through the dealing platform, follow-up of each order.",
            "Prepared client presentations, country notes and market research for the senior bankers covering financial institutions in Latin America, the Middle East and Asia-Pacific.",
            "Built and maintained the team's Excel/VBA client database tracking activity, revenues and limits by client (multi-source consolidation, data checks).",
            "Ran KYC onboarding with Compliance; coordinated client requests with BIC-BRED teams in Dubai and Geneva; prepared the team's meeting programme for Sibos 2026 (Miami).",
        ],
        cncgp=CNCGP, modules="Financial Markets, Corporate Finance, International Financial Management", esb=ESB_STD, tours=TOURS_MKT,
        skill1="Markets: derivatives (futures, options, swaps) from the Financial Markets course; fixed income placement (NEU CP, EMTN) on a dealing platform; commodity fundamentals (resources, supply and trade flows) from geography studies.",
    ),
    "Deutsche_Bank_Geneva": dict(
        location="Malakoff | France – open to relocating to Geneva",
        target="Applying to the Sales Coverage Support Internship, Private Banking, Deutsche Bank, Geneva | " + TAIL + " | French native, English C1, Spanish B1",
        bred=[
            "Ran KYC onboarding and periodic reviews with Compliance: questionnaires, documentation collected and followed up until files were complete.",
            "Built and maintained the team's Excel/VBA client database tracking activity, revenues and limits by client (multi-source consolidation, data checks); credit applications for counterparty banks defended in committee.",
            "Coordinated client requests between the senior bankers, Compliance and BIC-BRED teams in Dubai and Geneva; client presentations and meeting materials for financial institutions in Latin America, the Middle East and Asia-Pacific.",
            "Placed BRED's NEU CP and EMTN with correspondent banks through the dealing platform; prepared the team's meeting programme for Sibos 2026 (Miami).",
        ],
        cncgp=CNCGP_PB, modules=GEM_MODULES, esb=ESB_PB, tours=TOURS_STD,
        skill1="Private banking support: KYC files and periodic reviews, client documentation quality control, credit limits tracking, liaison between front office and support teams; exposure to correspondent banking and payments (Sibos).",
    ),
    "ING_Luxembourg": dict(
        location="Malakoff | France – open to relocating to Luxembourg",
        target="Applying to the Internship – Account Manager, Private Banking, ING Luxembourg, 6 months from January 2027 | " + TAIL + " | French native, English C1",
        bred=[
            "Ran KYC onboarding and periodic reviews with Compliance: questionnaires, documentation collected and followed up until files were complete.",
            "Coordinated client requests between the senior bankers, Compliance and BIC-BRED teams in Dubai and Geneva, for financial institutions in Latin America, the Middle East and Asia-Pacific.",
            "Built and maintained the team's Excel/VBA client database tracking activity, revenues and limits by client (multi-source consolidation, data checks); client presentations and meeting materials.",
            "Placed BRED's NEU CP and EMTN with correspondent banks through the dealing platform; prepared the team's meeting programme for Sibos 2026 (Miami).",
        ],
        cncgp=CNCGP_PB, modules=GEM_MODULES, esb=ESB_PB, tours=TOURS_STD,
        skill1="Private banking and KYC: onboarding and periodic reviews, client documentation and quality control, regulatory file checks, liaison between front office, Compliance and back office.",
    ),
    "Indosuez_Luxembourg": dict(
        location="Malakoff | France – open to relocating to Luxembourg",
        target="Applying to the Marketing and Business Development Officer Internship, Indosuez Wealth Management, Luxembourg, 6 months from January 2027 | " + TAIL + " | French native, English C1, Spanish B1",
        bred=[
            "Built and maintained the team's Excel/VBA client database tracking activity, revenues and limits by client (multi-source consolidation, data checks), used by the senior bankers to prepare client meetings.",
            "Prepared client presentations and meeting materials for the senior bankers covering financial institutions in Latin America, the Middle East and Asia-Pacific; country notes and market research on client markets.",
            "Prepared credit applications for counterparty banks, defended in committee; ran KYC onboarding and periodic reviews with Compliance.",
            "Placed BRED's NEU CP and EMTN with correspondent banks through the dealing platform; prepared the team's meeting programme for Sibos 2026 (Miami); coordinated client requests with BIC-BRED teams in Dubai and Geneva.",
        ],
        cncgp=CNCGP, modules=GEM_MODULES, esb="Private Banking, Taxation, Banking Compliance, Financial Mathematics: 15/20 in every module. Obtained with honors, direct entry into the final year.", tours=TOURS_STD,
        skill1="Business development analytics: Excel/VBA dashboards on client activity and revenues, multi-source data consolidation and checks; investment products (savings and investment products sold at BNP Paribas, Private Banking module at ESB); wealth management distribution (CGPI, family offices, insurers).",
    ),
}

FR_DIPLOMA = "Je serai diplômé en décembre 2026 du Programme Grande École de Grenoble École de Management, spécialisation Finance, et ma convention de stage sera établie par l'Université Paris Nanterre, dans le cadre d'un DU."
FR_CLOSE = "Je serais heureux d'échanger avec vous et vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées."

LETTERS = {
    "Natixis_FIG": dict(
        lang="fr", address="Malakoff, 92240", date="Paris, le 8 novembre 2026",
        subject="Objet. Candidature au stage Financial Analyst – Advisory & Coverage FIG, Natixis CIB (janvier 2027)",
        salutation="Madame, Monsieur,",
        paras=[
            "Je vous adresse ma candidature au stage de Financial Analyst au sein du Coverage FIG de Natixis CIB, pour six mois à partir de janvier 2027. " + FR_DIPLOMA,
            "Le coverage FIG, je l'ai exercé pendant un an à la BRED, déjà au sein du Groupe BPCE. J'y travaillais auprès des banquiers qui couvrent des institutions financières d'Amérique latine, du Moyen-Orient et d'Asie-Pacifique. Je préparais les présentations clients et les notes pays, je montais des demandes de crédit sur des contreparties bancaires présentées en comité, et je menais les dossiers KYC avec la Conformité. J'ai aussi construit la base clients Excel/VBA de l'équipe, qui suit l'activité, les revenus et les limites par client : le type de reporting que vous automatisez sous NAT1.",
            "Auparavant, à la Chambre Nationale des Conseils en Gestion de Patrimoine, j'ai suivi plus de cent partenaires institutionnels, dont des sociétés de gestion et des assureurs. Banques, assureurs, asset managers : je connais déjà les clients de votre équipe, et les indicateurs qui servent à les analyser, de la rentabilité et du CET1 au LCR et au ratio Solvabilité II.",
            "Ce qui m'attire chez Natixis, c'est un Coverage qui porte toute la gamme de la CIB, du financement au M&A jusqu'à l'Asset & Wealth Management, pour des institutions en France et à l'international. Je n'ai pas encore participé à une exécution ni modélisé une contrepartie en profondeur, et c'est ce que je viens apprendre auprès de vos senior bankers. J'apporte de la rigueur, une bonne plume en français et en anglais, et l'habitude de mener plusieurs sujets de front.",
            FR_CLOSE,
        ],
        signoff=None,
    ),
    "Natixis_Commodities": dict(
        lang="fr", address="Malakoff, 92240", date="Paris, le 8 novembre 2026",
        subject="Objet. Candidature au stage Assistant Sales Commodities Markets, Natixis CIB (janvier 2027)",
        salutation="Madame, Monsieur,",
        paras=[
            "Je vous adresse ma candidature au stage d'Assistant Sales au sein de l'équipe Commodities Sales de Natixis CIB, pour six mois à partir de janvier 2027. " + FR_DIPLOMA,
            "Les matières premières sont le point de départ de mon parcours. Ma licence de géographie à l'Université de Tours portait sur les marchés émergents, les ressources et les flux commerciaux. J'y ai appris à lire un marché par ses fondamentaux et sa géopolitique. J'ai ensuite choisi la finance, à l'École Supérieure de la Banque puis à Grenoble École de Management, où le cours Financial Markets m'a formé aux futures, options et swaps.",
            "La vente, je l'ai pratiquée à la BRED, au sein du Groupe BPCE. En FI coverage, je plaçais les NEU CP et EMTN de la banque auprès de banques correspondantes, avec les prix et les ordres passés via la plateforme de dealing, et je préparais les présentations clients et les notes de marché des banquiers. J'ai aussi construit en Excel/VBA la base clients de l'équipe, qui suit l'activité et les revenus par client, un outil proche du suivi des ventes que vous digitalisez. Chez BNP Paribas, j'avais auparavant géré 300 clients sous objectifs mensuels.",
            "Ce qui m'attire chez Natixis, c'est un desk qui accompagne à la fois des institutionnels et des corporates dans la couverture de leurs risques sur l'énergie, les métaux et les produits agricoles. Je n'ai pas encore pricé de dérivés sur matières premières, et c'est ce que je viens apprendre auprès de vos sales et de vos structureurs. J'apporte un vrai sens commercial, de la rigueur et un anglais courant (C1).",
            FR_CLOSE,
        ],
        signoff=None,
    ),
    "Deutsche_Bank_Geneva": dict(
        lang="en", address="Malakoff, 92240, France", date="Paris, 8 November 2026",
        subject="Application – Sales Coverage Support Intern, Private Banking, Deutsche Bank, Geneva",
        salutation="Dear Hiring Team,",
        paras=[
            "I am applying for the Sales Coverage Support Internship within the Service Executive team of Deutsche Bank's Private Bank in Geneva. I will graduate in December 2026 from the Grande École programme of Grenoble École de Management (Master's in Management, Finance), and my internship agreement will be issued by Université Paris Nanterre through a university diploma (DU).",
            "This role sits between the Relationship Managers and the support functions, which is where I worked at BRED Banque Populaire. In the team covering financial institutions in Latin America, the Middle East and Asia-Pacific, I ran KYC onboarding and periodic reviews with Compliance, following each file until it was complete, and coordinated client requests with our teams in Dubai and Geneva. I also built the team's Excel/VBA client database tracking activity, revenues and limits by client, and prepared credit applications on counterparty banks for committee.",
            "Wealth management is the other half of my background. At the Chambre Nationale des Conseils en Gestion de Patrimoine, I worked with a network of 4,000+ independent wealth managers and family offices and verified 25+ regulatory files a month. At BNP Paribas, I managed around 300 clients under monthly targets. In both roles, client service came down to details: a complete file, a fast answer, a correct figure.",
            "I attended Deutsche Bank's Investment Bank & Capital Markets Insight Event in September, and I want to build my career in Geneva. Your Private Bank's offer to entrepreneur families, combining lending, FX and fixed income, matches what I know from corporate and institutional banking. I have not yet worked on Avaloq or on mandate management, and that is what I want to learn with your team. I bring rigour, fluent French and English, working Spanish, and daily use of AI tools with every output checked against the source.",
            "I would welcome the opportunity to discuss my application.",
        ],
        signoff="Kind regards,",
    ),
    "ING_Luxembourg": dict(
        lang="en", address="Malakoff, 92240, France", date="Paris, 8 November 2026",
        subject="Application – Internship, Account Manager, Private Banking, ING Luxembourg (January 2027)",
        salutation="Dear Hiring Team,",
        paras=[
            "I am applying for the Account Manager Internship in ING Luxembourg's Private Banking department, for six months from January 2027. I will graduate in December 2026 from the Grande École programme of Grenoble École de Management (Master's in Management, Finance), and Université Paris Nanterre will issue my internship agreement through a university diploma (DU).",
            "A large part of this role is KYC and onboarding, which I handled throughout my year at BRED Banque Populaire. In the team covering financial institutions in Latin America, the Middle East and Asia-Pacific, I ran onboarding and periodic reviews with Compliance: questionnaires, documents collected and followed up until each file was complete. I coordinated client requests with our teams in Dubai and Geneva and kept the team's Excel/VBA client database up to date.",
            "Wealth management is the other half of my background. At the Chambre Nationale des Conseils en Gestion de Patrimoine, I worked with 4,000+ independent wealth managers and family offices, in direct contact with senior executives of asset managers and insurers, and verified 25+ regulatory files a month. At BNP Paribas, I managed around 300 clients and sold savings and investment products. I also took the Private Banking, Banking Compliance and Taxation modules at École Supérieure de la Banque, with 15/20 in each.",
            "ING Luxembourg appeals to me because this role combines service to high-net-worth families with a strong regulatory side, in an international financial centre. I have not yet worked with HNW clients directly, and that is what I want to learn with your Private Bankers. I bring discretion, rigour, fluent French and English, and working Spanish.",
            "I would be glad to discuss my application.",
        ],
        signoff="Kind regards,",
    ),
    "Indosuez_Luxembourg": dict(
        lang="en", address="Malakoff, 92240, France", date="Paris, 8 November 2026",
        subject="Application – Marketing and Business Development Officer Internship, Indosuez Wealth Management, Luxembourg (January 2027)",
        salutation="Dear Hiring Team,",
        paras=[
            "I am applying for the six-month Marketing and Business Development internship at Indosuez Wealth Management in Luxembourg, starting in January 2027. I will graduate in December 2026 from the Grande École programme of Grenoble École de Management (Master's in Management, Finance), and Université Paris Nanterre will issue my internship agreement through a university diploma (DU).",
            "Building tools that drive business development is what I did at BRED Banque Populaire. In the team covering financial institutions in Latin America, the Middle East and Asia-Pacific, I built and maintained the Excel/VBA client database that tracks activity, revenues and limits by client, consolidating several sources and checking the data. The senior bankers used it to prepare client meetings, for which I produced presentations, country notes and market research. I also prepared credit applications for committee and ran KYC files with Compliance.",
            "Wealth management is the other side of my background. At the Chambre Nationale des Conseils en Gestion de Patrimoine, I worked with 100+ institutional partners, including asset managers and insurers, and a network of 4,000+ independent wealth managers and family offices, and produced documents for governance bodies. At BNP Paribas, I sold savings and investment products to a portfolio of around 300 clients under monthly targets.",
            "Indosuez attracts me for its European scale since the Degroof Petercam acquisition, and because this role sits at the heart of the bank's commercial management, from client reviews to action plans. I have not yet worked on pricing reviews, and that is what I want to learn with your Performance Management team. I bring advanced Excel and VBA, working knowledge of Python, fluent French and English, and working Spanish.",
            "I would be glad to discuss my application.",
        ],
        signoff="Kind regards,",
    ),
}
