class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)

        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:

                val = stack.pop()
                diff = index - val
                results[val] = diff
            
            stack.append(index)
            

        return results