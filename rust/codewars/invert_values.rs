// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/rust


// DESCRIPTION:
// Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

// invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
// invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
// invert([]) == []


// fn invert(values: &[i32]) -> Vec<i32> {
// your code here
// }




fn invert(values: &[i32]) -> Vec<i32> {
    let mut result = Vec::new();
    for value in values {
        result.push(-value);
    }
    result
}



// Best practices
fn invert(values: &[i32]) -> Vec<i32> {
    values.iter().map(|x| -x).collect()
}


// Clever
fn invert(values: &[i32]) -> Vec<i32> {
    values.iter().map(std::ops::Neg::neg).collect()
}