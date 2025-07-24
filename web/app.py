
from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"

with open("common_passwords.txt") as f:
    common_passwords = set(p.strip() for p in f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pwd = request.form.get("password", "")
        if is_valid(pwd):
            session["password"] = pwd
            return redirect(url_for("welcome"))
        flash("Password invalid or too common.", "error")
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    pwd = session.get("password")
    if not pwd:
        return redirect(url_for("index"))
    return render_template("welcome.html", password=pwd)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def is_valid(p):
    return (
        len(p) >= 12 and
        p not in common_passwords and
        re.search(r"[A-Z]", p) and
        re.search(r"[a-z]", p) and
        re.search(r"[0-9]", p) and
        re.search(r"[!@#$%^&*(),.?:{}|<>]", p)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
