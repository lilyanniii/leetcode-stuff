class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = 0

        stack = []
        operators = ["+", "-", "/", "*"]


        for num in tokens:
            if num not in operators:
                stack.append(int(num))
            else:
                if num == "+":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    res = val1 + val2
                elif num == "-":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    res = val1 - val2
                elif num == "/":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    res = int(val1 / val2)
                elif num == "*":
                    val2 = stack.pop()
                    val1 = stack.pop()
                    res = val1 * val2
                stack.append(res)
            
        return stack.pop()
