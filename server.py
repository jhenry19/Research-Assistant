from flask import Flask, render_template, request
import wikipedia as wiki
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return render_template('index.html')

@app.route("/wiki", methods=["POST"])
def wikipedia_function():
  return wiki.summary("Wikipedia")

@app.route("/wiki_lookup", methods=["POST"])
def wikipedia_search():
    # search_term = request.form.get("search")
    print(search_term)
    return wiki.summary(search_term)

if __name__ == '__main__':
  app.run(debug=True)
