from flask import Flask, render_template, request
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

connection = MySQLdb.connect("localhost", "majkel", "localhost", "majkel_flask")

app = Flask(__name__, static_url_path="/static")

# set FLASK_APP=__init__.py
# pip install Flask
# python -m flask run


@app.route("/")
def index():
	return render_template("index.html", title="Home")


@app.route("/personal")
def personal():
	return render_template("personal.html", title="Personal")


@app.route("/cv")
def cv():
	return render_template("cv.html", title="CV")


@app.route("/comments")
def comments():
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM comments ORDER BY ID desc")
	return render_template("comments.html", title="Comments", info=cursor)


@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		email = request.form.get("email")
		message = request.form.get("message")
		# file = open("comments.txt", "a+")
		# file.write(email + " " + message + "\n")
		cursor = connection.cursor()
		cursor.execute(
			"INSERT INTO comments (email, comment) VALUES ('"
			+ email
			+ "', '"
			+ message
			+ "');"
		)
		connection.commit()
		cursor.close()
		return render_template("sent.html", title="Thank You")
	else:
		return render_template("contact.html", title="Contact")


@app.route("/computing")
def computing():
	subpage = request.args.get("subpage")

	pages = {
		"1": render_template("interest1.html", title="Games"),
		"2": render_template("interest2.html", title="Music"),
		"3": render_template("interest3.html", title="Programming"),
	}

	return pages.get(subpage, render_template("computing.html", title="Computing"))


@app.route("/interest")
def interest():
	return render_template("interest.html", title="Interests")


if __name__ == "__main__":
	app.run(debug=True)
