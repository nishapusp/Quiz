import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
{
    "question": "What is the maximum limit for repatriation from an NRE (Non-Resident External) account for an NRI?",
    "options": ["No limit", "$10,000 per year", "$1 million per year", "$5 million per year", "$100,000 per year"],
    "correct_answer": "No limit"
},
{
    "question": "Who regulates the movement of Good with respect to Foreign Trade in India?",
    "options": ["Reserve Bank of India (RBI)", "Securities and Exchange Board of India (SEBI)", 
               "Director General of Foreign Trade (DGFT)", "Ministry of External Affairs", "None of the above"],
    "correct_answer": "Director General of Foreign Trade (DGFT)"
},
{
    "question": "Which document serves as a basis for reckoning the date of dispatch of goods in International Trade?",
    "options": ["GST Invoice", "Export License", "Bill of Lading", "Certificate of Origin", "Packing List"],
    "correct_answer": "Bill of Lading"
},
{
    "question": "What is the maximum maturity period of NRE Deposits in our bank?",
    "options": ["5 Years", "1 Year", "7 Years", "10 Years", "None of the above"],
    "correct_answer": "10 Years"
},
{
    "question": "Export Finance in India is insured by?",
    "options": ["ECGC", "NABARD", "SIDBI", "IRDA", "LIC"],
    "correct_answer": "ECGC"
},
{
    "question": "Which type of List ECGC is maintaining for Exporters/Directors/Guarantors of firm availing export credit?",
    "options": ["SAL", "BSAL", "VSAL", "PSAL", "GSAL"],
    "correct_answer": "SAL"
},
{
    "question": "Premium for Pre-Shipment is to be borne by?",
    "options": ["Bank", "Exporter", "50% by Exporter and 50% by Bank", "As per Sanction Terms", 
               "Percentage is decided on the basis of customers Internal Rating"],
    "correct_answer": "Exporter"
},
{
    "question": "Any modification in sanctioned term and conditions should be intimated to ECGC nearest office within?",
    "options": ["30 days", "45 days", "60 days", "90 days", 
               "No need to intimate modification in terms of sanction as it is our internal matter"],
    "correct_answer": "30 days"
},
{
    "question": "While opening a forced loan a/c (Devolved LC or Invoked Guarantee), what is the repayment period to be fed in the system?",
    "options": ["90 days", "30 days", "One day", "As per sanction terms", "180 days"],
    "correct_answer": "One day"
},
{
    "question": "Under Letter of credit Mechanism, the bank opening LC has an obligation to pay",
    "options": ["On receipt of goods by importer", "On the default of importer", 
               "On submission of specified documents in compliance with LC terms", "On request by overseas party", 
               "Any one of the above conditions is satisfied"],
    "correct_answer": "On submission of specified documents in compliance with LC terms"
},

