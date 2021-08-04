function myfunction(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var error = document.getElementById("error");
    var text;

    if (name.length <3 || name.length>30){
        text = "Name is not valid"
        error=text;
        return false;
    }

    if (email.length <3 || email.length>30){
        text = "Email is not valid"
        error=text;
        return false;
    }

    return true;
}