// Ownership, borrowing and refrence

// Ownership
// ---------
// C, C++ -> Memory Management Control Issue
// Grabage Collector solved this issue, but made a new issue
// -> slow preformance and bad outcome

// What is ownership
// everyvalue has a single owner
// can only be one owner at a time
// if the value goes out of scope it gets dropped

// ex. 1
/*fn main() {
    let s1 = String::from("RUST");
    // s1 is the owner of the string
    let len = calculate_length(&s1);
        // passing refrence to the owner
    println!("Length of '{}' is {}.", s1, len);

}

fn calculate_length(s: &String) -> usize{
    s.len()
}


// there can only be one owner at a time
fn main1(){
    let s1 = String::from("RUST");
    let s2 = s1;

    //println!("{}", s1);
    println!("{}", s2);

} */

// ex 3


fn main() {
    let s1 = String::from("RUST");
    let len = calculate_length(&s1);
    println!("Length of '{}' is {}. ", s1, len);
}

// s1 goes out of scope and its value goes out of memory
fn printLost(s: &string){ 
    println!("{}", &s1);
}

fn calculate_length(s: &String) -> usize{
    s.len()
}
