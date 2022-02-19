from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key="437026851"

@app.route('/')
def home():
	# if request.method == 'POST':
	# 	session['form']=request.form
	# 	return redirect("/result.html")
	# else:
	# 	print("rendering page index.html")
		return render_template("index.html")

@app.route('/result')
def results():
	# print(session['form'])
	return render_template("result.html")

@app.route('/submit', methods=['POST'])
def submit():
	print(request.form)
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	return redirect('/result')


if __name__ == '__main__':
	app.run(debug=True)