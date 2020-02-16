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

function displayData() {
  $.ajax({
    type : "POST",
    dataType : "json",
    contentType : "application/json",
    url : "/curAttractions",
    statusCode : {
      200 : function(attractions) {
        console.log("Sucessfully asked for data (displayData)");
        console.log(attractions);
        // TODO: shove google api here and use restaurants
        var eat = {attract : attractions.att};
        var all = eat.attract;
        var indivPlace = all.split("\n");
        indivPlace.forEach(element => function(element) {
          var att = element.split(",")
          for (var i = 0; i < att.length / 2; i++) {
            var p = document.createElement("p");
            if (i == 0) {
              var textnode =
                  document.createTextNode(att[i] + "   " + att[i + 1]);
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

        var image1 = document.createElement('img');
        var image2 = document.createElement('img');
        var image3 = document.createElement('img');
        var url1 = '../' +
                   'Amsterdam' +
                   '/image1.jpg';
        var url2 = '../' +
                   'Amsterdam' +
                   '/image2.jpg';
        var url3 = '../' +
                   'Amsterdam' +
                   '/image3.jpg';

        document.getElementById('image1contain').appendChild(image1);
        document.getElementById('image2contain').appendChild(image2);
        document.getElementById('image3contain').appendChild(image3);

        image1.id = 'image1id';
        image2.id = 'image2id';
        image3.id = 'image3id';

        document.getElementById("image1id").src = url1;
        document.getElementById("image2id").src = url2;
        document.getElementById("image3id").src = url3;

        document.getElementById('image1id').style.width = "100%";
        document.getElementById('image1id').style.height = "100%";
        document.getElementById('image1id').style.objectFit = "cover";

        document.getElementById('image2id').style.width = "100%";
        document.getElementById('image2id').style.height = "100%";
        document.getElementById('image2id').style.objectFit = "cover";

        document.getElementById('image3id').style.width = "100%";
        document.getElementById('image3id').style.height = "100%";
        document.getElementById('image3id').style.objectFit = "cover";

        // document.getElementById('image1id').style.borderRadius = '7px 7px 7px
        // 7px';
      }
    }
  });
}
