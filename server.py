from flask import Flask, render_template, request
import wikipedia as wiki
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return render_template('index.html')

@app.route("/wiki", methods=["POST"])
def wikipedia_function():
    earch_term = request.form.get("search")
    return wiki.summary(wiki.suggest(search_term), 3)

@app.route("/wiki_lookup", methods=["POST"])
def wikipedia_search():
    page_name = request.form.get("search") # what the user entered in the search bar

    try:
        page = wiki.page(wiki.search(page_name)[0], auto_suggest=False)
        page_name = wiki.search(page_name)[0]
    except wiki.DisambiguationError as e:
        print("DisambiguationError")
        page = wiki.page(e.options[0])
        page_name = e.options[0]
    except:
        print("PageError. Using wikipedia page")
        page = wiki.page("wikipedia")
        page_name = "wikipedia"
    # except:
    #     print("Wikipedia page not found. Try something else.")

    # Hold the page data for the next page
    global data
    data = {'page_name': page.title, 'summary': wiki.summary(page_name, auto_suggest=False, sentences=3), 'sources': page.references}

    return render_template('results.html', data=data)

@app.route("/add_bookmark", methods=["POST"])
def bookmark():
    link = request.args.get("link");
    #pass topic and link to C++
    print(link)
    global data
    return render_template('results.html', data=data)

if __name__ == '__main__':
  app.run(debug=True)
