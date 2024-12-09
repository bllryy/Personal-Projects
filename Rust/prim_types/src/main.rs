 // primative types
 // int, flaot, bool, char
 //
 // Int
 // Rust has signed (+ and -) and unsigned
 // integer (only+) types of diffrent sizes
 // sign: i8,i16,i32,i64, i128
 // unsign: u8,u16,u64,u128
 //
 fn main(){
    let x: i32 = -42;
    let y: u64 = 100;
    println!("Signed Int: {}", x);
    println!("Unsigned Int: {}", y);

// diff bet i32 (32 bits) and i64(64 bits)
// range : i32 - big numbers
// dont feel like writing the big nums
    let e: i32 = 2147483647;
//  let i: i64 = 214783647;
    println!("Max value of i32: {}", e);


// floats
// f32, f64
let pi: f64 = 3.14;
println!("Vale of pi: {}" , pi);

// Boolean values true or false 
let is_snowing: bool = true;
println!("Is it snowing? {}", is_snowing);

// character type = char
let letter: char = 'a';
println!("First letter of the alphabet: {}", letter);

}
