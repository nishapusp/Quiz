import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
        {
        "question": "Wealth Management Vertical deals with",
        "options": ["Third Party Products Marketing", "Home loans", "Car Loans", "Retail Loans", "Forex transactions"],
        "correct_answer": "Third Party Products Marketing"
    },
    {
        "question": "_____ policy from Bajaj Allianz General Insurance Company, catering to the needs of HNI customers",
        "options": ["Chola Farmer Care Package", "UNICARE", "PINK Health", "Rubeca", "Winzard"],
        "correct_answer": "UNICARE"
    },
    {
        "question": "Women's Cancer Plan covering 3 major cancers identified in women. This is a Benefit plan where entire sum insured will be paid to the customer on detection of any of the 3 cancers. Hospitalization is not mandatory.",
        "options": ["Chola Farmer Care Package", "UNICARE", "PINK Health", "Rubeca", "Winzard"],
        "correct_answer": "PINK Health"
    },
    {
        "question": "ASBA facility is available through",
        "options": ["Call", "WhatsApp", "Signed letter", "Physical Application", "Signed Chit"],
        "correct_answer": "Physical Application"
    },
    {
        "question": "Sovereign Gold Bonds facility is available through",
        "options": ["Call", "WhatsApp", "Signed letter", "Signed Chit", "Physical Application and Internet Banking"],
        "correct_answer": "Physical Application and Internet Banking"
    },
    {
        "question": "_____ platform has been launched for paperless investment in Mutual Funds by customers through branches. The platform has tie-up with BSE Star and presently has 18 MF houses.",
        "options": ["UnionInvest", "UniSure", "UniPure", "UniMiles", "UniByte"],
        "correct_answer": "UnionInvest"
    },
    {
        "question": "Unique Selling Proposition (USP's) of Mahila Samman Savings Certificate, 2023 is that the deposit will bear interest at the rate of ___ per annum compounded quarterly with effective interest rate of roughly ____",
        "options": ["7.4%, 7.7%", "7.4%, 7.7%", "7.5%, 7.6%", "7.5%, 7.7%", "7.8%, 7.9%"],
        "correct_answer": "7.5%, 7.7%"
    },
    {
        "question": "The facility of E-Stamping, which helps the bank generate non-interest income on value of e-Stamp Paper issued is being offered across ___ states.",
        "options": ["26", "18", "14", "21", "29"],
        "correct_answer": "21"
    },
    {
        "question": "Government Business Link Officers (GBLOs) are requested to ensure the monthly submission of Monthly Marketing Report (MMR) by ___ of succeeding month.",
        "options": ["30th/31st (last day)", "7th", "1st", "15th", "18th"],
        "correct_answer": "7th"
    },
    {
        "question": "Our bank has entered into breakthrough MOU's with __ prestigious departments/establishments for opening of various types of accounts",
        "options": ["11", "12", "13", "14", "15"],
        "correct_answer": "11"
    },
    {
        "question": "Penal interest for wrong claims for violation or noncompliance of instructions issued by Government or RBI shall attract imposition of penalty of:",
        "options": [
            "Penal interest at Bank Rate as notified by RBI plus 0.5% for any wrong claims of agency commission settled",
            "Penal interest at Bank Rate as notified by RBI plus 1% for any wrong claims of agency commission settled",
            "Penal interest at Bank Rate as notified by RBI plus 2% for any wrong claims of agency commission settled",
            "Penal interest at Bank Rate as notified by RBI plus 2.5% for any wrong claims of agency commission settled",
            "Penal interest at Bank Rate as notified by RBI plus 4% for any wrong claims of agency commission settled"
        ],
        "correct_answer": "Penal interest at Bank Rate as notified by RBI plus 2% for any wrong claims of agency commission settled"
    },
    {
        "question": "The number of transactions eligible for payment of agency commission should not exceed ___ per pensioner per year. This includes payment of net pension and payment for arrears.",
        "options": ["12", "13", "14", "15", "16"],
        "correct_answer": "14"
    },
    {
        "question": "The following activities do not come under the purview of agency bank and are not eligible for agency commission",
        "options": [
            "Revenue receipts of Central/State Governments",
            "Furnishing of bank guarantees by Government Contractors",
            "Pension payments",
            "Payments on behalf of Central/State Governments",
            "None of the above"
        ],
        "correct_answer": "Furnishing of bank guarantees by Government Contractors"
    },
    {
        "question": "The commission per transaction on payment for State/ Central Pension is:",
        "options": ["Rs. 40", "Rs. 60", "Rs. 75", "Rs. 90", "Rs. 110"],
        "correct_answer": "Rs. 75"
    },
    {
        "question": "The commission per transaction on payment for Kisan Vikas Patra is:",
        "options": ["3.5 paise per Rs100/-", "4.5 paise per Rs100/-", "5.5 paise per Rs100/-", "6.5 paise per Rs100/-", "8.5 paise per Rs100/-"],
        "correct_answer": "6.5 paise per Rs100/-"
    },
    {
        "question": "A grievance shall be considered as disposed-off and closed when: (a) Bank has acceded to the request of the complainant fully (b) complainant has indicated in writing, its acceptance of the response of the Bank (c) complainant has not preferred any appeal within 30 days from the date of receipt of resolution",
        "options": ["Only (a) is correct", "Both (a) and (b) are correct", "All are correct", "Only (c) is correct", "None of the above"],
        "correct_answer": "Both (a) and (b) are correct"
    },
    {
        "question": "As per directives from Reserve Bank of India, any complaints rejected fully or partially by the bank need to be vetted from the …………….",
        "options": ["Banking Ombudsman", "Internal Ombudsman", "Integrated Ombudsman", "External Ombudsman", "None of the above"],
        "correct_answer": "Internal Ombudsman"
    },
    {
        "question": "Which of the following complaints are routed through CRM Edge for their resolution: (a) Received at RO (b) CPGRAMS/INGRAMS (c) Banking Ombudsman",
        "options": ["Only (a) is correct", "(b) and (c) are correct", "(a) and (c) are correct", "All are correct", "None of the above"],
        "correct_answer": "All are correct"
    },
    {
        "question": "In which of the following scenarios can a customer move to Banking Ombudsman office against the Bank (a) Complaint was rejected by the Bank (b) Complaint was resolved by the Bank (c) No resolution was provided by the Bank within 30 Days",
        "options": ["All are correct", "Only (a) and (c) are correct", "Only (a) is correct", "Only (c) is correct", "None of the above"],
        "correct_answer": "All are correct"
    },
    {
        "question": "Which of the following is the initiative taken by our Bank for offering real-time assistance regarding products, circulars, policy guidelines to our staff",
        "options": ["CRM Edge", "My Diary Portal", "Union Sampark", "Union Disha", "None of the above"],
        "correct_answer": "Union Sampark"
    },
{
    "question": "Under Union Sampark, an in house dedicated helpline to clear all Day to Day Banking related doubts is?",
    "options": ["9419230077", "8975752211", "8976752211", "8976762211", "None of the above"],
    "correct_answer": "8976752211"
},
{
    "question": "A physically challenged customer complained that ramp facility is not available at branch. What is the TAT to resolve such complaint?",
    "options": ["7 Days", "15 Days", "30 Days", "45 Days", "None of the above"],
    "correct_answer": "7 Days"
},
{
    "question": "Which of the following is NOT a responsibility of the Regional Grievance Redressal Officer (GRO)?",
    "options": ["Monitoring complaints of the region on a daily basis", "Ensuring rejected complaints are not pending for recommendation", 
                "Vetting the complaints after rejection", "Responding to queries from the Chief Grievance Officer (CGO) and Internal Ombudsman (IO)", 
                "None of the above"],
    "correct_answer": "Vetting the complaints after rejection"
},
{
    "question": "What is the cash remittance limit allowed for transport in an Auto Rickshaw (Three-Wheeler)?",
    "options": ["₹ 50 Lakh", "₹ 5 Lakh", "₹ 10 Lakh", "₹ 20 Lakh", "None of the above"],
    "correct_answer": "₹ 50 Lakh"
},
{
    "question": "When are two armed guards mandatory during cash remittance?",
    "options": ["For cash amounts above Rs.200 lakhs", "For cash amounts above Rs.100 lakhs", 
                "For cash amounts above Rs.500 lakhs", "For cash amounts above Rs.50 lakhs", 
                "None of the above"],
    "correct_answer": "For cash amounts above Rs.200 lakhs"
},
{
    "question": "Which category of notes should NOT be accepted by bank branches for exchange due to their condition?",
    "options": ["Soiled notes with both pieces pasted together", 
                "Notes that are extremely brittle, burnt, or inseparably stuck together",
                "Mutilated notes missing a small portion", 
                "Soiled notes with normal wear and tear",
                "None of the above"],
    "correct_answer": "Notes that are extremely brittle, burnt, or inseparably stuck together"
},
{
    "question": "While accepting the cash deposit of ₹ 2 Lakh from the customer, branch detected 5 counterfeit notes. What course of action should be adopted?",
    "options": ["Return the notes to the customer", "Send the notes to police authorities at the end of the month",
                "Send the notes immediately to Police authorities", "Ask the customer to exchange the fake notes with original ones",
                "None of the above"],
    "correct_answer": "Send the notes immediately to Police authorities"
},
{
    "question": "While accepting Cash from a customer you detected a note with slogans and message of a political nature written across it. What will you do?",
    "options": ["Accept the Note", "Reject the Note", "Accept and keep it with soiled notes", 
                "Accept half value of the note", "None of the above"],
    "correct_answer": "Reject the Note"
},
{
    "question": "According to the guidelines, how frequently should the keys to the cash safe be exchanged with the duplicate set?",
    "options": ["Every 6 months", "Once in a year", "Every two years", "When directed by Auditor", "None of the above"],
    "correct_answer": "Every two years"
},
{
    "question": "In case of exigencies, what is the procedure if late cash is received after the closing of SOL operations in Finacle?",
    "options": ["Credit it to the customer's account immediately", 
                "Keep it in the drawer and record it as a receipt the next week",
                "Record it in the Cash Balance Book and update the system the next day", 
                "Reject the cash and return it to the customer",
                "None of the above"],
    "correct_answer": "Record it in the Cash Balance Book and update the system the next day"
},
{
    "question": "How often must the Concurrent Auditors (CAs) of a bank verify Currency Chest transactions?",
    "options": ["Daily", "Fortnightly", "Weekly", "Monthly", "None of the above"],
    "correct_answer": "Weekly"
},
{
    "question": "When is the Concurrent Auditor required to certify the balances of the Currency Chest?",
    "options": ["First day of April and May", "Last working day of February and March", 
                "Last working day of January and February", "Last day of June and July", 
                "None of the above"],
    "correct_answer": "Last working day of February and March"
},
{
    "question": "During the bi-monthly verification of balances of the Currency Chest, what percentage of the balances should be subjected to detailed verification through Note sorting machines?",
    "options": ["2%", "5%", "10%", "15%", "20%"],
    "correct_answer": "2%"
},
{
    "question": "How frequently should the balances of each Currency Chest be verified by officials deputed by the Zonal Office(ZO)?",
    "options": ["Quarterly", "Annually", "Half-yearly", "Bi-monthly", "None of the above"],
    "correct_answer": "Half-yearly"
},
{
    "question": "What is the minimum amount that can be deposited into or withdrawn from a currency chest?",
    "options": ["₹ 2,00,000", "₹ 1,50,000", "₹ 1,00,000", "₹ 50,000", "None of the above"],
    "correct_answer": "₹ 1,00,000"
},
{
    "question": "By what time must currency chests report all transactions through the CyM - CC portal on the same day?",
    "options": ["5PM", "6PM", "7PM", "8PM", "9PM"],
    "correct_answer": "7PM"
},
{
    "question": "Which of the following is a new menu for updating of mobile number in customer accounts through OTP validation?",
    "options": ["MODCD", "SCRM", "MOBREG", "SMSREG", "None of the above"],
    "correct_answer": "MODCD"
},
{
    "question": "Under centralized sending of overdue Locker notices recently adopted by our bank, the first notice will be sent after…………days of due date.",
    "options": ["2", "5", "7", "10", "15"],
    "correct_answer": "7"
},
{
    "question": "Our Bank launched a performance recognition drive exclusively for Currency Chests from 1st June to 30th September 2024. What is the name given to drive?",
    "options": ["Currency Performers - 2024", "Currency to Profit - 2024", "Mudra Shakti - 2024", 
                "Mudra se Munafa - 2024", "None of the above"],
    "correct_answer": "Mudra se Munafa - 2024"
},
{
    "question": "For offering hassle free customer service and to resolve customer query regarding cheque book status at the Branch level, our Bank has made cheque book dispatch details available in …….menu in Finacle.",
    "options": ["HCHBM", "CHQBOOK", "Both A & B", "CUSTVIEW", "None of the above"],
    "correct_answer": "Both A & B"
},
{
    "question": "Which of the following are recently added features in My diary Portal? (a) Zoho CRM Complaint Dashboard (b) Direct Selling Agent Information (c) Attrition Risk",
    "options": ["All are correct", "None are correct", "Only (a) and (b)", "Only (b) and (c)", "Only (a) and (c)"],
    "correct_answer": "All are correct"
},
{
    "question": "Which of the following functions are available in CRM Edge: (a) Account statement (b) Account lien details (c) Standing instructions?",
    "options": ["None of the above", "All of the above", "Only (a) is correct", "Only (c) is correct", "Only (b) is correct"],
    "correct_answer": "All of the above"
},
{
    "question": "In CRM Edge, Service request pending for more than………days will be treated as complaints",
    "options": ["2", "3", "4", "5", "6"],
    "correct_answer": "3"
},
{
    "question": "A customer having account in base branch A approaches your branch and wants to register a complain against branch A at your branch. What would you do?",
    "options": ["Tell the customer to register complaint at Branch A", "Take the complaint and register in Union Samadhan portal", 
                "Take the complaint and register in CRM Edge", "Take the complaint and mail it to Branch", "None of the above"],
    "correct_answer": "Take the complaint and register in CRM Edge"
},
{
    "question": "As per recent RBI guidelines, what will be the frequency of reporting of credit information by Credit Institutions including Banks to Credit Information Companies(CICs)?",
    "options": ["Bi-monthly", "Weekly", "Monthly", "Fortnightly", "None of the above"],
    "correct_answer": "Fortnightly"
},
{
    "question": "In honour of which Hockey Player, Hockey India announced the retirement of the No. 16 jersey, from the national senior men's team?",
    "options": ["Lalit Upadhyay", "PR Sreejesh", "Rajkumar Pal", "Harmanpreet Singh", "None of the above"],
    "correct_answer": "PR Sreejesh"
},
{
    "question": "Recently World Health Organization (WHO) declared Public Health Emergency of International Concern (PHEIC) for………infection",
    "options": ["Monkeypox", "chickenpox", "Nipah Virus", "Covid 19", "None of the above"],
    "correct_answer": "Monkeypox"
},
{
    "question": "Under Customer Service Excellence Matrix, how many marks out of 100 are allocated for Grievance Redressal & Service Requests",
    "options": ["10", "15", "20", "25", "30"],
    "correct_answer": "25"
},
{
    "question": "Consider the following statements on CRM Edge and select the right answer: 1. Statement of closed accounts can be viewed. 2. WhatsApp message containing link to download Vyom App can be sent. 3. Complaints are not auto escalated in CRM Edge.",
    "options": ["All are correct", "Only (1) and (2) are Correct", "Only (2) and (3) are correct", 
                "Only (1) is correct", "None of the above"],
    "correct_answer": "Only (1) and (2) are Correct"
},
{
    "question": "The Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act was enacted in the year",
    "options": ["2014", "2013", "2012", "2015", "2006"],
    "correct_answer": "2013"
},
{
    "question": "Bank constitutes 'Sexual Harassment Redressal Committee [SHRC] in compliance of which section of the Anti-Sexual Harassment Law",
    "options": ["5", "3", "2", "6", "4"],
    "correct_answer": "4"
},
{
    "question": "As per policy Meetings of the SHRC shall be conducted at least",
    "options": ["Bi monthly", "Quarterly", "Monthly", "Half yearly", "Annually"],
    "correct_answer": "Half yearly"
},
{
    "question": "Any aggrieved men/woman/transgender may make, in writing, a complaint of sexual harassment at workplace to the concerned Sexual Harassment Redressal Committee empowered herein to deal with the complaint within a period of ______ form date of incident",
    "options": ["Three Months", "One Months", "Five Months", "Two Months", "Six Months"],
    "correct_answer": "Three Months"
},
{
    "question": "Any person including the Respondent, complainant, who is aggrieved by the recommendations of S H R C may file an appeal before the Disciplinary Authority against acceptance of the recommendations within how many days from date of recommendation.",
    "options": ["45", "60", "90", "30", "15"],
    "correct_answer": "90"
},
{
    "question": "On receipt of complaint, SHRC shall send one of the copies received from the aggrieved person to the employee against whom the complaint is made (Respondent) within a period of how many working days",
    "options": ["7", "15", "90", "30", "45"],
    "correct_answer": "7"
},
{
    "question": "The Respondent shall file reply to the complaint along with list of documents, names and addresses of witness/es in support of his/her/their views within period not exceeding how many working days from the date of receipt of documents from the SHRC",
    "options": ["7", "15", "30", "45", "10"],
    "correct_answer": "10"
},
{
    "question": "SHRC should submit its recommendations within a period of how many working days of completion of inquiry to Chief General Manager (HR) or Zonal Head or the Regional Manager as the case may be for taking action",
    "options": ["7", "15", "30", "45", "10"],
    "correct_answer": "10"
},
{
    "question": "Chief General Manager (HR) or Zonal Head or Regional Manager as the case may be should take action on the report of the Committee within a period of how many days from the date of its receipt",
    "options": ["15", "30", "45", "60", "45"],
    "correct_answer": "60"
},
{
    "question": "Any aggrieved Person may make, in writing, a complaint of sexual harassment at workplace to the concerned Sexual Harassment Redressal Committee empowered herein to deal with the complaint within a period of …………. months from the date of incident.",
    "options": ["3", "1", "2", "6", "12"],
    "correct_answer": "3"
},
{
    "question": "Sexual harassment at workplace is a …….. offence.",
    "options": ["rare", "grave", "good", "acceptable", "light"],
    "correct_answer": "grave"
},
{
    "question": "Job Families allocated to eligible employees in",
    "options": ["Scale I to III", "Scale I to IV", "Scale IV and above", "Scale IV & V", "Scale I to VI"],
    "correct_answer": "Scale I to VI"
},
{
    "question": "How Many Job Families defined as per Union Prerna Project?",
    "options": ["8", "9", "7", "6", "5"],
    "correct_answer": "9"
},
{
    "question": "Which job family/es is /are the in the segment of source business?",
    "options": ["Sales, Marketing & Relationship Management", "Treasury, Forex & Corporate Banking", 
                "RAM Credit (incl. MLP, RLP, ALP)", "Only A and B", "All of the above"],
    "correct_answer": "Only A and B"
},
{
    "question": "Which job family/es is /are the in the segment of Manage business?",
    "options": ["RAM Credit (incl. MLP, RLP, ALP)", "Operations (Branch, Back office and Central)", 
                "Credit Monitoring, Collections & Recovery", "All of the above", "Only A and B"],
    "correct_answer": "All of the above"
},
{
    "question": "Which job family is not in the segment of Support business?",
    "options": ["Information Technology", "Human Resources", "RAM Credit (incl. MLP, RLP, ALP)", 
                "Risk, Audit, Compliance & Legal", "Strategy, Finance & Accounts"],
    "correct_answer": "RAM Credit (incl. MLP, RLP, ALP)"
},
{
    "question": "During Process and assigning Job Families to eligible employees, what is the eligibility of employee should be evaluated",
    "options": ["those completing 5 years of service in the Bank 2 years in officer cadre", 
                "those completing 4 years of service in the Bank 2 years in officer cadre",
                "those completing 4 years of service in the Bank 3 years in officer cadre", 
                "those completing 5 years of service in the Bank 3 years in officer cadre",
                "those completing 6 years of service in the Bank 3 years in officer cadre"],
    "correct_answer": "those completing 5 years of service in the Bank 2 years in officer cadre"
},
{
    "question": "Union Bank's DEI Vision is",
    "options": ["The Bank strives to include diversity, equity and inclusion practices at the centre of its day-to-day work and to create an environment of inclusion and belonging for the employees",
                "The Bank strives to include diversity, equity and inclusion practices at the centre of its day-to-day work and to create an environment of belonging for the employees",
                "The Bank strives to include diversity, equality and inclusion practices at the centre of its day-to-day work and to create an environment of inclusion and belonging for the employees",
                "The Bank strives to include digitisation, equity and inclusion practices at the centre of its day-to-day work and to create an environment of inclusion and belonging for the employees",
                "The Bank strives to include diversity, equity and inclusion practices at the centre to create an environment of inclusion and belonging for the employees"],
    "correct_answer": "The Bank strives to include diversity, equity and inclusion practices at the centre of its day-to-day work and to create an environment of inclusion and belonging for the employees"
},
{
    "question": "Diversity refers to who is represented in the workforce, which is not included",
    "options": ["Gender", "Age", "Ethnicity", "Physical and Mental", "HNI"],
    "correct_answer": "HNI"
},
{
    "question": "The term takes into consideration a person's unique circumstances, adjusting treatment accordingly so that the end result is equal",
    "options": ["Equity", "Equality", "Inclusion", "Diversity", "Socialisation"],
    "correct_answer": "Equity"
},
{
    "question": "A workplace is one where employees with all types of differences and disabilities feel valued and have the same opportunities for growth as their peers",
    "options": ["Closed", "Open", "Fair", "Inclusive", "Transparent"],
    "correct_answer": "Inclusive"
},
{
    "question": "If a workplace is a Weighing scale then what are its two balancing plates as per the modules.",
    "options": ["Diversity and Inclusion", "Diversity and Equity", "Equity and Equality", 
                "Transparency and Honesty", "Inclusion and Equity"],
    "correct_answer": "Diversity and Inclusion"
},
{
    "question": "The term refers to fair treatment for all people is",
    "options": ["Inclusion", "socialisation", "Diversity", "Equity", "Equality"],
    "correct_answer": "Equity"
},
{
    "question": "Inclusion inculcates a culture where all employees feel",
    "options": ["Challenged", "Stressed", "Burdened", "More work", "Welcomed"],
    "correct_answer": "Welcomed"
},
{
    "question": "Employee engagement is strongly linked with a sense of",
    "options": ["Inclusion", "Equity", "Equality", "Diversity", "Liaisoning"],
    "correct_answer": "Inclusion"
},
{
    "question": "If a workplace serves as Weighing scale, what serves as the weight to keep both sides balanced",
    "options": ["Equity", "Diversity", "Inclusion", "Transparency", "Fair Practise"],
    "correct_answer": "Equity"
},
{
    "question": "Bank embraces and encourages employees' differences in, which is not included",
    "options": ["Age", "Color", "Ethnicity", "Language", "State Wise"],
    "correct_answer": "State Wise"
},
{
    "question": "Maiden Policy on Diversity, Equity and Inclusion - DEI has been introduced from",
    "options": ["FY 2023 - 24", "FY 2018 -19", "FY 2019 - 20", "FY 2022 - 23", "FY 2016 - 17"],
    "correct_answer": "FY 2023 - 24"
},
{
    "question": "In DEI term E stands for",
    "options": ["Equality", "Equity", "Entrepreneurship", "Engaging", "Employee"],
    "correct_answer": "Equity"
},
{
    "question": "In DEI term D stands for",
    "options": ["Discipline", "Digitalisation", "Digitisation", "Diversity", "Determination"],
    "correct_answer": "Diversity"
},
{
    "question": "In DEI term I stands for",
    "options": ["Inclusivity", "Inclusion", "Inspection", "Inquiry", "Inspire"],
    "correct_answer": "Inclusion"
},
{
    "question": "What is PMS?",
    "options": ["Performance Management System", "Post Market Surveillance", "Performance Marketing Skills", 
                "Pre Managerial Skills", "Portfolio Management Services"],
    "correct_answer": "Performance Management System"
},
{
    "question": "How many phases are there in the revamped Performance appraisal system?",
    "options": ["1", "2", "3", "4", "5"],
    "correct_answer": "4"
},
{
    "question": "How many maximum number of roles can be assigned to an officer, where the strength of the branch officers is more than 3 (including the Branch Manager)?",
    "options": ["5", "1", "2", "3", "None of the above"],
    "correct_answer": "3"
},
{
    "question": "How many maximum number of roles can be assigned to an officer, where the strength of the branch officers is up to 3 (including the Branch Manager)?",
    "options": ["5", "1", "2", "3", "None of the above"],
    "correct_answer": "5"
},
{
    "question": "Operational Risk has been included for first time for calculation of Regulatory Capital requirement under …............?",
    "options": ["Basel-1", "Basel-2", "Basel 3", "Principal for responsible banking", "Basel 2.5"],
    "correct_answer": "Basel-2"
},
{
    "question": "How much Capital conservative buffer (CCB) % is required under Basel-3?",
    "options": ["0.50%", "1.00%", "1.50%", "2.00%", "2.50%"],
    "correct_answer": "2.50%"
},
{
    "question": "Banks classified as D-SIBs will be subjected to additional Common Equity Tier 1 (CET1) capital requirement ranging from 0 to 1.00%. Here D-SIB denotes…...........",
    "options": ["Domestic System important bank", "Domestic systematic important bank", "Domestic systemically international bank",
                "Domestic systemically important bank", "Domestic systematic international bank"],
    "correct_answer": "Domestic systemically important bank"
},
{
    "question": "Liquidity standard, LCR (Liquidity coverage ratio) was introduced in Basel…....",
    "options": ["1", "2", "2.5", "3", "4"],
    "correct_answer": "3"
},
{
    "question": "Internal capital adequacy assessment process (ICAAP) and Supervisory review and evaluation process (SREP) are part of …....... Pillar of Basel 3",
    "options": ["1", "2", "2.5", "3", "4"],
    "correct_answer": "2"
},
{
    "question": "Basel-3 was introduced in response to global financial crisis of 2007-2008. When Basel 3 was introduced globally?",
    "options": ["2008", "2009", "2010", "2011", "2012"],
    "correct_answer": "2010"
},
{
    "question": "Which one is not related to Basel 2?",
    "options": ["Introduction of LCR and NSFR", "Introduction of Operational risk capital calculation", 
                "Internal Capital Adequacy Assessment Process (ICAAP)", 
                "Basic indicator approach of operational risk capital calculation",
                "Market risk capital calculation"],
    "correct_answer": "Introduction of LCR and NSFR"
},
{
    "question": "Which of the following is not part of Pillar II Risk?",
    "options": ["Credit Concentration Risk", "Liquidity Risk", "Market Risk", "Strategic Risk", "Reputational Risk"],
    "correct_answer": "Market Risk"
},
{
    "question": "NSFR (Net stable funding ratio) liquidity measures introduced in which Basel accord?",
    "options": ["Basel-1", "Basel-2", "Basel 3", "Principal for responsible banking", "Basel 2.5"],
    "correct_answer": "Basel 3"
},
{
    "question": "Capital Adequacy Ratio is calculated as a percentage of Capital to Risk Weighted Asset. To calculate capital adequacy ratio, the banks are to consider, which of the following risk?",
    "options": ["Credit Risk, Market Risk and Operational Risk", "Credit Risk only", "Market Risk only", 
                "Operational Risk only", "Credit Risk and Market Risk only"],
    "correct_answer": "Credit Risk, Market Risk and Operational Risk"
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
    "question": "Basel-I was the first set of guidelines issued by BCBS which was focused on credit risk. Banks that operate internationally were required to maintain minimum …… of capital on percent of risk weighed assets.",
    "options": ["7.00%", "9.00%", "6.00%", "11.00%", "8.00%"],
    "correct_answer": "8.00%"
},
{
    "question": "The Common Equity Capital requirement for Banks in India is",
    "options": ["11.50%", "9.00%", "7.50%", "8.00%", "5.50%"],
    "correct_answer": "8.00%"
},
{
    "question": "Minimum Regulatory Capital for Banks in India is",
    "options": ["9.00%", "11.50%", "7.50%", "8.00%", "5.50%"],
    "correct_answer": "11.50%"
},
{
    "question": "Basel-III introduced following two liquidity ratios",
    "options": ["LCR and Current Ratio", "NSFR and Current Ratio", "Current Ratio and Quick Ratio",
                "Current Ratio and Debt Equity Ratio", "LCR and NSFR"],
    "correct_answer": "LCR and NSFR"
},
{
    "question": "Which of the following is not a type of credit risk?",
    "options": ["Concentration Risk", "Downgrade Risk", "Interest Rate Risk", "Country Risk", "Bankruptcy Risk"],
    "correct_answer": "Interest Rate Risk"
},
{
    "question": "Insurance works on which principal of credit risk management?",
    "options": ["Avoiding the risk", "Eliminating the risk", "Transferring the risk", "Accepting the risk", "Managing the risk"],
    "correct_answer": "Transferring the risk"
},
{
    "question": "Which credit risk mitigation technique is based on principal of 'Four eyes are better than two eyes'?",
    "options": ["Portfolio Management & Diversification", "Committee based approach", "Risk Rating and Hurdle Rate", 
                "Insurance and derivatives", "Risk Rating and Hurdle Rate"],
    "correct_answer": "Committee based approach"
},
{
    "question": "Which credit risk mitigation technique is based on principal of 'Don't put all the eggs in one basket'?",
    "options": ["Portfolio Management & Diversification", "Committee based approach", "Risk Rating and Hurdle Rate", 
                "Insurance and derivatives", "Risk Rating and Hurdle Rate"],
    "correct_answer": "Portfolio Management & Diversification"
},
{
    "question": "Hurdle rate for new borrowers is",
    "options": ["CR 3", "CR 4", "CR 5", "CR 6", "CR 2"],
    "correct_answer": "CR 5"
},
{
    "question": "Which of the following limits are not exempted from credit rating?",
    "options": ["MSME loan of Rs. 20 lakhs", "Advance against deposits, NSC, LIC policy", 
                "Direct Agriculture advances up to Rs.1.50 crore", "Union TReDS", "Loans to SHGs"],
    "correct_answer": "Direct Agriculture advances up to Rs.1.50 crore"
},
{
    "question": "A facility is rated for long term and it has secured a long-term rating of BBB-(Minus). As per mapping of external and internal credit rating it is equivalent to which internal rating?",
    "options": ["UCR 5", "UCR 4", "UCR 6", "UCR 2", "UCR 7"],
    "correct_answer": "UCR 5"
},
{
    "question": "An investment grade rating signifies the rating agency's belief that the rated instrument / facility is likely to meet its payment obligations. Which of the following is not an Investment grade rating?",
    "options": ["BBB -", "BB +", "BBB", "AA -", "BBB +"],
    "correct_answer": "BB +"
},
{
    "question": "Credit risk is one of the critical risks faced by the bank and this risk arises from various source of risk drivers. In case, there is default in repayment of Instalment and / or interest, such scenario is called as",
    "options": ["Credit Risk to Bank", "Credit Risk to Customer", "Operational Risk to Bank", 
                "Market Risk to Bank", "Monitoring Risk to Bank"],
    "correct_answer": "Credit Risk to Bank"
},
{
    "question": "Type of Credit Risk which is associated with exposure of any single or group with the potential to produce large losses to threaten the core operations of a bank is:",
    "options": ["Country Risk", "Bankruptcy Risk", "Downgrade Risk", "Concentration Risk", "Settlement Risk"],
    "correct_answer": "Concentration Risk"
},
{
    "question": "M/s. Indigenous Local Pvt Ltd. is a primer exporter firm enjoying credit facility of Rs. 500 Crs under consortium arrangement. Due to COVID-19 pandemic, the firm's business got affected and resulted in deterioration of financial parameter. The result of this development is that the decreased creditworthiness and there is downgrading of Credit Rating. Such downgrading may eventually lead to default, a Credit risk driver to the bank. This will be categorised as … subtype of Credit Risk.",
    "options": ["Downgrade Risk", "Bankruptcy Risk", "Default Risk", "Settlement Risk", "Market Risk"],
    "correct_answer": "Downgrade Risk"
},
{
    "question": "Internal Credit Risk Rating is done by using two models i.e. UBI Model and CRISIL ICON Models. The selection of appropriate model is based on rule based decision process, which includes various parameters. One of the parameters is the total credit exposure (exiting or proposed) of the borrower. What is the threshold limit of total credit exposer of a borrower for using CRISIL ICON model for rating?",
    "options": ["Rs. 5.00 Crore", "Rs. 1.00 Crore", "Rs. 50 Lakh", "Rs. 10.00 Crore", "Rs. 25.00 Crore"],
    "correct_answer": "Rs. 5.00 Crore"
},
{
    "question": "One of the objective of Credit rating process of credit exposer is to estimate ------------ of the account.",
    "options": ["Credit Default", "Expected Loss", "Probability of Default", "Exposure at Default", "Loss Given Default"],
    "correct_answer": "Probability of Default"
},
{
    "question": "Internal Credit Rating process is independent mechanism and rating assessment is based on the expert judgement using model based system. It is possible that human judgement is required to outcome of model based rating and delegated authority may not agree with rating assigned through this process. Under such scenario, Delegated Authority can revise rating by UPGRADING or DOWNGRADING the assigned scores. In this case, Low-side re-rating means",
    "options": ["Decision to upgrade credit rating of a borrower to a lower risk level in the investment grade",
                "Decisions to upgrade/downgrade the credit rating of a borrower whose credit rating falls below the investment grade as per the rating assigned by the rating officer",
                "Decision to downgrade credit rating of a borrower to a higher risk level in the investment grade",
                "Decision to downgrade/upgrade a borrower whose credit rating is above investment grade",
                "Decision to re-rate the credit rating given a lower office / branch"],
    "correct_answer": "Decisions to upgrade/downgrade the credit rating of a borrower whose credit rating falls below the investment grade as per the rating assigned by the rating officer"
},
{
    "question": "Our Bank's Internal rating models are",
    "options": ["UBI II & III, UTR I & II", "UBI I & II, UTR I & II", "UTR I & II", "UBI I & II", "UBI II & III"],
    "correct_answer": "UBI I & II, UTR I & II"
},
{
    "question": "Applicable credit rating model for Commercial Real Estate Exposure of Rs.75 Lakh is",
    "options": ["UBI-I", "UTR-I", "UBI-II", "CRISIL ICON", "Rating not applicable"],
    "correct_answer": "CRISIL ICON"
},
{
    "question": "Union Trade Model I is applicable for rating of exposure",
    "options": ["Rs.25 Lakh to Rs.50 Lakh", "Rs.2 Lakh to Rs.25 Lakh", "Rs.25 Lakh to Rs.100 Lakh", 
                "Rs.50 Lakh to Rs.100 Lakh", "Rs.50 Lakh to Rs.500 Lakh"],
    "correct_answer": "Rs.25 Lakh to Rs.100 Lakh"
},
{
    "question": "Rating model will be decided based on",
    "options": ["Exposure with our Bank only", "Aggregate Exposure", "Existing relation with Bank", 
                "Repayment history", "Asset classification"],
    "correct_answer": "Aggregate Exposure"
},
{
    "question": "M/s. Indigenous Export, a partnership firm of Bhatia family is a reputed sport goods manufacturer having factory unit is SEZ area. This firm is enjoying Term Loan of Rs. 10.00 Crs and Cash Credit limit of Rs. 30.00 Crs under consortium arrangement of three banks. Union Bank of India is a leader of consortium and has 50% share in total financial closure. Which rating model is to be used for doing Internal Credit Rating of this account?",
    "options": ["SME Manufacturing Model of CRISIL ICON", "Large Corporate Model of CRISIL ICON", 
                "SME Services Model of CRISIL ICON", "Trader Model of CRISIL ICON", 
                "Rating done by ECRA is sufficient"],
    "correct_answer": "Large Corporate Model of CRISIL ICON"
},
{
    "question": "Fraud is classified under which Risk?",
    "options": ["Operational Risk", "Legal Risk", "Market Risk", "Credit Risk", "Liquidity risk"],
    "correct_answer": "Operational Risk"
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