{
    "question": "Under Letter of Credit Mechanism, Banks deal with",
    "options": ["Documents & Goods", "Goods only", "Documents only", "Any one of above as specified in LC terms", "LC Applicant only"],
    "correct_answer": "Documents only"
},
{
    "question": "RMA in SWIFT stands for?",
    "options": ["Relationship Management Application", "Relationship Maintenance Application", 
               "Relationship Monitoring Application", "Relationship Marking Application", "None of the above"],
    "correct_answer": "Relationship Management Application"
},
{
    "question": "Importer has to submit the following form to the authorized dealer at the time of making import payment:",
    "options": ["Form A1", "Form A 2", "Shipping Bill", "Bill of Lading", "Composite declaration Form"],
    "correct_answer": "Composite declaration Form"
},
{
    "question": "If all the terms and conditions are given on the bill of lading document itself is called as:",
    "options": ["Clean bill of lading", "Long form bill of lading", "Short form bill of lading", "Straight bill of lading", "Claused Bill of Lading"],
    "correct_answer": "Long form bill of lading"
},
{
    "question": "At what rate interest is paid to NRI depositor, at the time of settlement of balance in inoperative account, which was transferred to RBI in compliance of Depositor Education and Awareness Fund Scheme, 2014?",
    "options": ["At the same rate at which deposit was accepted", 
               "At the rate which was applicable for Saving Bank Account in respective bank from time to time",
               "At the rate advised by RBI from time to time for the purpose",
               "At the present prevailing rate of deposit",
               "Nil, as no interest is accrued on the balance transferred into DEF"],
    "correct_answer": "At the rate advised by RBI from time to time for the purpose"
},
{
    "question": "How much amount in Indian Rupees, can resident individual, gift to his NRI or OCI Card holder Relative in India?",
    "options": ["Any amount provided the transaction is conducted through banking channel",
               "Any amount to NRIs through bank account since they are citizen of India but nothing to OCI Card holder",
               "Any amount to NRI relative and up to LRS limit to OCI Card holder relative",
               "A resident individual can make a rupee gift only to a NRI/PIO relative for amount not exceeding USD 250,000 per FY",
               "A resident individual cannot make any rupee gift to a NRI/PIO relative"],
    "correct_answer": "A resident individual can make a rupee gift only to a NRI/PIO relative for amount not exceeding USD 250,000 per FY"
},
{
    "question": "What action should an AD Bank initiate when residential status of a customer having Safe Deposit Locker changes to NRI?",
    "options": ["No action is warranted",
               "Bank should close the Safe Deposit Locker account as this facility is not permitted to NRI",
               "Bank should advise customer to surrender the locker within 6 months",
               "Bank should update the KYC Detail of the account including contact details",
               "Bank should close the locker and issue new one under NRI scheme"],
    "correct_answer": "Bank should update the KYC Detail of the account including contact details"
},
{
    "question": "Which of the following is our Joint Venture?",
    "options": ["UBI (UK) Ltd", "India International Bank (Malaysia) BHD", "Andhra Bank Financial Services Limited", 
               "UBI Services Ltd", "None of the above"],
    "correct_answer": "India International Bank (Malaysia) BHD"
},
{
    "question": "Associations receiving foreign assistance should register themselves with the _____?",
    "options": ["RBI", "Ministry of Home Affairs", "Ministry of External Affairs", "Ministry of Finance", "SEBI"],
    "correct_answer": "Ministry of Home Affairs"
},
{
    "question": "How many Foreign Branches does Union Bank of India maintains as on date?",
    "options": ["1", "2", "3", "4", "Nil"],
    "correct_answer": "2"
},
{
    "question": "Bank can pay interest on NRE deposits which can be higher than that on Domestic Deposits",
    "options": ["Yes", "Yes, subject to permission of MD & CEO", "Yes, under Branch Head Discretionary Powers", 
               "Yes, but only on high value deposits above Rs.1 Cr.", "No"],
    "correct_answer": "No"
},
{
    "question": "NRE account can be opened in which currency:",
    "options": ["Indian Rupees", "USD", "Either (a) or (b)", "EUR", 
               "Any permissible Foreign Currency from amongst USD/EUR/GBP/AUD/CAD/JPY"],
    "correct_answer": "Indian Rupees"
},
{
    "question": "Up to how much foreign currency in the form of currency notes can be encashed without insisting upon CDF Form?",
    "options": ["USD 2000.00", "USD 3000.00", "USD 5000.00", "USD 10000.00", "No ceiling"],
    "correct_answer": "USD 5000.00"
},
{
    "question": "Which act defines Close Relative?",
    "options": ["Indian Contracts Act, 1872", "Indian Companies Act, 2013", "Indian Partnership Act, 1932", 
               "FCRA, 2010", "FEMA, 1999"],
    "correct_answer": "Indian Companies Act, 2013"
},
{
    "question": "The following is the documentary evidence to be submitted by the importer to the bank as evidence of import:",
    "options": ["Shipping Bill", "Bill of entry", "Customs certified invoice", "Declaration Form", "Any one of the above"],
    "correct_answer": "Bill of entry"
},
{
    "question": "Please calculate the exchange rate for an Import Payment due after 3 months in current market in which USD/INR spot rate is 82.93/96 and USD is at a premium of 0.02/.03 for each ensuing month?",
    "options": ["83.02", "83.01", "82.99", "82.97", "83.05"],
    "correct_answer": "83.05"
},
{
    "question": "Which of the following constitutes Overseas Direct Investment?",
    "options": ["A speculator trying to make profit by buying foreign company shares on a foreign stock exchange",
               "Indian Energy company buying territory abroad where it expects to find oil reserves",
               "A tourist purchasing foreign currency to spend on a holiday abroad",
               "A company signing an agreement with a wholesaler to distribute its products in the foreign markets",
               "A company remitting money abroad for setting up their stall in upcoming marketing exhibition"],
    "correct_answer": "Indian Energy company buying territory abroad where it expects to find oil reserves"
},
{
    "question": "When foreign currency assets and liabilities match in terms of amount of exposure and timing of maturities, it is described as:",
    "options": ["Financial Hedge", "Natural Hedge", "Perfect Hedge", "Bi-lateral Netting", "Multi-Lateral Netting"],
    "correct_answer": "Natural Hedge"
},
{
    "question": "UCPDC means:",
    "options": ["Uniform code and practices for Documentary Credit",
               "Uniform Customs and Practices for Documentary credits",
               "Uniform practices for documentary credit",
               "Uniform Code and Procedures for Documentary Credits",
               "Uniform Customs and Procedures for Documentary Credit"],
    "correct_answer": "Uniform Customs and Practices for Documentary credits"
},
{
    "question": "An LC provides for allowing pre-shipment credit to the beneficiary. It is called:",
    "options": ["Confirmed LC", "Irrevocable LC", "Back-to-back LC", "Red clause LC", "Transferable LC"],
    "correct_answer": "Red clause LC"
},
{
    "question": "Drawal of foreign Exchange by a person in India is not permitted in respect of which of the following:",
    "options": ["Transactions with persons resident in Nepal and Bhutan",
               "Travel to Nepal and Bhutan",
               "Transactions given in Schedule 1 of FEMA",
               "All are permitted",
               "None of these"],
    "correct_answer": "None of these"
},
{
    "question": "The exporter should necessarily submit the export documents to the bank within:",
    "options": ["15 days from the date of the documents",
               "15 days from the date of shipment",
               "21 days from the date of the documents",
               "21 days from the date of shipment",
               "No such time limit"],
    "correct_answer": "21 days from the date of shipment"
},
{
    "question": "Which article deals with Principles of Examination of Documents under UCPDC?",
    "options": ["Article 11", "Article 12", "Article 13", "Article 14", "Article 15"],
    "correct_answer": "Article 14"
},
{
    "question": "When the seller place the goods at the side of the ship at named port and also clear the goods for Export, which incoterms will be used:",
    "options": ["FCA- Free Carrier", "FOB – Free on Board", "FAS – Free Alongside Ship", 
               "DAP – Delivery at Place", "DDP- Duty Delivery Paid"],
    "correct_answer": "FAS – Free Alongside Ship"
},
{
    "question": "INCOTERMS issued by ICC, Paris is called as:",
    "options": ["Indian company terms", "International Commercial Terms", "International Contract terms", 
               "International Company terms", "None of the above"],
    "correct_answer": "International Commercial Terms"
},
{
    "question": "A person does a transaction with Spot value on 8th January 2025(Friday), then the settlement will be done on:",
    "options": ["9th January 2025", "11th January 2025", "12th January 2025", "13th January 2025", "On the same day"],
    "correct_answer": "12th January 2025"
},
{
    "question": "The visits by a resident Indian to which of the following countries are not eligible for obtaining foreign exchange under forex facilities to residents:",
    "options": ["All SAARC countries", "All EEC countries", "All CIS countries", "Iraq and Libya", "Nepal and Bhutan"],
    "correct_answer": "Nepal and Bhutan"
},
{
    "question": "Under UCPDC-600, a bank assumes no responsibility for consequences arising out of the interruption of its business by the Acts of God, riots, civil commotions, insurrections, wars, acts of terrorism, or by any strikes or lockouts or causes beyond its control. This is called as:",
    "options": ["Disclaimer", "Force majeure", "Modus operandi", "Exclusion of liability", "Limitation Clause"],
    "correct_answer": "Force majeure"
},
{
    "question": "FCNR(B) deposits can be opened as Term deposit for the period:",
    "options": ["Minimum 15 days, Maximum 10 years", "Minimum 1 year, Maximum 5 years", 
               "Minimum 1 year 1 day, Maximum 2 years", "Minimum 1 year, Maximum 10 years", 
               "Minimum 7 days, Maximum 10 years"],
    "correct_answer": "Minimum 1 year, Maximum 5 years"
},
{
    "question": "LC issued in lieu of bank guarantee, is called:",
    "options": ["Red clause LC", "Green Clause LC", "Standby LC", "Revolving LC", "Back-to-Back LC"],
    "correct_answer": "Standby LC"
},
{
    "question": "Under UCPDC-600, branches of same bank in different countries are:",
    "options": ["Same bank", "Different bank", "Associate bank", "Subsidiary bank", "Correspondent bank"],
    "correct_answer": "Different bank"
},
{
    "question": "Under Gold Card Scheme, interchangeability allowed from Post-shipment to Pre-Shipment:",
    "options": ["10 %", "20 %", "30 %", "40 %", "50 %"],
    "correct_answer": "40 %"
},
{
    "question": "Under UCPDC 600, a nominated bank or issuing bank shall each have a maximum of __________ following the day of presentation to determine if the documents are in order:",
    "options": ["2 banking days", "5 working days", "5 banking days", "7 banking days", "15 banking days"],
    "correct_answer": "5 banking days"
},
{
    "question": "The terms which can vary in a transferred credit compared to the original credit is:",
    "options": ["name of applicant", "expiry date", "Insurance % age", "Price per unit", "All the above"],
    "correct_answer": "All the above"
},
{
    "question": "To what extent of USD ______ or equiv. customers can receive import bills directly?",
    "options": ["Up to USD 300,000", "Up to USD 100000", "Up to USD 200000", "Up to USD 25000", "No limit"],
    "correct_answer": "Up to USD 300,000"
},
{
    "question": "TCS to be charges when amount of remittance exceeds Rs. ___________ per financial year.",
    "options": ["5 Lacs", "7 Lac", "10 Lac", "15 Lac", "25 Lac"],
    "correct_answer": "7 Lac"
},
{
    "question": "Forward Contract cover facility cannot be given against balance lying in___________",
    "options": ["FCNR (B) Account", "NRE Term Deposit", "NRE SB Account deposit", "Both (a) and (c)", "Any of the above"],
    "correct_answer": "NRE SB Account deposit"
},
{
    "question": "Reporting of Issue of ADR / GDR to RBI must be within _____ days from the date of issue.",
    "options": ["15 Days", "30 Days", "45 Days", "60 Days", "90 Days"],
    "correct_answer": "30 Days"
},
{
    "question": "Draw down of ECB will be allowed only after the borrower obtains the following number from RBI:",
    "options": ["Account number", "Loan Registration Number", "License No", "Unique Identification Number", "Unique Registration Number"],
    "correct_answer": "Loan Registration Number"
},
{
    "question": "The running account facility for packing credit is available for……..",
    "options": ["Status holders only", "Export for specified goods.", "Exporters with good track record", 
                "Exporters with orders above Rs. 100 crores", "None of the above"],
    "correct_answer": "Exporters with good track record"
},
{
    "question": "Loan amount sanctioned to a NRI customer against NRE deposit should be credited to:",
    "options": ["NRE a/c", "NRO a/c", "Any of the above a/c as per party request", 
                "Depends upon the loan amount", "His account maintained with any Foreign Bank"],
    "correct_answer": "NRO a/c"
},
{
    "question": "Normally the maximum period for which packing credit advances are made is:",
    "options": ["90 days", "360 days", "120 days", "180 days", "270 days"],
    "correct_answer": "180 days"
},
{
    "question": "A Pre-shipment advance is not expected to be adjusted by:",
    "options": ["Proceeds of export bills", "Export Incentives", "Post-Shipment finance", "Advance payment for exports", "Local funds"],
    "correct_answer": "Local funds"
},
{
    "question": "For disbursement of Packing credit (pre-shipment) advance, exporter should submit:",
    "options": ["A Letter of Credit", "Firm Export Order", "IEC Number and Pan Card", 
               "Export License copy for that particular commodity", "Option A or B is correct"],
    "correct_answer": "Option A or B is correct"
},
{
    "question": "Pre-shipment finance in foreign currency can be availed in which currency?",
    "options": ["US Dollar", "Any currency other than INR", "The currency of Export only", "USD/GBP/EUR", "Any Permitted currency"],
    "correct_answer": "Any Permitted currency"
},
{
    "question": "Which of the following is not a post-Shipment finance?",
    "options": ["Negotiation of bill under Letter of Credit", "Purchase of foreign bill", 
               "Advance against foreign bill sent on collection", "Advance against export order or L/C", 
               "None of the above"],
    "correct_answer": "Advance against export order or L/C"
},
{
    "question": "The disbursements made under Pre-shipment credit on running account basis will be adjusted on the basis of:",
    "options": ["Last in first out basis", "Contract to contract basis", "First in first out basis", 
               "At the discretion of the bank", "At the discretion of the exporter"],
    "correct_answer": "First in first out basis"
},
{
    "question": "From which period we should stop paying premium to ECGC:",
    "options": ["When the a/c becomes NPA", "After filing Final claim", "After filing ROD", "After due date", "None of the above"],
    "correct_answer": "After filing ROD"
},
{
    "question": "The NRO a/c in the name of a foreign tourist who has come to India can be maintained for a maximum period not exceeding ......... months.",
    "options": ["6 months", "12 months", "24 months", "36 months", "48 months"],
    "correct_answer": "6 months"
},
{
    "question": "Whether the PCFC will be covered under WTPCG of ECGC?",
    "options": ["Yes", "No", "At the discretion of ECGC", "Separate Policy is required", "Yes but up to USD10000 only"],
    "correct_answer": "Yes"
},
{
    "question": "Packing Credit is granted to an exporter for the purpose of?",
    "options": ["Procurement and processing of raw materials of goods meant for export",
               "Manufacturing and Packing of goods meant for export",
               "Transporting, warehousing and shipping of goods meant for export",
               "All of the above",
               "At the discretion of the borrower or bank"],
    "correct_answer": "All of the above"
},
{
    "question": "Under Gold card scheme, in principle credit limits will be sanctioned to exporter up to:",
    "options": ["3 Years", "1 Year", "2 Years", "5 Years", "4 Years"],
    "correct_answer": "3 Years"
},
{
    "question": "Normally in how many days Rupee export credit to construction contractors be adjusted?",
    "options": ["180 days", "270 days", "365 days", "As per the requests of the borrower", "None of the above"],
    "correct_answer": "365 days"
},
{
    "question": "Extension of due date beyond __________ for disbursements made under packing credit to be obtained from controlling office?",
    "options": ["90 days", "180 days", "270 days", "360 days", "At the discretion of bank"],
    "correct_answer": "180 days"
},
{
    "question": "What is the maximum time limit stipulated by RBI to banks for Sanction of new advances / Renewal / adhoc sanctions for Gold Card customers?",
    "options": ["60/45/30", "25/15/7", "45/30/15", "90/45/30", "None of the above"],
    "correct_answer": "25/15/7"
},
{
    "question": "Running Packing Credit can be sanctioned _______",
    "options": ["For selected commodities", "For units located in SEZs", "For 100 % EOUs", 
               "For all types of commodities", "None of the above"],
    "correct_answer": "For all types of commodities"
},
{
    "question": "For Gold Card customers, our bank permitted concession in processing charges to the extent of _______?",
    "options": ["0.05", "0.10", "0.15", "0.20", "No Concession"],
    "correct_answer": "0.10"
},
{
    "question": "Pre-shipment advances which are not adjusted by submission of export documents within ______, will not qualify for concessional ROI for export credit to the exporter ab-initio",
    "options": ["180 days from the date of shipment", "180 days from the date of advance", 
                "360 days from the date of advance", "360 days from the date of shipment", 
                "As per the discretion of bank"],
    "correct_answer": "360 days from the date of advance"
},
{
    "question": "For Gold Card customers, our bank permitted interchangeability from Post to Pre shipment upto ___ % at BM's discretion?",
    "options": ["0.25", "0.50", "0.75", "0.40", "Not permitted"],
    "correct_answer": "0.40"
},
{
    "question": "Under deemed exports, goods are supplied to units:",
    "options": ["Within the country", "Outside the country", "As per choice of the buyer", 
               "As per choice of the seller", "To SEZ in the country"],
    "correct_answer": "Within the country"
},
{
    "question": "As per FEDAI guidelines, what is NTP (Notional Transit Period) in case of a Sight Bill in foreign currencies?",
    "options": ["10 Days", "21 Days", "25 Days", "30 Days", "None of the above"],
    "correct_answer": "25 Days"
},
{
    "question": "In normal course of business which Bill of Lading is preferred?",
    "options": ["Clean On-Board B/L", "Charter Party B/L", "Freight Forwarder's Cargo Receipt (FCR)", 
                "Claused B/L", "Any B/L is acceptable"],
    "correct_answer": "Clean On-Board B/L"
},
{
    "question": "Export advance against duty draw back can be sanctioned for a maximum period of:",
    "options": ["30 Days", "60 Days", "90 Days", "180 Days", "None of the above"],
    "correct_answer": "90 Days"
},
{
    "question": "Goods exported on consignment basis having warehouses abroad shall be realized within a maximum period of _______",
    "options": ["6 Months", "12 Months", "15 Months", "9 Months", "No time limit"],
    "correct_answer": "15 Months"
},
{
    "question": "Crystallisation of export bills for Gems & Jewellery exports is done________ days after due date?",
    "options": ["15 Days", "25 Days", "45 Days", "30 Days", "60 Days"],
    "correct_answer": "45 Days"
},
{
    "question": "The period permitted by RBI for repatriation of export proceeds for exporters on consignment basis?",
    "options": ["6 Months", "9 Months", "12 Months", "15 Months", "No time limit"],
    "correct_answer": "9 Months"
},
{
    "question": "AD Category – I banks may regularize cases of dispatch of shipping documents by the exporter direct to the consignee or his agent resident in the country of the final destination of goods, up to ----------, per export shipment, subject to the conditions.",
    "options": ["USD 5 million or its equivalent", "USD 1 million or its equivalent", 
                "USD 5 Lakhs or its equivalent", "USD 1 Lakhs or its equivalent", "No such limit"],
    "correct_answer": "USD 1 million or its equivalent"
},
{
    "question": "Who is the competent authority for extension of due date of Post Shipment finance beyond 180 days?",
    "options": ["Approval of Regional Office is required", "Approval of sanctioning authority is required, be it RO, ZO or CO", 
                "Approval of ECGC is required", "Branch Head May Approve the same.", 
                "Branch Head of B Category may Approve the same."],
    "correct_answer": "Approval of ECGC is required"
},
{
    "question": "The maximum time limit for realisation of export proceeds in the case of consignment exports is _________ from the date of shipment.",
    "options": ["6 Months", "9 Months", "12 Months", "15 Months", "No such restriction"],
    "correct_answer": "9 Months"
},
{
    "question": "In case of recovery of post shipment advance is made in cash, then what interest to be charged?",
    "options": ["Normal Interest plus 2 % penalty", "At commercial rate from date of advance till date of recovery", 
                "ECNOS from date of advance till date of recovery", "A, B or C whichever is higher", 
                "None of the above"],
    "correct_answer": "ECNOS from date of advance till date of recovery"
},
{
    "question": "When the branch is not comfortable in purchasing or allowing negotiation of documents due to any reason then which type of post shipment advance is involved?",
    "options": ["Advance against export on consignment basis", 
               "Advance against Foreign Documentary Bills sent on Collection basis (AFDBC)", 
               "Advance against Exports on elongated credit terms", 
               "Advance against deemed exports", 
               "Advance against Exports on deferred payment terms"],
    "correct_answer": "Advance against Foreign Documentary Bills sent on Collection basis (AFDBC)"
},
{
    "question": "What is crystallisation in Post Shipment Advance?",
    "options": ["Conversion of the foreign currency liability into rupee liability", 
               "Recovering the post shipment advance after due date", 
               "Making the post shipment advance crystal clear in terms of foreign liability",
               "Conversion of Rupee liability into foreign currency liability",
               "A or D"],
    "correct_answer": "Conversion of the foreign currency liability into rupee liability"
},
{
    "question": "In export credit under Post shipment, what is the rate of interest charged on Overdue bills up to 180 days?",
    "options": ["As applicable to overdue bills", "As applicable to regular bills", 
               "ECNOS from date of advance till date of recovery", "At the discretion of the bank",
               "None of the above"],
    "correct_answer": "As applicable to regular bills"
},
{
    "question": "Export advance against duty draw back can be sanctioned for a maximum period of:",
    "options": ["30 Days", "60 Days", "90 Days", "120 Days", "180 Days"],
    "correct_answer": "90 Days"
},
{
    "question": "Normally how much margin is kept for export advance against duty draw back?",
    "options": ["No margin", "0.10", "0.20", "As applicable to normal Bills", "0.25"],
    "correct_answer": "0.25"
},
{
    "question": "Whether Banks can sanction post shipment facility against EEFC A/c balances as margin?",
    "options": ["NO", "Yes", "Depends to the type of Commodity", "Yes for Status holder exporters", "Yes, with RBI permission"],
    "correct_answer": "NO"
},
{
    "question": "EDPMS module has which option relating to export bills?",
    "options": ["View Shipping Bills of respective AD Codes",
               "Total number of Shipping Bills Pending Transaction",
               "Pending AD Acknowledgement and Pending Payment",
               "Partially paid and IRMs received by the Branch / Outstanding IRMs / completed IRMs",
               "All of the above"],
    "correct_answer": "All of the above"
},
{
    "question": "The exporters would be caution listed if any shipping bill against them remains open for more than _________ in EDPMS provided no extension is granted by AD Branches/RBI.",
    "options": ["9 Months", "One Year", "15 Months", "Two Years", "5 Years"],
    "correct_answer": "Two Years"
},
{
    "question": "Which rates to be applied for crystallisation of export advance?",
    "options": ["TT Selling", "TT Buying", "Bill Buying", "Bill Selling", "None of the above"],
    "correct_answer": "TT Selling"
},
{
    "question": "For Gold Card customers, our bank permitted interchangeability from Post to Pre shipment upto ___ % at BM's discretion?",
    "options": ["0.25", "0.50", "0.75", "0.40", "0.60"],
    "correct_answer": "0.40"
},
{
    "question": "The maximum ceiling for receiving Export related receipts through Online Payment Gateway Service Providers (OPGSPs) is ______",
    "options": ["USD 3000", "USD 500", "USD 10000", "USD 25000", "No such limit"],
    "correct_answer": "USD 10000"
},
{
    "question": "Units in SEZs shall realize export proceeds within a maximum period of _______",
    "options": ["6 Months", "9 Months", "12 Months", "15 Months", "No time limit"],
    "correct_answer": "9 Months"
},
{
    "question": "The following category of unrealized export bills would not qualify for write off facility?",
    "options": ["Exports made to countries with externalization problem",
               "EDF/SB forms are under investigation by agencies like ED / DRI / CBI etc",
               "Bills are subject matter of civil/ criminal suit",
               "Bills are pending for realization for more than 2 years.",
               "All of the above"],
    "correct_answer": "EDF/SB forms are under investigation by agencies like ED/DRI/CBI etc"
},
{
    "question": "All trade transactions between a person resident in India and a person resident in Nepal or Bhutan may to be normally settled in:",
    "options": ["USD only", "Any freely convertible currency", "INR only", 
               "USD, GBP or EUR", "USD, GBP, EUR, JPY, CAD or SGD"],
    "correct_answer": "INR only"
},
{
    "question": "Extension of time for realization of export bills beyond 9 months from the date of export can be permitted by:",
    "options": ["AD only", "RBI only", "Extension beyond 12 months is not permissible", 
               "Both RBI or AD can approve subject to conditions", "Depends upon the amount"],
    "correct_answer": "Both RBI or AD can approve subject to conditions"
},
{
    "question": "For Self-write off by exporter / Status Holder Exporters / write off by AD Banks of unrealized export bills, the amount should remain outstanding for a period of more than ______",
    "options": ["6 Months", "9 Months", "12 Months", "15 Months", "No time limit"],
    "correct_answer": "12 Months"
},

