// Elevator Distance
// https://www.codewars.com/kata/59f061773e532d0c87000d16/rust



// Imagine you start on the 5th floor of a building, 
// then travel down to the 2nd floor, 
// then back up to the 8th floor. 
// You have travelled a total of 3 + 6 = 9 floors of distance.

// Given an array representing a series of floors you must reach by elevator, 
// return an integer representing the total distance travelled 
// for visiting each floor in the array in order.



// Mine
fn elevator_distance(floors: &[i16]) -> i16 {
    let mut total_distance = 0;
    let mut current_floor = floors[0];
    
    for &floor in floors {
        total_distance += (current_floor - floor).abs();
        current_floor = floor;
    }
    
    total_distance
}



// Best practice
fn elevator_distance(floors: &[i16]) -> i16 {
    floors.windows(2).map(|s| (s[0] - s[1]).abs()).sum()
}
1 similar code