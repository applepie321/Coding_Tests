// leetcode 0026
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150




// https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/774408/rust-0ms-solution/?envType=study-plan-v2&envId=top-interview-150
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        match nums.is_empty() {
            true => 0,
            false => {
                let mut prev = 0;
                for i in 1..nums.len() {
                    if nums[prev] != nums[i] {
                        prev += 1;
                        nums[prev] = nums[i];
                    }
                }
                (prev + 1) as i32
            }
        }
        
    }
}




//https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/2801656/rust-2-lines/?envType=study-plan-v2&envId=top-interview-150
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();
        nums.len() as i32
    }
}