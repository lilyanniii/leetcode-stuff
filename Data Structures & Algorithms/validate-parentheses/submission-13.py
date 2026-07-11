class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        parentheses_pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c == ")" or c == "}" or c == "]":
                if not stack:
                    return False
                top_pair = stack[-1]
                if top_pair == parentheses_pairs[c]:
                    stack.pop()
                else:
                    return False
            
            if c not in parentheses_pairs:
                stack.append(c)
        
        if not stack:
            return True
        
        return False
                