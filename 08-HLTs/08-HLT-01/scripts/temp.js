// Write a program that converts Celsius to Fahrenheit and Fahrenheit to Celsius
// The centigrade to Fahrenheit conversion formula is: C = (5/9) x (F -32) 
// The Fahrenheit formula is F = C x 9 / 5 + 32
//tempc = (5/9) * (tempf -32);
//tempf = (tempc * 9) / 5 + 32;

// var tempc = 30

function c2f(){
    tempf = (tempc * 9) / 5 + 32;
    alert("Temperature in Fahernheit is: "+tempf);
    }

function f2c(temp){
    tempc = (5/9) * (tempf -32);
    alert("Temperature in Celsius is: " +tempc);
 }