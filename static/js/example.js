function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var result = JSON.parse(this.responseText);
      var array = result["data"];

      var options = '';
      for (var i = 0; i < 5; i++) {
        options += '<option value="' + array[i] + '" />';
      }
     document.getElementById("browsers").innerHTML = options;
     console.log(array);
    }
  };
  var userInput = document.getElementById("autocomplete").value;
  console.log(document.getElementById("autocomplete").value);

  xhttp.open("GET", "http://localhost:5000/autocomplete/" + userInput, true);
  xhttp.send();
}
