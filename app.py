from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    # Serve the static `index.html` from the `static/` folder
    return render_template('index.html')


@app.route('/health')
def health():
    # Lightweight health endpoint for checks
    return 'Server is running!'

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




if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')