{
    "question": "Who will be given preference for granting PCFC?",
    "options": ["Status holders", "Who are enjoying INR Packing Credit", "Gold Card Holders", 
               "No such preference, First come first serve basis.", "None of the above"],
    "correct_answer": "Gold Card Holders"
},
{
    "question": "How much is the concession for Gold Card Holders in ECGC Premium in ECIB-WTPC/ECIB-WTPS?",
    "options": ["0.05", "0.1", "0.15", "0.20", "No such concession"],
    "correct_answer": "No such concession"
},
{
    "question": "In which SWIFT format export LC is received for advising to beneficiary?",
    "options": ["MT707", "MT700", "MT202", "MT999", "MT799"],
    "correct_answer": "MT700"
},
{
    "question": "Arrange the following steps in the process of GDR Issue: A) Registration with prescribed authority B) Appointment and vesting of shares with the custodian C) Approval of regulatory authorities D) Listing of GDR E) GDR Allotment",
    "options": ["C,A,B,E,D", "A,B,C,D,E", "A,C,B,E,D", "B,A,C,D,E", "D,A,C,B,E"],
    "correct_answer": "A,C,B,E,D"
},
{
    "question": "Extension of due date beyond __________ for disbursements made under packing credit to be obtained from controlling office?",
    "options": ["90 days", "180 days", "270 days", "360 days", "At the discretion of bank"],
    "correct_answer": "180 days"
},
{
    "question": "What is the maximum time limit stipulated by RBI to banks for Sanction of new advances/Renewal/adhoc sanctions for Gold Card customers?",
    "options": ["60/45/30", "25/15/7", "45/30/15", "90/45/30", "None of the above"],
    "correct_answer": "25/15/7"
},
{
    "question": "Running Packing Credit can be sanctioned for:",
    "options": ["For selected commodities", "For units located in SEZs", "For 100% EOUs", 
               "For all types of commodities", "None of the above"],
    "correct_answer": "For all types of commodities"
},
{
    "question": "When foreign currency assets and liabilities match in terms of amount of exposure and timing of maturities, it is described as:",
    "options": ["Financial Hedge", "Natural Hedge", "Perfect Hedge", "Bi-lateral Netting", "Multi-Lateral Netting"],
    "correct_answer": "Natural Hedge"
},
{
    "question": "Under UCPDC-600, branches of same bank in different countries are:",
    "options": ["Same bank", "Different bank", "Associate bank", "Subsidiary bank", "Correspondent bank"],
    "correct_answer": "Different bank"
},
{
    "question": "Under Gold Card Scheme, interchangeability allowed from Post-shipment to Pre-Shipment:",
    "options": ["10%", "20%", "30%", "40%", "50%"],
    "correct_answer": "40%"
},
{
    "question": "Under UCPDC 600, a nominated bank or issuing bank shall each have a maximum of __________ following the day of presentation to determine if the documents are in order:",
    "options": ["2 banking days", "5 working days", "5 banking days", "7 banking days", "15 banking days"],
    "correct_answer": "5 banking days"
},
{
    "question": "The terms which can vary in a transferred credit compared to the original credit is:",
    "options": ["name of applicant", "expiry date", "Insurance percentage", "Price per unit", "All the above"],
    "correct_answer": "All the above"
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