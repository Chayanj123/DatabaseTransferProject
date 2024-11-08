from flask import Flask, render_template
from scripts.logging_management import setup_logging

app = Flask(__name__)
setup_logging()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log')
def log():
    # This would fetch logs from your log file or database
    return render_template('log.html')

if __name__ == "__main__":
    app.run(debug=True)