import random# import random for random number generator
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

# index route will handle rendering our form
@app.route('/')
def index():
	try: # if the session exists, use the random number it has already generated
		session['random']
	except: # otherwise, create a random number and store it in session
		session['random'] = random.randrange(0,101)
	return render_template("index.html")

# get the number guessed by the user, and check it against the stored random number in session
@app.route('/get_number', methods=['POST'])
def get_number():
	guess = int(request.form['number_input']) #grab num inputted and covert to int to check against ran number
	print session['random']
	if guess > session['random']:
		flash("Too High", 'error') #Flash messages to user 
	elif guess < session['random']:
		flash("Too Low", 'error')
	elif guess == session['random']:
		flash("Correct!", 'success')
	return redirect('/')

@app.route('/reset') # reset the game
def reset():
	session.pop('random') #reset the random number by popping it out of the session dictionary
	return redirect('/') #redirect to index.html

app.run(debug=True) # run the app