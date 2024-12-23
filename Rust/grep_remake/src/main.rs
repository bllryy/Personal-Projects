use std::env;
use std::fs;
use std::process;
use std::error::Error;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    let config: Config = Config::new(&args).unwrap_or_else(op: |err: &str| {
        println!("Problem parsing arguments: {}", err);
        process::exit(code: 1);
    });

    println!("Searching for {}", Config.query);
    println!("In file {}", Config.filename);

    if let Err(e: Box<dyn Error>) = run(config) {
        println!("Application error: {}", e);
        process::exit(code: 1);
    }
}

fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents: String = fs::read_to_string(config.filename)?;

    println!("With text:\n{}", contents);

    Ok(())
}





// groups filename and paramaters into a unit
struct Config {
    query: String,
    filename: String,
}

impl Config {

    fn new(args: &[String]) -> Result<Config, &str> { // will either have a config in the ok case or a string in
                                        // the air case which represent error message
        if args.len() < 3{
            return Err("not enough arguments")
        }
        let query = args[1].clone();
        let filename = args[2].clone();

        Ok(Config { query, filename })
    }

}
