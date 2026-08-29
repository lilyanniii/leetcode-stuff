class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        outer_l = 0

        while outer_l <= len(nums) - 1:
            if outer_l > 0 and nums[outer_l - 1] == nums[outer_l]:
                outer_l += 1
                continue

            l, r = outer_l + 1, len(nums) - 1

            while l < r:
                if nums[outer_l] + nums[l] + nums[r] == 0:
                    res.append([nums[outer_l], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif nums[outer_l] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            
            outer_l += 1
        
        return res
            
