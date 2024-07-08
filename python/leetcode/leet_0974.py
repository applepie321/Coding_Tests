def sub_array_div_by_k(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix_mod, result = 0, 0

    mod_group = [0] * k
    mod_group[0] = 1

    for num in nums:
        prefix_mod = (prefix_mod + num % k + k) % k
        result += mod_group[prefix_mod]
        mod_group[prefix_mod] += 1

    return result
