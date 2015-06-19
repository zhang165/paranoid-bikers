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

{% for m in markers %}
var point = new google.maps.LatLng({{m.lon}}, {{m.lat}});
            var marker = new google.maps.Marker({
            position: point,
            map: map,
            icon: teemo,
            draggable: false,
        });
{% endfor %}

// var kmlLayer = new google.maps.KmlLayer({
//  url: data,
//  map: map,
//  suppressInfoWindows: false,
//   });

  }

google.maps.event.addDomListener(window, 'load', initialize);