// Holiday VIII - Duty Free
// https://www.codewars.com/kata/57e92e91b63b6cbac20001e5/rust

// DESCRIPTION
// The purpose of this kata is to work out just how many bottles of duty free whiskey 
// you would have to buy would effectively cover the cost of your holiday.

// You will be given price (normPrice), the duty free discount (discount) and the cost of the holiday.

// For example, if a bottle cost £10 and the discount in duty free was 10%, 
// you would save £1 per bottle. 
// If your holiday cost £500, the answer you should return would be 500.

// All inputs will be integers. Please return an integer. Round down.


// Best practice
fn duty_free(price: i32, discount: i32, holiday_cost: i32) -> i32 {
    holiday_cost *100   / (discount * price)
}

fn duty_free(price: i32, discount: i32, holiday_cost: i32) -> i32 {
    let discount = discount as f64 / 100.0;
    let savings_per_bottle = price as f64 * discount;
    
    (holiday_cost as f64 / savings_per_bottle) as i32
}