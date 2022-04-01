// Put the wikipedia page title as the page title
document.getElementById("name").innerHTML = page_data.page_name;

// Add wikipedia summary to the page
document.getElementById("summary").innerHTML = page_data.summary;

// List the sources
for (ref in page_data.sources) {
  const reference = document.createElement("a");
  reference.classList.add("wiki_reference");
  reference.href = page_data.sources[ref]

// Parse domain name from URL
  let domain = (new URL(page_data.sources[ref]));
  domain = domain.hostname.replace('www.','');
  reference.innerHTML = domain;

  document.getElementById("references").appendChild(reference);
  document.getElementById("references").appendChild(document.createElement("br"));
  document.getElementById("references").appendChild(document.createElement("br"));

}
