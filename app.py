import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# --------------------
# App Setup
# --------------------
app = Flask(__name__, static_folder="static")

# --------------------
# OpenAI Client (ONLY ONCE)
# --------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------
# Quiz Questions
# --------------------
quiz_questions = [
    {
        "question": "Why is warming up important before a workout?",
        "options": [
            "To prepare muscles and reduce the risk of injury",
            "To immediately build muscle",
            "To replace stretching",
            "To cool the body down"
        ],
        "answer": "To prepare muscles and reduce the risk of injury"
    },
    {
        "question": "What should you focus on during strength training?",
        "options": [
            "Lifting the heaviest weight possible",
            "Proper form and controlled movements",
            "Skipping rest between sets",
            "Training only one muscle group"
        ],
        "answer": "Proper form and controlled movements"
    },
    {
        "question": "What is a main benefit of cardio training?",
        "options": [
            "Increased joint stiffness",
            "Improved heart health and endurance",
            "Only muscle size growth",
            "Reduced flexibility"
        ],
        "answer": "Improved heart health and endurance"
    },
    {
        "question": "What is the purpose of cooling down after exercise?",
        "options": [
            "To increase workout intensity",
            "To reduce soreness and help the body recover",
            "To burn maximum calories",
            "To shorten recovery time"
        ],
        "answer": "To reduce soreness and help the body recover"
    },
    {
        "question": "Why is recovery important for progress?",
        "options": [
            "Muscles grow during workouts only",
            "Muscles grow and repair during rest",
            "Recovery replaces training",
            "Nutrition is not important"
        ],
        "answer": "Muscles grow and repair during rest"
    }
]

# --------------------
# Routes
# --------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "Server is running!"


@app.route("/step1")
def step1():
    return render_template("step1.html")


@app.route("/step2")
def step2():
    return render_template("step2.html")


@app.route("/step3")
def step3():
    return render_template("step3.html")


@app.route("/step4")
def step4():
    return render_template("step4.html")


@app.route("/step5")
def step5():
    return render_template("step5.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(quiz_questions):
            if request.form.get(f"question-{i}") == q["answer"]:
                score += 1

        return render_template(
            "quiz.html",
            questions=quiz_questions,
            score=score,
            submitted=True
        )

    return render_template(
        "quiz.html",
        questions=quiz_questions,
        submitted=False
    )

# --------------------
# WorkoutAI
# --------------------
@app.route("/workoutai")
def workoutai():
    return render_template("workoutai.html")


@app.route("/workoutai/chat", methods=["POST"])
def workoutai_chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Ask me something about workouts or fitness."})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are WorkoutAI, a certified fitness coach. "
                    "Only answer questions about workouts, training splits, "
                    "exercise form, recovery, and nutrition."
                )
            },
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })

# --------------------
# Run App (MUST BE LAST)
# --------------------
if __name__ == "__main__":
    app.run(debug=True, port=8000)
