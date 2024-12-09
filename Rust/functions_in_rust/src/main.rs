// Functions
// entry point
// any function or variables should be written in snake case
// snake case: hello_world
// kebab case: hello-world

fn main() {
   hello_world();
   tell_height(182);
   human_id("Fin", 17, 182.0);
   let _X: i32 = {
        let price: i32 = 5;
        let qty: i32 = 10;
        price * qty
    };
    println!("Result is: {}", _X);
    //add(4,6)
    let y: i32 = add(4,6);
    println!("The Value of y is: {}", y);
    println!("Value from function 'add' is: {}", add(4,6));

    // calling the BMI function
    let weight: f64 = 70.0;
    let height: f64 = 1.82;
    let bmi = calculate_bmi(weight,height);
    println!("Ur BMI is: {:.2}", bmi);
}

// Hoisiting - can call any function anywhere in your code
fn hello_world() {
    println!("Hello Rust!");
    
}

// you can insert input values
fn tell_height(height: u32) {
    println!("My height is {} cm", height);

} 


fn human_id(name: &str, age: u32, height: f32){
    println!("My name is {}, I am {} years old, and my height is {} cm.", name, age, height);

}


// Expressions and Statements
// Expression: anything that returns a value
// Statement: Anything that does not return a value
// Expression:
// --------------
// 5
// true, false
// add(3,4)
// if condition {value1} else {value2}
// ({code})
//
//
//
// functions returning values
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// statements
// final example
// BMI = height(kg)/height(m)^2
//
//
fn calculate_bmi(weight_kg: f64, height_m: f64) -> f64 {
    weight_kg / (height_m * height_m)
}
