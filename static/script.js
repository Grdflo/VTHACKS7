function sendData() {
  // The data we should send.
  data = {
    twitter : $("#twit").val(),
    instagram : $("#insta").val(),
    facebook : $("#fb").val()
  };
  // The ajax poster
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    data : JSON.stringify(data),
    // Call code to push to cloud
    url : "/push",

    statusCode : {
      200 : function() {
        // Call backend code
        $.ajax({
          type : "POST",
          dataType : "json",
          contentType : "application/json",
          data : JSON.stringify(data),
          url : "/push"

        });
      }
    }

  });
}

// IGNOREME:
/* TODO: revamp this function for final screen
function getData() {
  $.ajax({
    dataType : "json",
    url : "/index", // Maybe wrong was /list

    // In the case we succeed:
    success : function(data) {
      $('#users').html("")
      // Appendeach
      $.each(data, function(index, value) {
        $('#users').append(value.first + "  " + value.last + "<button id=\"" +
                           value.last + "\">Delete</button>" +
                           "<br>")

        $("#" + value.last).click(function() {
          console.log($(this).attr("id"))
          console.log(data);
          // TODO: Figure out how to remove the data I just appended
          for (var i = 0; i < data.length; i++) {
            if (data[i].last == value.last) {
              console.log("Trying to invoke\t" + i + "\n");
              $.ajax({dataType : "json", url : "/remove", index : i});
              break;
            }
          }
          getData();
        })
      })
    }
  });
}
*/
