// dynamic array that can grow and shrink when needed
fn main() {
    /* 
    //let _v:Vec<i32> = Vec::new();
    let mut _v:Vec<i32> = Vec::new();
    // Macro to create a vector of numbers
    let mut _v:Vec<i32> = vec![1,2,3];

    _v.push(5);
    _v.push(6);
    _v.push(7);
    _v.push(8);
    _v.push(9);

    println!("{:?}", _v);
*/
// indexing
let _v = vec![1,2,3,4,5];

//let third: &i32 = &_v[2]; // Direct Indexing

//println!("The third element is {}", third);

let third: Option<&i32> = _v.get(index: 2);
    Some(third: &i32) => println!("The third element is {third}"),
    None => println!("There is no element.");
}
