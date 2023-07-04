// Is this a triangle
// https://www.codewars.com/kata/56606694ec01347ce800001b/rust

// Implement a function that accepts 3 integer values a, b, c. 
// The function should return true if a triangle can be built 
// with the sides of given length and false in any other case.

// (In this case, all triangles must have surface greater than 0 to be accepted).


fn is_triangle(a: i32, b: i32, c: i32) -> bool {
    let max_value = a.max(b).max(c);
    if max_value < a + b + c - max_value {
        true
    } else {
        false
    }
}



// Best practice
fn is_triangle(a: i64, b: i64, c: i64) -> bool {
    a + b > c && a + c > b && b + c > a
}


fn is_triangle(a: i64, b: i64, c: i64) -> bool {
    let mut s = vec![a,b,c];
    s.sort();
    s[0]+s[1]>s[2]
}