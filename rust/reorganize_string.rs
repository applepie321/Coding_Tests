// https://leetcode.com/problems/reorganize-string/description/



//https://leetcode.com/problems/reorganize-string/solutions/3947780/100-2-approaches-priority-queue-sort/





// Approach 1: Priority Queue Approach
use std::cmp::Reverse;

impl Solution {
    pub fn reorganize_string(s: String) -> String {
        let mut freq_map = HashMap::new();
        for c in s.chars() {
            *freq_map.entry(c).or_insert(0) += 1;
        }

        let mut max_heap: BinaryHeap<(i32, char)> = BinaryHeap::new();
        for (&ch, &freq) in freq_map.iter() {
            max_heap.push((freq, ch));
        }

        let mut res = Vec::new();
        while max_heap.len() >= 2 {
            let (freq1, char1) = max.heap.pop().unwrap();
            let (freq2, char2) = max_heap.pop().unwrap();
            
            res.push(char1);
            res.push(char2);

            if freq1 > 1 { max_heap.push((freq1 - 1, char1)); }
            if freq1 > 1 { max_heap.push((freq2 - 1, char2)); }
        }

        if let Some((freq, ch)) = max_heap.pop() {
            if freq > 1 {
                return "".to_string();
            }
            res.push(ch);
        }

        let result: String = res.into_iter().collect();
        result

        
    }
}





// Approach 2: Array Sort Approach
use std::collections::HashMap;

impl Solution {
    pub fn reorganize_string(s: String) -> String {
        let mut freq_map: HashMap<char, usize> = HashMap::new();
        for c in s.chars() {
            *freq_map.entry(c).or_insert(0) += 1;
        }

        let mut sorted_chars: Vec<char> = freq_map.keys().cloned().collect();
        sorted_chars.sort_by_key(|&c| std::cmp::Reverse(freq_map[&c]));

        if freq_map[&sorted_chars[0]] > (s.len() + 1) / 2 {
            return "".to_string();
        }

        let mut res = vec![' '; s.len()];
        let mut i = 0;
        for &c in sorted_chars.iter() {
            for _ in 0..freq_map[&c] {
                if i >= s.len() {
                    i = 1;
                }
                res[i] = c;
                i += 2;
            }
        }

        res.iter().collect()
    }
}