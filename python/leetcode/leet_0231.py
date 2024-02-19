# Power of Two
# https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19

def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
