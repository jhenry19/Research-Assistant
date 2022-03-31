var submit = $("#submit");
var form_submit = $("#form_submit")

submit.click(function() {
  console.log("submit clicked")
  $.ajax({
      url: "/wiki",
      type: "post",
      success: function(response) {
          const info = document.getElementById("info");
          info.innerHTML = response;
      }
  });
});

form_submit.click(function() {
  $.ajax({
    url: "/wiki_lookup",
    type: "post",
    search_term: $("#search"),
    success: function(response) {
        const info = document.getElementById("info");
        info.innerHTML = response;
    }
  });
});
