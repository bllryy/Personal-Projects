#[derive(Debug)]
struct User {
    username: String,
    email: String,
    logged_in_counter: u64,
    active: bool,
}

// functrion that creates a struct and returns it
fn build_user(username: String, email: String) -> User {
    User {
        username,
        email,
        logged_in_counter: 0,
        active: true
    }
}


fn main() {
    let user = build_user(String::from("bllry"), String::from("abc@aaa.com"));
    let user2 = User {
        username: String::from("abcc")
        email: String::from("abcc@aaa.coom")
        logged_in_counter: user.logged_in_counter,
        active: user.active,
        // also ..user
    };
    println!("{:?}", user)
    println!("{:?}", user2)
}

