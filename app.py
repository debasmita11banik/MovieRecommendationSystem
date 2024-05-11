from flask import Flask,render_template,request,redirect
import recommendation_system as rs

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/login',methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    if username=="user1" and password=="admin@12345":
        return render_template("user_input.html")
    else:
        return render_template("index.html")

@app.route('/userinput',methods=['GET','POST'])
def userInput():
    genere=request.form.get('genere')
    language=request.form.get('language')
    data=rs.run(genere,language)
    return data.to_html()


if __name__ == '__main__':
    app.run()
