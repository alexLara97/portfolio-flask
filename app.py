from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mail", methods = ['GET', 'POST'])
def send_mail():
    if request.method == "POST":
        # Se obtiene los datos del form
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return render_template("send_mail.html")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
