// 7 kyu
// Search for letters
// https://www.codewars.com/kata/52dbae61ca039685460001ae/rust

fn change(string: &str) -> String {
    let mut result = String::with_capacity(26);

    for ch in 'a'..='z' {
        let present = string
            .chars()
            .any(|c| c == ch || c == ch.to_ascii_uppercase());

        result.push(if present { '1' } else { '0' });
    }

    result
}
