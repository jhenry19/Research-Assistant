// Put the wikipedia page title as the page title
let subject = page_data.page_name
document.getElementById("name").innerHTML = subject;


// Add wikipedia summary to the page
document.getElementById("summary").innerHTML = page_data.summary;

// List the sources
for (ref in page_data.sources) {
  const reference_shell = document.createElement("span");
  reference_shell.classList.add("wiki_reference");

// Set up link to resource
  const reference = document.createElement("a");
  reference.classList.add("reference_link");
  reference.href = page_data.sources[ref];
  reference.target="_blank";  // opens the link in a new tab
// Parse domain name from URL
  let domain = (new URL(page_data.sources[ref]));
  domain = domain.hostname.replace('www.','');
  reference.innerHTML = domain;

  // Make form for button to go into
  const bookmark_form = document.createElement("form");
  bookmark_form.classList.add("bookmark_form");
  bookmark_form.action= "/add_bookmark?link=" + page_data.sources[ref] + "&subject=" + subject;
  bookmark_form.method = "post";

  // Make button to add to bookmarks
  const bookmark_button = document.createElement("button");
  bookmark_button.classList.add("bookmark_button");
  bookmark_button.type = "submit";
  bookmark_button.innerHTML = "Add to bookmarks";
  bookmark_form.appendChild(bookmark_button);

  // Puts the link and the bookmark button inside the shell
  reference_shell.appendChild(reference);
  reference_shell.appendChild(bookmark_form);

  // Adds shell to the html
  document.getElementById("references").appendChild(reference_shell);
  document.getElementById("references").appendChild(document.createElement("br"));
  document.getElementById("references").appendChild(document.createElement("br"));

}
