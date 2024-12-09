// COmpund data types
// arrays, tuples, slices, and strings (slice string)


// arrays
fn main(){
    let numbers: [i32; 5] = [1,2,3,4,5];
    println!("Number Array: {:?}", numbers);
//  let mix = [1,2,"apple", true];
//  println!("Mix array: {:?}", mix);
    let fruits: [&str; 3] = ["Apple", "Banana", "Orange"];
    println!("Fruits Array: {:?}", fruits);
    println!("Fruits Array: {}", fruits[0]);
    println!("Fruits Array: {}", fruits[1]);
    println!("Fruits Array: {}", fruits[2]);



    // tuples
    let human: (String, i32, bool) = ("Alice".to_string(), 30, false);
    println!("Human Tuple: {:?}", human);
    let my_mix_tuple = ("Fin", 17, true, [1,2,3,4,5]);
    println!("My mix tuple: {:?}", my_mix_tuple);
    
    // slices: contigous sizes of mem [1,2,3,4,5]
    let number_slices:&[i32] = &[1,2,3,4,5];
    println!("Number Slice: {:?}", number_slices);


    let animal_slices :&[&str] = &["Lion", "Elephant", "Crocodile"]; 
    println!("Animal Slice: {:?}",animal_slices);


    let _book_slices :&[&String] = &[&"IT".to_string()]; 
    println!("Book Slice: {:?}",_book_slices);

    // Strings vs String Slices (&str)
    // Strings [ growable, mutable, owned, string type ]
    let mut stone_cold: String = String::from("Hell, ");
    stone_cold.push_str("Yeah!");
    println!("Stone Cold Says: {}", stone_cold);

    // B- &str (String Slice)
    let string: String = String::from("Hello World!");
    let slice: &str = &string[0..5];
    println!("Slice Value: {}", slice);



}

fn print(){
    println!("SLICE: {}", slice);



}
