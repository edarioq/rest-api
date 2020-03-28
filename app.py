from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    url = 'WORK pls !'
    return render_template("index.html", url=url)


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("DEBUG", False)
    app.run(host='0.0.0.0', port=5000, debug=ENVIRONMENT_DEBUG)