var map;
var poly = new google.maps.Polyline({
    strokeColor:'#000000',
    strokeOpacity:1.0,
    strokeWeight:3,
});

function initialize(){
    map = new google.maps.Map(document.getElementById("google_map"),
    {center: new google.maps.LatLng(0.347596,32.582520),
    zoom:13,mapTypeId: google.maps.MapTypeId.ROADMAP  }); 
    map.addListener('click',addLatLng);
    poly.setMap(map);
}  

function addLatLng(event){
    var path = poly.getPath();
    path.push(event.addLatLng);
    var marker = new google.maps.Marker({
        position : event.latLng,
        title: '#' + path.getLength(),
        map:map
    });
};
google.maps.event.addDomListener(window,"load",initialize);
