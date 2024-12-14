// If Else [ If Expression] [Else Expression]
#![allow(warnings)]

fn main() {
    /*
    let age: u16 = 16;
    if age >= 18 {
        println!("You can drive a car!");
    } else {
        println!("You are not old enough to drive a car!");
    }
    */
// elif

// Multiple conditions with else if
/* 
let number = 6;
if number % 4 == 0 {
    println!("The number is divisible by 4.");
} else if number % 3 == 0 {
    println!("The number is divisible by 3.");
} else if number % 2 == 0 {
    println!("The number is divisible by 2.");
} else {
    println!("The number is not divisible by 4, 3, or 2.");
}
 */

let condition = true;
let number = if condition {5} else {6};
println!("Number: {number}");

}
