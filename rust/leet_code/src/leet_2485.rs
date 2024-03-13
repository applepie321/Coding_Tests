// Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13

fn pivot_integer(n: i32) -> i32 {
    let mut left: i32 = 0;
    let mut right: i32 = (*(n + 1)) / 2;

    for x in 1..=n {
        let right_remaining = right - left - x;
        if right_remaining == left {
            return x;
        }
        left += x;
    }

    -1
}
