from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

# set FLASK_APP=__init__.py
# pip install Flask
# python -m flask run

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/personal")
def personal():
	return render_template("personal.html")  
	
@app.route("/cv")
def cv():
	return render_template("cv.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		email = request.form.get('email')
		message = request.form.get('message')
		file = open("comments.txt", "a+")
		file.write(email + " " + message + "\n")
		return render_template("sent.html")
	else:
		return render_template("contact.html")

if __name__ == "__main__":
	app.run()