class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []


        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        for c in s:
            if c in pairs and stack:
                val = stack.pop()
                if val != pairs[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack