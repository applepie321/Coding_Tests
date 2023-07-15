// Sort by Last Char
// https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/rust


// Given a string of words (x), you need to return an array of the words,
//  sorted alphabetically by the final character in each.

// If two words have the same last letter, they returned array should show
//  them in the order they appeared in the given string.

// All inputs will be valid.





// Best practices


// halflucifer
fn sort_by_last_char(s: &str) -> Vec<String> {
    let mut v = s.split(' ').map(|s|s.to_string()).collect::<Vec<_>>();
    v.sort_by_key(|k|k.chars().last());
    v
}




//Kiyōtaka
use itertools::Itertools;

fn sort_by_last_char(s: &str) -> Vec<String> {
    s.split_whitespace()
     .map(|w| w.to_string())  
     .sorted_by_key(|k| k.chars().last())
     .collect()
}