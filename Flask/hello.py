from flask import (Flask, render_template, request, session, redirect, url_for, g, flash)
from datetime import timedelta

# from chatbot import chatbot
from ChatBot import RoCo
from flask import Flask, render_template, request

chatbot = RoCo()


app = Flask(__name__)
app.secret_key = 'helloworld@tiemoko'
app.static_folder = 'static'
app.permanent_session_lifetime = timedelta(minutes=1)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def ___repr__(self):
        return f"User: {self.username}"

users = []
users.append(User(id=1, username='admin', password='admin'))

@app.route("/chat")
def chat():
    return render_template("chat.html")


# @app.route("/chat")
# def getBotResponse():
#     # userText = request.args.get('msg')
#     userText = request.args['msg']
#     print(userText)
#     return str(chatbot.get_RoCo_Response(userText))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username and x.password == password]
        if user:
            session['user_id'] = user[0].id
            return redirect(url_for('admin'))
        
        flash("Mot de pass ou username incorrect...!")
        return redirect(url_for('login'))
    else:
        if g.user:
            return redirect(url_for('admin'))
        
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for('login'))

@app.route("/admin")
def admin():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("admin.html")


if __name__ == "__main__":
    app.run()
    