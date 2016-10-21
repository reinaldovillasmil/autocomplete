from flask import Flask, render_template, jsonify
from SuffixArray import find

app = Flask(__name__)

# RESTFul APIs
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/careers")
def careers():
    return "hello, this is the careers page"

@app.route("/autocomplete/<word>")
def autocomplete(word=None):
    result = dict()
    data = find(word)
    result["data"] = data
    return jsonify(**result)

if __name__ == "__main__":
    app.run()
