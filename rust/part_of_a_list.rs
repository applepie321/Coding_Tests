// Part of a list
// https://www.codewars.com/kata/56f3a1e899b386da78000732/solutions/rust


// Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

// Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C: see Examples test Cases - )
// Each part will be in a string
// Elements of a pair must be in the same order as in the original array.





// gaxxx
fn part_list(arr: Vec<&str>) -> String {

    let mut out = "".to_string();
    for i in 1..arr.len() {
        out += combine(&arr[..i], &arr[i..]).as_str();
    }
    out
}

fn combine(left: &[&str], right : &[&str]) -> String {
    format!("({}, {})", left.join(" "), right.join(" "))
}


// steing
fn part_list(arr: Vec<&str>) -> String {
    let mut res = String::new();
    for i in 1..arr.len() {
        res.push_str(format!("({}, {})", &arr[..i].join(" "), &arr[i..].join(" ")).as_str());
    }
    res
}