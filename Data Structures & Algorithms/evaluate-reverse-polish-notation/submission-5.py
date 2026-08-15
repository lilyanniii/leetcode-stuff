class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        operators = ["+", "-", "*", "/"]

        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:

                if tok == "+":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1 + val2
                elif tok == "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 - val1
                elif tok == "*":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1 * val2
                elif tok == "/":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = int(val2 / val1)
            
                stack.append(res)   
        
        return stack.pop()
