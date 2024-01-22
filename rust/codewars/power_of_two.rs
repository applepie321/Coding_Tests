// Power of Two
// https://www.codewars.com/kata/534d0a229345375d520006a0/rust


//DESCRIPTION
// Complete the function power_of_two/powerOfTwo 

// that determines if a given non-negative integer is a power of two. From the corresponding Wikipedia entry:
// a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.
// You may assume the input is always valid.



fn power_of_two(x: u64) -> bool {
    x != 0 && (x & x - 1) == 0
}







// Best practice
fn power_of_two(x: u64) -> bool {
    x.is_power_of_two()
}



// Clever
fn power_of_two(x: u64) -> bool {
    x.count_ones() == 1
}





static power_of_two: fn(u64) -> bool = u64::is_power_of_two;