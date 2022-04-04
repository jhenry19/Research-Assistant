// Loops through the data sent from the server about the users bookmarks
for (bookmark in data) {
  let topic = data[bookmark].topic;
  let link = data[bookmark].link;

  // Puts both the topic and link in a shell so they are on the same line
  const bookmark_shell = document.createElement("div");
  const bookmark_topic = document.createElement("span");
  const bookmark_link = document.createElement("a");

  bookmark_shell.classList.add("wiki_reference");
  bookmark_link.classList.add("reference_link");
  bookmark_link.href = link;
  bookmark_link.target="_blank";

  // Parse domain name from URL
  let domain = (new URL(link));
  domain = domain.hostname.replace('www.','');
  bookmark_link.innerHTML = domain;

  bookmark_topic.classList.add("bookmark_topic");
  bookmark_topic.innerHTML = topic;

  // Places the link and the subject into the shell
  bookmark_shell.appendChild(bookmark_link);
  bookmark_shell.appendChild(bookmark_topic);

  // Adds a bookmark to the list
  document.getElementById("bookmarks").appendChild(bookmark_shell);
  document.getElementById("bookmarks").appendChild(document.createElement("br"));
  document.getElementById("bookmarks").appendChild(document.createElement("br"));
}
