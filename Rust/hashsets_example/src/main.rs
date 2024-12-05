use std::collection::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // HashSet::insert() return false if  
    // there was a value already present
    assert!(b.insert(4), "Value 4 is already in the set B!");
    // FIXME ^ Comment out this line
    
    b.insert(5);

    // If a collections element type implements 'Debug'
    // then the collection implements 'Debug'
    // It usually prints its elements in the format [elem1, elem2, ...]
    println!("A: {:?}",a);
    println!("B: {:?}",b);

    // If a collection element type implements debug 
    //
    //
    println!("A: {:?}", a);
    println!("B: {:?}", b);

}
