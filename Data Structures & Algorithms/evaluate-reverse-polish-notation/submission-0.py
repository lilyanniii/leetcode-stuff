class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0

        curr_value = 0

        stack = []
        operators = ["+", "-" , "/", "*"]

        for x in tokens:
            if x not in operators:
                stack.append(int(x))
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                operator = x
                if operator == "+":
                    curr_value = first_value + second_value
                elif operator == "*":
                    curr_value = first_value * second_value
                elif operator == "-":
                    curr_value = first_value - second_value
                elif operator == "/":
                    curr_value = int(first_value / second_value)
                stack.append(curr_value)
        
        return stack.pop()