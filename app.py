from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def home():
    # Serve the static `index.html` from the `static/` folder
    return app.send_static_file('index.html')


@app.route('/health')
def health():
    # Lightweight health endpoint for checks
    return 'Server is running!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')