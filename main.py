from flask import Flask, render_template

app = Flask(__name__)

base = ['Anton\n', 'Kirill\n']

@app.route("/")
def hello():
	global base
	return render_template("index.html", base=base)

if __name__ == "__main__":
    app.run()