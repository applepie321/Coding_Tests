// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/rust

// DESCRIPTION:


// Your task is to find the first element of an array that is not consecutive.

// By not consecutive we mean not exactly 1 larger than the previous element of the array.

// E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

// If the whole array is consecutive then return null2.

// The array will always have at least 2 elements1 and all elements will be numbers. 

// The numbers will also all be unique and in ascending order. 

// The numbers could be positive or negative and the first non-consecutive could be either too!


fn first_non_consecutive(arr: &Vec<i32>) -> Option<i32> {
    let mut prev = arr[0];
      for i in 1..arr.len() {
          if arr[i] != prev+1 {
              return Some(arr[i]);
          }
          prev = arr[i]
      }
      None
  }



  
// Best practice & clever
fn first_non_consecutive(arr: &[i32]) -> Option<i32> {
    arr.windows(2).find(|s| s[0] + 1 != s[1]).map(|s| s[1])
}



fn first_non_consecutive(arr: &Vec<i32>) -> Option<i32> {
    for i in 1..arr.len() {
      if arr[i] - arr[i - 1] != 1 {
        return Some(arr[i]);
      }
    };
    None
  }