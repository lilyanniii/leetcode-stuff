class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        triplet = []
        outer_p = 0

       

        while outer_p < len(nums):
            if outer_p > 0 and nums[outer_p] == nums[outer_p - 1]:
                outer_p += 1
                continue

            l, r = outer_p + 1, len(nums) - 1

            while l < r:
                if nums[outer_p] + nums[l] + nums[r] == 0:
                    triplet = nums[outer_p], nums[l], nums[r]
                    results.append(triplet)
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[outer_p] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

            outer_p += 1
        
        return results
                

        