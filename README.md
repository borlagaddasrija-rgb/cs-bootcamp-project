# 🛡️ CyberShield — Cyber Security Awareness Quiz

A full-stack **Cyber Security Awareness Quiz Web App** built with **Python Flask**.  
Test your knowledge on phishing, passwords, malware, public Wi-Fi, and OTP fraud.

---

## 🖥️ Preview

| Page | Description |
|---|---|
| **Homepage** | Dark hacker theme, 3 cyber stats, Start Quiz button |
| **Quiz Page** | 10 MCQs, one at a time, radio buttons, progress bar |
| **Result Page** | Score ring, category badge, answer review, 5 safety tips |

---

## 📁 Project Structure

```
CyberShield/
├── app.py                  ← Flask backend (routes, quiz logic, scoring)
├── README.md               ← You are here
├── templates/
│   ├── index.html          ← Homepage (hero, stats, topics)
│   ├── quiz.html           ← Quiz page (one question at a time)
│   └── result.html         ← Result page (score, review, learn section)
└── static/
    └── style.css           ← Dark hacker theme (neon green on black)
```

---

## ⚙️ Requirements

- Python 3.8 or higher
- Flask 2.x or higher

Install Flask if you haven't already:

```bash
pip install flask
```

---

## 🚀 How to Run

```bash
# 1. Navigate into the project folder
cd CyberShield

# 2. Run the Flask app
python app.py

# 3. Open your browser and visit
http://127.0.0.1:5000
```

---

## 📝 Quiz Topics (10 Questions)

| # | Topic |
|---|---|
| 1 | Phishing email recognition |
| 2 | Strong password selection |
| 3 | What is malware? |
| 4 | Public Wi-Fi safety |
| 5 | OTP / SIM fraud |
| 6 | HTTPS and secure browsing |
| 7 | Signs of malware infection |
| 8 | Two-Factor Authentication (2FA) |
| 9 | Risks of unofficial downloads |
| 10 | Social engineering attacks |

---

## 🏆 Scoring Categories

| Score | Category |
|---|---|
| 0 – 4 | 🛡️ Beginner |
| 5 – 7 | ⚔️ Intermediate |
| 8 – 10 | 🏆 Cyber Expert |

---

## 🎨 Design Theme

- **Background:** `#0a0a0a` (near-black)
- **Accent:** `#00ff41` (neon green)
- **Font:** `Courier New` (monospace / hacker aesthetic)
- **Effects:** CRT scanlines overlay, neon glow on text and buttons
- **Fully responsive** — works on desktop and mobile

---

## 🔧 How It Works (Technical Flow)

```
User visits /          → index.html shown (homepage)
User clicks Start Quiz → GET /quiz → session reset, Question 1 shown
User selects answer    → POST /quiz → answer saved to Flask session
                                    → next question shown (or redirect to /result)
After Q10              → GET /result → score calculated from session
                                     → breakdown + tips rendered
```

- **Flask `session`** stores the user's answers across requests (server-side cookie).
- **Jinja2 templates** render dynamic content (question text, options, score).
- **`enumerate` filter** is manually registered in `app.jinja_env.filters` since Jinja2 doesn't include it by default.
- **No database, no external API** — everything runs locally.

---

## 📚 Learn Section (on Result Page)

After the quiz, 5 actionable cyber safety tips are shown:

1. 🔑 Use strong, unique passwords (or a password manager)
2. 📱 Enable Two-Factor Authentication (2FA)
3. 📷 Think before you click — hover over links first
4. 📞 Never share OTPs or passwords over phone/email
5. 🔒 Keep your OS, browser, and antivirus updated

---

## 👨‍💻 Built With

| Technology | Purpose |
|---|---|
| Python 3 | Backend language |
| Flask | Web framework |
| Jinja2 | HTML templating engine |
| HTML5 | Page structure |
| CSS3 | Styling (dark hacker theme) |
| Vanilla JavaScript | Option highlight on quiz page |

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

> _"The weakest link in any security system is the human. Awareness is your first shield."_  
> — **CyberShield**
