fn subarray_div_by_k(nums: Vec<int>, k: i32) -> i32 {
    let mut prefix_mod = 0;
    let mut result = 0;

    let mut mod_group = vec![0; k as usize];
    mod_group[0] = 1;

    for num in nums {
        prefix_mod = (prefix_mod + num % k + k) % k;
        result += mod_group[prefix_mod as usize];
        mod_group[prefix_mod as usize] += 1;
    }

    result
}
