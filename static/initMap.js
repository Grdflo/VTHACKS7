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
  