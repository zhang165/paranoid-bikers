var myLatlng = new google.maps.LatLng(49.267, 236.924);

function initialize() {
  var mapOptions = {
    zoom: 12,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  };

var map = new google.maps.Map(document.getElementById('map'), mapOptions);
var teemo = 'static/images/teemo.png';
var data = 'http://data.vancouver.ca/download/kml/motorcycle_parking.kmz';

// generate markers

for (i = 0; i<4; i++){
var marker = new google.maps.Marker({
	draggable: true,
	position: new google.maps.LatLng(49.237, 236.839),
	map: map,
	icon: teemo,
  });

var infowindow = new google.maps.InfoWindow({
      content:  (i+1) + '<b><p>Teemo</p></b><b>Teemo</b> is a legend among his yordle brothers and sisters in Bandle City. As far as yordles are concerned, there is something just slightly off about him. While Teemo enjoys the companionship of other yordles, he also insists on frequent solo missions in the ongoing defense of Bandle City. Despite his genuinely warm personality, something switches off inside Teemos mind during combat so that the lives he must end while on patrol do not burden him. Even as a young recruit, the drill instructors and other trainees found it a little disconcerting that, while Teemo was normally charming and kind, he turned deadly serious and highly efficient the minute combat exercises began. Teemos superiors quickly steered him toward the Scouts of the Mothership, which is one of Bandle Citys most distinguished Special Forces unit alongside the Megling Commandos.' 
});

google.maps.event.addListener(marker, 'click', function() {
	infowindow.open(map,this);
  });
}

// generate KML layer
var kmlLayer = new google.maps.KmlLayer({
	url: data,
	map: map,
	suppressInfoWindows: false,
  });

google.maps.event.addListener(kmlLayer, 'click', function(kmlEvent) {
	var name = kmlEvent.featureData.description;
        showInContentWindow(name);
  });

  function showInContentWindow(text) {
    var sidediv = document.getElementById('desc-window');
    sidediv.innerHTML = text;
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
