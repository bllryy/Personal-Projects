// references and borrwoing
// saftey and preformance
// borrowing and refrences are powerful concepts
//
//  Understanding refrences
//  refrences enable you to borrow values without taking ownership
//  immutable refrence
//  mutable refrence
//  making a refrence add a &
/*fn main(){
    let mut _x = 5;

    let _r = &mut _x;
    *_r += 1;
    *_r -= 3;
    println!("Print the vale of _x: {}", _x);
    println!("Print the vale of _r: {}", _r);
} */

// data structure that allows you to group multiple feilds together under on name
fn main(){
   let mut account = BankAccount {
        owner: "alice".to_string(),
        balance: 150.55,
        
   };
   // immutable borrow to check the balance
   account.check_balance();

   // mutable borrow to withdraw money
   account.withdraw(45.5);


   // immutable borrow to check the balance
   account.check_balance();
}

struct BankAccount {
    owner: String,
    balance: f64,
}

impl BankAccount {
    fn withdraw(&mut self, amount: f64){
        println!("Withdrawing {} from account owned by {}", amount, self.owner);
        self.balance -= amount;

    }

    fn check_balance(&self){
        println!("Account owned by {} has a balance of {}", self.owner, self.balance);
    }
}
