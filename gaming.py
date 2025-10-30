import streamlit as st
import random

# --- QUIZ DATA ---
mc_questions = [
    {
        "question": "1. What were you doing at 8 PM yesterday?",
        "options": ["I was study.", "I was studying.", "I were studying.", "I am studying."],
        "answer": "I was studying."
    },
    {
        "question": "2. They ____ (watch) a movie when I called them.",
        "options": ["was watching", "were watching", "watched", "are watching"],
        "answer": "were watching"
    },
    {
        "question": "3. She wasn't listening because she ____ (think) about something else.",
        "options": ["was thinking", "were thinking", "thinks", "is thinking"],
        "answer": "was thinking"
    },
    {
        "question": "4. While we ____ (walk) home, it started to rain.",
        "options": ["were walking", "was walking", "walked", "walking"],
        "answer": "were walking"
    },
    {
        "question": "5. I ____ (not pay) attention when the teacher asked the question.",
        "options": ["wasn't paying", "weren't paying", "not paid", "didn't pay"],
        "answer": "wasn't paying"
    },
    {
        "question": "6. He ____ (drive) too fast when the police stopped him.",
        "options": ["was driving", "were driving", "drives", "is driving"],
        "answer": "was driving"
    }
]

fill_questions = [
    {
        "question": "7. I ____ (read) a book when the lights went out.",
        "answer": "was reading"
    },
    {
        "question": "8. They ____ (not sleep) when we arrived.",
        "answer": "weren't sleeping"
    },
    {
        "question": "9. What ____ you ____ (do) when I saw you at the park?",
        "answer": "were doing"
    },
    {
        "question": "10. It ____ (rain) heavily when we left the house.",
        "answer": "was raining"
    }
]

total_questions = len(mc_questions) + len(fill_questions)

# --- SESSION SETUP ---
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "key_seed" not in st.session_state:
    st.session_state.key_seed = random.randint(0, 10000)  # unique widget keys per run

st.title("⏳ Past Continuous Tense Quiz")
st.subheader("Answer all questions")

# --- QUIZ FORM ---
with st.form("quiz_form"):
    score = 0

    st.subheader("Multiple Choice Questions")
    mc_answers = []
    for i, q in enumerate(mc_questions):
        key = f"mc_{i}_{st.session_state.key_seed}"
        user_ans = st.radio(q["question"], q["options"], key=key)
        mc_answers.append(user_ans)

    st.subheader("Fill in the Blank Questions")
    fill_answers = []
    for i, q in enumerate(fill_questions):
        key = f"fill_{i}_{st.session_state.key_seed}"
        user_ans = st.text_input(q["question"], key=key)
        fill_answers.append(user_ans.strip().lower())

    submitted = st.form_submit_button("Submit Quiz")

# --- SCORING ---
if submitted:
    score = 0

    for i, q in enumerate(mc_questions):
        if mc_answers[i] == q["answer"]:
            score += 1

    for i, q in enumerate(fill_questions):
        if fill_answers[i] == q["answer"]:
            score += 1

    st.session_state.score = score
    st.session_state.submitted = True

# --- RESULTS DISPLAY ---
if st.session_state.submitted:
    progress = st.session_state.score / total_questions
    st.progress(progress)
    st.success(f"🎯 You got {st.session_state.score}/{total_questions} correct!")

    if st.button("🔄 Restart Quiz"):
        # reset everything including widget states
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

