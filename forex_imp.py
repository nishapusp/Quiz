import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
{
    "question": "The ECGC does not cover___________________",
    "options": ["Exchange Risk on the Foreign Currency/INR Conversion", 
                "Credit Risk on the Buyer",
                "War or Civil Disturbance in Buyer's Country",
                "Import Restrictions in Buyer's Country after the date of Shipment",
                "Exchange Transfer delays or Embargos"],
    "correct_answer": "Exchange Risk on the Foreign Currency/INR Conversion"
},
{
    "question": "Can an Exporter remit advance payment to overseas supplier in a merchanting trade transaction before receiving payment from ultimate overseas buyer?",
    "options": ["Yes, advance payment for import under merchant trade transaction is permitted",
                "Yes, provided the advance payment does not exceed USD 100000.00 or equivalent",
                "Yes, provided the advance payment does not exceed USD 300000.00 or equivalent",
                "Yes, provided the advance payment does not exceed USD 500000.00 or equivalent",
                "No, advance payment is not permitted for merchant trade transactions"],
    "correct_answer": "Yes, advance payment for import under merchant trade transaction is permitted"
},
{
    "question": "In which of the following cases exporter is required to file Export Declaration Form (EDF) under FEMA?",
    "options": ["When goods are sent overseas for testing purposes",
                "When goods are sent under lease-hire-purchase arrangement",
                "when goods are sent overseas as sample within prescribed limit",
                "when goods are sent as replacement for goods exported and found defective",
                "when goods are sent overseas as gift within prescribed limit"],
    "correct_answer": "When goods are sent under lease-hire-purchase arrangement"
},
{
    "question": "The maximum usance period in a letter of credit opened for import of precious stone is?",
    "options": ["90 days from receipt of goods in India",
                "90 days from date of shipment",
                "180 days from receipt of goods in India",
                "180 days from date of shipment",
                "LC opening is not allowed for precious stone"],
    "correct_answer": "90 days from date of shipment"
},
{
    "question": "Which is the nodal Agency/Department for formulation of the policy of the Government on Foreign Direct Investment (FDI)?",
    "options": ["Director General of Foreign Trade, Ministry of Commerce",
                "Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, GOI",
                "Department of External Investments & Operations, Reserve Bank of India",
                "Foreign Investment Promotion Board",
                "DGFT in consultation with RBI."],
    "correct_answer": "Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, GOI"
},
{
    "question": "Identify the incorrect pair",
    "options": ["USD-SOFR", "JPY-TONAR", "CHF-SARON", "EUR-SONIA", "GBP-SONIA"],
    "correct_answer": "EUR-SONIA"
},
{
    "question": "With respect to the recent modification in FEDAI Guidelines which one is incorrect",
    "options": ["Working Day is replaced with Business Day",
                "RTGS has been replaced with Domestic Wire Transfer",
                "Holiday has been classified as Known Holiday and Suddenly Declared Holiday",
                "Banks can pass gain on forward contract cancellation, even if request is received after due date, subject to their satisfaction",
                "Hours of Business for quoting Forex Rates is modified to 9:00 AM to 05:00 PM"],
    "correct_answer": "Hours of Business for quoting Forex Rates is modified to 9:00 AM to 05:00 PM"
},
{
    "question": "Export bill, if remains unrealised, to be crystallized after how many days from due date for units in Gems and Jewellery sector",
    "options": ["15 Days", "30 Days", "45 Days", "60 Days", "No need to crystallize"],
    "correct_answer": "45 Days"
},
{
    "question": "RBI has launched ___________ Portal to streamline the process of seeking authorizations, licenses, or regulatory approvals from RBI",
    "options": ["PRAVAAH", "NIRVAAH", "PRAVAAS", "NIRVAAS", "VISHVAAS"],
    "correct_answer": "PRAVAAH"
},
{
    "question": "Loan against NRE Deposit can be credited to",
    "options": ["NRE Account Only", 
                "NRO Account Only",
                "Separate Account to be opened for this purpose",
                "Either NRE or NRO as per customer's request",
                "No loan can be given against NRE Deposits"],
    "correct_answer": "NRO Account Only"
},
{
    "question": "This act was passed by USA to control tax evasion by its citizen by investing or holding assets in other countries",
    "options": ["FCRA", "CRS", "FATF", "FATCA", "OFAC"],
    "correct_answer": "FATCA"
},
{
    "question": "With respect to DDA Accounts, which one is incorrect",
    "options": ["It can be maintained in any permissible Foreign Currency",
                "Customers dealing in rough or cut and polished diamonds, precious metal jewellery or coloured gemstones are only eligible to maintain this account",
                "Maximum 5 DDA accounts can be maintained at a time",
                "Customer having satisfactory track record of at least 2-3 years in cut and polished diamonds, precious metal jewellery or coloured gemstones are eligible to maintain this account",
                "Customers having an average annual turnover of Rs. 3-5 Cr. Are eligible to maintain this account"],
    "correct_answer": "It can be maintained in any permissible Foreign Currency"
},
{
    "question": "For release of Foreign Exchange for any current account transaction, AD needs to obtain",
    "options": ["Form A2, only if the amount exceeds USD 25000.00 or equivalent",
                "Only Simple Letter for remittances up to USD 25000.00 or equivalent",
                "Digital Form A2 for remittances up to USD 1 Lac or equivalent",
                "Physical/Digital Form A2 irrespective of the amount",
                "Physical Form A2 for remittances above USD 1 Lac or equivalent"],
    "correct_answer": "Physical/Digital Form A2 irrespective of the amount"
},
{
    "question": "It is mandatory for banks that have obtained Whole Turnover Cover from ECGC to submit copy of sanction note along with notification to ECGC if the total limit under PC and PS is ________ and above",
    "options": ["Rs. 10.00 Cr.", "Rs. 50.00 Cr.", "Rs. 200.00 Cr", "Rs. 300.00 Cr", "In all cases"],
    "correct_answer": "Rs. 10.00 Cr."
},
{
    "question": "Which method of payment indicates high degree of mutual trust between buyer and seller in International Trade",
    "options": ["Advance Payment", "Open Account Trade", "Delivery against Payment", 
                "Settlement through L/Cs", "Part Advance and Part DP"],
    "correct_answer": "Open Account Trade"
},
{
    "question": "What is the fulform of NITI Aayog?",
    "options": ["National Initiative for Technological Innovation",
                "New India Transformation Initiative",
                "National Integrated Technology Institute",
                "National Institution for Transforming India",
                "National Institute for Transparency and Innovation"],
    "correct_answer": "National Institution for Transforming India"
},
{
    "question": "Which market structure is characterized by a single seller and no close substitutes for the product?",
    "options": ["Perfect Competition", "Monopolistic Competition", "Monopoly", "Oligopoly", "Duopoly"],
    "correct_answer": "Monopoly"
},
{
    "question": "Which of the following is considered part of narrow money (M1)",
    "options": ["Fixed Deposits", "Savings Account Balances", "Currency in Circulation", 
                "Government Bonds", "Mutual Fund Investments"],
    "correct_answer": "Currency in Circulation"
},
{
    "question": "Which type of inflation is caused by an increase in production costs, leading to higher prices for goods and services?",
    "options": ["Demand-Pull Inflation", "Cost-Push Inflation", "Built-In Inflation", "Hyperinflation", "Stagflation"],
    "correct_answer": "Cost-Push Inflation"
},
{
    "question": "In which market structure do many firms sell products that are similar but not identical, leading to product differentiation?",
    "options": ["Perfect Competition", "Monopolistic Competition", "Monopoly", "Oligopoly", "Monopsony"],
    "correct_answer": "Monopolistic Competition"
},
{
    "question": "Which of the following is included in broad money (M3) but not in narrow money (M1)",
    "options": ["Demand Deposits", "Savings Account Balances", "Time Deposits", 
                "Currency in Circulation", "Cheques"],
    "correct_answer": "Time Deposits"
},
{
    "question": "In which market structure do two firms dominate the market, often engaging in competitive strategies against each other?",
    "options": ["Perfect Competition", "Monopolistic Competition", "Monopoly", "Oligopoly", "Duopoly"],
    "correct_answer": "Duopoly"
},
{
    "question": "What type of inflation occurs when there is an increase in overall demand for goods and services that exceeds supply?",
    "options": ["Demand-Pull Inflation", "Cost-Push Inflation", "Built-In Inflation", "Hyperinflation", "Deflation"],
    "correct_answer": "Demand-Pull Inflation"
},
{
    "question": "Which of the following best describes the difference between nominal GDP and real GDP?",
    "options": ["Nominal GDP adjusts for inflation, while real GDP does not.",
                "Real GDP measures the value of goods and services at current market prices, while nominal GDP measures it at constant prices.",
                "Nominal GDP measures the value of goods and services at current market prices, while real GDP adjusts for inflation.",
                "Real GDP is calculated without considering government spending, while nominal GDP includes it.",
                "Nominal GDP includes only final goods and services, while real GDP includes intermediate goods."],
    "correct_answer": "Nominal GDP measures the value of goods and services at current market prices, while real GDP adjusts for inflation."
},
{
    "question": "Which sector has traditionally been the largest contributor to India's GDP?",
    "options": ["Agriculture", "Industry", "Services", "Construction", "Mining"],
    "correct_answer": "Services"
},
{
    "question": "Which type of inflation involves a situation where inflation and unemployment are both high, often caused by a supply shock?",
    "options": ["Demand-Pull Inflation", "Cost-Push Inflation", "Stagflation", "Hyperinflation", "Deflation"],
    "correct_answer": "Stagflation"
},
{
    "question": "What does 'inflation tax' refer to in an economic context?",
    "options": ["Taxes imposed directly on inflation-related profits by the government.",
                "The loss of purchasing power that individuals experience due to inflation, effectively acting as a tax on their wealth.",
                "Taxes collected specifically on goods and services that are subject to inflationary pressures.",
                "Government taxes used to fund inflation control measures.",
                "The cost of managing inflation through monetary policy tools."],
    "correct_answer": "The loss of purchasing power that individuals experience due to inflation, effectively acting as a tax on their wealth."
},
{
    "question": "What does 'inflation premium' refer to in the context of financial markets?",
    "options": ["The additional amount investors are willing to pay for stocks during high inflation periods.",
                "The extra return or interest rate that investors require to compensate for the expected inflation over the life of an investment.",
                "The government subsidies provided to counteract the effects of inflation.",
                "The discount offered on bonds to counteract inflationary losses.",
                "The cost incurred by companies to adjust prices in response to inflation."],
    "correct_answer": "The extra return or interest rate that investors require to compensate for the expected inflation over the life of an investment."
},
{
    "question": "Which type of inflation is characterized by a rapid and uncontrollable increase in prices, often leading to a severe economic crisis?",
    "options": ["Demand-Pull Inflation", "Cost-Push Inflation", "Built-In Inflation", "Hyperinflation", "Stagflation"],
    "correct_answer": "Hyperinflation"
},
{
    "question": "Which market structure features many small firms selling identical products with no control over prices?",
    "options": ["Perfect Competition", "Monopolistic Competition", "Duopoly", "Monopoly", "Oligopoly"],
    "correct_answer": "Perfect Competition"
},
{
    "question": "What is the present tolerance limit of RBI with respect to inflation?",
    "options": ["Up to 4%", "4% +/- 2%", "2% +/- 4%", "6% +/- 2%", "up to 6%"],
    "correct_answer": "4% +/- 2%"
},
{
    "question": "Who publishes CPI in India",
    "options": ["Office of Economic Affairs", "Ministry of Commerce and Industry", "National Statistics Commission", 
                "Central Statistical Office", "Ministry of Finance"],
    "correct_answer": "Central Statistical Office"
},
{
    "question": "RBI has reviewed the runoff rate on certain category of deposits under LCR framework for all Commercial banks (excluding PB, RRB & LAB) in July 2024. What is the date of its implementation?",
    "options": ["01.04.2025", "01.09.2024", "01.01.2025", "01.11.2024", "01.12.2024"],
    "correct_answer": "01.04.2025"
},
{
    "question": "Starting June 2024, Indian G-Sec Bonds are now included in a Global Bond Index. Name the index.",
    "options": ["Bloomberg Aggregate Bond Index", "Merrill Lynch Domestic Master", "JP Morgan Bond Index", 
                "FTSE Bond Index", "S&P Global Sovereign Bond Index"],
    "correct_answer": "JP Morgan Bond Index"
},
{
    "question": "With respect to hedging of FX risk, revised w.e.f. 05.04.2024, single position limit up to which amount does not require establishment of underlying exposure for foreign exchange derivative contract?",
    "options": ["$50 mio", "$100 mio", "$150 mio", "$200 mio", "$250 mio"],
    "correct_answer": "$100 mio"
},
{
    "question": "RBI has reclassified the investment portfolio of commercial banks w.e.f. 01.04.2024. Under the new classification which of the following portfolio does not form part of the banking book?",
    "options": ["HTM", "AFS", "FVTPL (Non-HFT)", "FVTPL (HFT)", "SPPI"],
    "correct_answer": "FVTPL (HFT)"
},
{
    "question": "IIBX IFSC in Feb 2024, allowed Indian Banks to act as Special Category Client for import gold/silver. What is the full form of IIBX.",
    "options": ["India International Bullion Exchange", "Indian Importers Bullion Exchange", 
                "India ISDA Bullion Exchange", "International Bullion Exchange of India",
                "Indian Integrated Bullion Exchange"],
    "correct_answer": "India International Bullion Exchange"
},
{
    "question": "The Master Direction on Non-Convertible Debentures of original or initial maturity up to one-year Directions, 2024, specifies the minimum tenor of the instruments as how many days?",
    "options": ["7 days", "15 days", "45 days", "60 days", "90 days"],
    "correct_answer": "90 days"
},
{
    "question": "Which of the following government bonds is a recent addition to the securities permissible for investment by non-residents under the Fully Automated Route?",
    "options": ["Sovereign Gold Bond", "Sovereign Green Bond", "G-sec Floating Rate Bond", 
                "Municipal Bond", "Oil Bond"],
    "correct_answer": "Sovereign Green Bond"
},
{
    "question": "From when will the Reserve Bank of India's Master Direction on Margining for Non-Centrally Cleared OTC Derivatives Directions, 2024 come into force?",
    "options": ["1st Sep 2024", "3rd October 2024", "8th November 2024", "11th December 2024", "1st January 2025"],
    "correct_answer": "8th November 2024"
},
{
    "question": "A derivative contract whose settlement is not guaranteed by a central counterparty is known as?",
    "options": ["NCD", "NCCD", "OCCPS", "ETCD", "ETD"],
    "correct_answer": "NCCD"
},
{
    "question": "CCIL has designed a solution to provide 'Valuation', 'Margining' (both Variation Margin (VM) and Initial Margin (IM)), 'Collateral Management and Margin Maintenance' and Risk Analytics services for NCCDs under its different modules. Name it.",
    "options": ["PRAVAAH", "SARVAM", "QUANTUM", "EKAM", "JEEVAN"],
    "correct_answer": "SARVAM"
},
{
    "question": "What is the full form of SARVAM?",
    "options": ["Service for Analysis of Risk, Valuation and Margining",
                "Service for Analytics of Risk, Valuation and Margining",
                "Solution for Analysis of Risk, Valuation and Margining",
                "Solution for Analytics of Risk, Valuation and Margining",
                "Service for Assessing Risk, Valuation and Margining"],
    "correct_answer": "Service for Analysis of Risk, Valuation and Margining"
},
{
    "question": "What is the minimum rating of NCD with original maturity of up to one year?",
    "options": ["A1", "A2", "A3", "A4", "A5"],
    "correct_answer": "A3"
},
{
    "question": "What is India's Sovereign Debt weightage in JP Morgan's Bond Index?",
    "options": ["2%", "5%", "7%", "10%", "15%"],
    "correct_answer": "10%"
},
{
    "question": "An Organization wish to obtain a License. Under which category of Procurement will it be categorized?",
    "options": ["Goods", "Works", "Consultancy Services", "Other services", "None of these"],
    "correct_answer": "Goods"
},
{
    "question": "An Organization wish to obtain a Patent. Under which category of Procurement will it be categorized?",
    "options": ["Goods", "Works", "Consultancy Services", "Other services", "None of these"],
    "correct_answer": "Goods"
},
{
    "question": "Payments to be made to MSEs within _______ days from the date of supplies by them",
    "options": ["15 days", "30 days", "45 days", "60 days", "90 days"],
    "correct_answer": "45 days"
},
{
    "question": "Who is the competent authority for in principal approval of undertaking the project relating to Construction Projects for Capital Expenditure items (Non-IT)?",
    "options": ["Regional Head in RO", "ZH in ZO", "Vertical Head in CO", 
                "Board of Directors", "Internal Committee of Executives (Premises & Real Estate)"],
    "correct_answer": "Board of Directors"
},
{
    "question": "What is the threshold for a transaction to be considered a 'Material Related Party Transaction' if the transaction exceeds a certain percentage of the Annual Consolidated Turnover of the Bank?",
    "options": ["2% of the Annual Consolidated Turnover", 
                "5% of the Annual Consolidated Turnover",
                "10% of the Annual Consolidated Turnover",
                "15% of the Annual Consolidated Turnover",
                "20% of the Annual Consolidated Turnover"],
    "correct_answer": "10% of the Annual Consolidated Turnover"
},
{
    "question": "A transaction involving payments made to a related party with respect to brand usage or royalty is considered material if it exceeds what percentage of the Bank's Annual Consolidated Turnover?",
    "options": ["2%", "5%", "7%", "10%", "15%"],
    "correct_answer": "5%"
},
{
    "question": "What is the minimum amount in Rupees that a transaction must exceed during a financial year to be classified as a 'Material Related Party Transaction'?",
    "options": ["500 crore", "750 crore", "1,000 crore", "1,500 crore", "2,000 crore"],
    "correct_answer": "1,000 crore"
},
{
    "question": "A 'Material Modification' to a Related Party Transaction is considered material if the value involved exceeds what percentage of the Bank's total income as per the last audited consolidated financial statements or percentage of the Bank's net worth?",
    "options": ["1%,3%", "2%,5%", "3%10%", "4%,6%", "5%,10%"],
    "correct_answer": "2%,5%"
},
{
    "question": "A subsidiary of the Bank will be considered a 'Material Subsidiary' if its Net Worth exceeds percentage of the Consolidated Net Worth of the Bank and its subsidiaries or the Income of the subsidiary must exceed percentage of the Consolidated Income of the Bank and its subsidiaries in the immediately preceding financial year?",
    "options": ["5, 15", "7.5, 12.5", "10, 10", "12.5, 7.5", "15,5"],
    "correct_answer": "10, 10"
},
{
    "question": "By which date must the Bank identify any Material Subsidiary(ies) each year?",
    "options": ["31st March", "30th April", "31st May", "30th June", "31st July"],
    "correct_answer": "30th June"
},
{
    "question": "What is the 'Trading Window' in the context of trading restrictions for Designated Persons and their immediate relatives?",
    "options": ["The period when insider trading is explicitly allowed",
                "The period during which trading in the Bank's securities is prohibited",
                "The period during which the purchase or sale of transactions is allowed, subject to certain conditions",
                "The period before the declaration of dividends",
                "The period after the release of unpublished price sensitive information"],
    "correct_answer": "The period during which the purchase or sale of transactions is allowed, subject to certain conditions"
},
{
    "question": "Who is responsible for deciding the period during which the Trading Window shall be closed?",
    "options": ["The Board of Directors", "The CEO of the Bank", "The Compliance Officer", 
                "The Chief Financial Officer (CFO)", "The Shareholders"],
    "correct_answer": "The Compliance Officer"
},
{
    "question": "How long after the declaration of financial results does the Trading Window remain closed?",
    "options": ["24 hours", "48 hours", "72 hours", "Until the next trading day", "Until the following quarter's results are declared"],
    "correct_answer": "48 hours"
},
{
    "question": "Which of the following is NOT typically a reason for the closure of the Trading Window for the Bank's securities?",
    "options": ["Declaration of dividends", 
                "Issue of securities by way of public/rights/bonus",
                "Amalgamation, mergers, takeovers, and buy-back",
                "Routine operational updates",
                "Disposal of whole or substantially whole of the undertaking"],
    "correct_answer": "Routine operational updates"
},
{
    "question": "Within how many days must a newly appointed Director, Key Managerial Personnel, Promoter, or member of the Promoter group disclose their holdings of the Bank's securities?",
    "options": ["3 days", "5 days", "7 days", "10 days", "15 days"],
    "correct_answer": "7 days"
},
{
    "question": "Pre-clearance by the Compliance Officer is required for trading by designated persons if the value of proposed trades in securities exceeds what amount in a calendar quarter?",
    "options": ["Rs. 5,00,000", "Rs. 7,50,000", "Rs. 10,00,000", "Rs. 15,00,000", "Rs. 20,00,000"],
    "correct_answer": "Rs. 10,00,000"
},
{
    "question": "What is the first step to be taken when a written complaint regarding the leak or suspected leak of UPSI is received?",
    "options": ["Immediate investigation by the MD & CEO",
                "Referral to the SEBI",
                "Notification to the Audit Committee",
                "The MD & CEO writes to the complainee within 5 working days",
                "Suspension of the complainee"],
    "correct_answer": "The MD & CEO writes to the complainee within 5 working days"
},
{
    "question": "Who has the authority to reverse a value-dated transaction in CD/SB/Operative accounts if the transaction is between 7 and 14 days old?",
    "options": ["Branch Head", "Chief Manager/Deputy Regional Head at Regional Office", "Regional Head", 
                "Compliance Officer", "General Manager"],
    "correct_answer": "Regional Head"
},
{
    "question": "What is the maximum period a Branch is allowed to give value-dated clearing credit in Term Loan/Demand Loan accounts without additional approval?",
    "options": ["1 working day", "2 working days", "3 working days", "5 working days", "7 working days"],
    "correct_answer": "3 working days"
},
{
    "question": "Who must approve the reversal of a value-dated transaction in a Term Loan/Demand Loan account if the transaction is over 14 working days old?",
    "options": ["Branch Head", "Chief Manager/Deputy Regional Head at Regional Office", "Regional Head", 
                "General Manager", "Compliance Officer"],
    "correct_answer": "Regional Head"
},
{
    "question": "What is the maximum period a Branch is allowed to value date the opening of a deposit account if the customer's instructions were received but the account couldn't be opened on time due to circumstances beyond the branch's control?",
    "options": ["3 days", "5 days", "7 days", "10 days", "14 days"],
    "correct_answer": "7 days"
},
{
    "question": "Which of the following is required to approve the backdated opening of a deposit account beyond 7 days?",
    "options": ["Branch Head", 
                "Chief Manager/Deputy Regional Head at Regional Office",
                "Regional Head",
                "Chief General Manager/General Manager of Deposit Mobilization Department, Central Office",
                "Compliance Officer"],
    "correct_answer": "Chief General Manager/General Manager of Deposit Mobilization Department, Central Office"
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