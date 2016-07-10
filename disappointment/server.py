from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('friendsdb')

@app.route('/')
def index():
   friends = mysql.fetch("SELECT * from friends")
   print friends
   return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
	# Insert form values into string without using separate data variable
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{0}','{1}','{2}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
	# If you want to, you can print out the query prior to running the next line to make sure it's formatting correctly. Would display on the server side (in your terminal)
	
    print query #<-- Uncomment this line if you want to check
	
    # Run query, with dictionary values injected into the query.
    mysql.run_mysql_query(query)
    return redirect('/')

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    # UPDATE query
    query = ("""UPDATE friends
              SET first_name = %s
              last_name = %s
              occupation = %s
              WHERE id = %s""" % (request.form['first_name'], request.form['last_name'], request.form['occupation'], friend_id)) # <-- Check out "Formatting Strings" in Python docs. Or don't. .format works just fine too.
    # Run the query
    mysql.run_mysql_query(query)
    return redirect('/')

app.run(debug=True)