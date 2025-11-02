import streamlit as st
import random

# --- QUIZ DATA ---
mc_questions = [
    {
        "question": "1. What are you doing right now?",
        "options": ["I read.", "I am read.", "I am reading.", "I reading."],
        "answer": "I am reading."
    },
    {
        "question": "2. She ____ (cook) dinner at the moment.",
        "options": ["are cooking", "is cooking", "cooks", "cook"],
        "answer": "is cooking"
    },
    {
        "question": "3. They ____ (not play) football today.",
        "options": ["aren't playing", "isn't playing", "don't playing", "aren't play"],
        "answer": "aren't playing"
    },
    {
        "question": "4. Look! It ____ (rain) outside.",
        "options": ["rains", "is raining", "are raining", "rain"],
        "answer": "is raining"
    },
    {
        "question": "5. We ____ (study) English this week.",
        "options": ["is studying", "are studying", "studies", "study"],
        "answer": "are studying"
    },
    {
        "question": "6. He ____ (not listen) to the teacher right now.",
        "options": ["isn't listening", "aren't listening", "doesn't listening", "isn't listen"],
        "answer": "isn't listening"
    }
]

fill_questions = [
    {
        "question": "7. I ____ (work) on my project right now.",
        "answer": "am working"
    },
    {
        "question": "8. They ____ (not sleep) at the moment.",
        "answer": "aren't sleeping"
    },
    {
        "question": "9. What ____ you ____ (do)?",
        "answer": "are doing"
    },
    {
        "question": "10. She ____ (talk) to her friend on the phone.",
        "answer": "is talking"
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

st.title("💬 Present Continuous Tense Quiz")

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
