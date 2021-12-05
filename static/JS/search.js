/*
* Author: Cameron Hunt
* Date of last modification: 27/11/2021
* Purpose of file: To provide the search functionality for the search bars
*/

// Function to ask user for their location and call function to send coords to python
navigator.geolocation.getCurrentPosition(function(position) {
	//returnLocation(position.coords.latitude, position.coords.longitude);
});

/* For Testing Just Now
function sendCity() {
    const search_term = "London";
    const city = search_term;
    const request = new XMLHttpRequest();
    request.open('POST', '/');
    request.send(city);
    alert(city);
}
*/