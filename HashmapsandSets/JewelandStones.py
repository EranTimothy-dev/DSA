class Solution():
    def numJewelsInStones(self, jewels: str, stones: str)-> int:
        """
        :type jewels: str
        :type stones: str
        :rtype: int

        time complexity: O(n + m); where n is amount of stones
        space complexity: O(n); where n is amount of jewels
        """
        jewelSet = set(jewels)
        count = 0
        
        for stone in stones:
            if stone in jewelSet:
                count += 1
        
        return count