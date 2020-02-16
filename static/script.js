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
    // Push data to cloud
    url : "/pushMain/",

    // Calls once data recieved
    statusCode : {200 : function() { console.log("Sucessfully pushed data"); }}
  });
}

// Calls when waiting for data
function requestData() {
  console.log("DEBUG: REQUEST DATA CALLED");
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    // Wait for data to load
    url : "/pushLoading/",

    statusCode : {
      200 : function() {
        // TODO: What do I do if I get a sucessfull call? change webpage to
        // modified results.html
        console.log("DEBUG: REQUEST DATA FINISHED");
        window.location.pathname = '/results'
      }
    }
  });
}

function displayData() {
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curCords",
    statusCode : {
      200 : function(cords) {
        console.log("Sucessfully asked for data");
        console.log(cords);
        // TODO: shove google api here and use cords.cords

        var bothCoords = {lat : cords.X, lng : cords.Y};
        var zoomAmount = 5;

        var map = new google.maps.Map(document.getElementById('map'),
                                      {center : bothCoords, zoom : zoomAmount});

        var marker = new google.maps.Marker({position : bothCoords, map : map});
      }
    }

  });
}

function updateImages() {
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curLoc",
    statusCode : {
      200 : function(locs) {
        console.log("Sucessfully asked for data");
        var image1 = document.createElement('image1');
        var image2 = document.createElement('image2');
        var image3 = document.createElement('image3');
        image1.src = 'link/to/folder/before/folder' + toString(locs.location) + 'image1';
        image2.src = 'link/to/folder/before/folder' + toString(locs.location) + 'image2';
        image3.src = 'link/to/folder/before/folder' + toString(locs.location) + 'image3';
      }
    }
  });
}