# =============================================================
#  CyberShield - Cyber Awareness Quiz
#  Backend: Flask (Python)
#  Run:  python app.py  then open http://127.0.0.1:5000
# =============================================================

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Secret key is required by Flask to sign/encrypt session cookies
app.secret_key = "cybershield_secret_2024"

# ------------------------------------------------------------------
# CUSTOM JINJA2 FILTER
# Jinja2 does not expose Python's built-in enumerate() by default.
# We register it as a filter so templates can write:
#   {% for i, option in question.options | enumerate %}
# ------------------------------------------------------------------
app.jinja_env.filters["enumerate"] = enumerate

# ------------------------------------------------------------------
# QUIZ DATA
# Each question has:
#   "question" : the question text
#   "options"  : list of 4 answer choices (A-D)
#   "answer"   : index of the correct option (0-based)
#   "explain"  : brief explanation shown on the result page
# ------------------------------------------------------------------
QUESTIONS = [
    {
        "question": "1. You receive an email saying 'Your bank account is locked. Click here to verify.' What should you do?",
        "options": [
            "Click the link and enter your details",
            "Ignore it and delete the email",
            "Forward it to all your contacts",
            "Reply with your account number"
        ],
        "answer": 1,
        "explain": "This is a classic phishing email. Legitimate banks NEVER ask for credentials via email. Always go directly to your bank's official website."
    },
    {
        "question": "2. Which of the following is the STRONGEST password?",
        "options": [
            "password123",
            "John1990",
            "P@ssw0rd",
            "Tr0ub4dor&3#xQ!"
        ],
        "answer": 3,
        "explain": "A strong password uses a mix of uppercase, lowercase, numbers, and symbols and is at least 12 characters long. 'Tr0ub4dor&3#xQ!' satisfies all these criteria."
    },
    {
        "question": "3. What is malware?",
        "options": [
            "A type of antivirus software",
            "Malicious software designed to harm or exploit systems",
            "A hardware firewall device",
            "A secure file compression tool"
        ],
        "answer": 1,
        "explain": "Malware (malicious software) includes viruses, ransomware, spyware, and trojans — all designed to damage systems or steal data."
    },
    {
        "question": "4. You are at a coffee shop and connect to free public Wi-Fi. What is the SAFEST action?",
        "options": [
            "Log into your internet banking immediately",
            "Share your work files over the network",
            "Use a VPN before doing anything sensitive",
            "Disable your firewall for better speed"
        ],
        "answer": 2,
        "explain": "Public Wi-Fi is unsecured. A VPN (Virtual Private Network) encrypts your traffic, protecting it from attackers on the same network."
    },
    {
        "question": "5. You get a call: 'Hi, I'm from Google. An OTP will come to your phone — please share it with me.' What do you do?",
        "options": [
            "Share the OTP immediately",
            "Ask the caller to wait and share it slowly",
            "Never share OTPs — hang up immediately",
            "Share only the last 4 digits"
        ],
        "answer": 2,
        "explain": "OTP (One-Time Password) fraud is rampant. No genuine company will EVER ask you to read out an OTP. Sharing it gives attackers full account access."
    },
    {
        "question": "6. What does HTTPS in a website URL indicate?",
        "options": [
            "The site is owned by the government",
            "The connection between your browser and the site is encrypted",
            "The site is completely safe from all threats",
            "The site loads faster than HTTP"
        ],
        "answer": 1,
        "explain": "HTTPS means the data exchanged is encrypted using TLS/SSL. However, HTTPS alone doesn't guarantee the site isn't malicious — always verify the domain."
    },
    {
        "question": "7. Which of these is a sign that your computer may be infected with malware?",
        "options": [
            "It runs faster than usual",
            "Your desktop background changed automatically",
            "You received a software update notification",
            "A new font appeared in your word processor"
        ],
        "answer": 1,
        "explain": "Unexplained changes like a new desktop background, new toolbars, slow performance, or pop-ups can indicate malware infection."
    },
    {
        "question": "8. What is two-factor authentication (2FA)?",
        "options": [
            "Using two different passwords for one account",
            "Logging in from two different devices simultaneously",
            "A security process requiring two forms of verification",
            "Sharing your password with a trusted person"
        ],
        "answer": 2,
        "explain": "2FA adds an extra layer of security. Even if your password is stolen, the attacker still can't log in without the second factor (e.g., OTP, fingerprint)."
    },
    {
        "question": "9. You download a free movie from an unofficial website. What risk do you face?",
        "options": [
            "No risk — it's just a movie file",
            "The file may contain hidden malware",
            "Your internet speed may increase",
            "Your screen resolution may change"
        ],
        "answer": 1,
        "explain": "Files from unofficial sources often bundle malware. Always download content from official, trusted sources only."
    },
    {
        "question": "10. What is 'social engineering' in the context of cyber security?",
        "options": [
            "Building social media applications",
            "Manipulating people into revealing confidential information",
            "Engineering software for social networks",
            "A type of firewall configuration"
        ],
        "answer": 1,
        "explain": "Social engineering exploits human psychology rather than technical vulnerabilities. Phishing, vishing, and pretexting are common social engineering attacks."
    }
]

# ------------------------------------------------------------------
# SCORE CATEGORY HELPER
# Returns a label and a CSS class based on the user's score
# ------------------------------------------------------------------
def get_category(score):
    if score <= 4:
        return "Beginner 🛡️", "beginner"
    elif score <= 7:
        return "Intermediate ⚔️", "intermediate"
    else:
        return "Cyber Expert 🏆", "expert"


# ------------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------------

@app.route("/")
def index():
    """Homepage — shows the landing page with stats and Start Quiz button."""
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """
    GET  — initialize the quiz in the session and show question 0.
    POST — save the submitted answer, advance to the next question,
           or redirect to results when all 10 are answered.
    """
    if request.method == "POST":
        # Read which question was just answered
        current = int(request.form.get("current_question", 0))
        selected = request.form.get("answer")  # Could be None if user skipped

        # Store answers in session (list of integers, -1 means skipped)
        answers = session.get("answers", [])
        if selected is not None:
            answers.append(int(selected))
        else:
            answers.append(-1)   # Mark as unanswered
        session["answers"] = answers

        next_q = current + 1

        # All 10 questions answered — go to results
        if next_q >= len(QUESTIONS):
            return redirect(url_for("result"))

        return render_template("quiz.html",
                               question=QUESTIONS[next_q],
                               q_index=next_q,
                               total=len(QUESTIONS))

    # GET request — fresh start
    session["answers"] = []
    return render_template("quiz.html",
                           question=QUESTIONS[0],
                           q_index=0,
                           total=len(QUESTIONS))


@app.route("/result")
def result():
    """
    Calculates score from session answers, builds a per-question
    breakdown, and renders the result page.
    """
    answers = session.get("answers", [])

    # Safety redirect if someone visits /result without taking the quiz
    if not answers:
        return redirect(url_for("index"))

    score = 0
    breakdown = []

    for i, question in enumerate(QUESTIONS):
        user_ans = answers[i] if i < len(answers) else -1
        is_correct = (user_ans == question["answer"])
        if is_correct:
            score += 1

        breakdown.append({
            "question": question["question"],
            "options":  question["options"],
            "correct":  question["answer"],
            "selected": user_ans,
            "explain":  question["explain"],
            "is_correct": is_correct
        })

    category_label, category_class = get_category(score)

    return render_template("result.html",
                           score=score,
                           total=len(QUESTIONS),
                           category_label=category_label,
                           category_class=category_class,
                           breakdown=breakdown)


# ------------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True enables auto-reload on code changes (dev only)
    app.run(debug=True)
