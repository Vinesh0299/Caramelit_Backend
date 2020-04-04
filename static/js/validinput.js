// This file implements several checks on input elements
var fname = document.getElementById('fname');
var email = document.getElementById('email');
var phone = document.getElementById('phone');
var pincode = document.getElementById('pincode');

var nameVal = false;
var phoneVal = false;
var emailVal = false;
var pincodeVal = false;

// If name, email, phone and pincode are in desirable range then this function will enable the submit button otherwise disable it
function submitButton() {
    if(nameVal & phoneVal & pincodeVal & emailVal) {
        document.getElementById('submitButton').disabled = false;
    } else {
        document.getElementById('submitButton').disabled = true;
    }
}

// Applies a simple length check on name input
function validateName(e) {
    if(fname.value.length < 3) {
        document.getElementById('fname').style.borderColor = 'red';
        nameVal = false;
    } else {
        document.getElementById('fname').style.borderColor = 'green';
        nameVal = true;
    }
    submitButton();
}

// Applies a simple length check on phone input
function validatePhone(e) {
    if(phone.value.length < 10) {
        document.getElementById('phone').style.borderColor = 'red';
        phoneVal = false;
    } else {
        document.getElementById('phone').style.borderColor = 'green';
        phoneVal = true;
    }
    submitButton();
}

// Applies a simple length check on pincode input
function validatePincode(e) {
    if(pincode.value.length < 6) {
        document.getElementById('pincode').style.borderColor = 'red';
        pincodeVal = false;
    } else {
        document.getElementById('pincode').style.borderColor = 'green';
        pincodeVal = true;
    }
    submitButton();
}

// Applies a set of checks including length and existence of '@' and '.' on email input
function validateEmail(e) {
    if(email.value.length > 5 & email.value.indexOf('@') >= 0 & email.value.indexOf('.') >= 0) {
        document.getElementById('email').style.borderColor = 'green';
        emailVal = true;
    } else {
        document.getElementById('email').style.borderColor = 'red';
        emailVal = false;
    }
    submitButton();
}

// Adding event listeners on all the input elements
fname.addEventListener("keyup", validateName);
phone.addEventListener("keyup", validatePhone);
email.addEventListener("keyup", validateEmail);
pincode.addEventListener("keyup", validatePincode);