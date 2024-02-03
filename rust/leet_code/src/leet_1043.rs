fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
    let n = arr.len();
    let mut dp = vec![0; n + 1];
    for i in 1..n {
        let mut max_val = 0;
        for j in 1..=k.min(i as i32) {
            max_val = max_val.max(arr[i - j as usize]);
            dp[i] = dp[i].max(dp[i - j as usize] + max_val * j);
        }
    }
    dp[n]
}
