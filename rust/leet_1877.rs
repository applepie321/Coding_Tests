// Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17

impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {

    // Sort the array
    nums.sort();

    // Initialize pointers
    let mut left = 0;
    let mut right = nums.len() - 1;

    // Initialize the result variable
    let mut result = 0;

    // Pair up the elements and find the maximum pair sum
    while left < right {
        result = result.max(nums[left] + nums[right]);
        left += 1;
        right -= 1;
    }

    result
    }
}