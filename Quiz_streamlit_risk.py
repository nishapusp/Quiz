import streamlit as st
import random

class QuizApp:
    def __init__(self):
        self.quiz_data = [
           {
        "question": "The special reports, as far as possible, shall be closed within --- days of submission of the reports.",
        "options": ["30", "60", "90", "70", "50"],
        "correct_answer": "90"
    },
    {
        "question": "ZAO should complete the Special audit within ---- days of assignment.",
        "options": ["30 days", "45 days", "60 days", "90 days", "120 days"],
        "correct_answer": "30 days"
    },
    {
        "question": "What is the submission period for COR of Quarterly Management Audit of Regional Offices?",
        "options": ["30 days", "45 days", "60 days", "90 days", "120 days"],
        "correct_answer": "30 days"
    },
    {
        "question": "What is the compliance period for closing Annual Management Audit (AMA) reports of Regional Offices?",
        "options": ["30 days", "45 days", "60 days", "90 days", "120 days"],
        "correct_answer": "45 days"
    },
    {
        "question": "If the irregularities mentioned in the special audit report are not rectifiable in nature/suspected fraud, Zonal Level Fraud Recommending Committee (ZLFRC) to submit its recommendation to FMG, CO within ----- days from the date of issue of the report for examining the element of fraud, as per Fraud Management (FM) Policy",
        "options": ["30 days", "48 days", "60 days", "90 days", "120 days"],
        "correct_answer": "48 days"
    },
    {
        "question": "What is the maximum period for rectification of irregularities in Flash Reports?",
        "options": ["30 days", "45 days", "50 days", "60 days", "90 days"],
        "correct_answer": "50 days"
    },
    {
        "question": "What is the compliance period for small and medium branches to submit their audit report?",
        "options": ["30 days", "45 days", "60 days", "90 days", "120 days"],
        "correct_answer": "60 days"
    },
    {
        "question": "The details of Special Reports closed by COAC shall be placed before ----- in the form of a statement.",
        "options": ["ACE", "ACB", "ZAC", "RAC", "COAC"],
        "correct_answer": "ACE"
    },
    {
        "question": "Who approves converting Flash Reports into Special Reports in exceptional cases?",
        "options": ["ZH", "RH", "ZAH", "DZH", "CGM/GM, A&I"],
        "correct_answer": "CGM/GM, A&I"
    },
    {
        "question": "In case of Special Audits of branches which are not under the control of Regional Office and in case of Special Audit of RO/ZO/CO Verticals, the same shall be closed by ---?",
        "options": ["ZAO", "RO", "ZO", "COAC", "ACE"],
        "correct_answer": "COAC"
    },
    
{
        "question": "RLPs shall submit their replies and COR to respective Regional Office. Who vets the replies submitted by RLPs?",
        "options": ["ZAO", "RO", "LCV", "CRBD, CO", "A&I"],
        "correct_answer": "CRBD, CO"
    },
    {
        "question": "'B' category branches shall submit their replies and CORs to concerned Regional Office and in respect of Forex Audit to---?",
        "options": ["ZAO", "RO", "ZO", "DFB, CO", "A&I"],
        "correct_answer": "DFB, CO"
    },
    {
        "question": "To whom do Large Corporate Vertical branches submit their replies and COR?",
        "options": ["ZAO", "RO", "LCV", "RAC", "COAC"],
        "correct_answer": "LCV"
    },
    {
        "question": "What is the sanction limit amount for closure of Special Reports by COAC?",
        "options": ["Rs.1.00 crore", "Rs.1.00 crore and above", "Rs.2.00 crore", "Less than Rs.1.00 crore", "More than Rs.2.00 crore"],
        "correct_answer": "Less than Rs.1.00 crore"
    },
    {
        "question": "How often should RAC meetings be conducted to review Special Reports?",
        "options": ["Weekly", "Bi-weekly", "Monthly", "Quarterly", "Annually"],
        "correct_answer": "Monthly"
    },
    {
        "question": "ZO to review the status of Special reports in ZAC on ----- basis and ensure closure of the reports within the prescribed timeline of 90 days by coordinating with the respective ROs/ ZAO.",
        "options": ["Weekly", "Bi-weekly", "Monthly", "Quarterly", "Annually"],
        "correct_answer": "Monthly"
    },
    {
        "question": "MLP shall submit their replies and COR to respective Regional Office. Who vets the replies submitted by MLPs?",
        "options": ["ZAO", "ZO", "LCV", "MSME, CO", "A&I"],
        "correct_answer": "MSME, CO"
    },
    {
        "question": "Staff Training Centers (STCs) shall submit their replies and CORs to Staff College, Bengaluru. The replies so submitted by STCs shall be vetted and countersigned by",
        "options": ["ZAO", "RO", "LCV", "Principal, Staff College", "A&I"],
        "correct_answer": "Principal, Staff College"
    },
    {
        "question": "Extra Large Branches with High Risk Rating shall submit their replies and COR to concerned Regional Offices. The replies so submitted by Branches shall be vetted and countersigned by ----- and shall be submitted to A&I, CO for closure at COAC.",
        "options": ["ZAH", "Zonal Head", "Regional Head", "DRH", "DZH"],
        "correct_answer": "Regional Head"
    },
    {
        "question": "How should Mid Corporate Branches (MCB) submit their replies and COR?",
        "options": ["ZAO", "RO", "MCV", "COAC", "DFB"],
        "correct_answer": "RO"
    },
    {
        "question": "Where are Quarterly Management Audit (QMA) reports of Regional Offices closed?",
        "options": ["COAC", "ZAC", "LCV", "RAC", "COAC"],
        "correct_answer": "ZAC"
    },
    {
        "question": "Annual Management Audit reports of Regional Offices shall be closed by -----",
        "options": ["RH", "ZH", "RAC", "ZAC", "COAC"],
        "correct_answer": "ZAC"
    },
    {
        "question": "Regional Heads along with------ shall interact with Concurrent Auditors at least once in a quarter through personal meetings or web conference.",
        "options": ["ZAHs", "RHs", "ZHs", "DZHs", "DRHs"],
        "correct_answer": "ZAHs"
    },
    {
        "question": "Who is responsible for ensuring closure of Special Reports within the prescribed timelines?",
        "options": ["ZAH", "DRH", "DZH", "ZH / RH", "CGM, A&I"],
        "correct_answer": "ZH / RH"
    },
    {
        "question": "Who shall be responsible for ensuring closure of special Audit within the prescribed timelines?",
        "options": ["ZAO", "RO", "LCV", "A&I", "ZH/RH"],
        "correct_answer": "ZH/RH"
    },
    {
        "question": "The Common Equity Capital requirement for Banks in India is",
        "options": ["11.50%", "9.00%", "7.50%", "8.00%", "5.50%"],
        "correct_answer": "8.00%"
    },
    {
        "question": "Basel-I was the first set of guidelines issued by BCBS which was focused on credit risk. Banks that operate internationally were required to maintain minimum …… of capital on percent of risk weighed assets.",
        "options": ["7.00%", "9.00%", "6.00%", "11.00%", "8.00%"],
        "correct_answer": "8.00%"
    },
    {
        "question": "Minimum Regulatory Capital for Banks in India is",
        "options": ["9.00%", "11.50%", "7.50%", "8.00%", "5.50%"],
        "correct_answer": "11.50%"
    },
    {
        "question": "Internal capital adequacy assessment process (ICAAP) and Supervisory review and evaluation process (SREP) are part of …....... Pillar of Basel 3?",
        "options": ["1", "2", "2.5", "3", "4"],
        "correct_answer": "2"
    },
    {
        "question": "How much Capital conservative buffer (CCB) % is required under Basel-3?",
        "options": ["0.50", "1.00", "1.50", "2.00", "2.50"],
        "correct_answer": "2.50"
    },
{
        "question": "Liquidity standard, LCR (Liquidity coverage ratio) was introduced in Basel…....?",
        "options": ["1", "2", "2.5", "3", "4"],
        "correct_answer": "3"
    },
    {
        "question": "BCBS is housed in BIS office at Switzerland and is called Basel Committee on Banking Supervision. The Committee was established in the year",
        "options": ["1974", "1981", "1980", "1984", "1949"],
        "correct_answer": "1974"
    },
    {
        "question": "Basel-I was the first set of guidelines issued by the Basel Committee of Banking Supervision which was mainly focused on credit risk was introduced in year …",
        "options": ["1988", "1974", "1991", "1984", "1981"],
        "correct_answer": "1988"
    },
    {
        "question": "Basel-3 was introduced in response to global financial crisis of 2007-2008. When Basel 3 was introduced globally?",
        "options": ["2008", "2009", "2010", "2011", "2012"],
        "correct_answer": "2010"
    },
    {
        "question": "Basel-III recommendations were introduced in response to the Global Financial Crises (GFC) 2007, which seeks to strengthen the resilience to individual banks in order to reduce the risk of system-wide shock and prevent future economic meltdowns. First set of guidelines under Basel-III was released in the year.",
        "options": ["2008", "2009", "2013", "2011", "2010"],
        "correct_answer": "2010"
    },
    {
        "question": "As per RBI guidelines in line with Basel-III, Banks in India are required to maintain 9.00% CAR. The break up of CAR (CET1+AT1+T2) is",
        "options": ["4.50 + 1.50 + 3.00", "4.50 + 2.50 + 2.00", "5.50 + 1.50 + 2.00", "5.50 + 2.50 + 1.00", "3.50 + 3.50 + 2.00"],
        "correct_answer": "5.50 + 1.50 + 2.00"
    },
    {
        "question": "In India, the banks are required to maintain a minimum pillar-1 capital to risk weighted assets ratio of ………… as on ……………….",
        "options": ["8.0%, 31st March each Year", "9.00%, Ongoing basis", "9.00%, 31st March each Year", "8.00%, ongoing basis", "8.50%, ongoing basis"],
        "correct_answer": "9.00%, Ongoing basis"
    },
    {
        "question": "NSFR(Net stable funding ratio) liquidity measures introduced in which Basel accord?",
        "options": ["Basel-1", "Basel-2", "Basel 3", "Principal for responsible banking", "Basel 2.5"],
        "correct_answer": "Basel 3"
    },
    {
        "question": "BCBS Full form is…..................................?",
        "options": ["Banking committee on Banking Supervision", "Basel commission on Banking Supervision", "Basel community on Banking Supervision", 
                   "Basel Committee on Banking Supervision", "Basel Committee of Banking Supervision"],
        "correct_answer": "Basel Committee on Banking Supervision"
    },
    {
        "question": "Basel is a place in Switzerland which is Head office of Bank of International Settlements (BIS). The Committee on Banking Regulators and Supervisors is housed in BIS office and is called Basel Committee on Banking Supervision (BCBS).",
        "options": ["It is Regulator of International Banks and Indian Banks are also regulated by Basel", 
                   "Basel is division of United Nation Organization which supervises Banking and Finance in Member countries",
                   "Basel is an extended part of World Bank to guide member countries about Best Practices in Banking across the globe",
                   "Basel is a place in Switzerland which is Head office of Bank of International Settlements (BIS). The Committee on Banking Regulators and Supervisors is housed in BIS office and is called Basel Committee on Banking Supervision (BCBS).",
                   "None of the above"],
        "correct_answer": "Basel is a place in Switzerland which is Head office of Bank of International Settlements (BIS). The Committee on Banking Regulators and Supervisors is housed in BIS office and is called Basel Committee on Banking Supervision (BCBS)."
    },
    {
        "question": "Operational Risk has been included for first time for calculation of Regulatory Capital requirement under …............?",
        "options": ["Basel-1", "Basel-2", "Basel 3", "Principal for responsible banking", "Basel 2.5"],
        "correct_answer": "Basel-2"
    },
    {
        "question": "Basel Committee on Banking Supervision is a committee of banking super authorities that was established by:",
        "options": ["World Bank", "Unites state of America", "European countries", "Central Bank governors of the group of 10 countries", "RBI"],
        "correct_answer": "Central Bank governors of the group of 10 countries"
    },
    {
        "question": "Capital Adequacy Ratio is calculated as a percentage of Capital to Risk Weighted Asset. To calculate capital adequacy ratio, the banks are to consider, which of the following risk?",
        "options": ["Credit Risk, Market Risk and Operational Risk", "Credit Risk only", "Market Risk only", "Operational Risk only", "Credit Risk and Market Risk only"],
        "correct_answer": "Credit Risk, Market Risk and Operational Risk"
    },
    {
        "question": "Banks classified as D-SIBs will be subjected to additional Common Equity Tier 1 (CET1) capital requirement ranging from 0 to 1.00%.Here D-SIB denotes…...........?",
        "options": ["Domestic System important bank", "Domestic systematic important bank", "Domestic systemically international bank", 
                   "Domestic systemically important bank", "Domestic systematic international bank"],
        "correct_answer": "Domestic systemically important bank"
    },
    {
        "question": "Which one is not related to Basel 2?",
        "options": ["Introduction of LCR and NSFR", "Introduction of Operational risk capital calculation", "Internal Capital Adequacy Assessment Process (ICAAP)", 
                   "Basic indicator approach of operational risk capital calculation", "Market risk capital calculation"],
        "correct_answer": "Introduction of LCR and NSFR"
    },
{
        "question": "Basel-III introduced following two liquidity ratios",
        "options": ["LCR and NSFR", "LCR and Current Ratio", "NSFR and Current Ratio", "Current Ratio and Quick Ratio", "Current Ratio and Debt Equity Ratio"],
        "correct_answer": "LCR and NSFR"
    },
    {
        "question": "Which of the following is not part of Pillar II Risk?",
        "options": ["Credit Concentration Risk", "Liquidity Risk", "Market Risk", "Strategic Risk", "Reputational Risk"],
        "correct_answer": "Market Risk"
    },
    {
        "question": "Basel-I was the first set of guidelines issued by the Basel Committee of Banking Supervision which was mainly focused on credit risk. So, it came with set of guidelines about",
        "options": ["Maximum loan exposure to an entity with the goal of minimizing credit risk",
                   "Maximum number of loans to be extended i.e. quantitively aspect of Credit",
                   "Maximum Capital requirements of financial institutions with the goal of minimizing credit risk",
                   "Maximizing profit by using Risk Pricing to offset Credit Risk",
                   "Minimum Capital requirements of financial institutions with goal of minimizing risk"],
        "correct_answer": "Minimum Capital requirements of financial institutions with goal of minimizing risk"
    },
    {
        "question": "Basel norms are set of guidelines published by the Basel Committee of Banking Supervision which focuses on",
        "options": ["Risk to Banks and Financial System",
                   "Cooperation among Apex Banks on banking supervisory matter",
                   "Strengthen the International banking system",
                   "Option a and b are true",
                   "Option a, b and c are true"],
        "correct_answer": "Option a, b and c are true"
    },
    {
        "question": "Treasury functions are one of the critical business activity of bank and are under priority level -----under BCP.",
        "options": ["1", "2", "3", "4", "Not under any priority"],
        "correct_answer": "1"
    },
    {
        "question": "What is 80: 20 Principle in BCP?",
        "options": ["80 % banking activity is nonessential and 20 % activity is essential.",
                   "80% banking activity is essential activity and 20% activity is non essential",
                   "80% revenue is earned by 20% of banking activity.",
                   "20% banks does 80% of total banking business.",
                   "there is no such principle in BCP"],
        "correct_answer": "80% revenue is earned by 20% of banking activity."
    },
    {
        "question": "Which of the following is not a BCP coordinator?",
        "options": ["Chief security officer", "Chief Risk Officer", "CTO / Vertical Head - DIT", "Vertical Head - SSD", "Vertical Head - HRD"],
        "correct_answer": "Chief Risk Officer"
    },
    {
        "question": "As per business impact rating, Massive business impact rating is defined as-------------. Please select the correct one.",
        "options": ["Direct loss between Rs.1.00 Lakh to Rs.25.00 Lakh.",
                   "Direct loss in excess of Rs.10.00 Crore.",
                   "Direct Loss between Rs.25.00 Lakh up to Rs.2.50 Crore.",
                   "Direct Loss of Rs.2.50 Crore up to Rs.10.00 Crore.",
                   "Direct loss less than Rs.1.00 Lakh."],
        "correct_answer": "Direct loss in excess of Rs.10.00 Crore."
    },
    {
        "question": "As per business impact rating, Major business impact rating is defined as-------------. Please select the correct one.",
        "options": ["Direct loss between Rs.1.00 Lakh to Rs.25.00 Lakh.",
                   "Direct loss in excess of Rs.10.00 Crore.",
                   "Direct Loss between Rs.25.00 Lakh up to Rs.2.50 Crore.",
                   "Direct Loss of Rs.2.50 Crore up to Rs.10.00 Crore.",
                   "Direct loss less than Rs.1.00 Lakh."],
        "correct_answer": "Direct Loss of Rs.2.50 Crore up to Rs.10.00 Crore."
    },
    {
        "question": "In DR site, DR stands for:",
        "options": ["Dummy Resource", "Disaster Recovery", "Duplicate Resource", "Data Recovery", "Data Reservoir"],
        "correct_answer": "Disaster Recovery"
    },
    {
        "question": "Under BCP when there is more than one source that has contributed towards disruptions, then a Committee of coordinators shall be formed under the leadership of -----------. Please fill in the blank with the appropriate word.",
        "options": ["General Manager DIT", "Chief security officer", "Chief Risk Officer", "General manager SSD", "General manager HRD"],
        "correct_answer": "General Manager DIT"
    },
    {
        "question": "Branch BCP Task force is to be constituted with BH as head & Deputy branch head and two other member staff. It has to meet once in---------. Which is the correct option?",
        "options": ["Half yearly", "Yearly", "Quarterly", "Monthly", "Bimonthly"],
        "correct_answer": "Half yearly"
    },
    {
        "question": "What is the periodicity of Staff awareness test, under BCP testing?",
        "options": ["Yearly", "Half yearly", "quarterly", "Monthly", "Bimonthly"],
        "correct_answer": "Half yearly"
    },
    {
        "question": "An incident with a business impact rating as massive will be classified as Level ---------- priority and will have an RTO of ------- hours. Please select the correct options.",
        "options": ["Level 1, RTO- 8 Hours", "Level 2, RTO- 4 Hours", "Level 3, RTO-24 Hours", "Level 2, RTO-24 Hours", "Level 1, RTO-4 Hours"],
        "correct_answer": "Level 1, RTO-4 Hours"
    },
    {
        "question": "--------------------------- is the acceptable latency of data that will be recovered and have been identified for the critical systems of the bank.",
        "options": ["Recovery time objective", "Recovery point objective", "Maximum tolerable period of disruption", "Disaster Management plan", "Data backup system"],
        "correct_answer": "Recovery point objective"
    },
{
        "question": "Which of the following is not a measure to be taken to prevent disruption under Business continuity plan?",
        "options": ["Carrying out continuous health checks of existing systems",
                   "Removal of disaster recovery team at regional offices and creation of disaster recovery team at central office.",
                   "Evaluation of BCP service providers.",
                   "Staff awareness and BCP Training",
                   "Comparison of BCP with other peers to adopt best practices."],
        "correct_answer": "Removal of disaster recovery team at regional offices and creation of disaster recovery team at central office."
    },
    {
        "question": "As per the risk assessment process, BCP is to be tested periodically. Which of the following test is not used for BCP testing?",
        "options": ["Partial live test", "Walk through test", "Run through test", "Staff awareness test", "System connectivity test"],
        "correct_answer": "Run through test"
    },
    {
        "question": "Which of the following information is not correct about BCP Committee?",
        "options": ["MD & CEO is the chairman of BCP committee",
                   "In absence of MD & CEO senior most ED is chairman of committee",
                   "The meeting is conducted at least once a year.",
                   "Chief risk officer is the convenor of meeting.",
                   "Vertical head corporate communication takes the responsibility of spokesperson of bank"],
        "correct_answer": "The meeting is conducted at least once a year."
    },
    {
        "question": "Which of the following term is not associated with BCP?",
        "options": ["Business impact rating", "Business impact analysis", "Recovery point objective", "Recovery time objective", "Turn around time"],
        "correct_answer": "Turn around time"
    },
    {
        "question": "How many UN Sustainability development goals(SDGs) are there?",
        "options": ["15", "16", "17", "18", "19"],
        "correct_answer": "17"
    },
    {
        "question": "The Paris agreement states that the world should work to hold the increase in global average temperature to...........",
        "options": ["Well below 2 degree celsius above pre industrial level while pursuing efforts to limit the temperature increase to 1.5 degree Celsius.",
                   "Well below 3 degree celsius above pre industrial level while pursuing efforts to limit the temperature increase to 2 degree celsius.",
                   "Well below 4.5 degree celsius above today's level while pursuing efforts to limit the temperature increase to 1.5 degree Celsius of today's level.",
                   "Well below 3 degree celsius above today's level while pursuing efforts to limit the temperature increase to 2 degree Celsius of today's level.",
                   "Well below 3.5 degree celsius above today's level while pursuing efforts to limit the temperature increase to 2 degree Celsius of today's level."],
        "correct_answer": "Well below 2 degree celsius above pre industrial level while pursuing efforts to limit the temperature increase to 1.5 degree Celsius."
    },
    {
        "question": "What are the two subtype of physical climate risk?",
        "options": ["Acute and chronic", "Policy and legal", "Technological and reputational", "Hydrological and climatological", "Sudden and gradual"],
        "correct_answer": "Acute and chronic"
    },
    {
        "question": "Which SDG (Sustainability development goal) is related to taking urgent action to combat climate change and its impact?",
        "options": ["Goal 2", "Goal 4", "Goal 10", "Goal 12", "Goal 13"],
        "correct_answer": "Goal 13"
    },
    {
        "question": "Which of the following is a Physical climate risk? (a) Hurricane (b) Drought (c) Wildfire (d) Temperature rise (e) Sea level rise (f) Legal cases",
        "options": ["only Option (a), (b),(c) and (f) is correct",
                   "only option (b), (c), (d),(e) and (f) is correct",
                   "only option (a),(b)and (c) is correct",
                   "only option (a),(b),(c), (d) and (e) is correct",
                   "only option (a),(b),(c) and (d) is correct"],
        "correct_answer": "only option (a),(b),(c), (d) and (e) is correct"
    },
    {
        "question": "What are the two main types of climate risk?",
        "options": ["Market risk and operational risk",
                   "Physical risk and transition risk",
                   "Stranded asset risk and litigation risk",
                   "Environmental and physical risk",
                   "Physical risk and transformation risk"],
        "correct_answer": "Physical risk and transition risk"
    },
    {
        "question": "Which of the following is not an acute physical climate risk?",
        "options": ["Flood", "Wildfire", "Hurricane", "Sea level rise", "Tornado"],
        "correct_answer": "Sea level rise"
    },
    {
        "question": "Loan principal amount is Rs-120 crore, Economic capital required is equal to 12.50% of principal amount. If before tax risk adjusted return is equal to Rs- 2.07 crore. Calculate Risk adjusted return on capital if tax rate is 30%",
        "options": ["9.50%", "10%", "9.66%", "10.50%", "12%"],
        "correct_answer": "9.66%"
    },
    {
        "question": "Hurdle rate in RAROC is",
        "options": ["10.20%", "10.40%", "12.20%", "12.40%", "12.50%"],
        "correct_answer": "12.20%"
    },
    {
        "question": "What is risk weight assigned for the 'AAA' rated account?",
        "options": ["20%", "30%", "50%", "100%", "150%"],
        "correct_answer": "20%"
    },
{
        "question": "Under Standardised Approach of calculation of capital charge for Credit Risk, Risk Weights are assigned to various class of exposure depending up on nature of exposer. What is the Risk Weight for the credit facility to employee (staff) of bank which has been secured with superannuation benefit of employee?",
        "options": ["50%", "75%", "100%", "20%", "150%"],
        "correct_answer": "20%"
    },
    {
        "question": "RWA for AA Rated facility is",
        "options": ["20%", "30%", "40%", "50%", "25%"],
        "correct_answer": "30%"
    },
    {
        "question": "A housing loan of Rs.50.00 Lakh was sanctioned for construction of house at an estimated cost of Rs.60.00 Lakh. Borrower has repaid Rs.5.00 Lakh as per stipulated repayment terms. What is the Risk Weight applicable?",
        "options": ["30%", "35%", "50%", "75%", "100%"],
        "correct_answer": "35%"
    },
    {
        "question": "RWA for Unrated facility is",
        "options": ["100%", "150%", "200%", "125%", "250%"],
        "correct_answer": "100%"
    },
    {
        "question": "Under Standardised Approach of calculation of capital charge for Credit Risk, What is the Risk Weight for the exposer under Venture Capital portfolio?",
        "options": ["50%", "75%", "100%", "125%", "150%"],
        "correct_answer": "150%"
    },
    {
        "question": "What is periodicity of review renewal if account is rated CR-01?",
        "options": ["12 Months", "18 Months", "6 Months", "15 Months", "9 Months"],
        "correct_answer": "12 Months"
    },
    {
        "question": "Short Term Rating by External Credit Rating Agency is for the security with a maturity period of...",
        "options": ["3 months", "6 months", "9 months", "12 months", "18 months"],
        "correct_answer": "12 months"
    },
    {
        "question": "Short-term ratings relate to securities or bank facilities of up to ----------- maturity, whereas long-term rating is beyond -----------.",
        "options": ["12 months, 18 months", "6 months, 12 months", "15 months, 18 months", "12 months, 12 months", "12 months, 24 months"],
        "correct_answer": "12 months, 12 months"
    },
    {
        "question": "Please calculate Loss given default for a credit exposure of Rs.250 crore with a Recovery rate of 40%. Please note that exposure is assumed to be same at the time of default.",
        "options": ["100 crore", "120 crore", "130 crore", "140 crore", "150 crore"],
        "correct_answer": "150 crore"
    },
    {
        "question": "Bank has inhouse developed Internal Credit Rating Models. How many models are there under Union Trade Model?",
        "options": ["one model", "2 models", "3 models", "4 models", "5 models"],
        "correct_answer": "2 models"
    },
    {
        "question": "Please calculate Expected credit loss for a credit exposure of Rs.250 crore. Probability of default for this pool of assets are 20% with a Recovery rate of 40%. Please note that exposure is assumed to be same at the time of default.",
        "options": ["20 crore", "30 crore", "40 crore", "45 crore", "47 crore"],
        "correct_answer": "30 crore"
    },
    {
        "question": "Which one statement is incorrect about external credit rating?",
        "options": [
            "External Credit Rating is an opinion about whether counterparty is likely to make timely repayment of its financial obligations",
            "External Credit Rating is a qualitative & quantitative assessment of Probability of Default.",
            "It is an attempt to measure the ability and willingness of a borrower to meet its debt obligations in a timely manner",
            "External Credit Rating is not a recommendation to Enter in financial transactions.",
            "A Credit Rating does reflect other types of risk, such as market or liquidity risks, which may also affect the value of a security."
        ],
        "correct_answer": "A Credit Rating does reflect other types of risk, such as market or liquidity risks, which may also affect the value of a security."
    },
    {
        "question": "As per our bank guidelines, which of the following is true regarding scope of RBRCA?",
        "options": [
            "MSME proposal (New/ Enhancement) with exposure Rs 10.00 Crore & above",
            "Other than MSME proposals (New/ Enhancement) with exposure Rs 50.00 Crore and above",
            "All retails loans are excluded",
            "Only A & C are true",
            "A, B & C are true"
        ],
        "correct_answer": "A, B & C are true"
    },
    {
        "question": "RAROC can be calculated as",
        "options": [
            "After Tax Risk Adjusted Return / Regulatory Capital",
            "After Tax Risk Adjusted Return / WACC",
            "WACC / Economic Capital",
            "ROA / Regulatory capital",
            "Net profit / Economic capital"
        ],
        "correct_answer": "After Tax Risk Adjusted Return / Regulatory Capital"
    },
    {
        "question": "Rating model will be decided based on",
        "options": [
            "Exposure with our Bank only",
            "Aggregate Exposure",
            "Existing relation with Bank",
            "Repayment history",
            "Asset classification"
        ],
        "correct_answer": "Aggregate Exposure"
    },
{
        "question": "Hurdle rate for RAROC is to be calculated …........... Based on ….............. Of the bank.",
        "options": ["Quarterly, Audited Financials", "Half yearly, Audited Financials", "As and when required, Subjective assessment", 
                   "Annually, Audited Financials", "Monthly, Subjective assessment"],
        "correct_answer": "Annually, Audited Financials"
    },
    {
        "question": "Audit and Inspection department shall carry only audit of the functioning of Scrutiny Committee in respect of High Risk/ No Go Proposal. The frequency of audit is…",
        "options": ["At least once a year", "At least once a month", "At least once a quarter", 
                   "At least once in Half year", "Only at the time of Management Audit of Zonal Office."],
        "correct_answer": "At least once a year"
    },
    {
        "question": "Which rating and below is classified as speculative rating?",
        "options": ["BBB -", "BBB", "BB +", "BBB +", "AA -"],
        "correct_answer": "BB +"
    },
    {
        "question": "Management Risk is covered under which aspect of credit rating?",
        "options": ["Facility rating", "Risk mitigators", "Business aspects", "Borrower rating", "Management rating"],
        "correct_answer": "Borrower rating"
    },
    {
        "question": "The Credit Rating Agencies are functioning under the guidelines of",
        "options": ["RBI", "SEBI", "CRAD", "MOF", "Both A&B"],
        "correct_answer": "Both A&B"
    },
    {
        "question": "Which of the following is not an RBI approved agency for external Credit Rating in India?",
        "options": ["ICRA", "Moody", "CARE", "CRISIL", "CIBIL"],
        "correct_answer": "CIBIL"
    },
    {
        "question": "Which of the following is not the purpose of internal credit rating?",
        "options": ["Pricing of loan", "Setting approval authority", "Classifying NPA", "Credit quality monitoring", "Surveillance"],
        "correct_answer": "Classifying NPA"
    },
    {
        "question": "Which credit risk mitigation technique is based on principal of 'Four eyes are better than two eyes'?",
        "options": ["Portfolio Management & Diversification", "Committee based approach", "Risk Rating and Hurdle Rate", "Insurance and derivatives", "Risk Rating and Hurdle Rate"],
        "correct_answer": "Committee based approach"
    },
    {
        "question": "Type of Credit Risk which is associated with exposure of any single or group with the potential to produce large losses to threaten the core operations of a bank is:",
        "options": ["Country Risk", "Bankruptcy Risk", "Downgrade Risk", "Concentration Risk", "Settlement Risk"],
        "correct_answer": "Concentration Risk"
    },
    {
        "question": "Which of the following exposures are not exempted under RAROC approach?",
        "options": ["Exposure to central/ state government", "Exposure against fixed deposit", "Corporate advances above Rs- 5 crore", 
                   "MSME advances exposure below Rs- 1 crore", "MSME Exposure of Rs.50 lakhs"],
        "correct_answer": "Corporate advances above Rs- 5 crore"
    },
    {
        "question": "Hurdle rate for new borrowers is",
        "options": ["CR 3", "CR 4", "CR 5", "CR 6", "CR 2"],
        "correct_answer": "CR 5"
    },
    {
        "question": "…......... means the potential for direct loss due to an internal or external rating downgrade or upgrade.",
        "options": ["incremental risk", "Credit migration risk", "Credit spread risk", "Individual risk", "Market risk"],
        "correct_answer": "Credit migration risk"
    },
    {
        "question": "Risk associated with changes in the credit profile of the borrowers and counter parties, is called:",
        "options": ["Credit Risk", "Liquidity Risk", "Settlement Risk", "Payment Risk", "Market Risk"],
        "correct_answer": "Credit Risk"
    },
    {
        "question": "Underwriting of Loans & Advances to the customer is the largest and most obvious source of _____ risk",
        "options": ["Operational Risk", "Credit Risk", "Market Risk", "Liquidity Risk", "Reputational Risk"],
        "correct_answer": "Credit Risk"
    },
    {
        "question": "Credit default risk, Concentration risk, country risk, Bankruptcy risk, Downgrade risk and Settlement risk are type of …........... ?",
        "options": ["Operational Risk", "Legal Risk", "Technology Risk", "Credit Risk", "Liquidity risk"],
        "correct_answer": "Credit Risk"
    },
    {
        "question": "Credit risk is one of the critical risks faced by the bank and this risk arises from various source of risk drivers. In case, there is default in repayment of Instalment and/or interest, such scenario is called as",
        "options": ["Credit Risk to Bank", "Credit Risk to Customer", "Operational Risk to Bank", "Market Risk to Bank", "Monitoring Risk to Bank"],
        "correct_answer": "Credit Risk to Bank"
    },
    {
        "question": "Rating model used for Term Loan of Rs.1 Crore for a firm with 3 years' average sales of Rs.28.50 Crore is",
        "options": ["CRISIL ICON", "UBI-I", "UBI-II", "UTR-I", "UTR-II"],
        "correct_answer": "CRISIL ICON"
    },
    {
        "question": "Applicable credit rating model for Commercial Real Estate Exposure of Rs.75 Lakh is",
        "options": ["UBI-I", "UTR-I", "UBI-II", "CRISIL ICON", "Rating not applicable"],
        "correct_answer": "CRISIL ICON"
    },
{
        "question": "Internal Credit Rating process is independent mechanism and rating assessment is based on expert judgement. Under such scenario, Low-side re-rating means",
        "options": [
            "Decision to upgrade credit rating of a borrower to a lower risk level in the investment grade",
            "Decisions to upgrade/downgrade the credit rating of a borrower whose credit rating falls below the investment grade as per the rating assigned by the rating officer",
            "Decision to downgrade credit rating of a borrower to a higher risk level in the investment grade",
            "Decision to downgrade/upgrade a borrower whose credit rating is above investment grade",
            "Decision to re-rate the credit rating given a lower office / branch"
        ],
        "correct_answer": "Decisions to upgrade/downgrade the credit rating of a borrower whose credit rating falls below the investment grade as per the rating assigned by the rating officer"
    },
    {
        "question": "Combined rating available in CRISIL ICON will help bank",
        "options": [
            "Identify probability of default of the borrower",
            "Identify the un expected loss that can occur in that account",
            "Decide the collaterals to be taken for the facility",
            "Derive the total loss expected from the borrower",
            "Risk in the securities offered by the borrower"
        ],
        "correct_answer": "Derive the total loss expected from the borrower"
    },
    {
        "question": "Which of the following limits are not exempted from credit rating?",
        "options": [
            "MSME loan of Rs. 20 lakhs",
            "Advance against deposits, NSC, LIC policy",
            "Direct Agriculture advances of Rs. 1.50 crore",
            "Union TReDS",
            "Loans to SHGs"
        ],
        "correct_answer": "Direct Agriculture advances of Rs. 1.50 crore"
    },
    {
        "question": "Due to COVID-19 pandemic, a firm's decreased creditworthiness and there is downgrading of Credit Rating. This will be categorised as which subtype of Credit Risk?",
        "options": ["Downgrade Risk", "Bankruptcy Risk", "Default Risk", "Settlement Risk", "Market Risk"],
        "correct_answer": "Downgrade Risk"
    },
    {
        "question": "Expected Credit loss can be calculated as",
        "options": [
            "ECL= PD X EAD",
            "ECL= PD X LGD X EAD",
            "ECL= LGD X EAD",
            "ECL= PD X LGD",
            "ECL= PD X LGD X Actual Loss"
        ],
        "correct_answer": "ECL= PD X LGD X EAD"
    },
    {
        "question": "Which statement made about RAROC is not correct?",
        "options": [
            "RAROC, ROA and ROE are used for return calculation.",
            "RAROC uses economic capital towards calculation of return.",
            "It deducts Expected loss associated with lending while making calculation",
            "Expected losses are calculated on short term average default rate and recovery rates",
            "Expected credit loss is the product of probability of default, loss given default and exposure at default."
        ],
        "correct_answer": "Expected losses are calculated on short term average default rate and recovery rates"
    },
    {
        "question": "Which statement is correct about External credit rating?",
        "options": [
            "A Credit Rating does reflect other types of risk, such as market or liquidity risks, which may also affect the value of a security.",
            "External Credit Rating is a recommendation to Enter in a financial transaction.",
            "External Credit Rating is a qualitative & quantitative assessment of Probability of Default.",
            "credit rating should be interpreted as investment advice.",
            "A credit rating is a guarantee that a financial obligation will be repaid."
        ],
        "correct_answer": "External Credit Rating is a qualitative & quantitative assessment of Probability of Default."
    },
    {
        "question": "RBRCA process leads to categorization of proposal into Low Risk, Medium Risk, High Risk and No go categories. Which category indicates 'High Possibility of loss from the borrower'?",
        "options": ["Low Risk", "Medium Risk", "High Risk", "No- Go", "No Risk"],
        "correct_answer": "High Risk"
    },
    {
        "question": "In the options given Which type of security will be preferred?",
        "options": [
            "Land and buildings used for religious worship",
            "Properties of political parties",
            "Disputed properties",
            "Mortgage of agriculture land for non-agriculture loans",
            "House on a freehold land"
        ],
        "correct_answer": "House on a freehold land"
    },
    {
        "question": "Which statement is wrong about use of insurance in credit risk mitigation?",
        "options": [
            "Insurance is used to transfer risk to third party.",
            "Insurance Policies are renewed in time and should be enforceable",
            "If insured assets are prone to risks like flood, storm, cyclone, explosion then policy should cover such risk",
            "Generally, it is used for residual risk, but it can also be used as a primary strategy of Risk Management",
            "Insurance Policy should not have the bank clause"
        ],
        "correct_answer": "Insurance Policy should not have the bank clause"
    },
    {
        "question": "Which of the following is not a type of credit risk?",
        "options": ["Concentration Risk", "Downgrade Risk", "Interest Rate Risk", "Country Risk", "Bankruptcy Risk"],
        "correct_answer": "Interest Rate Risk"
    },
    {
        "question": "Which of the following is true about RAROC calculation?",
        "options": [
            "It deducts actual loss associated with lending while making calculation",
            "Expected losses are calculated on short term average default rate and recovery rates",
            "It represents the short term view on loan losses",
            "RAROC represents a view on profitability which is economic cycle sensitive",
            "It deducts Expected loss associated with lending while making calculation"
        ],
        "correct_answer": "It deducts Expected loss associated with lending while making calculation"
    },
{
        "question": "Which of the following is not true about RBRCA in our bank?",
        "options": [
            "It is fully objective assessment process with no room for subjectivity",
            "It has 7 mandatory categories for risk assessment parameters",
            "RBRCA aims at strengthening the Credit Risk assessment and underwriting process",
            "RBRCA demands calculative decision based on analysis of the risk factors in detail.",
            "Regulator has also given emphasis on the RBRCA through EASE agenda"
        ],
        "correct_answer": "It is fully objective assessment process with no room for subjectivity"
    },
    {
        "question": "Who will be the sanctioning authority for High Risk/ No go Proposal originally in the delegation power ZLCC?",
        "options": [
            "It will be sanctioned by CAC-III",
            "The proposal is to be straightaway rejected and not to be sanctioned",
            "It will be sanctioned by CAC-II",
            "It will be sanctioned by ZLCC only but after the scrutiny of proposal through RLCC-I of concerned Regional office for RBRCA only.",
            "The scrutiny and Sanction will be done at ZLCC only."
        ],
        "correct_answer": "It will be sanctioned by ZLCC only but after the scrutiny of proposal through RLCC-I of concerned Regional office for RBRCA only."
    },
    {
        "question": "Which of the following is not true about credit proposal where RAROC > Hurdle Rate?",
        "options": [
            "It is called green zone",
            "It will do the value addition to the shareholders value",
            "This proposal should be accepted in normal course",
            "It will destroy the value to shareholders capital.",
            "Positive RAROC means it will generate income"
        ],
        "correct_answer": "It will destroy the value to shareholders capital."
    },
    {
        "question": "Which of the following is not true about credit proposal where RAROC is positive but below Hurdle rate?",
        "options": [
            "It is called Amber Zone",
            "It will not generate any income",
            "It will generate income but less than shareholders expectations",
            "Borrower coming under this category can be accepted after careful consideration by sanctioning authority",
            "Bank may explore obtaining financial collateral to improve RAROC"
        ],
        "correct_answer": "It will not generate any income"
    },
    {
        "question": "For a sports goods manufacturer with Term Loan of Rs. 10.00 Crs and Cash Credit limit of Rs. 30.00 Crs under consortium arrangement, which rating model should be used?",
        "options": [
            "SME Manufacturing Model of CRISIL ICON",
            "Large Corporate Model of CRISIL ICON",
            "SME Services Model of CRISIL ICON",
            "Trader Model of CRISIL ICON",
            "Rating done by ECRA is sufficient"
        ],
        "correct_answer": "Large Corporate Model of CRISIL ICON"
    },
    {
        "question": "What does Probability of Default (PD) mean?",
        "options": [
            "The exposure that will be lost if default occurs",
            "Likelihood that borrower will default over a given time horizon.",
            "Loss in normal course of business and banks make provision against it",
            "Measures amount of the facility that is likely to be drawn if default occurs",
            "None of the Above"
        ],
        "correct_answer": "Likelihood that borrower will default over a given time horizon."
    },
    {
        "question": "LGD stands for",
        "options": [
            "Loss Given Default",
            "Loss Gain Dividend",
            "Loss Giving Defaulter",
            "Losses Gain Diversion",
            "Loan Given Delinquency"
        ],
        "correct_answer": "Loss Given Default"
    },
    {
        "question": "CRMC meeting is chaired by",
        "options": [
            "CRO (In case of absence, Second In command of Risk Management Department",
            "ED- looking after the risk portfolio",
            "MD&CEO (In case of absence, Senior Most ED)",
            "Any one ED can be the chairman of CRMC",
            "RBI nominee director"
        ],
        "correct_answer": "MD&CEO (In case of absence, Senior Most ED)"
    },
    {
        "question": "RBRCA process leads to categorization of proposal into Low Risk, Medium Risk, High Risk and No go categories. Which category indicates 'Higher than average possibility of Risk'?",
        "options": ["Low Risk", "Medium Risk", "High Risk", "No- Go", "No Risk"],
        "correct_answer": "Medium Risk"
    },
    {
        "question": "In which of the following case RBRCA is applicable?",
        "options": [
            "Loans classified as NPA",
            "Loans fully secured by Deposits/SBLC/ Financial Collateral",
            "Proposal for AD-hoc/ TOD",
            "Loans covered under UGECL",
            "MSME proposal (New/ Enhancement) with exposure Rs 10.00 Crore & above"
        ],
        "correct_answer": "MSME proposal (New/ Enhancement) with exposure Rs 10.00 Crore & above"
    },
    {
        "question": "Which one is not the benefit of risk rating under credit risk management?",
        "options": ["Identification of risk", "Measurement of risk", "Monitoring of risk", "Risk based pricing", "NPA management"],
        "correct_answer": "NPA management"
    },
    {
        "question": "Which of the following is true about RBRCA cell?",
        "options": [
            "It is formed at Central office level",
            "Branch originating the proposal and Risk officer at RO, ZO and CO are the part of RBRCA cell",
            "The cell is headed by Risk officer at Central Office",
            "Only Zonal and Regional Risk officers will be part of RBRCA cell",
            "It is formed at MLP"
        ],
        "correct_answer": "Only Zonal and Regional Risk officers will be part of RBRCA cell"
    },
    {
        "question": "External Credit Rating is ---------- about whether the counterparty is likely to make timely repayment of its financial obligations.",
        "options": ["Judgement", "Opinion", "Suggestion", "Guarantee", "Decision"],
        "correct_answer": "Opinion"
    },
    {
        "question": "Credit Risk Management not only includes bank's exposer in Balance Sheet but also Off-Balance Sheet exposure. This Off-Balance Sheet exposure includes...",
        "options": [
            "Bank Guarantee",
            "Letter of Credit",
            "Deferred Payment Guarantee",
            "Option (a), (b) and (c)",
            "Term Loan"
        ],
        "correct_answer": "Option (a), (b) and (c)"
    },
    {
        "question": "Which credit risk mitigation technique is based on principal of 'Don't put all the eggs in one basket'?",
        "options": [
            "Portfolio Management & Diversification",
            "Committee based approach",
            "Risk Rating and Hurdle Rate",
            "Insurance and derivatives",
            "Risk Rating and Hurdle Rate"
        ],
        "correct_answer": "Portfolio Management & Diversification"
    },
{
        "question": "One of the objective of Credit rating process of credit exposer is to estimate ------------ of the account.",
        "options": ["Credit Default", "Expected Loss", "Probability of Default", "Exposure at Default", "Loss Given Default"],
        "correct_answer": "Probability of Default"
    },
    {
        "question": "In which of the following case RBRCA is not applicable?",
        "options": [
            "Loans classified as standard account",
            "Loans partially secured by Deposits/SBLC/ Financial Collateral",
            "Proposal for AD-hoc/ TOD",
            "Loans covered under ECGC",
            "B & D"
        ],
        "correct_answer": "Proposal for AD-hoc/ TOD"
    },
    {
        "question": "Which of the following is not true about Red Zone Proposal as per RAROC Categorization?",
        "options": [
            "RAROC is less than Hurdle rate.",
            "It will erode the value of Shareholders Equity",
            "The proposal can be accepted with proper justification and concrete assurance about additional Non interest income",
            "RAROC is less than hurdle rate and positive.",
            "RAROC is less than hurdle rate and negative."
        ],
        "correct_answer": "RAROC is less than hurdle rate and positive."
    },
    {
        "question": "Rating model used for SOD limit of Rs.50 Lakh is",
        "options": ["UBI-I", "UTR-I", "UBI-II", "CRISIL ICON", "Rating not applicable"],
        "correct_answer": "Rating not applicable"
    },
    {
        "question": "Rating concept which indicates the direction in which a rating is likely to move over a one to two year period.",
        "options": ["Rating Outlook", "Rating watch", "Issue rating", "Issuer Rating", "Unsolicited Rating"],
        "correct_answer": "Rating Outlook"
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
    },
    {
        "question": "The review of relevance and effectiveness of KRIs shall be taken up at a bank wide level once in every -------- or as & when need arises.",
        "options": ["quarter", "Half year", "Year", "Two year", "Month"],
        "correct_answer": "Two year"
    },
    {
        "question": "Bank undertake selling of Mutual Funds and Insurance Policies through its branch network, this activity is mapped to which of the Business Line.",
        "options": ["Corporate Finance", "Commercial Banking", "Retail Banking", "Agency Services", "Retail Brokerage"],
        "correct_answer": "Agency Services"
    },
    {
        "question": "Which one is not under the purview of Operational Risk management Committee?",
        "options": [
            "Reviewing aggregated Operational Risk reports.",
            "Evaluating Operational Risk in new products",
            "Reviewing Risk and Control Self-Assessment (RCSA)",
            "understand future changes and threats, and concur on areas of highest priority and related mitigation strategy.",
            "Analysis of Stressed Asset in credit portfolio"
        ],
        "correct_answer": "Analysis of Stressed Asset in credit portfolio"
    },
    {
        "question": "Cases of Theft / Burglary / Dacoity / Robbery should be",
        "options": [
            "reported as Fraud",
            "not be reported as Fraud",
            "be reported by Operations Department to RBI",
            "be reported by Security Department to RBI",
            "B & D"
        ],
        "correct_answer": "B & D"
    },
    {
        "question": "The operational Risk Does not include",
        "options": ["Legal Risk", "Reputational Risk", "Strategic Risk", "Both B&C", "A,B and C"],
        "correct_answer": "Both B&C"
    },
    {
        "question": "Which of the following statement is incorrect about KRIs process?",
        "options": [
            "Internal and external loss data studied and trend is identified and analysed for identification of KRIs.",
            "Internal and external audit reports are also a sources for identification of KRIs.",
            "Business lines without conjunction with RMD should identify the KRIs. RMD only monitors the performance of KRIs.",
            "Business Lines are encouraged to conduct internal workshops to identify high risks and define KRIs to track the same.",
            "KRIs shall be developed based on the risk events that have been identified as having a high inherent or residual risk."
        ],
        "correct_answer": "Business lines without conjunction with RMD should identify the KRIs. RMD only monitors the performance of KRIs."
    },
    {
        "question": "As per Bank's Operational Risk Management Policy, Syndication of Loan activity of a bank is mapped to which of the Business Line?",
        "options": ["Corporate Finance", "Commercial Banking", "Retail Banking", "Agency Services", "Retail Brokerage"],
        "correct_answer": "Corporate Finance"
    },
    {
        "question": "Lagging Indicators are one which are----------?",
        "options": [
            "Accurate in prediction",
            "Predictive in nature",
            "Detective in nature and based on historical measures.",
            "Helps in detecting and managing risk before it actually happens.",
            "Helps in benchmarking."
        ],
        "correct_answer": "Detective in nature and based on historical measures."
    },
{
        "question": "Key risk indicator process give us insight into how key risk process works. Who is responsible for KRIs management?",
        "options": ["Only Risk Department", "Every department", "Only compliance department", "Only audit & inspection department", "Central office top management"],
        "correct_answer": "Every department"
    },
    {
        "question": "Under Revised standardised approach Business indicator (BI) is defined as, BI = ILDC + SC + FC. What FC denotes?",
        "options": ["Fiscal component", "Financial component", "Factoring component", "Future value component", "Future risk component"],
        "correct_answer": "Financial component"
    },
    {
        "question": "Under Standardised approach of Operational Risk Calculation, which is not one of the business lines?",
        "options": ["Retail Banking", "Corporate Banking", "Forex Banking", "Trading", "Asset Management"],
        "correct_answer": "Forex Banking"
    },
    {
        "question": "KRI should have an escalation matrix in place. Risk indicator should ---------.",
        "options": [
            "Have an explicit relationship with the specific risk whose exposure it represents.",
            "Independent of the specific risk whose exposure it presents",
            "Give broader information about various risks in banks",
            "Be dependent upon the external variables for getting the information and data",
            "Not be benchmarked with any other KRIs."
        ],
        "correct_answer": "Have an explicit relationship with the specific risk whose exposure it represents."
    },
    {
        "question": "From the given main areas of Operational risk find the odd one out",
        "options": ["People", "Process", "System", "External Events", "Interest Rate Risk"],
        "correct_answer": "Interest Rate Risk"
    },
    {
        "question": "Under Revised standardised approach Business indicator (BI) is defined as, BI = ILDC + SC + FC. What ILDC denotes?",
        "options": [
            "Investment, lease and discount component",
            "Interest, lease and discount component",
            "Investment, lease and dividend component",
            "Interest, loan and dividend component",
            "Interest, lease and dividend component"
        ],
        "correct_answer": "Interest, lease and dividend component"
    },
    {
        "question": "As per Basel-III recommendations, which of the followings is NOT an approach to calculate Operational Risk?",
        "options": [
            "Basic Indicator Approach",
            "The Standardized Approach",
            "Advanced Measurement Approach",
            "Internal Model Approach",
            "None of the above"
        ],
        "correct_answer": "Internal Model Approach"
    },
    {
        "question": "As prescribed by RBI, 'Selling of Gold on consignment basis' services is categorised in which Business Line?",
        "options": ["Retail Banking", "Commercial Banking", "Corporate Finance", "Agency Services", "Investment Banking"],
        "correct_answer": "Investment Banking"
    },
    {
        "question": "The indicators which helps an organization determine the success of its key risk indicators",
        "options": ["Key performance Indicators", "Key Success Indicator", "Key Control Indicators", "Key risk Indicators", "key win indicators"],
        "correct_answer": "Key Control Indicators"
    },
    {
        "question": "The predictors of adverse events which are likely to impact organizations is known as",
        "options": ["Key Risk Identifiers", "Key Risk Indicators", "Key Lead Indicators", "Potential Loss", "Near Miss events"],
        "correct_answer": "Key Risk Indicators"
    },
    {
        "question": "Which of the following is not a characteristic of KRIs?",
        "options": [
            "KRIs shall be useful to management in taking decision",
            "KRIs should be quantifiable",
            "KRIs should work as early warning indicator",
            "KRIs should have comparability through benchmarking.",
            "KRIs should be made up from leading indicators only."
        ],
        "correct_answer": "KRIs should be made up from leading indicators only."
    },
    {
        "question": "Which Indicators are those which are predictive in nature?",
        "options": ["Lagging", "Leading", "Forward", "Future", "Neutral"],
        "correct_answer": "Leading"
    },
    {
        "question": "Which of the following is part of operational risk:",
        "options": ["Legal Risk", "Reputational Risk", "Strategic Risk", "Option b & c are correct", "Option a & b are correct"],
        "correct_answer": "Legal Risk"
    },
    {
        "question": "A key risk indicator is a measure used by bank management to indicate how risky an activity is. KRIs are tools for?",
        "options": [
            "Monitoring controls, risk drivers, and exposure which can provide insights into potential risk events.",
            "Complying with RBI Guidelines",
            "For audit of particular department",
            "Information collection of competitors risk exposure",
            "For capital calculation"
        ],
        "correct_answer": "Monitoring controls, risk drivers, and exposure which can provide insights into potential risk events."
    },
    {
        "question": "Basic indicator approach (BIA), The standard approach (TSA) and Advance measurement approach (AMA) are used for which capital calculation?",
        "options": ["Operational Risk", "Legal Risk", "Market Risk", "Credit Risk", "Liquidity risk"],
        "correct_answer": "Operational Risk"
    },
{
        "question": "The customer service in a bank branch, has been delayed for two hours, due to failure of central server. What type of risk it is?",
        "options": ["Reputational risk", "Operational Risk", "Settlement Risk", "Systemic Risk", "Systematic Risk"],
        "correct_answer": "Operational Risk"
    },
    {
        "question": "'Payment Credited to the wrong account' is an example of:",
        "options": ["Credit Risk", "Operational Risk", "Market Risk", "Liquidity Risk", "Account Risk"],
        "correct_answer": "Operational Risk"
    },
    {
        "question": "The Risk control and self-assessment (RCSA) process does not take place at",
        "options": ["Unit Level", "Organisation Level", "product level", "Process Level", "People Level"],
        "correct_answer": "Organisation Level"
    },
    {
        "question": "Finding Key Risk Indicators and Doing RCSA exercise is one other technique of Risk Management. Conducting RCSA come under purview of which of the following?",
        "options": ["ORMC", "CRMC", "GRMC", "ALCO", "ESGSC"],
        "correct_answer": "ORMC"
    },
    {
        "question": "Which of the following is a type of operational Risk?",
        "options": ["Strategic Risk", "Reputational Risk", "Default Risk", "People Risk", "Interest risk"],
        "correct_answer": "People Risk"
    },
    {
        "question": "Transaction Risk comes under",
        "options": ["people Risk", "System Risk", "Technology Risk", "Digital risk", "Process Risk"],
        "correct_answer": "Process Risk"
    },
    {
        "question": "A risk event is an incident/experience that has caused or has the potential to cause material loss to the bank. Which of the following is not a correct option for recognizing risk events?",
        "options": ["Experience", "Judgement", "Intuition", "Linked events", "Recurring events"],
        "correct_answer": "Recurring events"
    },
    {
        "question": "Which of the following is not a major activity of KRIs framework?",
        "options": ["Developing KRIs", "Monitoring KRIs", "Follow-up Breaches", "Setting up reasonable threshold", "Reporting to RMD"],
        "correct_answer": "Reporting to RMD"
    },
    {
        "question": "As per RBI definition, which of following is NOT a part of the Operational Risk?",
        "options": ["Legal risk", "Reputational risk", "Internal frauds", "External frauds", "All are part of Operational Risk"],
        "correct_answer": "Reputational risk"
    },
    {
        "question": "Under KRIs, which roles and responsibility is not correctly matched with the associated department?",
        "options": [
            "Business line- Identification of KRIs",
            "Risk Management department- Monthly reporting on KRI breach.",
            "Risk management department - Provide independent assurance around the KRI process.",
            "Business lines- Monitor position against targets and limits.",
            "Internal Audit department - Incorporate output in the audit plan."
        ],
        "correct_answer": "Risk management department - Provide independent assurance around the KRI process."
    },
    {
        "question": "Under Revised standardised approach Business indicator (BI) is defined as, BI = ILDC + SC + FC. What SC denotes?",
        "options": ["Service component", "Security component", "Solvency component", "Seniority component", "Sector component"],
        "correct_answer": "Service component"
    },
    {
        "question": "Which of the following is not an approach to calculate Operational Risk?",
        "options": [
            "Basic indicator approach",
            "The new standardised approach",
            "Standard Measurement Approach",
            "Advanced measurement approach",
            "The standardised approach"
        ],
        "correct_answer": "Standard Measurement Approach"
    },
    {
        "question": "Which of the following is not a type of operational Risk?",
        "options": ["Strategic Risk", "Legal Risk", "Natural disaster", "Regulatory Risk", "Fraud"],
        "correct_answer": "Strategic Risk"
    },
    {
        "question": "Now a days, banking is more relied on IT system for executing banking transactions, which element of Operational Risk is become more crucial for bank?",
        "options": ["Internal People", "Process", "System", "External Events", "Cyber Security"],
        "correct_answer": "System"
    },
    {
        "question": "Which statement is incorrect about the KRIs analysis and revision?",
        "options": [
            "KRIs are evolving in nature and analysis of actual loss and near miss event helps in identifying the best KRIs.",
            "Best KRIs are those which are good in providing early warning which allows timely action.",
            "Periodic review needs to be taken up regarding the indicators themselves to ensure they remain aligned with the changing business environment",
            "The review of the relevance and effectiveness of KRIs shall be taken up at a Bank wide level once every year.",
            "Periodic reviews are taken to check the effectiveness of indicators and their associated threshold."
        ],
        "correct_answer": "The review of the relevance and effectiveness of KRIs shall be taken up at a Bank wide level once every year."
    },
{
        "question": "When does a risk indicator become 'Key risk indicator'?",
        "options": [
            "When it can function on minimal data",
            "When it represent a key risk which is critical for bank",
            "When it can indicate a little about a lot of risks",
            "When it is cost effective to implement irrespective of quality of result it gives.",
            "When it is in form of leading indicator only."
        ],
        "correct_answer": "When it represent a key risk which is critical for bank"
    },
    {
        "question": "Which of the following is not a type of risk in Banking Sector?",
        "options": ["Credit Risk", "Operational Risk", "Market Risk", "Liquidity Risk", "Account Risk"],
        "correct_answer": "Account Risk"
    },
    {
        "question": "When a bank chooses the wrong strategy or follow a long-term business strategy which might lead to its failure, it is called",
        "options": ["Credit Risk", "Business Risk", "Operational Risk", "Market Risk", "Reputational Risk"],
        "correct_answer": "Business Risk"
    },
    {
        "question": "Banks factor their Unexpected Loss by way of",
        "options": ["Rating", "Provisioning", "Pricing", "Insurance", "Capital"],
        "correct_answer": "Capital"
    },
    {
        "question": "Which of the following is a Financial Risk?",
        "options": ["Operational Risk", "Reputational Risk", "Legal Risk", "Strategic Risk", "Credit Risk"],
        "correct_answer": "Credit Risk"
    },
    {
        "question": "To calculate capital adequacy ratio, which of the following risks must banks take into account?",
        "options": [
            "Credit Risk",
            "Market Risk",
            "Operational Risk",
            "Credit risk, market risk and operational risk",
            "Credit risk and operational risk"
        ],
        "correct_answer": "Credit risk, market risk and operational risk"
    },
    {
        "question": "Which statement is not correct with regards to CRO in bank?",
        "options": [
            "CRO is having business targets and variable pay structure linked with target achievement",
            "CRO is appointed on the approval of Board",
            "CRO shall directly report to MD & CEO",
            "CRO shall be member of all CO level credit approval committees",
            "CRO is the head of Risk Management Functions of Bank"
        ],
        "correct_answer": "CRO is having business targets and variable pay structure linked with target achievement"
    },
    {
        "question": "Which of the following is not a source of capital for banks?",
        "options": ["Govt. equity infusion", "Deposits of the customers", "Shareholders' equity", "Reserved and Surplus", "Perpetual Non-Cumulative Preference Shares"],
        "correct_answer": "Deposits of the customers"
    },
    {
        "question": "Risk and Return have what relation?",
        "options": ["Profit", "Indirect", "Natural", "Direct", "Negative"],
        "correct_answer": "Direct"
    },
    {
        "question": "Which of the following is not a systemic risk?",
        "options": ["Market Risk", "Interest rate Risk", "purchasing power risk", "financial risk", "both C & D"],
        "correct_answer": "financial risk"
    },
    {
        "question": "Please fill the blanks. Higher the risk ….......... the premium or Interest?",
        "options": ["Lower", "Less", "Higher", "Easier", "No effect on premium"],
        "correct_answer": "Higher"
    },
    {
        "question": "Risk that could arise due to legal actions or uncertainty of interpretations of contracts and agreements is called:",
        "options": ["Legal Risk", "Contract Risk", "Country risk", "Market Risk", "Counter-party Risk"],
        "correct_answer": "Legal Risk"
    },
    {
        "question": "Data adequacy, model assumptions and methodology error etc comes under",
        "options": ["process Risk", "Technology Risk", "Model Risk", "People Risk", "credit risk"],
        "correct_answer": "Model Risk"
    },
    {
        "question": "Which is not a type of Financial Risk?",
        "options": ["Operational Risk", "Market Risk", "Credit risk", "Liquidity risk", "Solvency Risk"],
        "correct_answer": "Operational Risk"
    },
    {
        "question": "An example of risk mitigation is:",
        "options": [
            "Doing extensive research in the development of product to reduce the probability of failure of product in market",
            "Purchasing insurance",
            "Eliminating the cause of a risk",
            "Option a, b & c are correct",
            "Option a & b are correct"
        ],
        "correct_answer": "Option a & b are correct"
    },
{
        "question": "Which of the following condition is cause of strategic risk?",
        "options": [
            "Weak execution of decisions",
            "Insufficient resource allocation",
            "Inability to respond well to change in the market conditions",
            "Options b & c are correct",
            "Options a, b & c are correct"
        ],
        "correct_answer": "Options a, b & c are correct"
    },
    {
        "question": "What better explains the meaning of risk in banking business?",
        "options": [
            "Probability of loss that could arise due to uncertainty",
            "Risk due to loss as a result of uncertainty",
            "Loss arising on happening of some event",
            "Loss arising on non-happening of some event",
            "Probability of risk that could arise due to uncertainty"
        ],
        "correct_answer": "Probability of loss that could arise due to uncertainty"
    },
    {
        "question": "Non compliance to KYC and AML guidelines are coming under",
        "options": ["Compliance Risk", "KYC Risk", "AML Risk", "Regulatory Risk", "Legal Risk"],
        "correct_answer": "Regulatory Risk"
    },
    {
        "question": "When Bank's image and public standing is in doubt and leads to public's loss of confidence in a bank, it is called as",
        "options": ["Reputational Risk", "Moral Hazard", "Operational Risk", "Market Risk", "Systematic Risk"],
        "correct_answer": "Reputational Risk"
    },
    {
        "question": "Which Committee makes recommendations to the Board of Directors on strategic decisions?",
        "options": ["ALCO", "CRMC", "ORMC", "Investment Committee", "Risk Management Committee"],
        "correct_answer": "Risk Management Committee"
    },
    {
        "question": "Risk associated with failure of banks in payment of amount representing clearing cheques presented by collecting banks is called as",
        "options": ["Liquidity Risk", "Settlement Risk", "Credit Risk", "Legal Risk", "Clearing Process Risk"],
        "correct_answer": "Settlement Risk"
    },
    {
        "question": "…………….. risk arises because of the fact that the financial system is one intricate and connected network",
        "options": ["Credit", "Operational", "Market", "Systemic", "Account"],
        "correct_answer": "Systemic"
    },
    {
        "question": "Legal Risk, from banking point of view is known as -",
        "options": [
            "When the actions can lead to the financial system coming to a standstill.",
            "When there is a financial loss to bank arising from legal suits filed against the bank or by a bank for applying a law wrongly",
            "When a bank chooses the wrong strategy or follow a long-term business strategy which might lead to its failure",
            "When bank's image and public standing is in doubt and leads to public's loss of confidence in a bank",
            "When any Regulator take an action against bank and threatens to revoke the license"
        ],
        "correct_answer": "When there is a financial loss to bank arising from legal suits filed against the bank or by a bank for applying a law wrongly"
    },
    {
        "question": "In Mini CRMC for credit spurt in advances is considered for advance increase to the extent of",
        "options": ["10", "15", "20", "25", "30"],
        "correct_answer": "20"
    },
    {
        "question": "In Mini CRMC meeting Agenda the number of days overdue of rating is",
        "options": ["30", "60", "90", "180", "365"],
        "correct_answer": "180"
    },
    {
        "question": "Under Mini ORMC the agenda related to pending suspense entries is beyond",
        "options": ["3 Months", "6 Months", "60 days", "30 days", "45 days"],
        "correct_answer": "6 Months"
    },
    {
        "question": "Following is not an agenda under Mini ORMC",
        "options": ["Fraud in Loans and Advances", "Frauds happened in branch", "Increase in stressed accounts", "spurt in credit portfolio", "Both C&D"],
        "correct_answer": "Both C&D"
    },
    {
        "question": "Which of the following is not an agenda in Mini ALCO",
        "options": ["Deposit portfolio", "analysis of bulk deposits", "Maturity of deposits", "Dormant accounts", "Business continuity plan"],
        "correct_answer": "Business continuity plan"
    },
    {
        "question": "Which of the following is not an Mini CRMC Agenda",
        "options": ["performance of MSME advances", "Performance of retail Advances", "performance of MSME Products", "Frauds in Advances", "Both C&D"],
        "correct_answer": "Frauds in Advances"
    },
    {
        "question": "Which of the following is not an agenda in Mini CRMC",
        "options": ["Stressed Assets portfolio", "Undrawn Limits", "Interest rate wise advance portfolio", "NPA Portfolio", "Credit Spurt during the quarter"],
        "correct_answer": "Interest rate wise advance portfolio"
    }

        ]
        
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'questions_answered' not in st.session_state:
            st.session_state.questions_answered = []

    def next_question(self):
        st.session_state.current_question += 1
        
    def restart_quiz(self):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.questions_answered = []

    def run(self):
        st.title("U Aspire Quiz")
        
        # Display progress
        progress = st.progress(st.session_state.current_question / len(self.quiz_data))
        st.write(f"Question {st.session_state.current_question + 1} of {len(self.quiz_data)}")
        st.write(f"Score: {st.session_state.score}")
        
        # Display current question
        question = self.quiz_data[st.session_state.current_question]
        st.write(f"\n{question['question']}")
        
        # Display options as radio buttons
        answer = st.radio("Choose your answer:", question['options'], key=f"q_{st.session_state.current_question}")
        
        # Submit button
        if st.button("Submit Answer"):
            if answer == question['correct_answer']:
                st.success("Correct!")
                if st.session_state.current_question not in st.session_state.questions_answered:
                    st.session_state.score += 1
            else:
                st.error(f"Wrong! The correct answer is: {question['correct_answer']}")
            
            st.session_state.questions_answered.append(st.session_state.current_question)
            
            # Move to next question
            if st.session_state.current_question < len(self.quiz_data) - 1:
                st.button("Next Question", on_click=self.next_question)
            else:
                st.balloons()
                st.success(f"Quiz completed! Final score: {st.session_state.score}/{len(self.quiz_data)}")
                st.button("Restart Quiz", on_click=self.restart_quiz)

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()