
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Dockerized Web Application</h1>
    <p>My first DevOps internship project.</p>
    <p>Application successfully deployed using Docker.</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
