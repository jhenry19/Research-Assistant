from flask import Flask, render_template
import wikipedia as wiki
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return render_template('index.html')

@app.route("/wiki", methods=["POST"])
def wikipedia_function():
  print(wiki.summary("Wikipedia"))
  return wiki.summary("Wikipedia")

if __name__ == '__main__':
  app.run(debug=True)
