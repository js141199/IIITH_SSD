
function resetForm(){

    document.getElementById("myForm").reset();
}

function validateManagerName(){

    var name = document.getElementById("managerName").value;

    if(name == ""){
        document.getElementById("managerNameError").innerHTML = 'This field is required'
        return false;
    }else{
        document.getElementById("managerNameError").innerHTML = ''
        return true;
    }

}

function validateEmail(){

    var email = document.getElementById("emailAddress").value;
    var pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2, 4}$";

    if(email.match(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)){
        document.getElementById("emailError").innerHTML = '';
        return true;
    }else{
        document.getElementById("emailError").innerHTML = 'Invalid Email';
        return false;
    }

}

function validateUsername(){

    var username = document.getElementById("username").value;
    var upper = /[A-Z]/.test(username);
    var digit = /[0-9]/.test(username);

    if(!upper || !digit){
        document.getElementById("usernameError").innerHTML = 'Invalid Username Must have 1 upper case and 1 digit';
        return false;
    }else{
        document.getElementById("usernameError").innerHTML = '';
        return true;
    }
}

function validatePassword(){

    var pass = document.getElementById("password").value;
    var cpass = document.getElementById("confirmPassword").value;

    if(pass == "" || cpass == ""){
        document.getElementById('passwordError').innerHTML = 'Required';
        document.getElementById('confirmPasswordError').innerHTML = 'Required';
        return false;
    }

    if(pass === cpass){
        document.getElementById('confirmPasswordError').innerHTML = '';
        return true;
    }else{
        document.getElementById('confirmPasswordError').innerHTML = 'Password and confirm password does not match';
        return false;
    }
    
}

function validateMyForm(){

    if(validateManagerName() &&  
    validateUsername() && validateEmail() && validatePassword() ){

        var name = document.getElementById("managerName").value;
        var email = document.getElementById("emailAddress").value;
        var username = document.getElementById("username").value;
        var leadName = document.getElementById("teamLead").value;

        var output = "Name: " + name + " \n";
        output += "Email: " + email + "\n";
        output += "Username: " + username + "\n";
        output += "Team Lead: " + leadName;

        alert(output);

        return true;
        }
    else{
        return false;
    }

}

function changeBackgroundColor(e){

    var keycode = e.keyCode;
            
    if(keycode === 97){
        document.getElementById("bodyDisplay").style.backgroundColor = 'red';
    }else{
        document.getElementById("bodyDisplay").style.backgroundColor = 'aqua';
    }

}