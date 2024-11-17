import streamlit as st
import random
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = [
          {
        "question": "Volume of cheque-based payments to be less than …% of the total retail payments:",
        "options": [
            "0.25",
            "0.2", 
            "0.3",
            "0.5",
            "0.75"
        ],
        "correct_answer": "0.25"
    },
    {
        "question": "Payment Vision Document is published by:",
        "options": [
            "SEBI",
            "RBI",
            "Government of India",
            "Department of Financial Services",
            "PFRDA"
        ],
        "correct_answer": "RBI"
    },
    {
        "question": "The Payment Vision Document was published for the first time in:",
        "options": [
            "2000",
            "2008",
            "2001",
            "2022",
            "2016"
        ],
        "correct_answer": "2001"
    },
    {
        "question": "… System is used to settle financial transactions through the transfer of monetary value:",
        "options": [
            "Payment",
            "Settlement",
            "SWIFT",
            "CHAP",
            "TARGET"
        ],
        "correct_answer": "Payment"
    },
    {
        "question": "Which is not a benefit of a successful payment and settlement system?",
        "options": [
            "Increase in the number of bank branches",
            "Convenience",
            "Reduced transaction cost",
            "Improved efficiency",
            "Increased transparency"
        ],
        "correct_answer": "Increase in the number of bank branches"
    },
    {
        "question": "Payment Vision 2025 document outlines the thought process for the period up to:",
        "options": [
            "January 2025",
            "December 2025",
            "July 2025",
            "December 2024",
            "January 2026"
        ],
        "correct_answer": "December 2025"
    },
    {
        "question": "Vision 2021 document was provided by RBI in:",
        "options": [
            "January 2019",
            "January 2020",
            "May 2019",
            "December 2020",
            "January 2021"
        ],
        "correct_answer": "May 2019"
    },
    {
        "question": "As per PV 2025, the intention is to increase debit card transactions at PoS by:",
        "options": [
            "20%",
            "30%",
            "25%",
            "15%",
            "10%"
        ],
        "correct_answer": "20%"
    },
    {
        "question": "It is envisioned that UPI will register average annualized growth of … and IMPS/NEFT at …:",
        "options": [
            "10 and 10",
            "50 and 20",
            "40 and 30",
            "50 and 10",
            "20 and 50"
        ],
        "correct_answer": "50 and 20"
    },
    {
        "question": "Payments Vision 2025 document is presented across the … anchor goalposts:",
        "options": [
            "SEVEN",
            "THREE",
            "FOUR",
            "FIVE",
            "SIX"
        ],
        "correct_answer": "FIVE"
    },
    {
        "question": "The core theme for Payment Vision has four 'E's. Which of the following is not one of them?",
        "options": [
            "Everything",
            "Everytime",
            "Everywhere",
            "E-Payments",
            "Everyone"
        ],
        "correct_answer": "Everything"
    },
    {
        "question": "Which of the following is not a goal post of the Payment Vision 2025?",
        "options": [
            "Inclusion",
            "Innovation",
            "Institutionalisation",
            "Information",
            "Internationalisation"
        ],
        "correct_answer": "Information"
    },
    {
        "question": "What is phishing?",
        "options": [
            "A type of fish",
            "A security attack to steal sensitive data",
            "A software program",
            "A data analysis method",
            "None of the above"
        ],
        "correct_answer": "A security attack to steal sensitive data"
    },
    {
        "question": "Which of these is considered a strong password?",
        "options": [
            "12345",
            "password",
            "john123",
            "ASD123!@#",
            "noneoftheabove"
        ],
        "correct_answer": "ASD123!@#"
    },
# Continue previous list...
    {
        "question": "What is a firewall?",
        "options": [
            "Filters network traffic",
            "Steals data",
            "Manages database",
            "Speeds up the network",
            "None of the above"
        ],
        "correct_answer": "Filters network traffic"
    },
    {
        "question": "Which of the following is a malware used to exploit a target computer?",
        "options": [
            "Keylogger",
            "VPN",
            "SSD",
            "HDMI",
            "CPU"
        ],
        "correct_answer": "Keylogger"
    },
    {
        "question": "What is the main purpose of two-factor authentication?",
        "options": [
            "To double the password strength",
            "To add a second password",
            "To require two forms of user verification",
            "To lock the account after two attempts",
            "None of the above"
        ],
        "correct_answer": "To require two forms of user verification"
    },
    {
        "question": "What is a blockchain primarily used for?",
        "options": [
            "Data storage",
            "Transaction management",
            "Creating digital art",
            "Network configuration",
            "None of the above"
        ],
        "correct_answer": "Transaction management"
    },
    {
        "question": "What does the term 'mining' mean in the context of cryptocurrency?",
        "options": [
            "Extracting stone",
            "Creating new coins",
            "Data processing",
            "Developing new blockchains",
            "All of the above"
        ],
        "correct_answer": "Creating new coins"
    },
    {
        "question": "Which of the following is a popular blockchain platform?",
        "options": [
            "Ethereum",
            "Google",
            "Facebook",
            "Amazon",
            "None of the above"
        ],
        "correct_answer": "Ethereum"
    },
    {
        "question": "What is a 'smart contract'?",
        "options": [
            "A legal agreement",
            "A computer protocol intended to digitally facilitate a contract",
            "A new smartphone feature",
            "An AI lawyer",
            "None of the above"
        ],
        "correct_answer": "A computer protocol intended to digitally facilitate a contract"
    },
    {
        "question": "Which entity does blockchain technology make less necessary?",
        "options": [
            "Miners",
            "Programmers",
            "Middlemen",
            "Graphic designers",
            "None of the above"
        ],
        "correct_answer": "Middlemen"
    },
    {
        "question": "What is artificial intelligence?",
        "options": [
            "Machines performing tasks that require human intelligence",
            "A science fiction movie",
            "A type of computer",
            "A programming language",
            "None of the above"
        ],
        "correct_answer": "Machines performing tasks that require human intelligence"
    },
    {
        "question": "What is machine learning?",
        "options": [
            "A robot that learns from books",
            "A computer program that improves through experience",
            "A method for data storage",
            "A network protocol",
            "None of the above"
        ],
        "correct_answer": "A computer program that improves through experience"
    },
    {
        "question": "Which of the following is an application of AI?",
        "options": [
            "Automated driving",
            "Calculators",
            "Web browsers",
            "Electricity",
            "None of the above"
        ],
        "correct_answer": "Automated driving"
    },
    {
        "question": "Which algorithm is commonly used for recommendation systems?",
        "options": [
            "Linear regression",
            "Naive Bayes",
            "Collaborative filtering",
            "Binary search",
            "None of the above"
        ],
        "correct_answer": "Collaborative filtering"
    },
    {
        "question": "What does 'natural language processing' enable computers to do?",
        "options": [
            "Calculate faster",
            "Understand human language",
            "Connect to the Internet",
            "Display graphics",
            "None of the above"
        ],
        "correct_answer": "Understand human language"
    },
    {
        "question": "What is robotic process automation?",
        "options": [
            "Using robots to perform manual tasks",
            "Automating repetitive tasks with software",
            "Developing new robotics technology",
            "Programming in C++",
            "None of the above"
        ],
        "correct_answer": "Automating repetitive tasks with software"
    },
    {
        "question": "What is a 'bot' in RPA?",
        "options": [
            "A robot that performs surgeries",
            "A term for a bug in software",
            "An automated software that mimics human actions",
            "A new gaming console",
            "None of the above"
        ],
        "correct_answer": "An automated software that mimics human actions"
    },
    {
        "question": "Which sector most benefits from RPA?",
        "options": [
            "Agriculture",
            "Banking",
            "Construction",
            "Retail",
            "All of the above"
        ],
        "correct_answer": "Banking"
    },
    {
        "question": "What type of tasks is RPA best suited for?",
        "options": [
            "Highly complex tasks",
            "Tasks requiring emotional judgment",
            "Repetitive, rule-based tasks",
            "Creative tasks",
            "None of the above"
        ],
        "correct_answer": "Repetitive, rule-based tasks"
    },
    {
        "question": "Which of these is a common tool used in RPA?",
        "options": [
            "UiPath",
            "Photoshop",
            "Excel",
            "Oracle",
            "None of the above"
        ],
        "correct_answer": "UiPath"
    },
{
        "question": "What does UPI stand for?",
        "options": [
            "Unified Payment Interface",
            "Universal Payment Integration",
            "Unique Payment Identification",
            "User Profile Information",
            "None of the above"
        ],
        "correct_answer": "Unified Payment Interface"
    },
    {
        "question": "What is required to use UPI?",
        "options": [
            "Credit card",
            "Bank account",
            "Smartphone",
            "Both b) and c)",
            "All of the above"
        ],
        "correct_answer": "Both b) and c)"
    },
    {
        "question": "Which feature is a major advantage of UPI?",
        "options": [
            "Instant money transfer",
            "International transactions",
            "Investment tracking",
            "Credit scoring",
            "None of the above"
        ],
        "correct_answer": "Instant money transfer"
    },
    {
        "question": "How does UPI ensure security?",
        "options": [
            "Using encryption",
            "Physical security measures",
            "User education",
            "Software updates",
            "None of the above"
        ],
        "correct_answer": "Using encryption"
    },
    {
        "question": "Which of the following can be done via UPI?",
        "options": [
            "Paying utility bills",
            "Booking flights",
            "Shopping online",
            "All of the above",
            "None of the above"
        ],
        "correct_answer": "All of the above"
    },
    {
        "question": "What is SQL used for?",
        "options": [
            "Programming games",
            "Managing databases",
            "Editing videos",
            "Writing documents",
            "None of the above"
        ],
        "correct_answer": "Managing databases"
    },
    {
        "question": "What feature in Excel performs calculations?",
        "options": [
            "Tables",
            "Charts",
            "Formulas",
            "Themes",
            "None of the above"
        ],
        "correct_answer": "Formulas"
    },
    {
        "question": "What is the primary purpose of PowerPoint?",
        "options": [
            "Word processing",
            "Database management",
            "Creating presentations",
            "Email",
            "None of the above"
        ],
        "correct_answer": "Creating presentations"
    },
    {
        "question": "What is a key goal of disaster recovery?",
        "options": [
            "Data preservation",
            "Cost reduction",
            "Increasing sales",
            "Employee training",
            "None of the above"
        ],
        "correct_answer": "Data preservation"
    },
    {
        "question": "What is the main focus of business continuity planning?",
        "options": [
            "Maintaining business operations during disruptions",
            "Reducing business costs",
            "Expanding into new markets",
            "Hiring staff",
            "None of the above"
        ],
        "correct_answer": "Maintaining business operations during disruptions"
    },
    {
        "question": "What is the purpose of a firewall in cybersecurity?",
        "options": [
            "Network monitoring",
            "Malware detection",
            "Intrusion prevention",
            "Access control",
            "Data encryption"
        ],
        "correct_answer": "Access control"
    },
    {
        "question": "What is the most common type of cyber attack?",
        "options": [
            "Phishing",
            "DDoS",
            "SQL Injection",
            "Ransomware",
            "Man in the middle"
        ],
        "correct_answer": "Phishing"
    },
{
        "question": "Which of the following is NOT a best practice for creating strong passwords?",
        "options": [
            "Use Password Manager",
            "Using easy and simple passwords",
            "Using Pass phrases",
            "Using unique phrases",
            "Using upper and lower case letters, numbers and symbols"
        ],
        "correct_answer": "Using easy and simple passwords"
    },
    {
        "question": "Which encryption protocol is widely used for securing web traffic?",
        "options": [
            "SSL: Secure Sockets Layer",
            "TLS: Transport Layer Security",
            "SSH:Secure Socket Shell",
            "PGP: Pretty Good Privacy",
            "Ipsec:Internet Protocol Security"
        ],
        "correct_answer": "TLS: Transport Layer Security"
    },
    {
        "question": "What does VPN stand for in the context of cybersecurity?",
        "options": [
            "Virtual Private Network",
            "Very Private Network",
            "Valid Public Network",
            "Virtual Protection Network",
            "Verified Private Network"
        ],
        "correct_answer": "Virtual Private Network"
    },
    {
        "question": "What is the primary purpose of a penetration test?",
        "options": [
            "Test software",
            "Test security",
            "Test usability",
            "Test compatibility",
            "Test performance"
        ],
        "correct_answer": "Test security"
    },
    {
        "question": "Which of the following is NOT a common authentication factor when we talk about Cyber Security?",
        "options": [
            "Something you have",
            "Something you know",
            "Something you are",
            "Something you desire",
            "Something you wear"
        ],
        "correct_answer": "Something you desire"
    },
    {
        "question": "What does the term 'phishing' refer to in cybersecurity?",
        "options": [
            "Malicious software",
            "Social Engineering",
            "Physical Intrusion",
            "Denial of Service",
            "Unauthorised Access"
        ],
        "correct_answer": "Social Engineering"
    },
    {
        "question": "What type of cyber attack involves flooding a network with excessive requests to overload it?",
        "options": [
            "Phishing",
            "DDoS",
            "Spoofing",
            "Bruteforce",
            "Cross side scripting"
        ],
        "correct_answer": "DDoS"
    },
    {
        "question": "What is the purpose of a honeypot in cybersecurity?",
        "options": [
            "Gather data",
            "Detect Intrusions",
            "Encrypt Data",
            "Block Access",
            "Filter traffic"
        ],
        "correct_answer": "Detect Intrusions"
    },
    {
        "question": "Which of the following is NOT a potential consequence of a data breach?",
        "options": [
            "Financial Loss",
            "Reputational Damage",
            "Legal Penalties",
            "Improved Security",
            "Identity Theft"
        ],
        "correct_answer": "Improved Security"
    },
    {
        "question": "What is the term for a piece of software that appears legitimate but actually carries out malicious activities?",
        "options": [
            "Trojan",
            "Worm",
            "Spyware",
            "Rootkit",
            "Ransomware"
        ],
        "correct_answer": "Trojan"
    },
    {
        "question": "What does the 'S' stand for in the abbreviation 'HTTPS'?",
        "options": [
            "Secret",
            "Secure",
            "Software",
            "Session",
            "Storage"
        ],
        "correct_answer": "Secure"
    },
    {
        "question": "Which of the following is a common method for protecting sensitive data in transit?",
        "options": [
            "Encryption",
            "Compression",
            "Obfuscation",
            "Redundancy",
            "Fragmentation"
        ],
        "correct_answer": "Encryption"
    },
    {
        "question": "What does IDS stand for in the context of cybersecurity?",
        "options": [
            "Intrusion Detection System",
            "Internet Defense System",
            "Internal Data Scanner",
            "Intruder Deterrent System",
            "Information Defense System"
        ],
        "correct_answer": "Intrusion Detection System"
    },
    {
        "question": "What is a common method for protecting against SQL injection attacks?",
        "options": [
            "Parameterized queries",
            "Captcha",
            "Two factor authentication",
            "Session management",
            "Biometric Authentication"
        ],
        "correct_answer": "Parameterized queries"
    },
    {
        "question": "What type of cyber attack involves manipulating users into performing actions or divulging confidential information?",
        "options": [
            "Social Engineering",
            "Ransomware",
            "DDoS",
            "Man in the Middle",
            "Phishing"
        ],
        "correct_answer": "Social Engineering"
    },
    {
        "question": "Which of the following is a characteristic of a strong cybersecurity culture within an organization?",
        "options": [
            "Blaming individuals",
            "Reactive approach",
            "Proactive approach",
            "Lack of Training",
            "Ignoring Incidents"
        ],
        "correct_answer": "Proactive approach"
    },
    {
        "question": "What is a zero-day vulnerability?",
        "options": [
            "Known and Patched Vulnerability",
            "Previously unknown vulnerability",
            "Expired Vulnerability",
            "Vulnerability with no fix",
            "Temporary Vulnerability"
        ],
        "correct_answer": "Previously unknown vulnerability"
    },
    {
        "question": "What is the purpose of multi-factor authentication (MFA)?",
        "options": [
            "Increase security",
            "Decrease Usability",
            "Decrease Cost",
            "Increase Speed",
            "Decrease complexity"
        ],
        "correct_answer": "Increase security"
    },
{
        "question": "Which of the following is NOT a common cyber threat actor?",
        "options": [
            "Hactivist",
            "Insider Threat",
            "Script Kiddie",
            "Black Hat Hacker",
            "Marketing Manager"
        ],
        "correct_answer": "Marketing Manager"
    },
    {
        "question": "What is the primary objective of a security policy in an organization?",
        "options": [
            "Secure the network",
            "Secure the Data",
            "Secure the premises",
            "Secure the employees",
            "Secure the finances"
        ],
        "correct_answer": "Secure the Data"
    },
    {
        "question": "Which of the following is a common method for securing IoT devices?",
        "options": [
            "Weak passwords",
            "Regular Updates",
            "Network Segmentation",
            "Firmware downgrades",
            "Public Access Points"
        ],
        "correct_answer": "Network Segmentation"
    },
    {
        "question": "What is the main purpose of encryption in cybersecurity?",
        "options": [
            "Protect data at rest",
            "Protect data in transit",
            "Protect data in use",
            "Protect data at risk",
            "Protect data at storage"
        ],
        "correct_answer": "Protect data in transit"
    },
    {
        "question": "What does the term 'malware' refer to in cybersecurity?",
        "options": [
            "Malicious software",
            "Security hardware",
            "Network protocol",
            "Encryption algorithm",
            "Secure Authentication"
        ],
        "correct_answer": "Malicious software"
    },
    {
        "question": "Which of the following is NOT a component of the CIA triad in cybersecurity?",
        "options": [
            "Confidentiality",
            "Integrity",
            "Authentication",
            "Availability",
            "All the above"
        ],
        "correct_answer": "Authentication"
    },
    {
        "question": "What is a common method for protecting against ransomware attacks?",
        "options": [
            "Regular backups",
            "Anti-virus software",
            "Strong passwords",
            "Public Wi-Fi",
            "Data sharing"
        ],
        "correct_answer": "Regular backups"
    },
    {
        "question": "Which of the following is NOT a common type of malware?",
        "options": [
            "Virus",
            "Trojan",
            "Worm",
            "Firewall",
            "Spyware"
        ],
        "correct_answer": "Firewall"
    },
{
        "question": "What does the term 'botnet' refer to in cybersecurity?",
        "options": [
            "Network of infected devices",
            "Secure network",
            "Group of security experts",
            "Network of automated tasks",
            "Virtual private network"
        ],
        "correct_answer": "Network of infected devices"
    },
    {
        "question": "What is the purpose of a security audit in cybersecurity?",
        "options": [
            "Identify weaknesses",
            "Test software",
            "Secure the network",
            "Encrypt data",
            "Monitor traffic"
        ],
        "correct_answer": "Identify weaknesses"
    },
    {
        "question": "What is the full form of UVConn?",
        "options": [
            "Union Video Connect",
            "Union Virtual Connection",
            "Union Virtual Connect",
            "Union Voice Assistant",
            "Union Virtual Banking"
        ],
        "correct_answer": "Union Virtual Connect"
    },
    {
        "question": "When was UVConn first launched for customers?",
        "options": [
            "11.11.2018",
            "11.11.2019",
            "11.11.2020",
            "11.11.2021",
            "11.11.2022"
        ],
        "correct_answer": "11.11.2021"
    },
    {
        "question": "How many languages were supported during the initial launch of UVConn?",
        "options": [
            "1",
            "3",
            "4",
            "5",
            "7"
        ],
        "correct_answer": "4"
    },
    {
        "question": "How many languages UVConn 2.0 and 3.0 supports?",
        "options": [
            "1",
            "3",
            "4",
            "5",
            "7"
        ],
        "correct_answer": "7"
    },
    {
        "question": "What is the Bank's Official Business Account Number used for UVConn?",
        "options": [
            "9606060660",
            "9660606060",
            "9666606060",
            "9666666060",
            "9660606660"
        ],
        "correct_answer": "9666606060"
    },
    {
        "question": "How many factor of authentication UVConn Supports?",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ],
        "correct_answer": "3"
    },
    {
        "question": "Which of the mentioned languages was not supported during initial launch of UVConn?",
        "options": [
            "English",
            "Hindi",
            "Kannada",
            "Telugu",
            "Bengali"
        ],
        "correct_answer": "Bengali"
    },
    {
        "question": "Which of these is not a factor of authentication in UVConn?",
        "options": [
            "MPIN",
            "TPIN",
            "OTP",
            "OTP & MPIN",
            "Mobile Lock"
        ],
        "correct_answer": "Mobile Lock"
    },
    {
        "question": "MPIN for UVConn is of how many digit or character?",
        "options": [
            "2",
            "3",
            "4",
            "5",
            "6"
        ],
        "correct_answer": "4"
    },
    {
        "question": "Which of the features is not available in UVConn?",
        "options": [
            "Account Balance",
            "Locker rent Enquiry",
            "Locker rent payment",
            "Positive Pay",
            "Interest Certificates"
        ],
        "correct_answer": "Locker rent payment"
    },
    {
        "question": "How many new services have been launched in UVConn 3.0?",
        "options": [
            "5",
            "10",
            "12",
            "14",
            "15"
        ],
        "correct_answer": "14"
    },
    {
        "question": "Which of the following is not a new feature added under UVConn 3.0?",
        "options": [
            "Balance Enquiry",
            "Balance Certificate",
            "Re-KYC",
            "Credit Card Statement",
            "Green Pin for Credit Card"
        ],
        "correct_answer": "Balance Enquiry"
    },
    {
        "question": "In which endpoint device metaverse(Uni-Verse) portal can be opened?",
        "options": [
            "Laptop",
            "Desktop",
            "Laptop & Desktop",
            "Mobile",
            "Iphones"
        ],
        "correct_answer": "Laptop & Desktop"
    },
{
        "question": "URL to access the metaverse(Uni-Verse) of Union bank of India?",
        "options": [
            "https://metaverse.unionbankofindia.co.in/WebGL",
            "https://metaverse.unionbankofindia.co.in/",
            "https://unionbankofindia.co.in/MetaVerse",
            "https://unionbankofindia.co.in/MetaVerse_WebGL",
            "https://unionbankofindia.co.in/MetaVerse.aspx"
        ],
        "correct_answer": "https://metaverse.unionbankofindia.co.in/WebGL"
    },
    {
        "question": "Users can select one out of how many available Avatar in MetaVerse(Uni-Verse)?",
        "options": [
            "2",
            "3",
            "4",
            "5",
            "6"
        ],
        "correct_answer": "3"
    },
    {
        "question": "In Metaverse, which of the options/features are not available under customer service?",
        "options": [
            "Balance Enquiry",
            "360 Account Statement",
            "Personalized Debit Card",
            "Mini Statement",
            "Card Hotlisting"
        ],
        "correct_answer": "Card Hotlisting"
    },
    {
        "question": "In Metaverse, Which of the following option/features not available under Banking Services?",
        "options": [
            "Deposit",
            "Govt. Sponsered schemes",
            "Digital",
            "Loan",
            "Insurance & MF"
        ],
        "correct_answer": "Insurance & MF"
    },
    {
        "question": "Which of the following is not available in Metaverse?",
        "options": [
            "Digital Lounge",
            "Banking Services",
            "Customer Services",
            "Hall of Fame",
            "Wall of Fame"
        ],
        "correct_answer": "Hall of Fame"
    },
    {
        "question": "In Metaverse, Which of the following is not available under Govt. Sponsered schemes?",
        "options": [
            "VKYC",
            "PMJJBY",
            "PMSBY",
            "APY",
            "SSY"
        ],
        "correct_answer": "VKYC"
    },
{
        "question": "In Metaverse, Which of the following is not available under Digital tab of Banking Services?",
        "options": [
            "Internet",
            "SMS",
            "Mobile",
            "WhatsAPP",
            "Voice Banking"
        ],
        "correct_answer": "Voice Banking"
    },
    {
        "question": "Which of the following award is not listed in wall of Fame of Metaverse?",
        "options": [
            "CIO 100 Award 2022",
            "BFSI Use of emerging Technologies 2023",
            "IBA Banking Technology Awards 2022",
            "Retail Banker Asia Trailblazer Awards 2022",
            "CIO Cloud Leadership Award 2022"
        ],
        "correct_answer": "CIO Cloud Leadership Award 2022"
    },
    {
        "question": "What action will be initiated when any user clicks of 'more info' in Metaverse?",
        "options": [
            "Feedback form will open",
            "SMS will be sent to user",
            "email will be sent to user",
            "whatsapp message will be sent to user",
            "automated call will be generated"
        ],
        "correct_answer": "email will be sent to user"
    },
    {
        "question": "Metaverse can be accessed in?",
        "options": [
            "1D",
            "2D",
            "3D",
            "2D & 3D",
            "1D & 3D"
        ],
        "correct_answer": "2D & 3D"
    },
    {
        "question": "What is the full form of GBM in terms of digital products?",
        "options": [
            "Google Business Messages",
            "Google Business Messaging",
            "Geo Business Messaging",
            "Google Business Machine",
            "Google Business Message"
        ],
        "correct_answer": "Google Business Messaging"
    },
    {
        "question": "In case of GBM, what are the categories of features?",
        "options": [
            "Apply now",
            "Know Our Products",
            "Service",
            "Locate Us",
            "Search"
        ],
        "correct_answer": "Search"
    },
    {
        "question": "Which of the following is not a part of Know Our Products of GBM?",
        "options": [
            "VKYC",
            "VYOM",
            "UVA",
            "UVCONN",
            "UNIVERSE"
        ],
        "correct_answer": "VKYC"
    },
    {
        "question": "Which of the following is not a part of Apply now features of GBM?",
        "options": [
            "Savings Account",
            "Business Loan",
            "Gold Loan",
            "Credit Card",
            "Current account"
        ],
        "correct_answer": "Current account"
    },
    {
        "question": "Which of the following is not a part of Service under GBM?",
        "options": [
            "Positive Pay",
            "Aadhar Linking",
            "Nomination details",
            "Grievance Redressal",
            "Debit Card Hotlisting"
        ],
        "correct_answer": "Debit Card Hotlisting"
    },
    {
        "question": "What can be located using GBM?",
        "options": [
            "Branches",
            "ATMs",
            "Regional Office",
            "Branches & ATMs",
            "Regional Office & Branches"
        ],
        "correct_answer": "Branches & ATMs"
    },
    {
        "question": "What search needs to be entered, in order to start GBM services?",
        "options": [
            "My Bank",
            "Union Bank",
            "Union Bank of India",
            "Union Bank or Union Bank of India",
            "Union Bank online"
        ],
        "correct_answer": "Union Bank or Union Bank of India"
    },
    {
        "question": "What is the full form of CRV in CRM EDGE?",
        "options": [
            "Customer report view",
            "Customer relationship value",
            "Current report version",
            "Current relationship verification",
            "None of the options"
        ],
        "correct_answer": "Customer relationship value"
    },
    {
        "question": "Which of the following detail is not available in the home page of customer 360 search in CRM EDGE?",
        "options": [
            "Services Availed",
            "Cross Sell/Up Sell",
            "Deposits",
            "Advances",
            "None of the options"
        ],
        "correct_answer": "None of the options"
    },
    {
        "question": "Which of the following statement is false in customer 360 search of CRM EDGE?",
        "options": [
            "Data in CRM EDGE is shown in Transaction + 1 day",
            "Details of Government schemes is available",
            "Details of Non-fund based advances is not available",
            "Whatsapp message in predefined template can be sent to the customer",
            "Lead can be created for an existing customer"
        ],
        "correct_answer": "Details of Non-fund based advances is not available"
    },
    {
        "question": "Under customer 360 search in CRM EDGE, which field is not available for searching the customer",
        "options": [
            "Mobile",
            "Name",
            "E-Mail",
            "customer ID",
            "None of the options"
        ],
        "correct_answer": "None of the options"
    },
{
        "question": "Which project or initiative is not integrated with CRM EDGE?",
        "options": [
            "Union LEAP",
            "Union Connect",
            "Union Phoenix",
            "Union Advith",
            "All the options"
        ],
        "correct_answer": "Union Advith"
    },
    {
        "question": "Which are the key criteria in generating the CRV value in CRM EDGE?",
        "options": [
            "Total number of Services availed",
            "Total Deposit",
            "Stress Category",
            "Loan Account",
            "All the options"
        ],
        "correct_answer": "All the options"
    },
    {
        "question": "How many fields are Mandatory for creating a Lead in CRM EDGE?",
        "options": [
            "5",
            "6",
            "4",
            "7",
            "8"
        ],
        "correct_answer": "5"
    },
    {
        "question": "Lead verification can be done using which option in CRM EDGE",
        "options": [
            "Voter ID",
            "Driving License",
            "CIBIL report",
            "GSTIN",
            "None of the options"
        ],
        "correct_answer": "CIBIL report"
    },
    {
        "question": "What is the primary role of a bank's treasury department?",
        "options": [
            "Marketing banking products",
            "Managing liquidity, funding, and investment portfolios",
            "Processing customer transactions",
            "Conducting internal audits",
            "None of the above"
        ],
        "correct_answer": "Managing liquidity, funding, and investment portfolios"
    },
{
        "question": "What is the primary source of income for a bank's treasury?",
        "options": [
            "Transaction fees",
            "Investment income from government securities and bonds",
            "Interest on savings accounts",
            "Loan processing fees",
            "None of the above"
        ],
        "correct_answer": "Investment income from government securities and bonds"
    },
    {
        "question": "Which of the following instruments is commonly used in treasury management?",
        "options": [
            "Savings accounts",
            "Government bonds",
            "Fixed deposits",
            "Credit cards",
            "None of the above"
        ],
        "correct_answer": "Government bonds"
    },
    {
        "question": "What is 'ALM' in treasury management?",
        "options": [
            "Asset Loss Management",
            "Asset and Liability Management",
            "Advanced Loan Management",
            "Arbitrage and Liquidity Management",
            "None of the above"
        ],
        "correct_answer": "Asset and Liability Management"
    },
    {
        "question": "Which of the following is a type of risk managed by the treasury department?",
        "options": [
            "Operational risk",
            "Interest rate risk",
            "Market risk",
            "Cybersecurity risk",
            "None of the above"
        ],
        "correct_answer": "Interest rate risk"
    },
    {
        "question": "Which of the following is NOT a treasury function?",
        "options": [
            "Loan disbursement",
            "Cash management",
            "Risk management",
            "Investment in securities",
            "None of the above"
        ],
        "correct_answer": "Loan disbursement"
    },
    {
        "question": "What is the main objective of treasury management?",
        "options": [
            "Maximizing customer satisfaction",
            "Managing risks, ensuring liquidity, and optimizing returns",
            "Providing customer loans",
            "Managing bank branches",
            "None of the above"
        ],
        "correct_answer": "Managing risks, ensuring liquidity, and optimizing returns"
    },
    {
        "question": "What does CRR stand for?",
        "options": [
            "Cash Retention Ratio",
            "Cash Reserve Ratio",
            "Credit Risk Rating",
            "Capital Retention Rule",
            "None of the above"
        ],
        "correct_answer": "Cash Reserve Ratio"
    },
    {
        "question": "CRR is maintained by banks with:",
        "options": [
            "Their own branches",
            "The central bank",
            "Foreign banks",
            "Customers",
            "None of the above"
        ],
        "correct_answer": "The central bank"
    },
    {
        "question": "What is the main purpose of the CRR?",
        "options": [
            "To manage the profitability of banks",
            "To ensure that banks have enough liquidity",
            "To reduce the bank's interest rate risk",
            "To facilitate international trade",
            "None of the above"
        ],
        "correct_answer": "To ensure that banks have enough liquidity"
    },
    {
        "question": "Which of the following is directly affected by changes in CRR?",
        "options": [
            "The amount of money banks can lend",
            "The number of bank branches",
            "The value of currency exchange rates",
            "Loan approval time",
            "None of the above"
        ],
        "correct_answer": "The amount of money banks can lend"
    },
    {
        "question": "An increase in CRR results in:",
        "options": [
            "Higher loan approvals",
            "Less money available for banks to lend",
            "Lower interest rates",
            "Greater bank profits",
            "None of the above"
        ],
        "correct_answer": "Less money available for banks to lend"
    },
    {
        "question": "Who decides the Cash Reserve Ratio in a country?",
        "options": [
            "The bank itself",
            "The government",
            "The central bank",
            "International Monetary Fund (IMF)",
            "None of the above"
        ],
        "correct_answer": "The central bank"
    },
    {
        "question": "CRR is calculated as a percentage of:",
        "options": [
            "Bank's equity capital",
            "Net Demand and Time Liabilities (NDTL)",
            "Loan book size",
            "Fixed deposits",
            "None of the above"
        ],
        "correct_answer": "Net Demand and Time Liabilities (NDTL)"
    },
    {
        "question": "If the central bank lowers the CRR, what happens to liquidity in the banking system?",
        "options": [
            "Increases",
            "Decreases",
            "Remains the same",
            "Reduces slightly",
            "None of the above"
        ],
        "correct_answer": "Increases"
    },
    {
        "question": "What happens if a bank fails to maintain the required CRR?",
        "options": [
            "It is penalized by the central bank",
            "It can lend more money",
            "It receives a government subsidy",
            "Nothing happens",
            "None of the above"
        ],
        "correct_answer": "It is penalized by the central bank"
    },
{
        "question": "What is the impact of a high CRR on inflation?",
        "options": [
            "Reduces inflationary pressures",
            "Increases inflation",
            "Has no effect on inflation",
            "Directly increases economic growth",
            "None of the above"
        ],
        "correct_answer": "Reduces inflationary pressures"
    },
    {
        "question": "SLR stands for:",
        "options": [
            "Statutory Loan Requirement",
            "Statutory Liquidity Ratio",
            "Sovereign Liability Ratio",
            "State Liquidity Requirement",
            "None of the above"
        ],
        "correct_answer": "Statutory Liquidity Ratio"
    },
    {
        "question": "SLR is maintained by banks in the form of:",
        "options": [
            "Loans",
            "Cash, gold, and government securities",
            "Corporate bonds",
            "Foreign currency reserves",
            "None of the above"
        ],
        "correct_answer": "Cash, gold, and government securities"
    },
    {
        "question": "What is the objective of maintaining SLR?",
        "options": [
            "To increase the bank's profits",
            "To provide more loans to customers",
            "To ensure the liquidity and solvency of banks",
            "To meet international banking standards",
            "None of the above"
        ],
        "correct_answer": "To ensure the liquidity and solvency of banks"
    },
    {
        "question": "The SLR requirement is imposed by:",
        "options": [
            "Commercial banks",
            "The government",
            "The central bank",
            "Insurance companies",
            "None of the above"
        ],
        "correct_answer": "The central bank"
    },
    {
        "question": "An increase in SLR leads to:",
        "options": [
            "Increased loan availability",
            "Decreased ability to lend",
            "More liquidity for banks",
            "Higher interest rates on loans",
            "None of the above"
        ],
        "correct_answer": "Decreased ability to lend"
    },
    {
        "question": "Which type of bond is backed by the full faith and credit of the issuing government and is considered low-risk?",
        "options": [
            "Municipal bonds",
            "Corporate bonds",
            "Treasury bonds",
            "Junk bonds",
            "None of the above"
        ],
        "correct_answer": "Treasury bonds"
    },
    {
        "question": "What is a bond's 'maturity date'?",
        "options": [
            "The date the bond is issued",
            "The date the bondholder receives their first coupon payment",
            "The date the bond issuer repays the principal amount",
            "The date when interest rates will reset",
            "None of the above"
        ],
        "correct_answer": "The date the bond issuer repays the principal amount"
    },
    {
        "question": "What is the primary risk faced by bondholders?",
        "options": [
            "Interest rate risk",
            "Currency risk",
            "Market capitalization risk",
            "Asset liquidity risk",
            "None of the above"
        ],
        "correct_answer": "Interest rate risk"
    },
    {
        "question": "Which of the following bonds has the highest credit risk?",
        "options": [
            "Investment-grade bonds",
            "Junk bonds (high-yield bonds)",
            "Treasury bonds",
            "Municipal bonds",
            "None of the above"
        ],
        "correct_answer": "Junk bonds (high-yield bonds)"
    },
    {
        "question": "What is the 'yield to maturity' (YTM) of a bond?",
        "options": [
            "The bond's coupon payment divided by the bond's price",
            "The total return an investor can expect if the bond is held to maturity",
            "The amount of interest paid annually by the bond",
            "The market value of the bond at any point in time",
            "None of the above"
        ],
        "correct_answer": "The total return an investor can expect if the bond is held to maturity"
    },
    {
        "question": "What is the Liquidity Adjustment Facility (LAF) primarily aim to manage?",
        "options": [
            "Inflation",
            "Bank liquidity",
            "Foreign exchange rates",
            "Stock market volatility",
            "None of the above"
        ],
        "correct_answer": "Bank liquidity"
    },
    {
        "question": "Which of the following is a tool used by the RBI under the LAF?",
        "options": [
            "Open market operations",
            "Repo rate",
            "Cash Reserve Ratio (CRR)",
            "Statutory Liquidity Ratio (SLR)",
            "None of the above"
        ],
        "correct_answer": "Repo rate"
    },
    {
        "question": "What is forex arbitrage?",
        "options": [
            "Betting on future currency prices",
            "Borrowing foreign currency at lower rates",
            "Simultaneous buying and selling of currencies to profit from price differences",
            "Currency exchange rate forecasting",
            "None of the above"
        ],
        "correct_answer": "Simultaneous buying and selling of currencies to profit from price differences"
    },
    {
        "question": "What is the primary purpose of currency hedging?",
        "options": [
            "To speculate on currency movements",
            "To protect against adverse currency fluctuations",
            "To increase forex reserves",
            "To reduce bond yields",
            "None of the above"
        ],
        "correct_answer": "To protect against adverse currency fluctuations"
    },
    {
        "question": "What is FX Swap in Forex Treasury?",
        "options": [
            "Buying and selling the same currency in different markets",
            "A derivative contract to exchange cash flows in different currencies",
            "An agreement to exchange interest payments on bonds",
            "A contract to buy government bonds in foreign currencies",
            "None of the above"
        ],
        "correct_answer": "A derivative contract to exchange cash flows in different currencies"
    },
    {
        "question": "When can an American option be exercised?",
        "options": [
            "Only on the expiration date",
            "Anytime before the expiration date",
            "After 10 years",
            "On the day it is issued",
            "None of the above"
        ],
        "correct_answer": "Anytime before the expiration date"
    },
    {
        "question": "What is the strike price in an options contract?",
        "options": [
            "The price of the underlying asset at maturity",
            "The price at which the holder can exercise the option",
            "The current market price",
            "The original issue price of the option",
            "None of the above"
        ],
        "correct_answer": "The price at which the holder can exercise the option"
    },
    {
        "question": "Forex reserves are typically held in which form?",
        "options": [
            "Domestic currency",
            "Gold, foreign currency, and IMF Special Drawing Rights",
            "Real estate assets",
            "Government bonds",
            "None of the above"
        ],
        "correct_answer": "Gold, foreign currency, and IMF Special Drawing Rights"
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