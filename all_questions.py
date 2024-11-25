import streamlit as st
import json
import glob
import os
from datetime import datetime, timedelta

class QuizApp:
    def __init__(self):
        self.all_questions = []
        self.load_all_questions()

    def load_all_questions(self):
        try:
            # Try multiple possible locations for JSON files
            possible_paths = [
                'output_json/*.json',  # Original path
                'data/*.json',         # Common data directory
                '*.json',              # Root directory
                '../data/*.json',      # One level up data directory
            ]
            
            json_files = []
            for path in possible_paths:
                files = glob.glob(path)
                if files:
                    json_files.extend(files)
                    break  # Use first directory that contains JSON files
            
            if not json_files:
                st.error("No JSON files found. Please ensure question files are in the correct location.")
                return

            for file in json_files:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'questions' in data:
                            self.all_questions.extend(data['questions'])
                        elif isinstance(data, list):
                            self.all_questions.extend(data)
                except Exception as e:
                    st.error(f"Error loading file {file}: {e}")

            # Add question numbers
            for i, q in enumerate(self.all_questions):
                q['question_number'] = i + 1

            st.sidebar.success(f"Successfully loaded {len(self.all_questions)} questions")
            
        except Exception as e:
            st.error(f"Error loading questions: {e}")

    def initialize_session_state(self, num_questions, time_limit, start_from=0):
        if start_from >= len(self.all_questions):
            st.error("Starting position exceeds total questions available")
            return False
        
        available_questions = len(self.all_questions) - start_from
        if num_questions > available_questions:
            st.warning(f"Only {available_questions} questions available from position {start_from + 1}. Adjusting quiz length.")
            num_questions = available_questions

        st.session_state.current_index = 0
        st.session_state.start_from = start_from
        st.session_state.score = 0
        st.session_state.answers = {}
        st.session_state.total_questions = num_questions
        st.session_state.start_time = datetime.now()
        st.session_state.time_limit = time_limit * 60
        st.session_state.question_review = {}
        st.session_state.selected_questions = self.all_questions[start_from:start_from + num_questions]
        st.session_state.expanded_review = None
        return True

    def display_timer(self):
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        remaining = max(0, st.session_state.time_limit - elapsed)
        mins, secs = divmod(int(remaining), 60)

        if remaining <= 300:  # 5 minutes or less
            st.markdown(f"""
                <div class='timer-warning'>
                    ⚠️ Time Remaining: {mins:02d}:{secs:02d}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='timer-normal'>
                    ⏱️ Time Remaining: {mins:02d}:{secs:02d}
                </div>
            """, unsafe_allow_html=True)

        if remaining <= 0:
            st.session_state.show_results = True
            st.rerun()

    def jump_to_question(self):
        current_q_num = st.session_state.start_from + st.session_state.current_index + 1
        col1, col2 = st.columns([3, 1])
        with col1:
            jump_to = st.number_input(
                "Go to question number:",
                min_value=st.session_state.start_from + 1,
                max_value=st.session_state.start_from + st.session_state.total_questions,
                value=current_q_num
            )
        with col2:
            if st.button("Go", type="primary"):
                st.session_state.current_index = jump_to - st.session_state.start_from - 1
                st.rerun()

    def display_question(self, relative_idx):
        if relative_idx >= st.session_state.total_questions:
            st.session_state.show_results = True
            st.rerun()
            return

        question = st.session_state.selected_questions[relative_idx]
        absolute_idx = st.session_state.start_from + relative_idx
        prev_answer = st.session_state.answers.get(relative_idx, None)

        self.jump_to_question()
        
        st.markdown(f"### Question {absolute_idx + 1}")
        st.markdown(f"""
            <div style='font-size: 24px; font-weight: bold; margin-bottom: 20px;'>
                {question['question']}
            </div>
        """, unsafe_allow_html=True)

        selected = st.radio(
            "Choose your answer:",
            question['options'],
            index=None if prev_answer is None else question['options'].index(prev_answer),
            key=f"q_{relative_idx}"
        )

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if st.button("⬅️ Previous", disabled=relative_idx == 0):
                st.session_state.current_index -= 1
                st.rerun()

        with col2:
            if st.button("Submit Answer", type="primary"):
                if selected:
                    st.session_state.answers[relative_idx] = selected
                    if selected == question['correct_answer']:
                        if relative_idx not in st.session_state.question_review:
                            st.session_state.score += 1
                        st.success("Correct! 🎉")
                    else:
                        st.error(f"Wrong! The correct answer is: {question['correct_answer']}")
                    st.session_state.question_review[relative_idx] = {
                        'question': question['question'],
                        'user_answer': selected,
                        'correct_answer': question['correct_answer'],
                        'is_correct': selected == question['correct_answer'],
                        'question_number': absolute_idx + 1,
                        'options': question['options']
                    }
                else:
                    st.warning("Please select an answer")

        with col3:
            if st.button("Next ➡️", disabled=relative_idx >= st.session_state.total_questions - 1):
                st.session_state.current_index += 1
                st.rerun()

    def display_question_review(self, idx, review):
        if st.session_state.expanded_review == idx:
            with st.expander("Question Details", expanded=True):
                st.markdown(f"<div style='font-size: 18px; font-weight: bold;'>{review['question']}</div>", 
                          unsafe_allow_html=True)
                
                for option in review['options']:
                    if option == review['correct_answer']:
                        st.markdown(f"✅ {option} (Correct Answer)")
                    elif option == review['user_answer']:
                        st.markdown(f"❌ {option} (Your Answer)")
                    else:
                        st.markdown(f"◯ {option}")
                
                if st.button("Close", key=f"close_{idx}"):
                    st.session_state.expanded_review = None
                    st.rerun()
        else:
            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                st.markdown(
                    f"<div style='font-size: 24px; margin-right: 10px;'>{review['is_correct'] and '🟢' or '🔴'}</div>",
                    unsafe_allow_html=True
                )
            with col2:
                if st.button(f"Question {review['question_number']}", 
                           key=f"expand_{idx}",
                           use_container_width=True):
                    st.session_state.expanded_review = idx
                    st.rerun()

    def display_score_card(self):
        total = st.session_state.total_questions
        score = st.session_state.score
        percentage = (score / total) * 100

        st.markdown(f"""
            <div class='score-card'>
                <h2 style='text-align: center; color: #1E88E5;'>Quiz Results</h2>
                <div style='text-align: center; font-size: 2em; color: #2196F3; margin: 20px 0;'>
                    Score: {score} / {total}
                </div>
                <div style='text-align: center; font-size: 1.5em; color: #666;'>
                    Percentage: {percentage:.1f}%
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### Question Review")
        st.markdown("Click on any question to see details")
        
        for i in range(0, len(st.session_state.question_review), 2):
            col1, col2 = st.columns(2)
            with col1:
                if i in st.session_state.question_review:
                    self.display_question_review(i, st.session_state.question_review[i])
            with col2:
                if i + 1 in st.session_state.question_review:
                    self.display_question_review(i + 1, st.session_state.question_review[i + 1])

    def run(self):
        st.markdown("""
            <style>
            .main-title {
                text-align: center;
                color: #1E88E5;
                padding: 20px 0;
                margin-bottom: 30px;
            }
            .timer-warning {
                color: #ff4444;
                font-size: 1.2em;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                margin: 10px 0;
            }
            .timer-normal {
                color: #2196F3;
                font-size: 1.2em;
                padding: 10px;
                margin: 10px 0;
            }
            .stRadio > label {
                font-size: 18px;
                padding: 10px 0;
            }
            .question-review-item {
                cursor: pointer;
                padding: 10px;
                border-radius: 5px;
                margin: 5px 0;
                transition: background-color 0.3s;
            }
            .question-review-item:hover {
                background-color: #f5f5f5;
            }
            div[data-testid="stExpander"] {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 10px;
                margin: 10px 0;
            }
            .creator-info {
                font-size: 12px;
                color: #666;
                margin-top: 20px;
                padding-top: 10px;
                border-top: 1px solid #ddd;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1 class='main-title'>Bank Promotion Practice Sets</h1>", unsafe_allow_html=True)

        if 'initialized' not in st.session_state:
            with st.sidebar:
                st.markdown("### Question Bank Settings")
                total_questions = len(self.all_questions)
                st.write(f"Total Available Questions: {total_questions}")

                default_num = min(50, total_questions)
                max_num = min(100, total_questions)

                num_questions = st.number_input(
                    "Number of questions to attempt",
                    min_value=10,
                    max_value=max_num,
                    value=default_num
                )

                start_from = st.number_input(
                    "Start from question number",
                    min_value=1,
                    max_value=max(1, total_questions - num_questions + 1),
                    value=1
                ) - 1

                time_limit = st.number_input(
                    "Time limit (minutes)",
                    min_value=10,
                    max_value=180,
                    value=60
                )

                if st.button("Start Practice Set", type="primary"):
                    if self.initialize_session_state(num_questions, time_limit, start_from):
                        st.session_state.initialized = True
                        st.rerun()
                
                # Add creator info at bottom of sidebar
                st.markdown("<div class='creator-info'>Created by: Pushpender Sharma<br>Contact: +91 9920802159</div>", 
                          unsafe_allow_html=True)
        else:
            with st.sidebar:
                st.markdown("### Quiz Progress")
                self.display_timer()
                progress = min((st.session_state.current_index + 1) / st.session_state.total_questions, 1.0)
                st.progress(progress)
                current_q_num = st.session_state.start_from + st.session_state.current_index + 1
                st.markdown(f"Question: {current_q_num} (#{st.session_state.current_index + 1} of {st.session_state.total_questions})")
                st.markdown(f"Score: {st.session_state.score}/{st.session_state.total_questions}")

                if st.button("End Quiz", type="secondary"):
                    st.session_state.show_results = True
                    st.rerun()

                if hasattr(st.session_state, 'show_results') and st.session_state.show_results:
                    if st.button("Start New Quiz", type="primary"):
                        for key in list(st.session_state.keys()):
                            del st.session_state[key]
                        st.rerun()
                
                # Add creator info at bottom of sidebar
                st.markdown("<div class='creator-info'>Created by: Pushpender Sharma<br>Contact: +91 9920802159</div>", 
                          unsafe_allow_html=True)

            if hasattr(st.session_state, 'show_results') and st.session_state.show_results:
                self.display_score_card()
            else:
                self.display_question(st.session_state.current_index)

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()