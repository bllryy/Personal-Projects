// error handing tech
/*
    enum Option<T> { // define the generic Option type
        Some(T), // represents a value
        None, // represents no value
    }
 */ 
fn divide(numerator: f64, demonitator: f64) -> Option<f64> {
    if demonitator == 0.0 {
        None
    } else {
        Some(numerator / demonitator)
    }
}

fn divide_result(numerator: f64, demonitator: f64) -> Result<f64, String> {
    if demonitator == 0.0 {
        Err("Cannot divide by 0".to_string())
    } else {
        Ok(numerator / demonitator)
    }
}
 
fn main() {
/*
    let result = divide(10.0, 5.0);
    match result {
        Some(x) => println!("Result: {}", x),
        None => println!("Cant divide by zero!"),
    }
}
*/
match divide_result(numerator: 100.23, demonitator: 73.98)
    Ok(x) => println!("Result: {}", x),
    Err(e) => println!("Error: {}". e),
}
