class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        
        for curr_index, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_index = stack.pop()
                difference = curr_index - prev_index

                results[prev_index] = difference

            stack.append(curr_index)
        return results