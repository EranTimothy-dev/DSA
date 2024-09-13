class Solution:
    def isValid(self, s:str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else:
                if not stack or hashmap[bracket] != stack.pop():
                    return False

        return not stack
    
    
    
if __name__ == "__main__":
    s = "()[]{}"
    d = "()[{}]"
    e = "([{}])"
    f = "({)}"
    obj = Solution()
    print(obj.isValid(s))
    print(obj.isValid(d))
    print(obj.isValid(e))
    print(obj.isValid(f))