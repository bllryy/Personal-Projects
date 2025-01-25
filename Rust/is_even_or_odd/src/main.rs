use std::io;


fn main() {
    for _ in 0..10 {
        printGreeting();
    }

}

fn printUserGreeting() {
    let mut input = String::new();
    println!("Enter a even or odd number: ");
    if let Ok(number) {
        println!("Even Number"); 
    } else {
        println!("Odd Number");
}


fn isEvenNumber(value: i32) -> bool {
    value % 2 == 0
}
