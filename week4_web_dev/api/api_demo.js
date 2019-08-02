var div = document.getElementById("movies");

//creates a new html request
var request = new XMLHttpRequest();
request.open("GET", "https://ghibliapi.herokuapp.com/films");
request.onload = function () {
  //deals with the response here
  //data is a list of dictionary
  var data = JSON.parse(request.response);
  var i; //declare the variable i
  for (i=0; i<data.length; i++) {
    var movie = data[i];

    //create the html elements
    var title = document.createElement("h2");
    var description = document.createElement("p");

    //fill the html elements with text
    title.textContent = movie.title;
    description.textContent = movie.description;

    //add html elements to my webpage
    div.appendChild(title);
    div.appendChild(description);
  }
}

request.send();
