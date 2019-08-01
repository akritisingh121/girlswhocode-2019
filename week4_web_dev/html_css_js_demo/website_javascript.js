function change_div_color() {
  document.getElementById("change_color").style.opacity = "0.0";
  document.getElementById("change_color").style.transition = "1s";
}

function bring_back() {
  document.getElementById("change_color").style.opacity = "1.0";
  document.getElementById("change_color").style.transition = "1s";
}
