from flask import Flask, redirect, request, render_template, session, flash
import re #import re module to be able to use regular expression operations

#create a regular expression object that we can use run operations on 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "MyNameIsJonas"  #Weezer shoutout

#set up root route
@app.route('/')
def index():
	return render_template('index.html')

#set up '/registration' route and input validation
@app.route('/registration', methods=['POST'])
def registration():
	#set session to pull data from form
	session['fname'] = str(request.form['f_name'])
	session['lname'] = str(request.form['l_name'])
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm']
	#validate that no inputs are blank
	if len(session['fname']) < 1:
		flash("First Name must be filled out", 'error')
		#validate that fname and lname contain only letters
		if session['fname'].isalpha() != True:
			flash("First name must contain only letters.", 'error')
	if len(session['lname']) < 1:
		flash("Last Name must be filled out", 'error')
		#validate that fname and lname contain only letters
		if session['lname'] != True:
			flash("Last name must contain only letters.", 'error')
	if len(session['email']) < 1:
		flash("Email must be filled out", 'error')
		#check for valid email address
		if not EMAIL_REGEX.match(request.form['email']):
			flash("Invalid Email Address!")
	if len(session['password']) < 1:
		flash("You must supply a password", 'error')
	if len(session['confirm']) < 1:
		flash("Please confirm password", 'error')
	#check password < 8 characters and that password matches
	if len(session['password']) < 8:
		flash("Password must contain minimum of 8 characters.", 'error')
		if session['password'] != session['confirm']:
			flash("Passwords must match.", 'error')
	
	else:
		flash("Success", 'no_errors')

	return redirect('/')

# reset
@app.route('/reset')
def reset():
	print "Clear"
	session.clear()
	return redirect('/')

app.run(debug=True) # run the server
