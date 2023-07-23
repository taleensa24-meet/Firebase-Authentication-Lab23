from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={"apiKey": "AIzaSyB5KrNO6drGs2OryII5jnSPtpSmqlQJsyU",
  "authDomain": "cs-lab-dd1b4.firebaseapp.com",
  "projectId": "cs-lab-dd1b4",
  "storageBucket": "cs-lab-dd1b4.appspot.com",
  "messagingSenderId": "883753514061",
  "appId": "1:883753514061:web:08729c7b58823c05a9d804", "databaseURL": ""  }


firebase=pyrebase.initialize_app(config)
auth=firebase.auth()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
           login_session['user'] = auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except Exception as e:
           error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except Exception as e:
           error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)