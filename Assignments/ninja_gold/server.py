from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = "YOLOSwagLitFam"  #set the session secret key to someting awesome

# Build class Gold to keep track of gold count initialize at zero
class Gold(object):
	def __init__(self):
		self.count = 0

gold = Gold() # set instance of Gold()

#set index.html route
@app.route('/')
def index():
	session['gold_count'] = gold.count
	print "GOLD INDEX IS BOOMING", session['gold_count']
	return render_template('index.html')

#set up '/process_money route and function'
@app.route('/process_money', methods=['POST'])
def process_money():
	name = request.form['action']
	if(name == 'hidden_farm'):
		gold.count += 15
		flash("All that farming earned you 15 gold.", 'gold')
	elif name == "hidden_cave":
		gold.count += 7
		flash('Explore cave, get 7 gold', 'gold')
	elif name == "hidden_house":
		gold.count += 2
		flash('That house earned you 2 gold','gold')
	elif name == "hidden_casino":
		gold.count += 50
		flash("Hit that craps table!", "gold")
	return redirect('/')
#set up '/reset' route and function
@app.route('/reset')
def reset():
	print "No more gold :(" # prints to ensure button is working
	session.pop('gold_count') # clear out the session data for "gold_count"
	gold.count = 0 #reset gold to 0 count
	return redirect('/')
app.run(debug=True) #run the server