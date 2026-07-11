class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i, item in enumerate(nums):
            val[item] = i
        for i in range(len(nums)):
            target_val = target - nums[i]
            if target_val in val:
                complement_index = val[target_val]
                if complement_index != i:
                    return [i, complement_index]
        
        

        