import sys


class Solution():
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0] 
           # loop through the list and find the smallest positive/absolute value
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        # check if both the positive and negative values are present in the list
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
        # time: O(n)
        # space: O(1)
    
    def fasterSolution(self, nums: list[int]) -> int:
        closest= nums[0]

        for x in range(1, len(nums)):
            if abs(nums[x]) < abs(closest) or (abs(nums[x]) == abs(closest) and nums[x] > closest):
                closest = nums[x]
        
        return closest