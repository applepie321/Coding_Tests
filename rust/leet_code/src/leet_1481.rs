// Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16

use counter::Counter;
use std::collections::HashMap;

fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
    let counter = arr.into_iter().collect::<Counter<_>>();

    let mut sorted_counts: Vec<_> = counter.iter().collect();
    sorted_counts.sort_by_key(|&(_, count)| count);

    let mut removed_elements = 0;

    for (_, count) in sorted_counts.iter() {
        removed_elements += *count;
        if removed_elements > k {
            return sorted_counts.len() as i32 - removed_elements + *count;
        }
    }
    0
}
