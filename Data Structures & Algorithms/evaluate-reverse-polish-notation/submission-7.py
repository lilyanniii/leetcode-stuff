class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = 0
        stack = []
        operators = ["+", "-", "*", "/"]

        for num in tokens:
            if num not in operators:
                stack.append(int(num))
            else:
                if num == "+":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 + val1
                    
                elif num == "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 - val1
                elif num == "*":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 * val1
                elif num == "/":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = int(val2 / val1)
                
                stack.append(res)
        
        return stack.pop()
