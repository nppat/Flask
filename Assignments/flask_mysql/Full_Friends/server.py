from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "RedBullx20"
# Connect to the DB
mysql = MySQLConnector(app,'friendsdb')

# Set up index route
@app.route('/')
def index():
	query = """SELECT *
			FROM friends"""
	friends = mysql.fetch(query)
	return render_template('index.html', all_friends=friends)

#CREATE.  Is a POST method
@app.route('/friends', methods=['post'])
def create():
	#get form data and put into session
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['occupation'] = request.form['occupation']
	#Check that input is entered
	if len(session['first_name']) < 1:
		flash("First name must be filled out", 'error') # Flash error message if no input
		return redirect('/')
	elif len(session['last_name']) < 1:
		flash("Last name must be filled out", 'error') # Flash error message if no input
		return redirect('/')
	elif len(session['occupation']) < 1:
		flash("Occupation must be filled out", 'error') # Flash error message if no input
		return redirect('/')
	else:
		# This is what we want to insert into the database
		query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{0}','{1}','{2}', NOW(), NOW())".format(request.form['first_name'],request.form['last_name'],request.form['occupation'])
		# print query # Test that the query is working properly
		# Run the query
		mysql.run_mysql_query(query)
		# session['status'] = 'success'
		return redirect('/')

# EDIT.  This is a GET method
@app.route('/friends/<id>/edit/', methods=['GET'])
def edit(id):
	print "In edit function" # Test 
	# pull the data from the db
	query = "SELECT * FROM friends WHERE id = '{0}'".format(id)
	print "after query" # Test
	# run the query
	friend = mysql.fetch(query)
	#redirect to edit page, via the friend ID
	return render_template("edit.html", friend=friend[0])

# UPDATE.  POST method
@app.route('/friends/<id>', methods=['POST'])
def update(id):
	#get form data and put into session
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['occupation'] = request.form['occupation']
	# UPDATE query
	query = """UPDATE friends
	        SET first_name = '{0}',
	        last_name = '{1}',
	        occupation = '{2}',
	        WHERE id = '{3}'""".format(session['first_name'], session['last_name'], session['occupation'], id)
	        # Check out "Formatting Strings" in Python docs. Or don't. .format works just fine too.
	# Run the query
	mysql.run_mysql_query(query)
	return redirect('/')

# DESTROY.  POST method
@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
		query = "DELETE FROM friends WHERE id = '{0}'".format(id) 
		mysql.run_mysql_query(query)
		return redirect('/')
app.run(debug=True) # run the server


# I would like to come back and add in the updated_at feature and input validation to the UPDATE feature, but that will have to wait, as I have a lot of catching up to do for class at the moment.
