var submit = $("#submit");

submit.click(function() {
  console.log("submit clicked")
  $.ajax({
      url: "/wiki",
      type: "post",
      success: function(response) {
          console.log(response);
          const info = document.getElementById("info");
          const makeInfo = document.createElement("span");
          makeInfo.innerhtml = response;
          info.innerhtml = response;
      }
  });
});
