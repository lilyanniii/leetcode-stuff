class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()
        start_interval = intervals[0]
        check_interval = start_interval[1]

        for start, end in intervals[1:]:
            if check_interval > start:
                res += 1
                if check_interval > end:
                    check_interval = end
            else:
                check_interval = end

        return res    

        #sort the array (DONE)

        #compare the end of the first element to the beginning of the second element, if end > beginning, add 1 to result. (DONE)

        #after the initial comparison, check the value of the next element, if start of it is >= to the end of the check, move the new check to the new element and check the following elements after that