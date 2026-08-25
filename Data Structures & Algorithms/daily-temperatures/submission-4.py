class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                val = stack.pop()
                diff = index - val
                res[val] = diff
            stack.append(index)
        
        return res