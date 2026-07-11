class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            if c == ")":
                if not stack: 
                    return False
                top_of_stack = stack[-1]
                if top_of_stack == "(":
                    stack.pop()
                else: 
                    return False
            if c == "}":
                if not stack:
                    return False
                top_of_stack = stack[-1]
                if top_of_stack == "{":
                    stack.pop()
                else: return False
            if c == "]":
                if not stack:
                    return False
                top_of_stack = stack[-1]
                if top_of_stack == "[":
                    stack.pop()
                else: 
                    return False

        if len(stack) > 0:
            return False
        
        return True