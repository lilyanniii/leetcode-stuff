class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i, (start, end) in enumerate(intervals):

            if end < newInterval[0]:
                output.append([start, end])
            elif start > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        output.append(newInterval)
            
        return output