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
    statusCode : {
      200 : function() {
        console.log("Sucessfully pushed data");
        window.location.pathname = '/loading'
      }
    }
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

function initMap() {
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curCords",
    statusCode : {
      200 : function(cords) {
        console.log("Successfully displayed map with coords");
        console.log(cords);
        // TODO: shove google api here and use cords.cords

        var bothCoords = {lat : cords.X, lng : cords.Y};
        var zoomAmount = 8;

        var map = new google.maps.Map(document.getElementById('map'),
                                      {center : bothCoords, zoom : zoomAmount});

        var marker = new google.maps.Marker({position : bothCoords, map : map});
      }
    }

  });
}

function displayData() {
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curAttractions",
    statusCode : {
      200 : function(attractions) {
        console.log("Sucessfully asked for data");
        console.log(attractions);
        // TODO: shove google api here and use restaurants
        var eat = {attract : attractions.att};
        var all = eat.attract;
        var indivPlace = all.split("\n");
        indivPlace.forEach(element => function(element){
          var att = element.split(",")
          for(var i = 0; i  < att.length/2;i++)
          {
            var p = document.createElement("P");  
            if (i == 0)
            {
              var textnode = document.createTextNode(att[i] + "   " + att[i+1]); 
              p.appendChild(textnode);
              document.getElementById('locations').appendChild(p)
            }
            
          }
        })
        
      }
    }

  });
}

function updateImages() {
  displayData();
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curLoc",
    statusCode : {
      200 : function(locs) {
        console.log("Sucessfully loaded images");
        var image1 = document.createElement('image1');
        var image2 = document.createElement('image2');
        var image3 = document.createElement('image3');
        // toString(locs.location)
        image1.src = '/googleAPI/' +
                     'Amsterdam' +
                     '/image1.jpg';
        image2.src = '/googleAPI/' +
                     'Amsterdam' +
                     '/image2.jpg';
        image3.src = '/googleAPI/' +
                     'Amsterdam' +
                     '/image3.jpg';
        image1.id = 'image1id';
        image2.id = 'image2id';
        image3.id = 'image3id';
        document.getElementById('image1contain').appendChild(image1);
        document.getElementById('image2contain').appendChild(image2);
        document.getElementById('image3contain').appendChild(image3);

        document.getElementById('image1id').style.width = "100%";
        document.getElementById('image1id').style.height = "100%";
        // document.getElementById("image1").src = '/googleAPI/' + 'Amsterdam' +
        // '/image1.jpg';
      }
    }
  });
}
