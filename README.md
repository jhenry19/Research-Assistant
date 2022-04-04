# M3OEP-Large-jhenry3
Julian Henry
- Your name(s)
- Any added installations necessary to run the program
- A summary of the program (2-3 sentences) which includes the language you start the program in
- Any known bugs at time of submission
- Future work (how you could expand the program with more time)
- Citations for any code not written by you or the instructor
- The grade you think you have earned, based on the grading rubric below, with justification



## Installations
wikipedia python library - pip install wikipedia
flask app -  pip install Flask

## Summary
This site can be used to make researching a topic easier. It starts in python, where flask is used to host a web page (written in HTML) that takes a search topic from the user and give all the links to the references that topic has on wikipedia. When the user is shown those references, they can click a button that saves the link and topic into a text file that is managed by a C++ program that sorts the bookmarks alphabetically.

## Known Bugs
• the wikipedia api sometimes suggest different pages given the same input. For example, a search for "queen elizabeth" will somtimes bring you to the page about "Elizabeth the Queen Mother" or "Elizabeth I". This has to do with using the way the library chooses the page for you, but it's a pretty minor issue that doesn't happen on most pages
• if the browser's back button is used on the results page after the user has added a book mark, the page doesn't go back to the search but instead stays on the same page. This is because each time a bookmark is added, the page is refreshed.

## Future work
• More could be done to make the user interface more interactive, such as the add bookmark buttons changing once it is added
• Originally I wanted to show the headers on the research topic's wikipedia page with the references relating to those headers under them. This would allow for the user to be specific when looking for what type of information they want about their research topic. This is possible with webscraping but not built into the wikipedia library as far as I can tell.

## Citations
For parsing hostname fro url:
https://w3collective.com/get-domain-name-url-javascript/

The documentation for using the wikipeida library:
https://wikipedia.readthedocs.io/en/latest/code.html#indices-and-tables

Using flask to get parameters from a sites URL:
https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask

## Grading
I think this project deserves 75 points. I think for design, excecution, and usability this project gets a great. All requirements are satisfied, the program is consistent in style but has a bug or two, and it is clear and useful. 
