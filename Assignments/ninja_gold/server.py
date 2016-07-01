from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = "YOLOSwagLitFam"  #set the session secret key to someting awesome

#set index.html route
@app.route('/')
def index():
	gold = 0
	session['gold_count'] = gold
	print session['gold_count']
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	name = request.form['value'] #grab num inputted and covert to int to check against ran number
	if(name == 'hidden_farm'):
		print "FArm"
	return redirect('/')

app.run(debug=True) #run the server