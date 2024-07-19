# Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/?envType=daily-question&envId=2024-07-19

def lucky_numbers(matrix: list[list[int]]) -> list[int]:
    min_in_row = [min(row) for row in matrix]
    max_in_col = [max(col) for col in zip(*matrix)]

    lucky_numbers = []
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == min_in_row[i] and num == max_in_col[j]:
                lucky_numbers.append(num)

    return lucky_numbers
