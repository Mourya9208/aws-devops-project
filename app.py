from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS DevOps Project</title>
        </head>
        <body>
            <h1>AWS DevOps Deployment 🚀</h1>
            <p>Application is running successfully with automated CI/CD.</p>
            <p>Built with Flask, Docker, GitHub Actions and AWS EKS.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)