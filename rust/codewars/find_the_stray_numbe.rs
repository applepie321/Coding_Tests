// Find the stray number
// https://www.codewars.com/kata/57f609022f4d534f05000024/rust


// You are given an odd-length array of integers, in which all of them are the same, except for one single number.

// Complete the method which accepts such an array, and returns that single different number.

// The input array will always be valid! (odd-length >= 3)


fn stray(arr: &[u32]) -> u32 {
    let mut result = 0;
    for &num in arr {
        result ^= num;
    }
    result
}


// Best
fn stray(arr: &[u32]) -> u32 {
    arr.iter().fold(0, |acc, el| acc ^ el)
}