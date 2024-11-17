import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
    {
        "question": "What shall be the delegated authority for Adhoc proposals falling under low priority area?",
        "options": ["Respective Delegatee", "Next Higher Authority", "Minimum RLCC-I", "Minimum-ZLCC", "Minimum CAC-III"],
        "correct_answer": "Next Higher Authority"
    },
    {
        "question": "In case of CRE proposals, advance from customers up to",
        "options": ["5%", "7.50%", "10%", "15%", "20%"],
        "correct_answer": "10%"
    },
    {
        "question": "As per CVC guidelines, the takeover norms should also apply where the borrower comes to another bank after closing account with the previous bank. However, the prescription shall be applicable to accounts which",
        "options": ["6 months", "3 months", "1 month", "12 months", "18 months"],
        "correct_answer": "3 months"
    },
    {
        "question": "For Accounts/ limits rated as CR-6 to CR-10, delegation for Excess over Limit shall be with ……..?",
        "options": ["RLCC-I & above", "ZLCC & above", "CAC-III & above", "Next Higher Authority", "Respective Delegation"],
        "correct_answer": "ZLCC & above"
    },
    {
        "question": "In case higher authority does not communicate decision within …..... days of receipt of F-1 statement, such excess/TODs allowed shall be construed as",
        "options": ["45 Days", "15 Days", "30 Days", "10 Days", "60 days"],
        "correct_answer": "45 Days"
    },
    {
        "question": "In case a party is enjoying an exposure of Rs.40 Crores, which includes TL of Rs.10 Crores, CC of Rs.10 Crores, LC of Rs.10 Crores, BG of Rs.10 Crores, how much maximum Adhoc can be",
        "options": ["Rs. 5 Crores", "Rs. 10 Crores", "Rs. 7.5 Crores", "Rs. 4 Crores", "Rs. 20 Crores"],
        "correct_answer": "Rs. 5 Crores"
    },
    {
        "question": "What is the minimum FACR requirement for CRE Proposals?",
        "options": ["100%", "120%", "150%", "200%", "250%"],
        "correct_answer": "150%"
    },
    {
        "question": "What is the minimum margin stipulated for CRE proposals?",
        "options": ["10%", "13%", "35%", "20%", "25%"],
        "correct_answer": "35%"
    },
    {
        "question": "Loan to MSEs up to Rs……. are to be mandatorily covered under CGTMSE and the permission of regional head is required in case",
        "options": ["Rs.10 lakhs", "Rs.20 lakhs", "Rs.25 lakhs", "Rs.30 lakhs", "Rs.35 lakhs"],
        "correct_answer": "Rs.25 lakhs"
    },
    {
        "question": "What shall be the classification of a business unit when the Turnover is Rs.600 lakhs?",
        "options": ["Micro Enterprise", "Small Enterprise", "Medium Enterprise", "Corporate", "Tiny Enterprise"],
        "correct_answer": "Small Enterprise"
    },
    {
        "question": "What is the minimum collateral requirement for loans given for construction of Educational?",
        "options": ["10%", "50%", "25%", "40%", "No such minimum stipulation"],
        "correct_answer": "50%"
    },
    {
        "question": "What is FLDG in relation to Digital Lending?",
        "options": ["Future Loss Demand", "First Loss Default Guarantee", "First Loss Digital Guarantee", 
                   "Future Loss Digital", "Future Loss Domestic"],
        "correct_answer": "First Loss Default Guarantee"
    },
    {
        "question": "If applications in respect of SCs/STs or export advances are to be rejected, the same should be done at the ………….instead of",
        "options": ["ZLCC level", "Next Higher Level", "CAC-III & above", "CAC-II & above", "CAC-I & above"],
        "correct_answer": "Next Higher Level"
    },
    {
        "question": "What shall be the delegated authority for Adhoc proposals falling under low priority area?",
        "options": ["Respective Delegatee", "Next Higher Authority", "Minimum RLCC-I", "Minimum-ZLCC", "Minimum CAC-III"],
        "correct_answer": "Next Higher Authority"
    },
    {
        "question": "In case of CRE proposals, advance from customers up to",
        "options": ["5%", "7.50%", "10%", "15%", "20%"],
        "correct_answer": "10%"
    },
    {
        "question": "As per CVC guidelines, the takeover norms should also apply where the borrower comes to another bank after closing account with the previous bank. However, the prescription shall be applicable to accounts which",
        "options": ["6 months", "3 months", "1 month", "12 months", "18 months"],
        "correct_answer": "3 months"
    },
    {
        "question": "For Accounts/ limits rated as CR-6 to CR-10, delegation for Excess over Limit shall be with ……..?",
        "options": ["RLCC-I & above", "ZLCC & above", "CAC-III & above", "Next Higher Authority", "Respective Delegation"],
        "correct_answer": "ZLCC & above"
    },
    {
        "question": "In case higher authority does not communicate decision within …..... days of receipt of F-1 statement, such excess/TODs allowed shall be construed as",
        "options": ["45 Days", "15 Days", "30 Days", "10 Days", "60 days"],
        "correct_answer": "45 Days"
    },
    {
        "question": "In case a party is enjoying an exposure of Rs.40 Crores, which includes TL of Rs.10 Crores, CC of Rs.10 Crores, LC of Rs.10 Crores, BG of Rs.10 Crores, how much maximum Adhoc can be",
        "options": ["Rs. 5 Crores", "Rs. 10 Crores", "Rs. 7.5 Crores", "Rs. 4 Crores", "Rs. 20 Crores"],
        "correct_answer": "Rs. 5 Crores"
    },
    {
        "question": "What is the minimum FACR requirement for CRE Proposals?",
        "options": ["100%", "120%", "150%", "200%", "250%"],
        "correct_answer": "150%"
    },
    {
        "question": "What is the minimum margin stipulated for CRE proposals?",
        "options": ["10%", "13%", "35%", "20%", "25%"],
        "correct_answer": "35%"
    },
    {
        "question": "Loan to MSEs up to Rs……. are to be mandatorily covered under CGTMSE and the permission of regional head is required in case",
        "options": ["Rs.10 lakhs", "Rs.20 lakhs", "Rs.25 lakhs", "Rs.30 lakhs", "Rs.35 lakhs"],
        "correct_answer": "Rs.25 lakhs"
    },
    {
        "question": "What shall be the classification of a business unit when the Turnover is Rs.600 lakhs?",
        "options": ["Micro Enterprise", "Small Enterprise", "Medium Enterprise", "Corporate", "Tiny Enterprise"],
        "correct_answer": "Small Enterprise"
    },
    {
        "question": "What is the minimum collateral requirement for loans given for construction of Educational?",
        "options": ["10%", "50%", "25%", "40%", "No such minimum stipulation"],
        "correct_answer": "50%"
    },
    {
        "question": "What is FLDG in relation to Digital Lending?",
        "options": ["Future Loss Demand", "First Loss Default Guarantee", "First Loss Digital Guarantee", 
                   "Future Loss Digital", "Future Loss Domestic"],
        "correct_answer": "First Loss Default Guarantee"
    },
    {
        "question": "If applications in respect of SCs/STs or export advances are to be rejected, the same should be done at the ………….instead of",
        "options": ["ZLCC level", "Next Higher Level", "CAC-III & above", "CAC-II & above", "CAC-I & above"],
        "correct_answer": "Next Higher Level"
    },
    {
        "question": "Which of the following facility shall not rank for reckoning in aggregate fund/non fund based",
        "options": ["Term loan", "Cash Credit", "Letter of Credit", "Bill Discounting under LC", "Bank Guarantee"],
        "correct_answer": "Bill Discounting under LC"
    },
    {
        "question": "A proposal of Rs.40 Crore is falling under the delegation of ZLCC. However, the activity is falling under Low Priority Area.",
        "options": ["MCB", "ZLCC only", "CAC-II", "CAC-III", "CAC-I"],
        "correct_answer": "ZLCC only"
    },
    {
        "question": "What should be the door to door tenor of loan for single construction housing or commercial projects without any",
        "options": ["1 Year", "2 Years", "3 Years", "5 Years", "7 Years"],
        "correct_answer": "3 Years"
    },
    {
        "question": "Up to what percentage of soft cost is permitted to include in the total project cost as per margin norms to Commercial",
        "options": ["Soft costs are financed up to 20% of the total project cost", 
                   "Soft costs are financed up to 10% of the total project cost",
                   "Cost will include 100% of both the Hard and Soft costs",
                   "Soft costs are financed up to 15% of the total project cost",
                   "Soft costs are financed up to 25% of the total project cost"],
        "correct_answer": "Soft costs are financed up to 20% of the total project cost"
    },
    {
        "question": "Working capital requirement under Real estate project is",
        "options": ["Turnover method", "Cash Budget Method", "Net owned Fund Method", "FBF Method", "Any of the above"],
        "correct_answer": "Cash Budget Method"
    },
    {
        "question": "Total Real Estate exposure is restricted up to…...of total",
        "options": ["20%", "14%", "30%", "7%", "No such Restriction"],
        "correct_answer": "30%"
    },
    {
        "question": "In Integrated housing projects, the Commercial area in the residential housing project does not exceed …..... of the total Floor Space Index (FSI) of the",
        "options": ["5%", "10%", "15%", "20%", "25%"],
        "correct_answer": "10%"
    },
    {
        "question": "What is the minimum and maximum marks deduction for staff misbehavior complaints in the Grievance Redressal & Service Requests",
        "options": ["1,5", "0.5, 4", "0.25,3", "1,4", "0.5, 5"],
        "correct_answer": "0.5, 4"
    },
    {
        "question": "The target set for the number of feedback/suggestions to be received as ------% of the active customer base per",
        "options": ["4", "5", "2", "1", "10"],
        "correct_answer": "1"
    },
    {
        "question": "Which of the following is the initiative taken by our Bank for offering real-time assistance regarding products",
        "options": ["Union sampark", "CRM EDGE", "Union Disha", "My diary portal", "UPI portal"],
        "correct_answer": "Union sampark"
    },
    {
        "question": "Our Bank launched a performance recognition drive exclusively for ---------------------from 1st June to 30th September 2024. What is the",
        "options": ["Currency chest, Currency Performers - 2024", 
                   "Currency chest, Mudra se Munafa - 2024",
                   "Branch, Currency to Profit - 2024",
                   "Branch, Mudra Shakti - 2024",
                   "None of the above"],
        "correct_answer": "Currency chest, Mudra se Munafa - 2024"
    },
    {
        "question": "For offering hassle free customer service and to resolve customer query regarding cheque book status at the Branch level, our Bank has made cheque book dispatch details available in …….menu in Finacle.",
        "options": ["A. HCHBM Only", "Only B is correct", "A and B are correct", "All are correct", "Only A"],
        "correct_answer": "A and B are correct"
    },
    {
        "question": "Under Right to Transparency, Fair and Honest Dealing, it is mandatory to give ______ days prior notice to its customer before implementing any change with respect to discontinuation of products, Relocation of their offices",
        "options": ["30 days", "45 days", "15 days", "60 days", "90 days"],
        "correct_answer": "30 days"
    },
    {
        "question": "What is the turn-around time (TAT) for cases involving loss or damage to property documents, and what penalty applies if the process exceeds",
        "options": ["15 days plus an additional 30 days; penalty applies beyond 45 days",
                   "30 days plus an additional 15 days; penalty applies beyond 45 days",
                   "30 days plus an additional 30 days; penalty applies beyond 60 days",
                   "45 days plus an additional 30 days; penalty applies beyond 75 days",
                   "15 days plus an additional 45 days; penalty applies beyond 30 days"],
        "correct_answer": "30 days plus an additional 30 days; penalty applies beyond 60 days"
    },
    {
        "question": "What is the bank's liability in case of locker, incidents such as fire, theft, burglary, robbery, dacoity, and building collapse due to its own",
        "options": ["An amount equivalent to one hundred times the prevailing annual rent of the locker",
                   "An amount equal to the value of the lost or damaged locker",
                   "No liability in such cases",
                   "An amount equivalent to the insurance coverage of the locker",
                   "None of the above"],
        "correct_answer": "An amount equivalent to one hundred times the prevailing annual rent of the locker"
    },
    {
        "question": "Which of the following statement is correct with respect to RB-IOS scheme 2021? A) There is no limit on the amount in a dispute that can be brought before ombudsman. B) There is limitation of dispute amount maximum Rs 20 lacs. C) For any consequential loss suffered by complainant the ombudsman can provide a compensation up to Rs 20 lacs. D) Additional",
        "options": ["Only A and C are correct", "Only A and D are correct", "Only C and D are correct",
                   "A, C and D are correct", "All are correct"],
        "correct_answer": "A, C and D are correct"
    },
    {
        "question": "Which of the following is/are responsibilities of the Regional Grievance Redressal Officer (GRO)?",
        "options": ["A, B and D are correct", "A and D are correct", "B, C and D are correct",
                   "B and D are correct", "All are correct"],
        "correct_answer": "A, B and D are correct"
    },
    {
        "question": "A customer having account in base branch A approaches your branch and wants to register a complain against branch A at your branch.",
        "options": ["Tell the customer to register complaint at Branch A",
                   "Take the complaint and register in CRM Edge",
                   "Take the complaint and mail it to Branch",
                   "Take the complaint and register in Union Samadhan portal",
                   "None of the above"],
        "correct_answer": "Take the complaint and register in CRM Edge"
    },
    {
        "question": "Within how many days should the bank dispose of the claim if all papers are in order and within the delegated powers",
        "options": ["15 days", "5 days", "2 days", "7 days", "10 days"],
        "correct_answer": "2 days"
    },
    {
        "question": "A joint deposit account is maintained by a bank in the name of Mr. Khursheed and Mr Hamid and operation in the account are as joint operations. They have also nominated Mr. Azad as nominee in the account. On death of Mr. Khursheed, his",
        "options": ["Survivor will get the payment",
                   "Survivor and nominee will get the payment",
                   "Nominee will get the payment",
                   "Legal heirs and survivor will get the payment jointly",
                   "Nominee and survivor will get the payment"],
        "correct_answer": "Legal heirs and survivor will get the payment jointly"
    },
    {
        "question": "What is the minimum value of original works for which a contract may be awarded on",
        "options": ["40 lacs", "20 lacs", "1 crore", "2 crores", "50 lacs"],
        "correct_answer": "2 crores"
    },
    {
        "question": "How should records that are more than three years old be",
        "options": ["As current records", "As old records", "As outdated records", "As historical records", "As bank records"],
        "correct_answer": "As old records"
    },
    {
        "question": "What is the deadline for submitting the ATM cash-out report to the RBI's Issue",
        "options": ["1st day of the succeeding month", 
                   "3rd day of the succeeding month",
                   "5th day of the succeeding month",
                   "7th day of the succeeding month",
                   "10 days of the succeeding month"],
        "correct_answer": "5th day of the succeeding month"
    },
    {
        "question": "Which of the following is NOT a feature of Bhavishya?",
        "options": ["Integration with Digilocker", 
                   "Self-filling of pension form by",
                   "Real-time Updates via",
                   "Manual pension calculation",
                   "None of the above"],
        "correct_answer": "Manual Pension"
    },
    {
        "question": "Which of the following initiatives has the Reserve Bank of India launched to streamline the process of",
        "options": ["FinTech Repository", 
                   "Retail Direct Mobile App",
                   "EmTech Repository",
                   "PRAVAAH Portal",
                   "None of the above"],
        "correct_answer": "PARVAAH portal"
    },
    {
        "question": "For a Corporate Agent [Composite], what is the maximum total number of arrangements with life,",
        "options": ["27", "21", "24", "9", "18"],
        "correct_answer": "27"
    },
    {
        "question": "To assess the quality of customer service delivery across the regions and the zones,the ranking of RO and ZO is now being introduced.For RO ranking total marks 100 : The weighted average score will",
        "options": ["50,75", "75,50", "25,50", "50,50", "50,25"],
        "correct_answer": "75,50"
    },
    {
        "question": "Under centralized sending of overdue Locker notices recently adopted by our bank, which of the statement is incorrect",
        "options": ["A,B and C are correct", 
                   "A and B are correct",
                   "C) A,B and D are correct",
                   "None of these",
                   "All are correct"],
        "correct_answer": "All are correct"
    },
    {
        "question": "As per the latest guidelines on Default Loss Guarantee (DLG) in digital lending, lenders shall invoke DLG within a maximum Overdue period of",
        "options": ["360 days", "90 days", "120 days", "180 days", "45 days"],
        "correct_answer": "120 days"
    },
    {
        "question": "Which of the following statements with respect to Short Term Bank Deposit (STBD) of Gold under Revamped Gold Deposit Scheme (R-GDS)-2021 is not",
        "options": ["The period of deposits can be for a period of 1-3 years",
                   "Interest in respect of STBD shall be denominated and paid in Indian Rupee only",
                   "Redemption of principal at maturity will, at the option of depositor, be either in Indian",
                   "Any premature redemption shall be in Indian Rupee equivalent or gold at the",
                   "The deposits will be outside the purview of CRR & SLR requirements"],
        "correct_answer": "The deposits will be outside the purview of CRR & SLR requirements"
    },
    {
        "question": "Limitation period for filing the complaint (Within how many days) under Copra 2019 is?",
        "options": ["Within two years from the date on which the cause of action has arisen or deficiency in",
                   "Within three years from the date on which the cause of action has arisen",
                   "Within 3 months from the date on which the cause of action has arisen or",
                   "Within 30 days from the date on which the cause of action has arisen or",
                   "Within 60 days from the date on which the cause of action has arisen or"],
        "correct_answer": "within two years from the date on which the cause of action has arisen or deficiency in"
    },
    {
        "question": "Which of the following statement with respect to e-Rupi is not true?",
        "options": ["e-RUPI is a one-time/multiple use digital solution to facilitate cashless payment which is person & purpose specific solutions",
                   "e-RUPI can be issued only by banks authorized by RBI to issue PPIs and members of UPI",
                   "Maximum limit of per e-RUPI voucher shall not exceed INR 100,000 for government schemes and Up",
                   "E-RUPI is operated with UPI infrastructure",
                   "e-RUPI shall also be permitted for cash out or cash back on redemption"],
        "correct_answer": "e-RUPI shall also be permitted for cash out or cash back on redemption"
    },
    {
        "question": "All payment transactions using RTGS/NEFT of value of Rs and above undertaken by individuals should include remitter and",
        "options": ["Rs. 50 crore", "Rs. 25 crore", "Rs. 100 crore", "Rs. 5 crore", "Rs. 15 crore"],
        "correct_answer": "Rs. 5 crore"
    },
    {
        "question": "Under 'Long Term Repo Operations (LTROs)' a bank can borrow from RBI against the government securities or with similar collaterals for",
        "options": ["3 months to 1 years", "6 months to 3 years", "1 year to 3 years", "1 year to 5 years", "1 year to 2 years"],
        "correct_answer": "1 year to 3 years"
    },
    {
        "question": "The type of risk in which a Single bank's failure may cause collapse of whole Banking System and result",
        "options": ["Strategic Risk", "Herstatt Risk", "Systemic Risk", "Market risk", "Reputation Risk"],
        "correct_answer": "Systemic Risk"
    },
    {
        "question": "Under Basel III, what is the Leverage Ratio, Banks in India have to maintain as per RBI",
        "options": ["4% for Domestic Systemically Important Banks",
                   "3.5% for Domestic Systemically",
                   "3.5% for all banks",
                   "3.0% for Domestic Systemically",
                   "4% for all banks"],
        "correct_answer": "4% for Domestic Systemically Important Banks"
    },
    {
        "question": "'Per drop More crop' is a water conservation programme with Micro Irrigation and other",
        "options": ["Pradhan Mantri Rural Development Mission",
                   "Pradhan Mantri Krishi Sinchayee Yojana",
                   "Pradhan Mantri Krishi Seva Yojana",
                   "Pradhan Mantri Krishi Sampada Yojana",
                   "Har Ghar Nal se Jal (tap water to all households)"],
        "correct_answer": "Pradhan Mantri Krishi Sinchayee Yojana"
    },
    {
        "question": "Bank credit to registered NBFCs –MFIs and other MFIs for on- lending will be eligible for classification as priority sector under respective",
        "options": ["₹ 10 lakh per borrower",
                   "₹ 20 lakh per borrower",
                   "No Maximum limit",
                   "₹ 15 lakh per borrower",
                   "₹ 40 lakh per borrower"],
        "correct_answer": "No Maximum limit"
    },
    {
        "question": "As per the latest RBI guidelines, A 'microfinance loan' is defined as a collateral-free loan given to a household having annual household",
        "options": ["₹ 5,00,000", "₹ 2,00,000", "₹ 3,00,000", "₹ 1,00,000", "₹ 1,60,000"],
        "correct_answer": "₹ 3,00,000"
    },
    {
        "question": "PM Vishwakarma scheme aims to strengthen and nurture the family-based practice of traditional skills by artisans and crafts people working with their hands and tools. The scheme",
        "options": ["15", "16", "17", "18", "19"],
        "correct_answer": "18"
    },
    {
        "question": "As per THE RERA ACT, 2016, a builder or developer needs to register the project with Real Estate Regulatory Authority",
        "options": ["Number of apartments is more than 8 or the total area",
                   "Number of apartments is more than 10 or the total area",
                   "Number of apartments is more than 8 or the total area",
                   "Number of apartments is more than 10 or the total area",
                   "Number of apartments is more than 15 or the total area"],
        "correct_answer": "Number of apartments is more than 8 or the total area"
    },
    {
        "question": "Which of the following education loan subsidy scheme for OBC and others which is created by merging National Fellowship for OBC & Dr. Ambedkar Central Sector Scheme of Interest Subsidy on Educational Loans for Overseas Studies for Other",
        "options": ["Vidya Jyothi", "Nav Bharath", "SHREYAS", "UDDIPAN", "Vidhya Lakshmi"],
        "correct_answer": "SHREYAS"
    },
    {
        "question": "As per the new foreign trade policy (FTP-2023), a three start export house is the one which has export performance upto",
        "options": ["500 million USD", "50 million USD", "100 million USD", "15 million USD", "20 million USD"],
        "correct_answer": "50 million USD"
    },
    {
        "question": "Gross NPA of our bank as on 30.06.2024 stood at Rs.",
        "options": ["41,432", "42,134", "41,423", "41,324", "42,324"],
        "correct_answer": "41,423"
    },
    {
        "question": "PCR of our bank as on",
        "options": ["92.69", "93.49", "92.54", "92.49", "93.69"],
        "correct_answer": "93.49"
    },
    {
        "question": "Net profit of our bank as on 30.06.2024 stood at Rs.",
        "options": ["3,311", "3,569", "3,679", "3,590", "3,611"],
        "correct_answer": "3,679"
    },
    {
        "question": "Total slippages of our bank for FY 23-24 was Rs.",
        "options": ["11,877", "11,878", "11,788", "11,778", "11,677"],
        "correct_answer": "11,877"
    },
    {
        "question": "SARFAESIA is expanded as",
        "options": ["Securitization and Recompositing of Financial Assets and Enforcement of Securities Interest",
                   "Securitization and Reconstruction of Financial Assets and Enforcement of Securities Interest",
                   "Securitization and Reconstruction of Financial Amount and Enforcement of Securities Interest",
                   "Securitization and Reconstruction of Financial Assets and Encroachment of Securities Interest",
                   "Securitization and Reconstruction of Financial Accounts and Enforcement of Securities Interest"],
        "correct_answer": "Securitization and Reconstruction of Financial Assets and Enforcement of Securities Interest"
    },
    {
        "question": "CPA is mandatory for accounts with aggregate credit limits of Rs.",
        "options": ["100 lakh & above", "10 lakh & above", "50 lakh & above", "25 lakh & above", "30 lakh & above"],
        "correct_answer": "100 lakh & above"
    },
    {
        "question": "What has been stipulated regarding periodicity of inspection of collateral security in the form of fixed assets?",
        "options": ["Quarterly", "Monthly", "Half-Yearly", "Annually", "Once in 3 Years"],
        "correct_answer": "Annually"
    },
    {
        "question": "Monitoring action points such as; whether stock/sales/purchases register maintained, whether free access/no lien letter obtained, whether bank's padlock affixed, whether insurance policies are adequate & in force etc. are part of which",
        "options": ["MSOD", "Q-4", "QPR", "MCMR", "F-1"],
        "correct_answer": "Q-4"
    },
    {
        "question": "Total limit availed by a borrower is Rs.6 crores w/w adhoc limit of Rs.1 crore. The MCMR will be sent to",
        "options": ["ZO", "CO", "Branch itself", "RO", "MLP"],
        "correct_answer": "RO"
    },
    {
        "question": "What is the periodicity of review/renewal of proposals under restructuring rated as CR",
        "options": ["18 months", "Half yearly", "Quarterly", "Annually", "Monthly"],
        "correct_answer": "Annually"
    },
    {
        "question": "Which of the following monitoring tools comments on production capacity, method of valuation, correct DP, acceptability level of inventory",
        "options": ["Stock & Book debts Statement", "Q 4", "Stock Audit Report", "MCMR", "Legal Audit Compliance"],
        "correct_answer": "Stock Audit Report"
    },
    {
        "question": "Under EASE agenda, MOF has advised to appoint ASM for large credit exposure of _____ and exposure of a specialized",
        "options": ["Above Rs.100 Crores", "Rs.150 Crores & above", "Above Rs.250 Crores", 
                   "Rs.50 Crores & above", "Above Rs.200 Crores"],
        "correct_answer": "Above Rs.250 Crores"
    },
    {
        "question": "Monitoring of accounts up to Rs.____ shall be done at the Branch level.",
        "options": ["₹ 10 lakh", "₹ 50 lakh", "₹ 1 crore", "₹ 5 crores", "₹ 2 crores"],
        "correct_answer": "1 crores"
    },
    {
        "question": "Expand CRILC.",
        "options": ["Credit Depository of Information on Large Credits",
                   "Central Repository of Information on Large Credits",
                   "Credit Repository of Information on Large Credits",
                   "Central Repositioning of Information on Credit",
                   "Credit Repositioning of Information on"],
        "correct_answer": "Central Repository of Information on Large Credits"
    },
    {
        "question": "Which of the following is the basis for classification of an account as Special Mention Account (SMA)?",
        "options": ["Non submission of stock statement",
                   "Non renewal of expired credit limit",
                   "Overdue",
                   "Down gradation in credit rating",
                   "Non submission of Book Debt statement"],
        "correct_answer": "Overdue"
    },
    {
        "question": "With reference to the new risk rating of the Regions (RO) based on various credit monitoring parameters, which of the following is the correct",
        "options": ["High Risk: <60", "Medium Risk: 60-75", "Low Risk: >75", "Medium Risk: >75", "None of these"],
        "correct_answer": "High Risk: <60"
    },
    {
        "question": "Any modification in MIS codes of loan accounts above Rs.___ lakh will be done at Centralized Credit Operations Back Office after getting approval from respective credit vertical.",
        "options": ["₹10 lakh", "₹25 lakh", "₹50 lakh", "₹100 lakh", "₹75 lakh"],
        "correct_answer": "₹50 lakh"
    },
    {
        "question": "Which of the following is not an agenda of Asset Quality Management Committee (AQMC) meeting? Choose the most appropriate.",
        "options": ["Stressed Assets", "Review/Renewal", "Quick Mortality", "Credit Monitoring Visit", "Overdue"],
        "correct_answer": "Quick Mortality"
    },
    {
        "question": "Complexity of resolution plan increases in which of the following combinations?",
        "options": ["PSA<SMA<NPA", "SMA<PSA<NPA", "NPA<SMA<PSA", "PSA<NPA<SMA", "All of these"],
        "correct_answer": "PSA<SMA<NPA"
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