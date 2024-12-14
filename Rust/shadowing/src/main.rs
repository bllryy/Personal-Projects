// Shadowing 
// declare a new variable with the same name as an existing one
// shadowing is not the same as marking a value as mut
// no resiging

fn main() {
    let x = 5; // ofc 5

    let x = x + 1; // 6

    let x = x * 1000;
    
    
    
    {
        let x = x * 2; // 12
        println!("Inside inner scope: {}", x);
        // Shadows the outer variable
    }
    println!("Outside the value of x is: {x}");
}
