fn main() {
    let s = "whatever".to_string();
    let s = String::from("whatever");
    // mutate the variable [push to it]
    let mut s = String::from("foo");
    s.push_str("bar");
    s.push_str("!");

    println!("the value of s = {}", s);


    // combine strings use the + operator
    let s1 = String::from("Hello, ");
    let s2 = String::from("World!");
    let s3 = s1 + &s2; // the s1 has been moved here and can no longer be used
    println!("{}", s3);
}
