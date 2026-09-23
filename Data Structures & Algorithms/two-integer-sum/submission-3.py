class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        res = []

        for i, value in enumerate(nums):
            complement = target - nums[i]

            if complement not in val:
                val[nums[i]] = i
            else:
                res.append(val[complement])
                res.append(i)
        
        return res