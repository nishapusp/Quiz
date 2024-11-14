import streamlit as st
import random

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "To be eligible under Union Contractor Scheme, The borrower must be engaged in the contractor work for minimum….... Years.",
                "options": ["1 year", "2 years", "3 years", "4 years", "5 years"],
                "correct_answer": "2 years"
            },
            {
                "question": "Under Union Contractor Scheme, What shall minimum margin be maintained, if DP is arrived based on BD above 90 days up to 180 days?",
                "options": ["10%", "20%", "30%", "40%", "50%"],
                "correct_answer": "40%"
            },
            {
                "question": "If credit facility of Rs 7 crore to be extended to New to bank customer, what should be minimum collateral required over and above CGTMSE coverage?",
                "options": ["10%", "15%", "20%", "25%", "50%"],
                "correct_answer": "25%"
            },
            {
                "question": "If borrower offered minimum collateral coverage is more than 35%, then margin on loan amount under Union Solar scheme can be reduced up to.....",
                "options": ["20%", "25%", "10%", "15%", "5%"],
                "correct_answer": "15%"
            },
            {
                "question": "The maximum Quantum of Loan permitted under the Union Textile scheme is ….for MSME unit?",
                "options": ["Rs. 10 Crore", "Rs.50 Crore", "Rs.100 Core", "Rs. 25 Crore", "No Ceiling"],
                "correct_answer": "No Ceiling"
            },
            {
                "question": "Under Union Textile Scheme, to consider a unit as Manufacturing unit, then the sales from manufacturing activities should be at least…. of total sales.",
                "options": ["25%", "35%", "50%", "75%", "85%"],
                "correct_answer": "75%"
            },
            {
                "question": "What should be the Minimum margin in case of Union Nari Shakti scheme, if loan amount is up to Rs. 100 lacs",
                "options": ["5%", "10%", "15%", "25%", "20%"],
                "correct_answer": "5%"
            },
            {
                "question": "Which Transaction will be considered as Digital Transaction under Union Turnover Plus Scheme?",
                "options": ["Demand Draft", "Cheques", "Transfer from own account", "UPI", "All of the above"],
                "correct_answer": "UPI"
            },
            {
                "question": "The computation of Bank Finance under Union Turnover Plus Scheme will be",
                "options": [
                    "30% of Digital Portion of Projected Sales",
                    "25% of Balance Portion of Projected Sales",
                    "30% of Digital Portion of Audited Sales",
                    "Option 1 & 2 Both",
                    "Option 2 & 3 Both"
                ],
                "correct_answer": "Option 1 & 2 Both"
            },
            {
                "question": "What would be the Maximum amount of term loan if second hand equipment is financed under Union Ayushman Plus Scheme?",
                "options": ["Rs. 5 crore", "Rs. 10 crore", "Rs. 25 crore", "Rs. 50 crore", "Nil"],
                "correct_answer": "Nil"
            },
            {
                "question": "The repayment period should be co-terminus with maximum permissible age ….....of Medical professional Under Union Ayushman Plus Scheme",
                "options": ["60 Yrs", "70 Yrs", "65 Yrs", "75 Yrs", "No Such age barrier"],
                "correct_answer": "70 Yrs"
            },
            {
                "question": "DSCR Complaince as per benchmark is applicable for loan limit above RS…...... Under Union Equipment Finance Scheme",
                "options": ["Above 25 Lacs", "Above 50 Lacs", "Above 100 Lacs", "Above 200 Lacs", "Above 500 Lacs"],
                "correct_answer": "Above 50 Lacs"
            },
            {
                "question": "What would be Minimum Margin of loan amount under Union Equipment Finance, if borrower is having DSRA of 3 months",
                "options": ["5%", "10%", "15%", "20%", "25%"],
                "correct_answer": "5%"
            },
            {
                "question": "What is the name of the scheme which provide guarantee to the credit facilities under Stand up India Scheme?",
                "options": ["CGTMSE", "CGFMU", "CGSSI", "CEFSSC", "NCGTC"],
                "correct_answer": "CGSSI"
            },
            {
                "question": "Who Launched the ZED Certification Scheme?",
                "options": ["MSDE", "MoMSME", "RBI", "NABARD", "SIDBI"],
                "correct_answer": "MoMSME"
            }
{
                "question": "M/s XYZ Pvt ltd. Having consortium banking exposure of Rs 600 Crore. Out of that one single account of Rs.275 Crore extended by our bank, Now customer approach Rs. 2o Crore loan to new established sister concern. Who will be the delegated authority for the new loan?",
                "options": ["RLCC I Headed by DGM", "ZLCC", "LCV", "MSME CO", "MCV"],
                "correct_answer": "LCV"
            },
            {
                "question": "Which of the following is an information service provider who collects information related to corporate companies from various repositories like MCA, CRILC, RBI, Court Judgements etc?",
                "options": ["CERSAI", "ICRA", "NeSL", "Corpository", "Bank Bazar"],
                "correct_answer": "Corpository"
            },
            {
                "question": "CIBIL MSME Rank shall be applicable for MSME proposals having exposure of ............",
                "options": [
                    "Above Rs.10 lakhs up to Rs.10 Crores",
                    "Above Rs.10 lakhs up to Rs.25 Crores",
                    "Above Rs.25 lakhs up to Rs.10 Crores",
                    "Above Rs.25 lakhs up to Rs.25 Crores",
                    "Above Rs.10 lakhs up to Rs.100 Crores"
                ],
                "correct_answer": "Above Rs.25 lakhs up to Rs.25 Crores"
            },
            {
                "question": "Who is the authority to permit internet banking facility in CC accounts for borrowers rated CR-4 as per Internal Rating?",
                "options": ["Branch Head", "Regional Head", "Zonal Head", "ZLCC", "RLCC I"],
                "correct_answer": "Regional Head"
            },
            {
                "question": "Which of the followings does not falls under thrust areas of lending?",
                "options": ["Channel Financing", "Trade Financing", "Data Center Infrastructure", "Rice Mills", "HAM Project-NHAI"],
                "correct_answer": "Rice Mills"
            },
            {
                "question": "Which of the following statement is not correct regarding takeover of advances?",
                "options": [
                    "The takeover norms should also apply where the borrower comes to another bank after closing account with the previous bank within 3 months.",
                    "The advance to be taken over should be rated CR4/UBC4 or better",
                    "The unit should be in existence for minimum 1 years",
                    "The TOL/TNW shall be permitted up to 6:1 for advances taken over under Union Liqui Property scheme",
                    "In case of takeover of composite limit (TL+CC), the minimum remaining period of scheduled repayment for term loan in future may be less than 2 years."
                ],
                "correct_answer": "The unit should be in existence for minimum 1 years"
            },
            {
                "question": "As per loan policy, the acceptable ratios for considering loan proposal favorably is..........",
                "options": [
                    "Current Ratio 1.17, TOL/TNW 4 :1, Average DSCR 1.25, DER 2 : 1",
                    "Current Ratio 1.33, TOL/TNW 3 :1, Average DSCR 1.5, DER 2 : 1",
                    "Current Ratio 1.15, TOL/TNW 4 :1, TOL: TNW 5:1 (for Trade Advance) Average DSCR 1.5, DER 3 : 1",
                    "Current Ratio 1.15, TOL/TNW 4 :1, Average DSCR 1.5, DER 3 : 1",
                    "No such ratios to be maintained/considered"
                ],
                "correct_answer": "Current Ratio 1.15, TOL/TNW 4 :1, TOL: TNW 5:1 (for Trade Advance) Average DSCR 1.5, DER 3 : 1"
            },
            {
                "question": "The activity of a trader, who is requesting loan of Rs. 10 Crore under Union MSME Suvidha Scheme, falls under Low priority area. Delegation of proposal in the said account......",
                "options": [
                    "Respective sanctioning authority",
                    "Minimum RLCC-I",
                    "Minimum ZLCC",
                    "Next higher authority up to RLCC",
                    "Next higher authority up to ZLCC"
                ],
                "correct_answer": "Respective sanctioning authority"
            },
            {
                "question": "What is the hurdle rate of internal credit rating............",
                "options": [
                    "CR 2 for New and CR 5 for Take over",
                    "CR 4 for New and CR 5 for Take over",
                    "CR 5 for both New and Take over",
                    "CR 4 for Take over and CR 5 for New accounts",
                    "CR-3 for new account & CR-4 for takeover account"
                ],
                "correct_answer": "CR 4 for Take over and CR 5 for New accounts"
            },
            {
                "question": "In case of new Commercial Loan proposal of Rs.25.00 lacs and above to staff relative, the delegation shall vest with.............",
                "options": ["CAC-I & Above", "CAC-II & Above", "CAC-III & Above", "ZLCC", "RLCC I"],
                "correct_answer": "CAC-II & Above"
            },
            {
                "question": "Who has to conduct vetting of documents for loans up to Rs.10.00 lakh?",
                "options": [
                    "Branch Manager/Credit officer",
                    "Branch Manager only",
                    "Law officer",
                    "Empanel advocate",
                    "Vetting is not mandatory for all loans up to Rs.10.00 lacs"
                ],
                "correct_answer": "Branch Manager/Credit officer"
            },
            {
                "question": "Average DSCR of …........and minimum DSCR of …......... is applicable for appraisal for projects under Infrastructure other than social & commercial Infra.",
                "options": ["1.3 & 1.1", "1.5 & 1.2", "1.5 & 1.1", "1.3 & 1.2", "1.2 & 1.5"],
                "correct_answer": "1.3 & 1.1"
            },
            {
                "question": "Takeover norms are not applicable to retail lending schemes, except…...",
                "options": ["Union Home", "Union Awas", "Union Miles", "Union Mortgage", "Union Education"],
                "correct_answer": "Union Mortgage"
            },
            {
                "question": "The cut-off date for pricing of loan as per credit rating will be…....",
                "options": [
                    "3 Months from Closure of FY",
                    "6 Months from Closure of FY",
                    "7 Months from Closure of FY",
                    "8 Months from Closure of FY",
                    "31st December"
                ],
                "correct_answer": "8 Months from Closure of FY"
            },
            {
                "question": "The CIBIL MSME Rank of an existing borrower is CMR 7, requesting enhancement in the existing exposure, who will be the delegated authority in this case…",
                "options": [
                    "Respective sanctioning authority",
                    "Minimum RLCC-I",
                    "Minimum ZLCC",
                    "Next higher authority up to RLCC- I",
                    "Next higher authority up to ZLCC"
                ],
                "correct_answer": "Next higher authority up to RLCC I"
            },
            {
                "question": "What is the global mix of our Bank's Business as of March 24?",
                "options": ["21.38 Trillion", "21.26 Trillion", "21.36 Trillion", "21.58 trillion", "21.46 trillion"],
                "correct_answer": "21.36 Trillion"
            },
            {
                "question": "What is our Bank's Share amongst PSBs in terms business?",
                "options": ["9.32%", "9.40%", "9.26%", "9.50%", "9.38%"],
                "correct_answer": "9.40%"
            },
            {
                "question": "In terms of Business Mix Our Bank is ranked at?",
                "options": ["2nd", "3rd", "4th", "5th", "6th"],
                "correct_answer": "5th"
            },
            {
                "question": "Which of the following is NOT the newly created vertical by the Bank?",
                "options": ["Digitization", "Wealth Management", "Recon", "TMFM", "RUSU & FI"],
                "correct_answer": "Digitization"
            },
            {
                "question": "Our Bank's Operating Profit as of Mar 24 is (in Rs)?",
                "options": ["25434 cr", "28311 cr", "27453cr", "28211 cr", "27654cr"],
                "correct_answer": "28211 cr"
            },
            {
                "question": "Which of the following is not the JV of our Bank?",
                "options": [
                    "SUD Life",
                    "India International Bank Malaysia",
                    "Chaitanya Godavari Gramin Bank",
                    "ASREC India Ltd",
                    "none of the above"
                ],
                "correct_answer": "Chaitanya Godavari Gramin Bank"
            },
            {
                "question": "Our Bank has been awarded Finnoviti Award 2024 which is given for?",
                "options": [
                    "Two innovative products organized by banking frontiers",
                    "Exemplary Leadership in areas of BFSI",
                    "For Training in BFSI",
                    "Fintech collaboration",
                    "For HR transformation"
                ],
                "correct_answer": "Two innovative products organized by banking frontiers"
            },
            {
                "question": "Current Chairman of our Bank is?",
                "options": [
                    "Sameer Shukla",
                    "Srinivasan Vardarajan",
                    "Laxman Singh Uppal",
                    "Jayadev M",
                    "Shri Suraj Srivastava"
                ],
                "correct_answer": "Srinivasan Vardarajan"
            },
            {
                "question": "Under LEAD, one of the Aspirations of the Bank is '1 Trillion Incremental CASA Plus'",
                "options": [
                    "Term Deposit",
                    "Retail Term Deposit",
                    "Recurring Term Deposit",
                    "Flexi Term Deposit",
                    "Bulk Term Deposit"
                ],
                "correct_answer": "Retail Term Deposit"
            },
            {
                "question": "Each District will have one BRM who will be an Officer in Scale___cadre. Fill in the blank.",
                "options": ["III", "IV", "V", "III or IV", "IV or V"],
                "correct_answer": "III or IV"
            },
            {
                "question": "What is the aspiration of Bank under WIN?",
                "options": [
                    "To become bank of first choice",
                    "To become next generation bank",
                    "To become digital bank",
                    "To become most preferred bank",
                    "To become best bank in RAM Sector"
                ],
                "correct_answer": "To become most preferred bank"
            },
            {
                "question": "Women constitutes ___ % of total Bank's customer base, however their share in total business is around ___% only",
                "options": ["45, 15", "43,11", "42,19", "41, 17", "42,11"],
                "correct_answer": "41, 17"
            },
            {
                "question": "Bank has identified __ Growth Hotspots in the country out of which __ hotspots are in aspirational district.",
                "options": ["51,33", "53,11", "56,33", "53,31", "54, 31"],
                "correct_answer": "51,33"
            },
            {
                "question": "Under Union Phoenix's bank initiative, there is a 4-step targeted customer reach out with a minimum 2 Hr/day commitment from each branch. Which one of these steps is not part of this approach?",
                "options": [
                    "Understand customer grievances and initiate customer relationship building",
                    "Follow up with the concerned vertical to resolve the issue/customer grievance",
                    "Resolve issue and communicate a/c upgrade benefit enable transaction mode and take balance increase promise",
                    "Follow up on balance increase and pitch for upgrade benefits",
                    "Follow up on balance increase and product cross-sell to drive stickiness"
                ],
                "correct_answer": "Follow up with the concerned vertical to resolve the issue/customer grievance"
            },
            {
                "question": "Bank has introduced Union SWAR which is focusing on four areas heart, body mind and soul wellness for the employees. Fill in the banks: SWAR Stands for ______",
                "options": ["Wellness", "and", "Resilience", "Self", "Supporting"],
                "correct_answer": "Supporting"
            },
            {
                "question": "Which of the following is a Corporate borrower?",
                "options": [
                    "Sole Proprietorship Firm",
                    "Hindu Undivided Family (HUF)",
                    "Limited Liability Partnership",
                    "Trust",
                    "Co-operative Society"
                ],
                "correct_answer": "Limited Liability Partnership"
            },
            {
                "question": "TReDS stands for…..",
                "options": [
                    "Trade Receivable Discounting System",
                    "Trade Receivable e-Discounting System",
                    "Trade Recoverable e-Discounting System",
                    "Trade Retrievable e-Discounting System",
                    "Trade Receivable Digital System"
                ],
                "correct_answer": "Trade Receivable Discounting System"
            }

        ]
        
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'questions_answered' not in st.session_state:
            st.session_state.questions_answered = []

    def run(self):
        st.title("Promotion Quiz")
        
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
                st.session_state.current_question += 1
                st.experimental_rerun()
            else:
                st.balloons()
                st.success(f"Quiz completed! Final score: {st.session_state.score}/{len(self.quiz_data)}")
                if st.button("Restart Quiz"):
                    st.session_state.current_question = 0
                    st.session_state.score = 0
                    st.session_state.questions_answered = []
                    st.experimental_rerun()

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()