# Number of Sumbatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/?envType=daily-question&envId=2024-01-28

def num_submatrix(matrix, target):
    def sub_array(nums, k):
        count = 0
        prefix_sum = {0: 1}
        current_sum = 0
        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count

    m, n = len(matrix), len(matrix[0])
    result = 0
    for i in range(m):
        pre_sum = [0] * n
        for j in range(i, m):
            for k in range(n):
                pre_sum[k] += matrix[j][k]
            result += sub_array(pre_sum, target)
    return result


# test
# matrix = [[0,1,0],[1,1,1],[0,1,0]]
# target = 0
