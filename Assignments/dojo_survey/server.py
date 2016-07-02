from flask import Flask, render_template,redirect,request,session,flash #add session and flash for validation assighnment
app = Flask(__name__)
app.secret_key = "YOLOSwagLitFam"  # add session secret key

@app.route('/')
def index():
	return render_template("index.html")

#Get input from form ,validate, and return results back to front-end
@app.route('/result', methods=["POST"])
def result():
	# set session to store data from form, also eases typing load on programmer
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	# error handling
	if len(session['name']) < 1: # check that name input is not blank
		flash("Must enter a name.") #if <1, flash message to user
		return redirect('/') # send back to index
	elif len(session['comment']) < 1: # check that comment is not blank
		flash("Must enter a comment.")
		return redirect('/')
	elif len(session['comment']) > 120: #check that comment is not >120 characters
		flash("Comments must be less than 120 characters.")
		return redirect('/')
	else:
		return render_template('result.html') #if conditions are met, send user to reults.html

app.run(debug=True) # run the server