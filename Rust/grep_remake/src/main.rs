use std::env;
use minigrep::Config;


fn main() {
    let args: Vec<String> = env::args().collect();
    
    let config: Config = Config::new(&args).unwrap_or_else(|err: &str| {
        println!("Problem parsing arguments: {}", err);
        process::exit(code: 1);
    });

    println!("Searching for {}", Config.query);
    println!("In file {}", Config.filename);

    if let Err(e: Box<dyn Error>) = minigrep::run(config) {
        println!("Application error: {}", e);
        process::exit(code: 1);
    }
}



/* 
1. main function which takes in cli arguments stores them in a var called args
2. constructs a config struct and passes the config struct into the run function
3. as of this line try molving stuff to a library crate to unbloat the main.rs


*/