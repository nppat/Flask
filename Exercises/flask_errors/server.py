from flask import Flask, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'')

@app.route('/')
def index():
	print mysql.fetch("SELECT * FROM users")
	return redirect('/')

app.run(debug=True)