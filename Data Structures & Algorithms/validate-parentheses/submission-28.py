class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        values = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in values and stack:
                if stack.pop() != values[c]:
                    return False
            else:
                stack.append(c)
        

        return not stack


