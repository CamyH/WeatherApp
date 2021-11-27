/*
* Author: Cameron Hunt
* Date of last modification: 27/11/2021
* Purpose of file: To provide the weather map for the weather-map page using the leaflet library and openweathermap data
*/

// JavaScript for embedding the interactive map
// Taken from the example at https://github.com/buche/leaflet-openweathermap

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 18, attribution: 'Weather Data supplied by OpenWeatherMap.org' });
// Placeholder Lat and Lon for now
var map = L.map('map', { center: new L.LatLng(55.9533, 3.1883), zoom: 10, layers: [osm] });
var baseMaps = { "OSM Standard": osm };
var rain = L.OWM.rainClassic({opacity: 0.5,appId: '3b1175067ddb84b48f3f5f82fb3e8ecf', showLegend: true});
var clouds = L.OWM.cloudsClassic({opacity: 0.5, appId: '3b1175067ddb84b48f3f5f82fb3e8ecf', showLegend: true});
var city = L.OWM.current({minZoom: 1, appId: '3b1175067ddb84b48f3f5f82fb3e8ecf'})
var overlayMaps = { "Rain": rain, "Clouds": clouds, "City": city };
var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);

// https://github.com/buche/leaflet-openweathermap
// https://openweathermap.org/api/weather-map-2#library
// https://leafletjs.com/reference.html#tilelayer