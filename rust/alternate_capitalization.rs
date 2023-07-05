Alternate capitalization
https://www.codewars.com/kata/59cfc000aeb2844d16000075/rust

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.



// Best practice

// sjud
fn capitalize(s: &str) -> Vec<String> {
    let (left, right) : (String, String) = s.chars().enumerate().map(|(i,c)| 
        {if i % 2 == 0 {
            (c.to_ascii_uppercase(), c)
        } else {
            (c.to_ascii_lowercase(), c.to_ascii_uppercase())
    }}).unzip();
    vec![left,right]
}



// miso-belica
fn capitalize(s: &str) -> Vec<String> {
    vec![
        s.chars().enumerate().map(|(i, c)| if i % 2 == 0 { c.to_ascii_uppercase() } else { c } ).collect(),
        s.chars().enumerate().map(|(i, c)| if i % 2 == 1 { c.to_ascii_uppercase() } else { c } ).collect(),
    ]
}