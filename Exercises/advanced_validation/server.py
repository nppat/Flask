from flask import Flask, redirect, render_template, request, session, flash

#import re module will let us perform some regular expression operations
import re

#create a regular expression object that we can use run operations on 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "YOLO"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    # else if email doesn't match regular expression display an "invalid email address" message
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)