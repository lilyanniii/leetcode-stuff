class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in res.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            