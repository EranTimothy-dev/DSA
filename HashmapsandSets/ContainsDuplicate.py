class Solution:
    def containDuplicate(self, nums: list) -> bool:
        """ 
        :type nums: List[int]
        :rtype: bool
        """
        # time complecity: O(n) for both worst case and best case
        # space complexity: O(n + m); where n is the list nums and m is the set elements
        elements = set(nums)
        
        if len(elements) < len(nums):
            return True
        else:
            return False
            
    def containDuplicateMethod2(self, nums: list) -> bool:
        
        s = set()
        
        for number in nums:
            if number in s:
                return True
            s.add(number)
        return False

        
        
if __name__ == "__main__":
    nums = [1,2,3,1]
    obj = Solution()
    print(obj.containDuplicate(nums))