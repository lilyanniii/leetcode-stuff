class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in pairs and stack:
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack