/*function searchBar() {
    var input, filter, ul, li, a, i, value;
    input = document.getElementById("search-bar");
    filter = input.value.toUpperCase();
    ul = document.getElementById("city-list");
    li = document.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        value = a.textContent || a.innerText;
        if (value.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}*/
/* Doesn't work yet */
function retrieveCity() {
    const button = document.getElementById("button");
    const searchBar = document.getElementById("search-bar")
    const submittedData = document.getElementById("search")
    const search_term = "";
    button.addEventListener("submit", (event) => {
        search_term = button.querySelector(button).innerText;
    });
    // Call Function to send entered city to app.py
    sendCity(search_term);
}

function sendCity(search_term) {
    const city = search_term;
    const request = new XMLHttpRequest();
    request.open('POST', '/${JSON.stringify(city)}');
    request.send();
}