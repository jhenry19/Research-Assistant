var submit = $("#submit");
var form_submit = $("#form_submit")

submit.click(function() {
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
    success: function(response) {
        console.log("changing elements")
        const info = document.getElementById("info");
        info.innerHTML = response;
    }
  });
});
