/*
* Author: Cameron Hunt
* Date of last modification: 30/11/2021
* Purpose of file: To provide the weather map for the weather-map page using the leaflet library and openweathermap data
* Resources and help used:
* // https://github.com/buche/leaflet-openweathermap
* // https://openweathermap.org/api/weather-map-2#library
* // https://leafletjs.com/reference.html#tilelayer
* // Taken from the example at https://github.com/buche/leaflet-openweathermap and modified slightly
* // Used to help pass variables from flask to JS: https://stackoverflow.com/questions/37259740/passing-variables-from-flask-to-javascript
*/

// Function to initialise the map with the user's lat and lon coordinates
function initMap(lat, lon) {
	var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 18, attribution: 'Weather Data supplied by OpenWeatherMap.org' });
	var map = L.map('map', { center: new L.LatLng(lat, lon), zoom: 10, layers: [osm] });
	var baseMaps = { "OSM Standard": osm };
	var rain = L.OWM.rainClassic({opacity: 0.5, appId: '3b1175067ddb84b48f3f5f82fb3e8ecf', showLegend: true});
	var clouds = L.OWM.cloudsClassic({opacity: 0.5, appId: '3b1175067ddb84b48f3f5f82fb3e8ecf', showLegend: true});
	var city = L.OWM.current({minZoom: 1, appId: '3b1175067ddb84b48f3f5f82fb3e8ecf', showLegend: true})
	var overlayMaps = { "Rain": rain, "Clouds": clouds, "City": city };
	var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);
}

