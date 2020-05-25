function formValidate() {
    //name 
    var fn = document.getElementByName('fname').value;
        //empty box
    if (fn == "") {
        alert('First name needed please');
        document.getElementByName('fname').style.borderColor = "red";
        return false;
    } else {
        document.getElementByName('fname').style.borderColor = "green";
    }

        //name contains a number
    if (/[0-9]+$/.test(document.getElementByName("fname").value)) {
        alert("Please enter a valid first name");
        document.getElementByName('fname').style.borderColor = "red";
        return false;
    } else {
        document.getElementByName('fname').style.borderColor = "green";
    }     
}

//jumping to result page after every question is answered and submit is clicked
function resultPage() {
    // var radio = document.forms; (not complete)
    var options = document.getElementsByName('Options');
    var checkRadio = false;
    for ( var i = 0; i < options.length; i++) {
        if(options[i].checked) {
            checkRadio = true;
            break;
        }
    }
    if(!checkRadio)   { //a radio button is not checked
        alert("Please complete the questions");
    }
}

//countdown
var timeleft = 600;

var startingTime = 0;
var currentTime = 0;

function convertSeconds(s) {
  var min = floor(s / 60);
  var sec = s % 60;
  return nf(min, 2) + ':' + nf(sec, 2);
}


function setup() {
  noCanvas();
  startingTime = millis();


  var params = getURLParams();
  console.log(params);
  if (params.minute) {
    var min = params.minute;
    timeleft = min * 60;
  }

  var timer = select('#timer');
  timer.html(convertSeconds(timeleft - currentTime));

  var interval = setInterval(timeIt, 1000);

  function timeIt() {
    currentTime = floor((millis() - startingTime) / 1000);
    timer.html(convertSeconds(timeleft - currentTime));
    if (currentTime == timeleft) {
      clearInterval(interval);
      // where counter = 0;
    }
  }
//referenced : https://www.youtube.com/watch?v=MLtAMg9_Svw  [delete this line later]
}