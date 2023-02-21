function sumvalidate(){
    v = 1;
    var number1error = document.getElementById('error1').value;
    var number2error = document.getElementById('error2').value;
    var number1 = document.getElementById('num1').value;
    var number2 = document.getElementById('num2').value;
    if(number1 == ""){
        number1error.innerHTML = "Enter first number";
        v = 0;
    }
    else{
        v = 1;
    }
    if(number2 == ""){
        number2error.innerHTML = "Enter second number";
        v = 0;
    }
    else{
        v = 1;
    }
    if(v == 1){
        return true;
    }
    else{
        return false;
    }
}