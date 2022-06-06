function contact() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("messege").innerHTML =this.responseText;
      }
    };
    xhttp.open("GET", "./contact.html", true);
    xhttp.send();
  }
  
  function aboutus() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("messege").innerHTML =this.responseText;
      }
    };
    xhttp.open("GET", "./aboutus.html", true);
    xhttp.send();
  }
