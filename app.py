
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    return "hello world test"

if __name__ == '__main__':
	app.run(debug=True)
