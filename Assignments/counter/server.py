from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

# Build class Count to and initialize at zero
class Counter(object):
	def __init__(self):
		self.count = 0

count = Counter()


# set index route
@app.route('/')
def index():
	count.count += 1 # each time the page is loaded, add +1 to the counter
	session['counter'] = count.count
	return render_template("index.html")


# ninjas and hacker
# add a button that adds +2 to the counter and resets the page
@app.route('/ninja', methods=['POST'])
def plus_two_or_reset():
	action = request.form['action']
	if(action == 'addTwo'): # +2 to the counter
		count.count += 1

	if(action == 'reset'): # reset counter
		count.count = 0

	return redirect('/') #redirect back to index
app.run(debug=True) # run the server