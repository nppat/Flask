from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re # for use of regular expressions
#create a regular expression object that we can use run operations on 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "BrandNew"
mysql = MySQLConnector(app,"semirestfuldb")

# root route
@app.route('/')
def index():
	query = "SELECT id, CONCAT_WS(' ', first_name, last_name) as full_name, email, created_at FROM users ORDER BY id"
	print query
	users = mysql.fetch(query)
	return render_template('index.html', users=users)

# Back route
@app.route('/back', methods=["GET"])
def back():
	return redirect('/')

# new user route
@app.route('/users/new', methods=['GET'])
def new():
	return render_template('add_user.html')

# Create
@app.route('/users/create', methods=['POST'])
def create():
	#get form data and put into session
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	#Check that input is entered
	if len(session['first_name']) < 1:
		flash("First name must be filled out", 'error') # Flash error message if no input
		return redirect('/users/new')
	elif len(session['last_name']) < 1:
		flash("Last name must be filled out", 'error') # Flash error message if no input
		return redirect('/users/new')
	elif len(session['email']) < 1:
		flash("Email must be filled out", 'error') # Flash error message if no email input
		return redirect('/users/new')
	#check for valid email address
	elif not EMAIL_REGEX.match(session['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/users/new')
	else:
		# This is what we want to insert into the database
		query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ('{0}','{1}','{2}', NOW(), NOW())".format(session['first_name'],session['last_name'],session['email'])
		print query # Test that the query is working properly
		# Run the query
		mysql.run_mysql_query(query)
		# session['status'] = 'success'
		return redirect('/')

# Show route
@app.route('/users/<id>')
def show(id): #show by id
	query = "SELECT id, CONCAT_WS(' ', first_name, last_name) as full_name, email, created_at FROM users WHERE id = '{0}'".format(id)
	user = mysql.fetch(query)
	return render_template('show.html', user=user[0])

# Retrieve
@app.route('/users/<id>/edit', methods=['GET'])
def edit(id):
	# pull the data from the db
	query = "SELECT * FROM users WHERE id = '{0}'".format(id)
	# run the query
	user = mysql.fetch(query)
	#redirect to edit page, via the friend ID
	return render_template("edit.html", user=user[0])

# Update
@app.route('/user/<id>/update', methods=['POST'])
def update(id): #update by id
# This method is a lot like create, only checking each input for data and updating accordingly
	#get form data and put into session
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	# Check and validate input
	if len(session['first_name']) < 1:
		flash("First name must be filled out", 'error') # Flash error message if no input
		return redirect('/users/new')
	elif len(session['last_name']) < 1:
		flash("Last name must be filled out", 'error') # Flash error message if no input
		return redirect('/users/new')
	elif len(session['email']) < 1:
		flash("Email must be filled out", 'error') # Flash error message if no email input
		return redirect('/users/new')
	#check for valid email address
	elif not EMAIL_REGEX.match(session['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/users/new')
	else:
		if len(session['first_name']) > 1:
			query = "UPDATE users SET first_name = '{0}' WHERE id = '{1}'".format(session['first_name'], id)
			mysql.run_mysql_query(query)
		if len(session['last_name']) > 1:
			query = "UPDATE users SET last_name = '{0}' WHERE id = '{1}'".format(session['last_name'], id)
			mysql.run_mysql_query(query)
		if len(session['email']) > 1:
			query = "UPDATE users SET email = '{0}' WHERE id = '{1}'".format(session['email'], id)
			mysql.run_mysql_query(query)
	flash("You have successfully updated this contact.", 'success')
	return redirect('/users/{}'.format(id))
# Destroy
@app.route('/users/<id>/delete', methods=['POST'])
def delete(id):
		query = "DELETE FROM users WHERE id = '{0}'".format(id) 
		mysql.run_mysql_query(query)
		return redirect('/')

app.run(debug=True) # run the server yo