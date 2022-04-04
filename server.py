from flask import Flask, render_template, request
import wikipedia as wiki
import os
app = Flask(__name__)

# Default link the opened when web page requested
@app.route("/", methods=["GET"])
def index():
    os.system("G++ -std=c++1y -o output add_bookmark.cpp") ## compiles the C++ used later for efficiency
    return render_template('index.html')

# Used when the user navigated back to the home page
@app.route("/index", methods=["POST"])
def other_index():
    return render_template('index.html')

# Triggered when the user looks up a term
@app.route("/wiki_lookup", methods=["POST"])
def wikipedia_search():
    page_name = request.form.get("search") # what the user entered in the search bar

    # Wikipedia module can throw errors if there are too many results or none
    try:
        page = wiki.page(wiki.search(page_name)[0], auto_suggest=False)
        page_name = wiki.search(page_name)[0]
    except wiki.DisambiguationError as e: # too many results found. First option chosen
        print("DisambiguationError")
        page = wiki.page(e.options[0])
        page_name = e.options[0]
    except: # if no page is found, the wikipedia page about wikipedia is used
        print("PageError. Using wikipedia page")
        page = wiki.page("wikipedia")
        page_name = "wikipedia"

    # Holds the page data for the next page
    global data
    data = {'page_name': page.title, 'summary': wiki.summary(page_name, auto_suggest=False, sentences=3), 'sources': page.references}

    return render_template('results.html', data=data) # sends the user to different html with the wiki page information

# Used when the user clicks the add a bookmark
@app.route("/add_bookmark", methods=["POST"])
def bookmark():
    # Get information from the URL
    subject = request.args.get("subject")
    link = request.args.get("link")

    # Shortens subject to one word so that the format is the statement
    subject.replace(' ', '')

    # Pass topic and link to C++ to be saved to the bookmark file
    os.system("./output " + subject + " " + link)
    global data
    return render_template('results.html', data=data)

# Used when the user chooses to look at their bookmarks
@app.route("/bookmarks", methods=["POST"])
def load_bookmarks():
    # Reads data from the saved bookmark file
    file = open("bookmarks.txt", "r")
    file_content = file.readlines()

    bookmark_data = {}

    # Loops through every other element of the list becasue bookmarks are held every other element
    for i in range(0, len(file_content), 2):
        # If statement makes sure dictionary write to the right element
        if(i == 0):
            bookmark_data[0] = {'topic': file_content[i], 'link':file_content[i+1]}
        else:
            bookmark_data[i // 2] = {'topic': file_content[i], 'link':file_content[i+1]}

    file.close()
    return render_template('bookmark_view.html', data=bookmark_data)

if __name__ == '__main__':
  app.run(debug=True) # Make it so I don't have to rerun the script in CLI if I change something
