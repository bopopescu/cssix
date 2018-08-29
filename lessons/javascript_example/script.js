function sendAlert() {
  alert("Hello World");
}

let name = "Brenda";
console.log('Hello ' + name);
alert(name);

let age = 16;

if(age >= 18){
    //run if true
    console.log("You can vote AND get your permit!");
}else if (age <16){
    //rune if not true
    console.log("You weill ahve to wait :( ");
}else{
    console.log("You can't get your driver's permit, BUT you can vote");
}

function firstFunction(){
    console.log('My first function!');
}

function greetPerson(name1, name2, num){
    console.log("Hello, " + name1 + " and " + name2);
    console.log("This is your number: " + num);
}

var result = greetPerson('Alice', 'Bob', 9);
console.log(result);

function getFullName(firstName, lastName){
    //console.log(firstName + " " + lastName)
    return firstName + " " + lastName;
}

//getFullName('Edgar',"Licup")

let fullName = getFullName('Edgar', 'Licup');
console.log("Output: " + fullName);

function checkout(item1, item2, coupon){
    let subtotal = item1 + item2;
    let couponValue = subtotal * coupon;
    let total = subtotal - couponValue
    console.log(total);
    return total;
}

let total = checkout(33,19,.15)
let total2 = checkout(29,14,.20)

console.log(total + " : " + total2);