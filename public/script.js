function sendData() {
  data = {first : $("#first").val(), last : $("#last").val()} $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    data : JSON.stringify(data),
    url : "/user"
  })
}

function getData() {
  $.ajax({
    dataType : "json",
    url : "/list",
    success : function(data) {
      $('#users').html("")

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
