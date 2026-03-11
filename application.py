from flask import Flask, render_template, request, redirect
import logging
import msal

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

articles = []

# Azure Entra ID configuration
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
AUTHORITY = "https://login.microsoftonline.com/common"
SCOPE = ["User.Read"]

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

# Microsoft login route
@app.route("/login")
def login():
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    auth_url = msal_app.get_authorization_request_url(
        scopes=SCOPE,
        redirect_uri=request.url_root + "getAToken"
    )

    return redirect(auth_url)

# Redirect URI handler
@app.route("/getAToken")
def authorized():
    return "Microsoft login successful!"

# Route to generate logs for Azure Log Stream screenshot
@app.route("/testlogs")
def testlogs():
    logging.warning("Invalid login attempt")
    logging.info("admin logged in successfully")
    return "Logs generated successfully"

if __name__ == "__main__":
    app.run()
