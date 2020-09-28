from flaks import Flask
app = Flask(__name__)

@app.route("/")
def main_page():
	return hello world
