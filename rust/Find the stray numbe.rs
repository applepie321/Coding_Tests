fn stray(arr: &[u32]) -> u32 {
    let mut result = 0;
    for &num in arr {
        result ^= num;
    }
    result
}