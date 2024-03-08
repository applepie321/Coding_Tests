# Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08


def max_frequency_elements(nums: list[list]) -> int:
    freq = {}
    max_freq = 0
    total_freq = 0

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        i = freq[num]

        if i > max_freq:
            max_freq = i
            total_freq = i

        elif i == max_freq:
            total_freq += i

    return total_freq
