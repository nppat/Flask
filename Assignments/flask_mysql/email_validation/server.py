from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
import re # this is imported to be able to use regular expressions

#create a regular expression object that we can use run operations on 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "Ragggggggga_BoMB"  #Skrillex shoutout
# Connect to the DB
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/email', methods=['post'])
def registration():
	#get form data and put into session
	session['email'] = request.form['email']
	#Check that email is entered into input 
	if len(session['email']) < 1:
		flash("Email must be filled out", 'error') # Flash error message if no email input
		return redirect('/')
	#check for valid email address
	elif not EMAIL_REGEX.match(session['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/')
	else:
		# print session['email'] # Test to see that email is being pulled from form
		# This is what we want to insert into the database
		query = "INSERT INTO email_addresses (email_address, created_at, updated_at) VALUES ('{0}', NOW(), NOW())".format(session['email'])
		# print query # Test that the query is working properly
		# Run the query
		mysql.run_mysql_query(query)
		session['status'] = 'success'
		return redirect('/success')
	
# Success route
@app.route('/success')
def success():
	if session['status'] == 'success':
		flash("The email address you entered, {}, is a VALID email address. Thank you.".format(session['email']), 'no_errors') # No errors
		query = "SELECT email_address, created_at FROM email_addresses"
		emails = mysql.fetch(query)
		return render_template('index.html', all_email=emails)

app.run(debug=True) # run the server









