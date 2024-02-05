// First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/?envType=daily-question&envId=2024-02-05

use std::collections::HashMap;

fn first_uniq_char(s: String) -> i32 {
    let mut char_count: HashMap<char, i32> = HashMap::new();

    for ch in s.chars() {
        *char_count.entry(ch).or_insert(0) += 1;
    }

    for (i, ch) in s.chars().enumerate() {
        if char_count[&ch] == 1 {
            return i as i32;
        }
    }
    -1
}
