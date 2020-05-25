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

//check if one radio in every qs is clicked then submit it
function submit() {
    var radio = document.forms[0];
}

//jumping to result page after every question is answered and submit is clicked
function resultPage() {
    // var radio = document.forms;
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

    location.replace("3.html");
    //replace() doesn't let you use 'back' to go previous page
}
