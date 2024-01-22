// Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

fn is_palidrome(s: String) -> bool {
    let answer: String = s
        .char()
        .filter(|c| c.is_ascii_alphanumeric())
        .map(|c| c.to_lowercase().to_string())
        .collect();

    answer == answer.char().rev().collect::<String>()
}
