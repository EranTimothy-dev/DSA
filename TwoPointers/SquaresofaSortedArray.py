class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
    #    squaredList = [n ** 2 for n in nums]
        left = 0
        right = len(nums) -1
        result = []
       
        while left <= right:
           if nums[left] ** 2 > nums[right] ** 2:
               result.append(nums[left] ** 2)
               left += 1
           else:
               result.append(nums[right] ** 2)
               right += 1
          
               
        result.reverse()
        return result
        












if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    obj = Solution()
    print(obj.sortedSquares(nums))