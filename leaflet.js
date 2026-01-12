document.addEventListener('DOMContentLoaded', function () {

    var map = L.map('map').setView([51.505, -0.09], 13);
    L.control.locate({
    position: 'topleft', // Where the button will appear
    strings: {
        title: "Show me where I am"
    },
    locateOptions: {
        enableHighAccuracy: true
    }
}).addTo(map);
    var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    navigator.geolocation.getCurrentPosition(success, error);

});