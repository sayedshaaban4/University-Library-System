function validation(form){
    var username = form.email.value;
    var pass     = form.password.value;

    if(username == "" || pass == ""){
        
        alert("Error: Please check that you are entered Your Email or Password !");
        form.email.focus();
        return false;
    }

    return true;

}