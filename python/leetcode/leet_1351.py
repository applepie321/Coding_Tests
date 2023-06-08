# 1351. Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.


# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0



class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
    	count = 0
        for arr in grid:
    		#the last element is positive or zero, so skip the array
    		if arr[-1]>=0:
    			continue
    		#the first element is negative, so will be the whole array
    		elif arr[0]<0:
    			count += len(arr)
    		else:
    			#otherwise, perform binary search
    			count += self.binary_search(arr, 0, len(arr)-1)
    	return count
    
    def binary_search(self, arr: List[int], l:int, r:int) -> int: 
    	if r >= l: 
    
    		mid = l + (r - l) // 2
    		#if arr[mid] is negative, so will be the following elements
    		#just in case you missed some negative numbers on the left half, conduct a binary search on it as well
    		if arr[mid] <0:
    			return (r-mid+1) + self.binary_search(arr, l, mid-1)
    		#if arr[mid]>=0, all numbers in the left half will either be positive or zero,
    		#so skip that and check the right half
    		else: 
    			return self.binary_search(arr, mid + 1, r) 
    
    	else: 
    		return 0
	



# Source: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/solutions/627321/python-3-using-binary-search-99-39-speed-100-space-with-explanatory-comments/