// leetcode 169
// https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times.
// You may assume that the majority element always exists in the array.




// https://leetcode.com/problems/majority-element/solutions/1885812/rust-solution-0ms-100-faster/?envType=study-plan-v2&envId=top-interview-150
use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut count = 1;

        for i in 1..nums.len() {
            if nums[res] == nums[i] {
                count += 1;
            } else {
                count -= 1;
            }

            if count == 0 {
                res = i;
                count = 1;
            }
        }

        count = 0;
        for i in 0..nums.len() {
            if nums[i] == nums[res] {
                count += 1;
            }
        }

        if count > (nums.len() / 2) {
            return nums[res];
        }
        return -1;
    }
}