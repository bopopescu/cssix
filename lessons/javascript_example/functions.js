// This covers some of the different labs within the Functions and Scope section (within JavaScript Fundamentals module) of Learn.co’s Bootcamp Prep.

// Task No. 1: Define the following functions
let number;
function add(a, b){ //add a and b and return the result.
 let sum = a+b;
 return sum;
}
function subtract(a, b){//subtract a and b and return the result.
    let sum = a-b;
    return sum;


}
function multiply(a, b){ //multiply a and b and return the result.
    let sum = a*b;
    return sum;

}
function divide(a, b){ //divide a and b and return the result.
    let sum = a/b;
    return sum;

}
function inc(a){ //Increment a by 1 and return the result.
    let sum = a+1;
    return sum;

}
function dec(a){ //Decrement a by 1 and return the result.
    let sum = a-1;
    return sum;

}

//Test your code! Run the following code and compare your output to the expected output 
console.log(add(3,4)); // number = 7
console.log(number);

console.log(subtract(3,4)); // number = -1
console.log(number);

console.log(multiply(3,4)); // number = 12
console.log(number);

console.log(divide(3,4)); // number = 0.75
console.log(number);

console.log(inc(3)); // number = 4
console.log(number);

console.log(dec(4)); // number = 3
console.log(number); 

// Task No. 2: Guess what the output will be after the following functions are called 
let str = "I Love CSSIx!"; 
console.log(str.toUpperCase()); 
console.log(str);
console.log(str.toLowerCase());
console.log(str);

console.log(str.search("I"));
console.log(str.search("Love"));
console.log(str.search("!"));

str = str.toLowerCase();
console.log(str);
console.log(str.search("I"));
console.log(str.search("Love"));
console.log(str.search("!"));

// Task No. 2: 
/*
Create a function called fahrenheitToCelsius:
Now store a fahrenheit temperature into a variable.
Convert it to celsius and output the result.
*/ 
function toCelsius(num){
    let fahrenheit = num;
    let celsius = (fahrenheit - 32)/1.8;
    return celsius;
}
//Test your code! Run the following code and compare your output to the expected output 
console.log(toCelsius(32)); // 0
console.log(toCelsius(58)); // 14.4...
console.log(toCelsius(100)); // 37.7...
            

// Task No. 4
/* You know how old your dog is in human years, but what about dog years? Calculate it!
Write a function named calculateDogAge that:
takes 1 argument: your puppy's age.
calculates your dog's age based on the conversion rate of 1 human year to 7 dog years.
outputs the result to the screen like so: "Your doggie is NN years old in dog years!"
Call the function three times with different sets of values.
Bonus: Add an additional argument to the function that takes the conversion rate of human to dog years.
*/
function calculateAge(num){
    let age = num * 7;
    return age;
}
//Test your code! Run the following code and compare your output to the expected output 
calculateAge(1); // 7
calculateAge(0.5); // 3.5
calculateAge(12); // 84

// Task No. 5
/* Ever wonder how much a "lifetime supply" of your favorite snack is? Wonder no more!
Write a function named calculateSupply that:
takes 2 arguments: age, amount per day.
calculates the amount consumed for rest of the life (based on a constant max age).
outputs the result to the screen like so: "You will need NN to last you until the ripe old age of X"
Call that function three times, passing in different values each time.
Bonus: Accept floating point values for amount per day, and round the result to a round number.
*/
function calculateSupply(age, amount){
    console.log("You will need " + age + " to last you until the ripe old age of " + amount );
}
//Test your code! Run the following code and compare your output to the expected output 
calculateSupply(28, 36); // You will need 946080 cups of team to last you until the ripe old age of 100
calculateSupply(28, 2.5); // You will need 65700 cups of team to last you until the ripe old age of 100
calculateSupply(28, 400); // You will need 10512000 cups of team to last you until the ripe old age of 100