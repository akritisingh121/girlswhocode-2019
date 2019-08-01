function change_div_color() {
  document.getElementById("change_color").style.opacity = "0.0";
  document.getElementById("change_color").style.transition = "1s";
}

function bring_back() {
  document.getElementById("change_color").style.opacity = "1.0";
  document.getElementById("change_color").style.transition = "1s";
}

var current_image;
var i = 0;
var images = ["puppies/pic1.jpg", "puppies/pic2.jpg", "puppies/pic3.jpg", "puppies/pic4.jpg"];

function show_images() {
	i = i + 1;
	if (i >= images.length) {
		i = 0;
	}
	current_image = images[i];
	document.getElementById("slideshow").src = current_image;
}
