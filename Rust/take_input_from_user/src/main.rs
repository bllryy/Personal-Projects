use std::io;


fn main() {
    println!("Please type somthing or type x to exit");
    let mut input_string = String::new();

    while input_string.trim() != "x" {
        input_string.clear();
        // to get input
        // and read whats coming in
        io::stdin().read_line(&mut input_string).unwrap();
        println!("You wrote: {:?}", input_string);
    // dont forget debug print for the exit b/c rust looks at x like: x\n
    }




}


// .trim() to clear x
