from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
import re # this is imported to be able to use regular expressions
from flask_bcrypt import Bcrypt # imports the Bcrypt module

#create a regular expression object that we can use run operations on 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "HolySmokeS"
# Connect to the DB
mysql = MySQLConnector(app,'login_registerdb')

#set up index route
@app.route('/')
def index():
	return render_template('index.html')

#Login Route and function
@app.route('/login',methods=['POST'])
def login():
	#set session to pull data from form
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	#Check that email is entered into input 
	if len(session['email']) < 1:
		flash("Email must be filled out", 'error') # Flash error message if no email input
		return redirect('/')
	#check for valid email address
	elif not EMAIL_REGEX.match(session['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/')
	#check password is not empty, < 8 characters and that password matches
	if len(session['password']) < 1:
		flash("Must enter a password", 'error')
		return redirect('/')
	#  look pw_hash in DB that is connected to user email
	query = "SELECT pw_hash FROM users WHERE email = '{0}' LIMIT 1".format(session['email'])
	#run query, put into variable exists
	exists = mysql.fetch(query)
	if exists: # if email is in DB
		# print exists # test to see if we get the email back from the DB
		# check to see that the password matches
		if bcrypt.check_password_hash(exists[0]['pw_hash'], session['password']):
			# print "in check password" # Test to see if we make it this far
			session['status'] = 'success'
			flash("You have successfully logged in!", 'success')
			return render_template("success.html")
		else:
			flash("Login error.  Email and/or password is incorrect.  Please try again.", 'error')
			return redirect('/')
	else:
		flash("Login error.  Email and/or password is incorrect.  Please try again.", 'error')
		return redirect('/')

#CREATE route and input validation
@app.route('/register',methods=['POST'])
def create():
	#set session to pull data from form
	session['fname'] = str(request.form['first_name'])
	session['lname'] = str(request.form['last_name'])
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm_password']
	#validate that no inputs are blank
	if len(session['fname']) < 2:
		flash("First Name must be filled out", 'error')
		return redirect('/')
	#validate that fname and lname contain only letters
		if session['fname'].isalpha() != True:
			flash("First name must contain only letters.", 'error')
			return redirect('/')
	if len(session['lname']) < 2:
		flash("Last Name must be filled out", 'error')
		return redirect('/')
	#validate that fname and lname contain only letters
		if session['lname'].isalpha != True:
			flash("Last name must contain only letters.", 'error')
			return redirect('/')
	#Check that email is entered into input 
	if len(session['email']) < 1:
		flash("Email must be filled out", 'error') # Flash error message if no email input
		return redirect('/')
	#check for valid email address
	elif not EMAIL_REGEX.match(session['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/')
	if len(session['password']) < 1:
		flash("You must supply a password", 'error')
		return redirect('/')
	elif len(session['confirm']) < 1:
		flash("Please confirm password", 'error')
		return redirect('/')
	#check password < 8 characters and that password matches
	elif len(session['password']) < 8:
		flash("Password must contain minimum of 8 characters.", 'error')
		return redirect('/')
	elif session['password'] != session['confirm']:
		flash("Passwords must match.", 'error')
		return redirect('/')
	else:
		#encrypt the password befdore sending to DB
		pw_hash = bcrypt.generate_password_hash(session['password'])
		# This is what we want to insert into the database
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES ('{0}','{1}','{2}','{3}', NOW(), NOW())".format(session['fname'], session['lname'], session['email'], pw_hash)
		# print query # Test that the query is working properly
		# Run the query
		mysql.run_mysql_query(query)
		session['status'] = 'success'
		flash("You have successfully registered", 'success')
		return render_template('success.html')

# Return to index, clear session data
@app.route('/back', methods=['POST'])
def go_back():
	session.clear()
	return redirect('/')

app.run(debug=True) # run the server







