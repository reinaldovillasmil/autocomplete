from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<word>")
def autocomplete(word=None):
    print(word)
    return word

if __name__ == "__main__":
    app.run()
