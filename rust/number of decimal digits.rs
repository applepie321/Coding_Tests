// Number of Decimal Digits
// https://www.codewars.com/kata/58fa273ca6d84c158e000052


// Description
// Determine the total number of digits in the integer (n>=0) given as input to the function.
// For example, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

// All inputs will be valid.





fn digits(n: u64) -> usize {
    if n == 0 {
        return 1;
      }
      
      let mut count = 0;
      let mut num = n;
      
      while num > 0 {
          num /= 10;
          count += 1;
      }
      
      count
  }





// Best practice


fn digits(n: u64) -> usize {
    n.to_string().len()
  }