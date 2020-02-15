function initMap()
{
	var uluru = {lat: -25.344, lng: 131.036};
	var zoomAmount = 5;
		
	var map = new google.maps.Map(document.getElementById('map'), {
	center: uluru,
	zoom: zoomAmount
	});

	var marker = new google.maps.Marker({position: uluru , map: map});

}
