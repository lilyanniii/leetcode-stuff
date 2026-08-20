class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer_p = 0
        nums.sort()
        res = []

        while outer_p < len(nums):
            l, r = outer_p + 1, len(nums) - 1

            if outer_p > 0 and nums[outer_p] == nums[outer_p - 1]:
                outer_p += 1
                continue
                
            while l < r:
                if nums[outer_p] + nums[l] + nums[r] == 0:
                    res.append([nums[outer_p], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[outer_p] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            
            outer_p += 1
        
        return res
            


