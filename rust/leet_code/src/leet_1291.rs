// Sequential Digits
// https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02

fn sequential_digit(low: i32, high: i32) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();

    for digit in 1..=9 {
        let mut num = digits;
        let mut next_digit = digit;
        while num <= high && next_digit < 10 {
            if num >= low {
                result.push(num);
            }
            next_digit += 1;
            num = num * 10 + next_digit;
        }
    }
    result.sort();
    result
}
