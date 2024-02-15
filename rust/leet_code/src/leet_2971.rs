// Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15

fn largest_perimeter(nums: Vec<i32>) -> i64 {
    let mut nums: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
    nums.sort();
    let mut previous_sum: i64 = 0;
    let mut answer: i64 = -1;

    for &i in nums.iter() {
        if i < previous_sum {
            answer = i + previous_sum;
        }
        previous_sum += i;
    }
    answer
}
