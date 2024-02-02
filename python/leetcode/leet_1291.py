# Sequential Digits
# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02

def sequentail_digits(low, high):
    result = []
    for digit in range(1, 10):
        num = digit
        next_digit = digit
        while num <= high and next_digit < 10:
            if num >= low:
                result.append(num)
            next_digit += 1
            num = num * 10 + next_digit
    return sorted(result)
