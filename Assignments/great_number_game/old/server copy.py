import random# import random for random number generator
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
key = {app.secret_key}

random = random.randrange(0,101)

# index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")

#set up the /get_number route and function
@app.route('/get_number', methods=['POST'])
def get_number():
	# create random number 0-100
	session['random'] = random
	session['get_number'] = int(request.form['number_input']) # session is set up to grab the number input from the form 
	print session['get_number'] # Test to see if user input is being harvested.  Working as expected.
	print session['random']
	# if (session['get_number'] <  0):  # <---- Error handling, running short on time, will come back to later on this week.
	# 	error = "Must choose a number between 0 and 100."
	# elif(session['get_number'] != int):
	# 	error= "Must input an number."
	if(session['random'] == session['get_number'] ):
		print "Correct!"
		session['option'] = 1
	elif (session['random'] < session['get_number']):
		print "Too high"
		session['option'] = 2
	else: 
		(session['random'] > session['get_number'])
		print "Too low"
		session['option'] = 3

	return redirect('/')

# reset game
@app.route('/reset', methods=['POST'])
def reset():
	session['option']  == 4
	session.pop('random', None)
	session.clear()
	return redirect('/')


app.run(debug=True) # run the server