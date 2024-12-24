use std::fs;
use std::error::Error;

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents: String = fs::read_to_string(config.filename)?;

    println!("With text:\n{}", contents);

    Ok(())
}

// groups filename and paramaters into a unit
pub struct Config {
    pub query: String,
    pub filename: String,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &str> { // will either have a config in the ok case or a string in
                                        // the air case which represent error message
        if args.len() < 3{
            return Err("not enough arguments")
        }
        let query = args[1].clone();
        let filename = args[2].clone();

        Ok(Config { query, filename })
    }
}

pub fn search(query: &str, contents: &str) -> Vec<&str> {
    vec![]
}


#[cfg(test)]
mod test
    use super::*;

    #[test]
    fn one_result() {
        let query: &str = "duct";
        let contents: &str = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(vec!["safe, fast, productive."], search(query,contents));
    }
}