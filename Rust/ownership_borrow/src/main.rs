// this is a fix for the violation in book


fn main() {
    let s1: String = String::from("Hello World");
    let s2 = &s1;

    println!("{}", s1);
    println!("{}", s2);

}