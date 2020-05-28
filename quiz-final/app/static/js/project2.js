//COUNTDOWN TIMER (10 minutes)
var timeleft = 900; //time for completing quiz
var counter = 0;

//so the numbers are in 2 digits form
function twoD(n){
    if (n>=0 && n<=9){
        return "0" + n;
    }
    else
        return n;
}

//e.g. convert 60s into 1 : 00
function convertSeconds(s) {
    var min = Math.floor(s / 60);
    var sec = s % 60;
    return twoD(min) + ':' + twoD(sec);
}


function setup() {
    var timer = document.getElementById("timer");

    var interval = setInterval(count, 1000); 
    //want count event to happen every 1000ms

    function count() {
        timer.innerHTML= convertSeconds(timeleft - counter);
        if (counter == timeleft) {
            clearInterval(interval);
            // becomes 00:00
            alert("Oops, time is up! Quiz auto submitted.");
            location.replace("Results.html");
        }
        else{
            counter++;
        }
    }
}
