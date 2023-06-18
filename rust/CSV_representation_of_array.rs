// CSV representation of array
// https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/rust

// DESCRIPTION

// Create a function that returns the CSV representation of a two-dimensional numeric array.

// Example:

// input:
//    [[ 0, 1, 2, 3, 4 ],
//     [ 10,11,12,13,14 ],
//     [ 20,21,22,23,24 ],
//     [ 30,31,32,33,34 ]] 
    
// output:
//      '0,1,2,3,4\n'
//     +'10,11,12,13,14\n'
//     +'20,21,22,23,24\n'
//     +'30,31,32,33,34'
// Array's length > 2.



fn to_csv_text(array: &[Vec<i8>]) -> String {
    let mut result = String::new();
    for row in array {
        for (i, &num) in row.iter().enumerate() {
            result.push_str(&num.to_string());
            if i != row.len() - 1 {
                result.push(',');
            }
        }
        result.push('\n');
    }
    result.pop();
    result
}



// Best Practice
fn to_csv_text(array: &[Vec<i8>]) -> String {
    array
    .iter()
    .map(|row| 
        row.iter()
           .map(|x| x.to_string())
           .collect::<Vec<_>>()
           .join(",")
    )
    .collect::<Vec<_>>()
    .join("\n")
}