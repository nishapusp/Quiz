import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
    {
    "question": "RAROC is a RAPM tool as it accounts for risk in measuring the performance of the bank. RAPM stands for?",
    "options": ["Risk Assessment Performance Metric", "Risk Adjusted Priority Measure", "Risk Adjustment and Performance Management", 
                "Risk Assessment and Priority Management", "Risk Adjusted Performance Measure"],
    "correct_answer": "Risk Adjusted Performance Measure"
},
{
    "question": "RAROC framework has been implemented in bank as per the guidelines of EASE agenda. RAROC stands for…...........",
    "options": ["Risk Added to Return on Capital", "Risk Assessment in Return on Capital", "Risk Adjusted Return on Capital", 
                "Risk Adjusted Return on Credit", "Risk Passement in Review of Credit"],
    "correct_answer": "Risk Adjusted Return on Capital"
},
{
    "question": "While assessing risk under UBI model, scores for availability of collateral security is done in------parameter. Please select the correct option?",
    "options": ["Borrower rating", "Facility rating", "Risk mitigator", "Management rating", "Business aspect"],
    "correct_answer": "Risk mitigator"
},
{
    "question": "As per RBRCA guidelines who will do the initiation of RCRCA rating?",
    "options": ["Risk officer at ZO", "Risk Officer at RO", "Branch Manager of Concerned Branch", "MLP Head", "Credit In charge at RO"],
    "correct_answer": "Risk Officer at RO"
},
{
    "question": "Which of the following is not true about Scrutiny Committee (RLCC-I)?",
    "options": ["The Convenor of committee shall be Credit In charge of RLCC-I", 
                "Minutes of scrutiny committee meeting along with the mitigants proposed to be recorded properly and shall be placed before ZLCC",
                "Risk Officer shall be a mandatory part of Committee", 
                "Convenor should preserve the minutes of Meeting for future use",
                "Scrutiny committee shall either reject or recommend the proposal"],
    "correct_answer": "Risk Officer shall be a mandatory part of Committee"
},
{
    "question": "Who will be the sanctioning authority for High Risk/ No go Proposal originally in the delegation power MLCC?",
    "options": ["RLCC-II", "ZLCC", "MLCC only", "RLCC-I", "CAC-III"],
    "correct_answer": "RLCC-I"
},
{
    "question": "What is the threshold limit of total credit exposer of a borrower for using CRISIL ICON model for rating?",
    "options": ["Rs. 5.00 Crs", "Rs. 1.00 Crs", "Rs. 50 lakhs", "Rs. 10.00 Crs", "Rs. 25.00 Crs"],
    "correct_answer": "Rs. 5.00 Crs"
},
{
    "question": "Union Trade Model I is applicable for rating of exposure above",
    "options": ["Rs.25 Lakh to Rs.50 Lakh", "Rs.2 Lakh to Rs.25 Lakh", "Rs.25 Lakh to Rs.100 Lakh", 
                "Rs.50 Lakh to Rs.100 Lakh", "Rs.50 Lakh to Rs.500 Lakh"],
    "correct_answer": "Rs.25 Lakh to Rs.100 Lakh"
},
{
    "question": "Which of the following approach is being used in our bank for calculating Credit Risk?",
    "options": ["Standardised approach", "Foundation Internal Rating-Based Approach (FIRB)", 
                "Advanced Internal Rating-Based Approach (AIRB)", "Standard approach", "Basic approach"],
    "correct_answer": "Standardised approach"
},
{
    "question": "Insurance works on which principal of credit risk management?",
    "options": ["Avoiding the risk", "Eliminating the risk", "Transferring the risk", "Accepting the risk", "Managing the risk"],
    "correct_answer": "Transferring the risk"
},
{
    "question": "Our Bank's Internal rating models are",
    "options": ["UBI II & III, UTR I & II", "UBI I & II, UTR I & II", "UTR I & II", "UBI I & II", "UBI II & III"],
    "correct_answer": "UBI I & II, UTR I & II"
},
{
    "question": "A facility is rated for long term and it has secured a long-term rating of BBB-(Minus). As per mapping of external and internal credit rating it is equivalent to which internal rating?",
    "options": ["UCR 5", "UCR 4", "UCR 6", "UCR 2", "UCR 7"],
    "correct_answer": "UCR 5"
},
{
    "question": "The credit ratings not arising out of the agreement between a CRA and the issuer is known as",
    "options": ["Uncalled", "Unwanted", "Self rating", "Unsolicited", "Unrated"],
    "correct_answer": "Unsolicited"
},
{
    "question": "WACC has been considered as Hurdle Rate of RAROC. WACC stands for…....",
    "options": ["Weighted Average Cost of Capital", "Working Average Cost of Capital", "Working Average Cost of Credit",
                "Weighted Average Cost of Credit", "Weighted Assessment Cost of Capital"],
    "correct_answer": "Weighted Average Cost of Capital"
},
{
    "question": "As per RBRCA guidelines and RBRCA Cell composition, Who is responsible for final Risk Categorization?",
    "options": ["Regional Risk officer", "Zonal Risk Officer", "Regional Head", "Risk Officer at Central Office", 
                "Both Regional Risk Officer and Zonal Risk Officer"],
    "correct_answer": "Zonal Risk Officer"
},
{
    "question": "What does the 'Social license to operate' signify in the context of ESG?",
    "options": ["Legal permission to operate a business", "A company's alignment with societal norms and expectations",
                "Certification for environmentally friendly practices", "Approval from international regulatory bodies",
                "Compliance with financial reporting standards"],
    "correct_answer": "A company's alignment with societal norms and expectations"
},
{
    "question": "What is the Greenhouse Gas (GHG) Protocol, and how does it categorize emissions?",
    "options": ["A set of accounting standards for sustainable investments, categorizing emissions by industry",
                "A framework for measuring a company's environmental footprint, dividing emissions into Scopes 1, 2, and 3",
                "A regulation mandating reductions in greenhouse gas emissions for different sectors",
                "An international agreement for carbon trading and emission reduction targets",
                "A methodology for assessing the social and economic impacts of climate change"],
    "correct_answer": "A framework for measuring a company's environmental footprint, dividing emissions into Scopes 1, 2, and 3"
},
{
    "question": "What are the two 'A's' of effective corporate governance?",
    "options": ["Agility and Adaptability", "Accountability and Alignment", "Affordability and Accessibility",
                "Awareness and Advocacy", "Authority and Autonomy"],
    "correct_answer": "Accountability and Alignment"
},
{
    "question": "What are some of the issues covered under environmental factors in ESG?",
    "options": ["Human rights and working conditions", "Climate change, resource depletion, and pollution",
                "Board diversity and executive pay", "Product liability and consumer protection",
                "Stakeholder relations and community engagement"],
    "correct_answer": "Climate change, resource depletion, and pollution"
},
{
    "question": "What is the primary focus of Scope 1 emissions in the GHG Protocol?",
    "options": ["Emissions from purchased energy sources (e.g., electricity)", 
                "Indirect emissions from the entire value chain (beyond Scopes 1 & 2)",
                "Emissions directly generated by a company's owned or controlled sources (e.g., factories)",
                "Emissions associated with employee commuting and business travel",
                "Emissions released during the transportation and use of a company's products"],
    "correct_answer": "Emissions directly generated by a company's owned or controlled sources (e.g., factories)"
},
{
    "question": "What does the ESG integration in risk management help companies achieve?",
    "options": ["Increased operational costs", "Enhanced long-term sustainability", "Reduced regulatory compliance", 
                "Decreased market share", "Lower employee satisfaction"],
    "correct_answer": "Enhanced long-term sustainability"
},
{
    "question": "What does ESG stand for?",
    "options": ["Environmental, Social and Governance", "Economic, Social, and Growth", "Ethical, Sustainable, and Green",
                "Energy, Sustainability, and Growth", "Environmental, Safety, and Government"],
    "correct_answer": "Environmental, Social and Governance"
},
{
    "question": "What are some of the social factors considered in ESG risk assessment?",
    "options": ["Energy use and resource efficiency", "Human capital development and labor rights", 
                "Waste management and pollution control", "Climate change mitigation and adaptation",
                "Sustainable product design and innovation"],
    "correct_answer": "Human capital development and labor rights"
},
{
    "question": "According to the Triple Bottom Line (TBL) accounting theory, what are the three key performance areas for a company?",
    "options": ["Financial performance, market share, and customer satisfaction",
                "Profitability, operational efficiency, and brand recognition",
                "Social responsibility, environmental impact, and economic prosperity",
                "Innovation, risk management, and regulatory compliance",
                "Short-term gains, long-term growth, and shareholder value"],
    "correct_answer": "Social responsibility, environmental impact, and economic prosperity"
},
{
    "question": "Fraud-loss limits shall be monitored regularly by the fraud risk management group and a review needs to be undertaken with the respective business group when fraud loss amount reaches _____ of the limit set.",
    "options": ["90%", "75%", "67%", "85%", "100%"],
    "correct_answer": "90%"
},
{
    "question": "On receipt of the information / trigger on suspicious fraud, Nodal Officer shall nominate any suitable officer to carry out investigation within ___ days.",
    "options": ["3", "5", "10", "15", "21"],
    "correct_answer": "3"
},
{
    "question": "In case of suspicious fraud cases, Investigating Officer shall submit a complete investigation report along with relevant documents within ___ days.",
    "options": ["7", "15", "21", "30", "60"],
    "correct_answer": "15"
},
{
    "question": "When there is delayed reporting of fraud cases to the Reserve Bank of India, what percentage of provision is made on the amount involved in fraud during the quarter of detection?",
    "options": ["25", "50", "75", "100", "It varies depending on the nature of the fraud."],
    "correct_answer": "100"
},
{
    "question": "All fraud cases must be reported to RBI in XBRL within _____ from the date of detection of fraud.",
    "options": ["1 week", "25 days", "3 weeks", "1 months", "3 days"],
    "correct_answer": "3 weeks"
},
{
    "question": "What is the minimum quorum for the Fraud Monitoring Group-I (FMG-I) at Central Office?",
    "options": ["3 members", "4 members", "5 members", "6 members", "7 members"],
    "correct_answer": "5 members"
},
{
    "question": "In case of accounts where forensic auditor is appointed, audit must be concluded within ________.",
    "options": ["75 days from the date of commencement of audit", 
                "90 days from the date of assignment of audit",
                "60 days from the date of assignment of audit",
                "60 days from the date of commencement of audit",
                "90 days from the date of commencement of audit"],
    "correct_answer": "60 days from the date of commencement of audit"
},
{
    "question": "Cash shortages resulting from negligence will be reported as Fraud if",
    "options": ["cash shortage more than Rs.10,000/-",
                "cash shortage more than Rs.5,000/-",
                "cash shortage more than Rs.5,000/- if detected by management/ auditor/ inspecting officer and not reported on the day of occurrence by the persons handling cash.",
                "A & C",
                "cash shortage more than Rs.10,000/- if detected by management/ auditor/ inspecting officer and not reported on the day of occurrence by the persons handling cash."],
    "correct_answer": "A & C"
},
{
    "question": "All fraud cases of Rs.___ & above must be reported in Union FRIEND (Fraud related Intelligent End to End Digitization) Portal.",
    "options": ["Rs.1 Lakh", "Rs. 10000", "Rs.1 Crore", "All cases irrespective of amount", "Rs.3 Crore"],
    "correct_answer": "All cases irrespective of amount"
},
{
    "question": "In fraud cases of Rs. 3.00 Crs & above, through which department should CRILC reporting be done?",
    "options": ["RMD", "Audit & Inspection", "CRILC Cell, CCM Department", "TM&FM", "Legal Department"],
    "correct_answer": "CRILC Cell, CCM Department"
},
{
    "question": "Who is the Nodal Officer at Regional Offices (ROs) for reporting suspicious elements or possible fraud?",
    "options": ["Regional Head", "Zonal Head", "Deputy Regional Head", "Branch Manager", "General Manager"],
    "correct_answer": "Deputy Regional Head"
},
{
    "question": "What type of fraud cases are NOT reported through the UNION FRIEND portal?",
    "options": ["Digital fraud cases", "Suspected credit fraud cases", "Non-credit fraud cases", 
                "Fraud cases involving amounts less than Rs.1 crore", "KYC related frauds"],
    "correct_answer": "Digital fraud cases"
},
{
    "question": "In which scenario does a fraud occur with the involvement of both bank employees and outsider who may or may not be customer of the bank?",
    "options": ["Customer-exclusive outsider fraud.", "Employee-insider collusion fraud.", 
                "Outsider-customer collusion fraud.", "Employee-outsider collusion fraud.",
                "Insider-supported outsider fraud."],
    "correct_answer": "Employee-outsider collusion fraud"
},
{
    "question": "Which type of fraud does the CHAKSHU portal NOT handle?",
    "options": ["KYC related to Bank/Electricity/Gas/Insurance policy", "Fake Customer Care Helpline",
                "Online job/lottery/gifts/loans offer", "Financial fraud",
                "Impersonation as Government official/relative"],
    "correct_answer": "Financial fraud"
},
{
    "question": "Cases of Attempted Fraud, shall be reported by the Regional Office to --------",
    "options": ["PBOD, CO", "FMD (TM&FM)", "Central Vigilance Dept.", "CA & ID", "Police Authorities"],
    "correct_answer": "FMD (TM&FM)"
},
{
    "question": "What does the acronym FRIEND stands for in the UNION FRIEND portal?",
    "options": ["Fraud Related Intelligent End to End Digitization", "Fraud Risk Intelligent End to End Digitization", 
                "Fraud Response Internal End to End Digitization", "Fraud Regulation Interactive End to End Digitization",
                "Fraud Review Integrated End to End Digitization"],
    "correct_answer": "Fraud Related Intelligent End to End Digitization"
},
{
    "question": "Cases of large value loan frauds of Rs.50.00 Cr & above, pertaining to Public Sector Bank (PSB) where there is allegation of involvement of Officers of the bank in rank of _____and above, shall be referred to Advisory Board for Banking Frauds prior to referring the case to investigating agencies.",
    "options": ["Chief General Manager", "General Manager", "Executive Director", "Deputy General Manager", "Assistant General Manager"],
    "correct_answer": "General Manager"
},
{
    "question": "Against which agencies should complaints be filed in cases of Chartered Accountants' collusion or failure in fraud cases involving amounts Rs 25.00 Crs and above?",
    "options": ["SEBI and RBI", "CBI and ED", "ICAI, NFRA, and any other relevant agencies", 
                "NCLT and NCLAT", "Ministry of Corporate Affairs and Finance Ministry"],
    "correct_answer": "ICAI, NFRA, and any other relevant agencies"
},
{
    "question": "In case of credit-related frauds where the account is under NPA Category at the time of detection of fraud, the provision shall not be:",
    "options": ["Equal to the provision made at the time of fraud detection.",
                "Greater than the provision made at the time of fraud detection.",
                "Less than the provision already made in the account (as per IRAC Norms)",
                "The same as the outstanding loan balance.",
                "Determined based on the recovery prospects of the fraud amount."],
    "correct_answer": "Less than the provision already made in the account (as per IRAC Norms)"
},
{
    "question": "How often does the Fraud Monitoring Group-I (FMG-I) meet by default, and how often might it convene under certain circumstances?",
    "options": ["Monthly; Never more than once a month.", 
                "Weekly; More than once a week.",
                "Quarterly; As needed.",
                "Monthly; More than once a month based on exigencies.",
                "Biannually; At least once every two months."],
    "correct_answer": "Monthly; More than once a month based on exigencies."
},
{
    "question": "Fraud is classified under which Risk?",
    "options": ["Operational Risk", "Legal Risk", "Market Risk", "Credit Risk", "Liquidity risk"],
    "correct_answer": "Operational Risk"
},
{
    "question": "All _____ related frauds, irrespective of value of fraud, irrespective if such incident has resulted any loss to the bank or not, either reported by customer or detected by the bank shall have to be reported to the CPFIR portal.",
    "options": ["Credit", "Payment", "Non-credit", "A & C", "A, B & C"],
    "correct_answer": "Payment"
},
{
    "question": "___ must examine and direct the branch for lodging complaint with police in appropriate cases of attempted fraud.",
    "options": ["Zonal Office", "Risk Management Department, Central Office", "Regional Office", 
                "Legal Services Department, Central Office", "TM&FM, Central Office"],
    "correct_answer": "Regional Office"
},
{
    "question": "What is the minimum threshold for non-credit related cases to be considered by the FMG-I?",
    "options": ["Rs. 5.00 Crores", "Rs. 7.50 Crores", "Rs. 10.00 Crores", "Rs. 15.00 Crores", "Rs. 20.00 Crores"],
    "correct_answer": "Rs. 10.00 Crores"
},
{
    "question": "What is the minimum threshold for credit-related fraud cases to be examined by the Zonal Level Fraud Recommendation Committee (ZLFRC-I)?",
    "options": ["Rs. 5.00 Crores", "Rs. 10.00 Crores", "Rs. 15.00 Crores", "Rs. 20.00 Crores", "Rs. 25.00 Crores"],
    "correct_answer": "Rs. 25.00 Crores"
},
{
    "question": "Scope of Zonal Level Fraud Recommendation Committee headed by Zonal Head (ZLFRC-I) includes examination of non-credit related frauds amounting to Rs._____ and above",
    "options": ["Rs.10 Crore", "Rs.5 Crore", "Rs.50 Crore", "Rs.25 Crore", "Rs.1 Crore"],
    "correct_answer": "Rs.10 Crore"
},
{
    "question": "Scope of Fraud Monitoring Group-II (FMG-II) at Central Office includes examination of non credit related frauds amounting up to Rs._____.",
    "options": ["Rs.1 Crore", "Rs.5 Crore", "Rs.10 Crore", "Rs.25 Crore", "Rs.50 Crore"],
    "correct_answer": "Rs.10 Crore"
},
{
    "question": "All actual fraud cases above _____ and cases where a unique modus operandi is involved, shall be reviewed immediately after such a fraud is detected.",
    "options": ["Rs.1 Lakh", "Rs.5 Lakh", "Rs.1 Crore", "Rs.25 Lakh", "Rs.10 Lakh"],
    "correct_answer": "Rs.10 Lakh"
},
{
    "question": "Scope of Zonal Level Fraud Recommendation Committee headed by Zonal Head (ZLFRC-I) includes examination of All credit related frauds amounting to Rs._____ and above (individual / group exposure) pertaining to branches/ offices including LCB/MCB/SAMB except Foreign Branches",
    "options": ["Rs.25 Crore", "Rs.5 Crore", "Rs.50 Crore", "Rs.10 Crore", "Rs.100 Crore"],
    "correct_answer": "Rs.25 Crore"
},
{
    "question": "Scope of Fraud Monitoring Group-I (FMG-I) at Central Office includes examination of credit related frauds amounting to Rs._____ and above",
    "options": ["Rs.5 Crore", "Rs.10 Crore", "Rs.25 Crore", "Rs.50 Crore", "Rs.100 Crore"],
    "correct_answer": "Rs.25 Crore"
},
{
    "question": "In fraud cases of Rs.___ & above, CRILC reporting to be done within ___ of detection of fraud.",
    "options": ["Rs.3 Crore, 1 week", "Rs.3 Crore, 3 weeks", "Rs.5 Crore, 1 week", "Rs.5 Crore, 3 weeks", "Rs.1 Crore, 3 days"],
    "correct_answer": "Rs.3 Crore, 1 week"
},
{
    "question": "All NPA accounts with exposure above _____ on date of NPA shall be examined for EWS (Early Warning Signals), Wilful Default and Fraud",
    "options": ["Rs.5 Crore", "Rs.10 Crore", "Rs.25 Crore", "Rs.50 Crore", "Rs.100 Crore"],
    "correct_answer": "Rs.50 Crore"
},
{
    "question": "Cases of large value loan frauds of Rs.___ & above, pertaining to Public Sector Bank (PSB) where there is allegation of involvement of Officers of the bank in rank of General Manager and above, shall be referred to Advisory Board for Banking Frauds prior to referring the case to investigating agencies.",
    "options": ["Rs.5 Crore", "Rs.10 Crore", "Rs.25 Crore", "Rs.50 Crore", "Rs.100 Crore"],
    "correct_answer": "Rs.50 Crore"
},
{
    "question": "Digital frauds also include incidents where:",
    "options": ["The bank suffers a significant financial loss", 
                "The credentials have been compromised by customers themselves or where no loss has been caused to the Bank.",
                "The fraud is limited to international transactions only",
                "The fraud is caused by internal bank staff only",
                "Only credit card transactions are involved"],
    "correct_answer": "The credentials have been compromised by customers themselves or where no loss has been caused to the Bank."
},
{
    "question": "Where should financial fraud complaints be raised?",
    "options": ["CHAKSHU Portal", "Local Police Station", "Cyber Crime Police Station", 
                "Through 1930 or https://www.cybercrime.gov.in", "Telecom Regulatory Authority of India"],
    "correct_answer": "Through 1930 or https://www.cybercrime.gov.in"
},
{
    "question": "What is the primary purpose of KYC compliance and due diligence standards?",
    "options": ["To assess customer creditworthiness", "To ensure the identification and verification of customers",
                "To evaluate market risk", "To monitor employee performance", "To detect system vulnerabilities"],
    "correct_answer": "To ensure the identification and verification of customers"
},
{
    "question": "What is the purpose of the UNION FRIEND portal?",
    "options": ["To handle customer service inquiries", "To manage payroll processing",
                "To facilitate all aspects of fraud governance", "To provide online banking services",
                "To monitor employee performance"],
    "correct_answer": "To facilitate all aspects of fraud governance"
},
{
    "question": "What is the primary purpose of the CHAKSHU portal under the Sanchar Saathi initiative?",
    "options": ["To handle financial fraud cases", 
                "To report suspected fraud communications through Call, SMS, or WhatsApp",
                "To monitor telecom service quality",
                "To provide customer support for telecom services",
                "To promote digital literacy"],
    "correct_answer": "To report suspected fraud communications through Call, SMS, or WhatsApp"
},
{
    "question": "How should incidents of fraud be reported to the FMD, TM&FM?",
    "options": ["Through a formal letter sent by post",
                "By filing a report on the CHAKSHU portal",
                "Via email to agmrmd.fraudrisk@unionbankofindia.bank, frmd@unionbankofindia.bank",
                "By calling the bank's customer service",
                "Through an online form"],
    "correct_answer": "Via email to agmrmd.fraudrisk@unionbankofindia.bank, frmd@unionbankofindia.bank"
},
{
    "question": "The LCR is a ratio of two factors, viz., the Stock of HQLA and the Net Cash Outflows over the next …......... calendar days.",
    "options": ["30", "60", "90", "120", "365"],
    "correct_answer": "30"
},
{
    "question": "NSFR is an important liquidity measure which measure stability of funding for …............?",
    "options": ["6 months", "1 year", "9 months", "30 days", "90 days"],
    "correct_answer": "1 year"
},
{
    "question": "What is the Quorum and Frequency of ALCO Meeting?",
    "options": ["6, Quarterly", "8, Monthly", "8, Quarterly", "8, Half Yearly", "6, Monthly"],
    "correct_answer": "8, Monthly"
},
{
    "question": "…............ Is entrusted with implementation of RBI guidelines on liquidity risk management and also to make business decision.",
    "options": ["General Manager(RMD)", "ALCO", "CRO", "Board of directors", "MD & CEO"],
    "correct_answer": "ALCO"
},
{
    "question": "In a situation of excess liquidity, the bank would look at which of the following options:",
    "options": ["Money Market lending", "Reverse REPO", "Buying T-bills, CP or securities depending upon the tenures of surplus liquidity",
                "Only option a & b", "All the above"],
    "correct_answer": "All the above"
},
{
    "question": "NSFR is a ratio of two factors, ASF and RSF. What ASF denotes?",
    "options": ["Available of stable funding", "Actual stable funding", "Actual secure funding",
                "Available of secure funding", "Actual security funding"],
    "correct_answer": "Available of stable funding"
},
{
    "question": "A bank has a Stock of high quality liquid asset(HQLA) worth Rs- 5 lakh crore and Available of stable funding (ASF) is worth Rs-23 lakh crore. Whether bank would be able to meet its short term liquidity requirement (LCR) if the net cash outflow over 30 days come to Rs-7 lakh crore?",
    "options": ["Bank will not be able to meet its liquidity needs of 30 days as its LCR is < 1.",
                "Bank will not be able to meet its liquidity needs of 30 days as its LCR is > 1.",
                "Bank will be able to meet its liquidity needs of 30 days as its LCR is > 1.",
                "Bank will be able to meet its liquidity needs of 30 days as its LCR is < 1.",
                "Data is insufficient to take decision."],
    "correct_answer": "Bank will not be able to meet its liquidity needs of 30 days as its LCR is < 1."
},
{
    "question": "A bank has a Stock of high quality liquid asset(HQLA) worth Rs- 13 lakh crore and Available of stable funding (ASF) is worth Rs-20 lakh crore. Whether bank would be able to sustain funding for 1 year (NSFR) if the required of stable funding( RSF) comes to Rs-22 Lakh crore?",
    "options": ["Bank will not be able to meet its liquidity needs of 1 year as its NSFR is < 1.",
                "Bank will not be able to meet its liquidity needs of 1 year as its NSFR is > 1.",
                "Bank will be able to meet its liquidity needs of 1 year as its NSFR is > 1.",
                "Bank will be able to meet its liquidity needs of 1 year as its NSFR is < 1.",
                "Data is insufficient to take decision."],
    "correct_answer": "Bank will not be able to meet its liquidity needs of 1 year as its NSFR is < 1."
},
{
    "question": "…............ is overall responsible for the management of the Liquidity Risk in the bank.",
    "options": ["RBI", "ALCO", "CRO", "Board of directors", "General manager (RMD)"],
    "correct_answer": "Board of directors"
},
{
    "question": "…...................metric is meant to identify those sources of funding that are of such significance, withdrawal of which could trigger liquidity problems.",
    "options": ["Contractual Maturity Mismatch", "Concentration of Funding", "Available Unencumbered Assets",
                "LCR by Significant Currency", "Market-related Monitoring Tools"],
    "correct_answer": "Concentration of Funding"
},
{
    "question": "…...........helps the bank to identify the gaps between the contractual inflows and outflows of liquidity for defined time bands.",
    "options": ["Contractual Maturity Mismatch", "Concentration of Funding", "Available Unencumbered Assets",
                "LCR by Significant Currency", "Market-related Monitoring Tools"],
    "correct_answer": "Contractual Maturity Mismatch"
},
{
    "question": "Which of the following are the two ways to measure liquidity in banks?",
    "options": ["Market approach and Flow approach", "Stock approach and income approach", 
                "Flow approach and stock approach", "stock approach and cash flow approach",
                "Stock approach and business approach"],
    "correct_answer": "Flow approach and stock approach"
},
{
    "question": "There are two types of liquidity risk in banks. One is Market liquidity risk and second is…........",
    "options": ["Funding liquidity risk", "Bank liquidity risk", "Security liquidity risk",
                "Derivative liquidity risk", "T Bond liquidity risk"],
    "correct_answer": "Funding liquidity risk"
},
{
    "question": "Bank through Asset Liability Management functions try to hedge a portfolio of Assets and Liabilities with the same duration, against interest rate risk and maintain the spread. This process is known as",
    "options": ["Corridor", "Caps", "Strategies with Interest Rate Futures", "Simulations", "Immunisation"],
    "correct_answer": "Immunisation"
},
{
    "question": "ALM function encompass identifying, measuring, monitoring and managing",
    "options": ["Interest Rate Risk and Foreign Exchange Risk", 
                "Liquidity Risk, Credit risk and Operational risk",
                "Credit risk, Interest rate risk, and Currency risk",
                "Interest Rate risk, Liquidity risk and Foreign Exchange Risk",
                "Credit Risk, Operational Risk and Market Risk"],
    "correct_answer": "Interest Rate risk, Liquidity risk and Foreign Exchange Risk"
},
{
    "question": "A Bank finds it difficult to repay short-term deposits on maturity to its depositor because of funds with that bank are locked in long term loans or investments. The risk arising from this situation is called",
    "options": ["Liquidity Risk", "Interest Rate Risk", "Operational Risk", "Market Risk", "Counter-party Risk"],
    "correct_answer": "Liquidity Risk"
},
{
    "question": "Bank's Assets Liabilities Management Committee (ALCO) makes the assessment of",
    "options": ["Liquidity Risk", "Credit Risk", "Operations risk", "Reputational Risk", "Legal Risk"],
    "correct_answer": "Liquidity Risk"
},
{
    "question": "NSFR is a ratio of two factors, ASF and RSF. What RSF denotes?",
    "options": ["Requested stable funding", "Regulatory stable funding", "Required stable funding",
                "Required security funding", "Regulatory security funding"],
    "correct_answer": "Required stable funding"
},
{
    "question": "A bank has failed to meet its obligation on account of a payment on due date to its incapacity to pay. What kind of risk it is:",
    "options": ["Credit Risk", "Liquidity Risk", "Settlement Risk", "Payment Risk", "Reputation Risk"],
    "correct_answer": "Settlement Risk"
},
{
    "question": "Which of the following is not a function of ALCO",
    "options": ["To fix interest rate on all deposit products, fix Base rate and recommend BPLR for loan asset products",
                "To identify the ALM risk associated with the Bank's exposure and appropriate risk measurement methodology for capturing the ALM risk",
                "To determine, advise and guide on appropriate hedging for mismatches",
                "To fix interest rate on loans and advances based on credit rating",
                "To formulate/review methodologies, behavioural studies, stress testing scenarios for management of Interest Rate Risk, Liquidity Risk of all Branches"],
    "correct_answer": "To fix interest rate on loans and advances based on credit rating"
},
{
    "question": "Which of the following is not the main objective of ALM in the Bank?",
    "options": ["To protect or enhance the market value of net worth",
                "To increase Net Interest Income (NII)",
                "To protect the economic value of the assets held by bank",
                "To maintain or protect spreads or Net Interest Margin (NIM)",
                "All are objectives of ALM"],
    "correct_answer": "To protect the economic value of the assets held by bank"
},
{
    "question": "Treasury bills or T-bills, which are money market instruments, are short term debt instruments issued by the Government of India. Which of the following is not a tenor of such instruments?",
    "options": ["91", "182", "364", "365", "Both B&D"],
    "correct_answer": "365"
},
{
    "question": "Performance of the Bonds in the financial market are analysed by using Yield to Maturity (YTM). What does it mean from investor point of view?",
    "options": ["Present value of the bond", "Future value of the bond", "Bond's internal rate of return",
                "Present Value of Market Return", "Total income from the bond over a period of one year"],
    "correct_answer": "Bond's internal rate of return"
},
{
    "question": "Treasury bonds are exposed to additional risk which are",
    "options": ["Reinvestment Risk", "Interest rate Risk", "Investment Risk", "Both A&B", "All A,B and C"],
    "correct_answer": "Both A&B"
},
{
    "question": "Commodity risk does not arise from …...........",
    "options": ["Cash", "Gold", "Silver", "Oil", "Commodity derivative"],
    "correct_answer": "Cash"
},
{
    "question": "Which of the following are not considered as market exposure for market risk management?",
    "options": ["Investment in SLR securities", "Exposure in equity", "Forex trading business",
                "Commodities trading Business", "Credit underwriting"],
    "correct_answer": "Credit underwriting"
},
{
    "question": "Which of the following does not come under Interest Rate Risk?",
    "options": ["Embedded option risk", "Yield curve risk", "Reinvestment risk", "Basis risk", "Currency risk"],
    "correct_answer": "Currency risk"
},
{
    "question": "Immediate or short-term effect of changes in interest rates is on the Bank's earnings through Net Interest Income and is called as ….......... Select one",
    "options": ["Interest perspective", "Profit perspective", "Short term perspective", 
                "Earning perspective", "Security perspective"],
    "correct_answer": "Earning perspective"
},
{
    "question": "Long term impact of changes in interest rate is on Bank's Market Value of Equity (MVE) or Net Worth, as reduction in net interest earnings directly affects the profit and hence the amount that would be ploughed back would come down. This is called …............. Select one",
    "options": ["Interest perspective", "Profit perspective", "Short term perspective",
                "Economic value perspective", "Earning perspective"],
    "correct_answer": "Economic value perspective"
},
{
    "question": "The risk of change in value of assets lying in the trading book being affected by changes in stock prices, stock index prices, etc.",
    "options": ["Foreign Exchange Risk", "Interest rate Risk", "Stock Market Risk", "Equity Risk", "Commodity Risk"],
    "correct_answer": "Equity Risk"
},
{
    "question": "…………….. risk is the potential loss due to change in the value of a bank's assets or liabilities resulting from foreign exchange rate fluctuations.",
    "options": ["Interest Rate", "Equity", "Foreign Exchange", "Commodity", "None of the above"],
    "correct_answer": "Foreign Exchange"
},
{
    "question": "Which of the following is not a category of trading instrument",
    "options": ["Held till Maturity", "Available for sale", "Held for Trading", "Held for Selling", "Both B&D"],
    "correct_answer": "Held for Selling"
},
{
    "question": "Which of the following is not a type of market risk?",
    "options": ["Interest rate risk", "Exchange rate risk", "Equity risk", "Commodity risk", "Liquidity risk"],
    "correct_answer": "Liquidity risk"
},
{
    "question": "You have bought USD 1000 @ 82 and selling the same at 81 the net profit or loss is",
    "options": ["Profit of 1000", "loss of 1000", "profit of 100", "loss of 100", "profit of 10000"],
    "correct_answer": "loss of 1000"
},
{
    "question": "Treasury operations in the bank are of voluminous and complex in nature and any small amount of error may result in huge loss to bank. Hence, treasury functions are segregated in three distinct sections with defined set of responsibility. With reference to Dealing Room / Front Office responsibility, choose most appropriate response from the given options.",
    "options": ["Calculating VaR for Market Risk", "Managing investment for bank", "Risk-Return Analysis",
                "Deal Slip verification", "Accounting"],
    "correct_answer": "Managing investment for bank"
},
{
    "question": "Mark-to-Market system is used by bank to arrive profit or loss from investment held or available for training on a particular date. The profit or loss for a particular investment in Mark-to-Market system is the difference between",
    "options": ["Market price and Face Value", "Acquiring cost and Market Price", "Market price and Book Value",
                "Investment price and Book Value", "Face value and book value"],
    "correct_answer": "Market price and Book Value"
},
{
    "question": "Interest Rate Risk is a type of:",
    "options": ["Market Risk", "Credit Risk", "Operational Risk", "Systemic Risk", "Liquidity Risk"],
    "correct_answer": "Market Risk"
},
{
    "question": "As per Basel-III, the Risk of losses in on-balance sheet and off-balance sheet positions arising from movements in market prices is called:",
    "options": ["Credit Risk", "Market Risk", "Pricing Risk", "Liquidity Risk", "Settlement Risk"],
    "correct_answer": "Market Risk"
},
{
    "question": "Standard measurement method (Duration method and Maturity method) and Internal Model approach are used for which type of risk capital calculation?",
    "options": ["Operational Risk", "Legal Risk", "Market Risk", "Credit Risk", "Liquidity risk"],
    "correct_answer": "Market Risk"
},
{
    "question": "Which department is not reporting to treasury vertical",
    "options": ["Front office", "Back office", "Dealing Room", "Mid office", "Reconciliation Team"],
    "correct_answer": "Mid office"
},
{
    "question": "Market risk management process includes Identification, Measurement, Reporting, …........, Monitoring. Select the correct option",
    "options": ["Investigation", "Listing", "Mitigation", "Elimination", "adulteration"],
    "correct_answer": "Mitigation"
},
{
    "question": "The falling interest rate leads change to bondholder income which is",
    "options": ["More", "less", "No relationship", "same", "Both E&F"],
    "correct_answer": "More"
},
{
    "question": "Which of the following instrument does not contain equity price risk?",
    "options": ["Stock", "Corporate bonds with equity purchase warrants", "Equity derivatives",
                "Assets and liabilities whose cash flow is determined in reference to stock prices, stock indices, etc.",
                "Non convertible debentures"],
    "correct_answer": "Non convertible debentures"
},
{
    "question": "Market discipline supplements regulation as sharing of information facilitates assessment of the bank by others, including investors, analysts, customers, other banks and rating agencies. When market participants have a sufficient understanding of bank's activities, they are better able to",
    "options": ["Distinguish between banking organizations on based of performance",
                "Reward those banks who manage their risk prudently",
                "Penalize those banks who don't manage their risk prudently",
                "Option a and b are correct",
                "Option a, b and c are correct"],
    "correct_answer": "Option a, b and c are correct"
},
{
    "question": "When the interest rate sensitive assets (RSA) are more than interest sensitive liabilities (RSL), an increase in the interest rate may impact the Net Interest Income (NII)",
    "options": ["Positively", "Negatively", "Remain unchanged (neutral)", "Cannot be predicted", "None of these"],
    "correct_answer": "Positively"
},
{
    "question": "Which of the following is not part of Market risk management process",
    "options": ["Identification", "Measurement", "Reporting", "Mitigation", "Processing"],
    "correct_answer": "Processing"
},
{
    "question": "Mr. Anil, a Dealer in Treasury Branch of the ABC Bank enters into a Forward Contract for USD 100 million at Rs. 75.32 per USD with M/s. Prime Exporter with a maturity period of 90 days. On maturity date, Spot rate is Rs. 74.15. In this transaction, M/s. Prime Exporter is at losing position, hence it refuses to pay and default its obligations. This will be categorised as which subtype of Credit Risk?",
    "options": ["Bankruptcy Risk", "Downgrade Risk", "Default Risk", "Settlement Risk", "Market Risk"],
    "correct_answer": "Settlement Risk"
},
{
    "question": "The risk of adverse movement in the price of individual security resulting from factors related to the security's issuer is called …......... Select one",
    "options": ["Issuer risk", "Specific risk", "General market risk", "Individual risk", "Security risk"],
    "correct_answer": "Specific risk"
},
{
    "question": "Under Basel-III, which of the followings is an approach to calculate Market Risk",
    "options": ["Standardized Approach", "Internal Model Approach", "Basic Indicator Approach",
                "Option a & c are correct", "Option a & b are correct"],
    "correct_answer": "Standardized Approach"
},
{
    "question": "The maximum movement of rate against the position held, so as to trigger the limit or around maximum loss limit for adverse movement of rates is known",
    "options": ["daylight Limit", "Intraday limit", "Stoploss Limit", "Overnight Limit", "Gap Limit"],
    "correct_answer": "Stoploss Limit"
},
{
    "question": "For ILM(Internal loss multiplier) calculation loss component shall be based on …....... Years of high quality of operational risk loss data.",
    "options": ["10", "11", "12", "13", "15"],
    "correct_answer": "10"
},
{
    "question": "Bank has fixed a threshold limit of Rs…............. For Operational risk loss data collection?",
    "options": ["100", "1,000", "10,000", "1,00,000", "5,000"],
    "correct_answer": "10,000"
}
        
    ]
        
        # Initialize session states if not exists
        if 'initialized' not in st.session_state:
            self.initialize_session_state()

    def initialize_session_state(self):
        st.session_state.initialized = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.session_state.question_states = {}  # Store state for each question
        st.session_state.start_time = datetime.now()
        st.session_state.total_time = 3600  # 1 hour in seconds
        
        # Initialize question states
        for i in range(len(self.quiz_data)):
            st.session_state.question_states[i] = {
                'answered': False,
                'selected_answer': None,
                'is_correct': False,
                'time_spent': 0
            }

    def set_question(self, question_number):
        st.session_state.current_question = question_number

    def next_question(self):
        if st.session_state.current_question < len(self.quiz_data) - 1:
            st.session_state.current_question += 1

    def prev_question(self):
        if st.session_state.current_question > 0:
            st.session_state.current_question -= 1

    def navigate_questions(self):
        # Create a grid of question numbers for navigation
        st.write("Question Navigator:")
        cols = st.columns(10)  # 10 questions per row
        for i in range(len(self.quiz_data)):
            with cols[i % 10]:
                # Color code based on question state
                if st.session_state.question_states[i]['answered']:
                    button_color = '🟢' if st.session_state.question_states[i]['is_correct'] else '🔴'
                else:
                    button_color = '⚪'
                
                # Create button for each question
                if st.button(f"{button_color} {i + 1}", key=f"nav_{i}"):
                    self.set_question(i)

    def display_timer(self):
        elapsed_time = (datetime.now() - st.session_state.start_time).total_seconds()
        remaining_time = max(0, st.session_state.total_time - elapsed_time)
        
        # Format time display
        mins, secs = divmod(int(remaining_time), 60)
        hours, mins = divmod(mins, 60)
        
        # Display timer with conditional formatting
        if remaining_time > 300:  # More than 5 minutes
            st.markdown(f"### ⏱️ Time Remaining: {hours:02d}:{mins:02d}:{secs:02d}")
        else:
            st.markdown(f"### ⚠️ Time Remaining: {hours:02d}:{mins:02d}:{secs:02d}")

    def run(self):
        st.title("U Aspire Quiz")
        
        # Display timer
        self.display_timer()
        
        # Jump to question input at top
        col1, col2 = st.columns([3, 1])
        with col1:
            new_question = st.number_input(
                "Go to Question Number:",
                min_value=1,
                max_value=len(self.quiz_data),
                value=st.session_state.current_question + 1
            )
        with col2:
            if st.button("Go to Question"):
                self.set_question(new_question - 1)

        # Display current question
        current_q = st.session_state.current_question
        question = self.quiz_data[current_q]
        
        # Display progress
        st.progress((current_q + 1) / len(self.quiz_data))
        st.write(f"Question {current_q + 1} of {len(self.quiz_data)}")
        
        # Display question
        st.markdown(f"### {question['question']}")
        
        # Get previous answer if it exists
        previous_answer = st.session_state.question_states[current_q]['selected_answer']
        
        # Display options
        selected_option = st.radio(
            "Choose your answer:",
            question['options'],
            index=None if previous_answer is None else question['options'].index(previous_answer)
        )
        
        # Navigation and submit buttons in a row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("⬅️ Previous", disabled=st.session_state.current_question == 0):
                self.prev_question()
                st.rerun()

        with col2:
            if st.button("Submit Answer"):
                if selected_option:
                    # Save answer
                    st.session_state.question_states[current_q]['answered'] = True
                    st.session_state.question_states[current_q]['selected_answer'] = selected_option
                    is_correct = selected_option == question['correct_answer']
                    st.session_state.question_states[current_q]['is_correct'] = is_correct
                    
                    # Update score if not previously answered correctly
                    if is_correct and not st.session_state.question_states[current_q].get('scored', False):
                        st.session_state.score += 1
                        st.session_state.question_states[current_q]['scored'] = True
                    
                    # Show feedback
                    if is_correct:
                        st.success("Correct! 🎉")
                    else:
                        st.error(f"Wrong! The correct answer is: {question['correct_answer']}")
                else:
                    st.warning("Please select an answer before submitting.")

        with col3:
            if st.button("Next ➡️", disabled=st.session_state.current_question == len(self.quiz_data) - 1):
                self.next_question()
                st.rerun()

        with col4:
            if st.button("Finish Quiz"):
                st.session_state.show_results = True
                st.rerun()

        # Display navigation grid
        st.write("---")
        self.navigate_questions()
        
        # Display score
        st.sidebar.markdown(f"### Current Score: {st.session_state.score}/{len(self.quiz_data)}")
        
        # Show results if finished
        if 'show_results' in st.session_state and st.session_state.show_results:
            self.show_results()

    def show_results(self):
        st.markdown("## Quiz Results")
        st.write(f"Final Score: {st.session_state.score} out of {len(self.quiz_data)}")
        percentage = (st.session_state.score / len(self.quiz_data)) * 100
        st.write(f"Percentage: {percentage:.2f}%")
        
        # Show question-wise review
        st.write("---")
        st.markdown("### Question Review")
        for i, question in enumerate(self.quiz_data):
            state = st.session_state.question_states[i]
            if state['answered']:
                status = "✅" if state['is_correct'] else "❌"
                selected = state['selected_answer']
                correct = question['correct_answer']
                st.markdown(f"{status} **Question {i+1}**: {question['question']}")
                st.write(f"Your answer: {selected}")
                if not state['is_correct']:
                    st.write(f"Correct answer: {correct}")
            else:
                st.markdown(f"⚪ **Question {i+1}**: Not attempted")
        
        if st.button("Restart Quiz"):
            self.initialize_session_state()
            st.rerun()

def main():
    st.set_page_config(page_title="Quiz Application", layout="wide")
    quiz = QuizApp()
    quiz.run()

if __name__ == "__main__":
    main()