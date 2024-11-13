struct User {
    username: String,
    email: String,
    logged_in_counter: u64,
    active: bool,
}

fn main() {
    let user = User {
        username: String::from("kamiyaa"),
        email: String::from("abc@aaa.com"),
        logged_in_counter: 0,
        active: true,
    };
    println!("{} {} {} {}", user.username, user.email, user.logged_in_counter, user.active)
}

