var myLatlng = new google.maps.LatLng(49.267, 236.924);
function initialize() {
  var mapOptions = {
    zoom: 12,
    center: myLatlng,
	mapTypeId: google.maps.MapTypeId.ROADMAP,
  };

  var map = new google.maps.Map(document.getElementById('map'),
      mapOptions);

	var image = 'images/teemo.png';
  var marker = new google.maps.Marker({
	draggable: false,
      position: myLatlng,
      map: map,
	icon: image
  });

  var marker2 = new google.maps.Marker({
      position: new google.maps.LatLng(49.227, 236.949),
      map: map,
	icon: image
  });

  var marker3 = new google.maps.Marker({
      position: new google.maps.LatLng(49.237, 236.839),
      map: map,
	icon: image
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
