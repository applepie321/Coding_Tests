// 1743. Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/?envType=daily-question&envId=2023-11-10


use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ad_map: HashMap<i32, Vec<i32>> = HashMap::new();

        for pair in adjacent_pairs.iter() {
            ad_map.entry(pair[0]).or_insert(vec![]).push(pair[1]);
            ad_map.entry(pair[1]).or_insert(vec![]).push(pair[0]);
        }

        let start_node = *ad_map.iter().find(|(_, neighbors)| neighbors.len() == 1).unwrap().0;

        let mut nums = Vec::with_capacity(adjacent_pairs.len() + 1);
        nums.push(start_node);

        for _ in 1..=adjacent_pairs.len() {
            let current_node = *nums.last().unwrap();
            let next_node = ad_map.get_mut(&current_node).unwrap().pop().unwrap();
            nums.push(next_node);
            ad_map.get_mut(&next_node).unwrap().retain(|&x| x != current_node);
        }

        nums
    }

}

