#![allow(warnings)]
// both hold related values just like touples
// pices of a structs can be diffrent types


fn main() {
    // tuple
    let rectangle = (200, 500);

    // Struct
    struct Book {
        title: String,
        author: String,
        pages: u32,
        available: bool,
    }
    struct User {
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }

    let mut user1 = User {
        active: true,
        username: String::from("someusername"),
        email: String::from("someusername@m.com"),
        sign_in_count: 1,
    };

    //user1.email = String::from("anotheremail@m.com");
    println!("User Email is: {}", user1.email);

    // Return a struct from a function
    fn build_user(email: String, username: String) -> User{
        User{
            active: true,
            email,
            username,
            sign_in_count: 1,
        }
    }

    // create instances from other instances
    let user2 = User {
        email: String::from("another@m.com"),
        ..user1
    };


    // tuples structs
    // no name feilds
    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);

    let black = Color(0,0,0);
    let white = Color(255,255,255);

    // unit like struct
    struct AlwaysEqual;
    let subject = AlwaysEqual;
    
}
