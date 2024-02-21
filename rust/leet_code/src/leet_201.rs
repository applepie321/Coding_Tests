// Bitwise And of Numbers Range
// https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=daily-question&envId=2024-02-21

fn range_bitwise_and(mut left: i32, mut right: i32) -> i32 {
    let mut shift = 0;

    while left < right {
        left >>= 1;
        right >>= 1;
        shift += 1;
    }

    return left << shift;
}
