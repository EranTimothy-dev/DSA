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
    
    def isValid2(self, s:str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    c == ')' and stack[-1] != '(' or \
                    c == ']' and stack[-1] != '[' or \
                    c == '}' and stack[-1] != '{':
                    return False
                stack.pop()
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