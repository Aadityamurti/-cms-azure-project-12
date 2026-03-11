from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()
