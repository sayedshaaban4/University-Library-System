function validation(form){
    var firstname = form.firstname.value;
    var lastname = form.lastname.value;
    
    if(firstname == "" ){
        alert("Error: Please enter Your firstname !");
        form.firstname.focus();
        return false;
    }
    if(lastname == ""){
        alert("Error: Please enter Your lastname !");
        form.lastname.focus();
        return false;
    }

    return true;

}