fn main() {
    // loop keyword
    //loop {
    //    println!("Hello world!")
    //}

    // while keyword
    /* 
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };
    println!("The result is {result}");
}
*/
/*   loop
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;
        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
        } 
        count += 1;
        remaining -= 1;
    }
}
*/ // While loop
    let mut number = 3;
    while number != 0 {
        println!("{number}", );
        number = number + 1;
        break;
    }


// looping through a collection with for loop
    let a = [1,2,3,4,5,6];
    let b = ["a", "b", "c", "d", "e", "f"];
    for element in a {
        println!("{element}");
    }
    for letter in b {
        println!("{letter}");
    }
}
