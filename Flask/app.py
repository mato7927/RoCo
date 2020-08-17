from flask import (Flask, render_template, request, session, redirect, url_for, g, flash)
from flask import Flask, render_template, request

# from chatbot import chatbot
from ChatBot import RoCo

chatbot = RoCo()


app = Flask(__name__)
app.secret_key = 'helloworld@tiemoko'


@app.route("/app")
def chat():
    return render_template("app.html")

@app.route("/app")
def getBotResponse():
    userText = request.args.get('msg')
    print(userText)
    return str(chatbot.get_RoCo_Response(userText))

#     if request.method == 'POST':
#         userText = request.form['msg']
#         print(userText)
#         return str(chatbot.get_RoCo_Response(userText))


if __name__ == "__main__":
    app.run()