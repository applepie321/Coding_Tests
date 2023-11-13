// Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13



fn permute_string(s: String) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    let mut vowel_indices: Vec<usize> = Vec::new();
    let mut vowel_values: Vec<char> = Vec::new();

    for (i, c) in chars.iter().enumerate() {
        if c.to_ascii_lowercase() == 'a' || c.to_ascii_lowercase() == 'e' || c.to_ascii_lowercase() == 'i' || c.to_ascii_lowercase() == 'o' || c.to_ascii_lowercase() == 'u' {
            vowel_indices.push(i);
            vowel_values.push(*c);
        }
    }

    vowel_values.sort();

    for (i, j) in vowel_indices.iter().enumerate() {
        chars[*j] = vowel_values[i];
    }

    chars.into_iter().collect()
}

fn main() {
    let s = String::from("lEetcOde");
    let result = permute_string(s);
    println!("{}", result);
}
