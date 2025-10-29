import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Present Continuous Quiz", page_icon="🧩")
st.title("🧩 Present Continuous Tense Quiz")
st.subheader("Answer all questions!")

# --- QUIZ DATA ---
multiple_choice = [
    {
        "question": "1️⃣ She ______ to music right now.",
        "options": ["listen", "listens", "is listening", "listened"],
        "answer": "is listening"
    },
    {
        "question": "2️⃣ Look! It ______ outside.",
        "options": ["is raining", "rains", "raining", "rain"],
        "answer": "is raining"
    },
    {
        "question": "3️⃣ We ______ for the bus at the moment.",
        "options": ["are wait", "are waiting", "wait", "waited"],
        "answer": "are waiting"
    },
    {
        "question": "4️⃣ They ______ football now.",
        "options": ["is playing", "play", "plays", "are playing"],
        "answer": "are playing"
    },
    {
        "question": "5️⃣ My parents ______ dinner right now.",
        "options": ["are cooking", "cooking", "cooked", "is cooking"],
        "answer": "are cooking"
    },
    {
        "question": "6️⃣ I can’t talk now — I ______.",
        "options": ["is studying", "study", "am studying", "studying"],
        "answer": "am studying"
    },
]

fill_in_blank = [
    {"question": "7️⃣ He ______ to the teacher. (talk)", "answer": "is talking"},
    {"question": "8️⃣ What ______ you ______? (do)", "answer": "are / doing"},
    {"question": "9️⃣ The children ______ TV at the moment. (watch)", "answer": "are watching"},
    {"question": "🔟 I ______ a book right now. (read)", "answer": "am reading"},
]

total_questions = len(multiple_choice) + len(fill_in_blank)

# --- QUIZ STATE ---
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- MULTIPLE CHOICE SECTION ---
st.header("🟢 Multiple Choice Questions")
mc_answers = []
for i, q in enumerate(multiple_choice):
    user_choice = st.radio(q["question"], q["options"], key=f"mc_{i}")
    mc_answers.append(user_choice)

# --- FILL IN THE BLANK SECTION ---
st.header("✍️ Fill in the Blank Questions")
fb_answers = []
for i, q in enumerate(fill_in_blank):
    user_input = st.text_input(q["question"], key=f"fb_{i}")
    fb_answers.append(user_input.strip())

# --- PROGRESS BAR ---
answered = sum(1 for a in mc_answers if a) + sum(1 for a in fb_answers if a)
st.subheader("Progress: ")
st.progress(answered / total_questions)
# --- SUBMIT BUTTON ---
if st.button("Submit Quiz 📝"):
    st.session_state.submitted = True
    st.session_state.mc_answers = mc_answers
    st.session_state.fb_answers = fb_answers

# --- RESULTS PAGE ---
if st.session_state.submitted:
    st.write("---")
    st.subheader("🎯 Final Results")
    score = 0

    # Check MC answers
    for i, q in enumerate(multiple_choice):
        if st.session_state.mc_answers[i] == q["answer"]:
            score += 1

    # Check Fill-in answers
    for i, q in enumerate(fill_in_blank):
        user = st.session_state.fb_answers[i].lower().replace(" ", "")
        correct = q["answer"].lower().replace(" ", "")
        if user == correct:
            score += 1
    st.markdown(f"### ✅ You scored **{score} / {total_questions}**")
    # --- RESTART ---
    if st.button("Restart Quiz 🔁"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
