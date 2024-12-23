use std::env::args;

fn main() {
    let input = args();

    for entry in input {
        println!("you entered: {}", entry);
    }
}
