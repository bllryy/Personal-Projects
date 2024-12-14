// Constants
// cant cahange to a mut
fn main() {
    println!("Hello, world!");
    let mut x = 5;

    const Y: i32 = 10;
    println!("The value of x is {}", x);
    println!("The value of y is {}", Y);
    println!("The value of PI is {}", PI);
    println!("Three hours in seconds is {}", THREE_HOURS_IN_SECONDS);
}



// you can declare a constant here with a type annotation
const PI: f64 = 3.14;
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
// slices

