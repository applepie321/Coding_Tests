// Power of Two
// https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19

fn is_power_of_two(n: i32) -> bool {
    if n <= 0 {
        return false;
    }

    (n & (n - 1)) == 0
}
