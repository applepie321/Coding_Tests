# Constrained Subsequence Sum
# https://leetcode.com/problems/constrained-subsequence-sum/description/?envType=daily-question&envId=2023-10-21

# Solution
# https://leetcode.com/problems/constrained-subsequence-sum/solutions/4191024/92-31-sliding-window-with-a-deque/?envType=daily-question&envId=2023-10-21

"""
주어진 정수 배열 nums와 정수 k가 있을 때, 
조건 j - i <= k가 만족되는 배열의 연속된 두 정수 
nums[i]와 nums[j] (여기서 i < j) 간의 비연속 부분 배열의 최대 합을 반환합니다. 
배열의 부분 배열은 배열에서 일정한 수의 요소 (0개일 수도 있음)를 
제거하여 남은 요소를 원래 순서대로 가져온 것입니다.
"""


from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            nums[i] += nums[dq[0]] if dq else 0
            
            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()
                
            if nums[i] > 0:
                dq.append(i)
                
        return max(nums)
