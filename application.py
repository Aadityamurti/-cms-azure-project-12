from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

articles = []

@app.route("/")
def home():
    return render_template("index.html", articles=articles)

@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    author = request.form.get("author")
    body = request.form.get("body")

    articles.append({
        "title": title,
        "author": author,
        "body": body
    })

    return render_template("index.html", articles=articles)


# Route to generate logs for Azure Log Stream screenshot
@app.route("/testlogs")
def testlogs():
    logging.warning("Invalid login attempt")
    logging.info("admin logged in successfully")
    return "Logs generated successfully"


if __name__ == "__main__":
    app.run()
