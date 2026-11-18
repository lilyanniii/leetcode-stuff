class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Do again....
        #Create a hash table to store the index of a complement. if complement is not in val, add the current number in the value and pair it with it's index.

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

