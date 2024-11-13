


fn main() {
    println!("Please enter the IP/Domain: ");

    // get the read
    let mut input = String::new();


    match res_ip(input) {
        Some(ip) => println!("Resolved to ip {}", ip),
        None => println!("Could not resolve IP address."),
        
    }
}
