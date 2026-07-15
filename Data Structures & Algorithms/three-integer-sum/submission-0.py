class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = []
        triplet = []

        outer_pointer = 0

        while outer_pointer <= len(nums):
            two_p_left = outer_pointer + 1
            two_p_right = len(nums) - 1

            while two_p_left < two_p_right:
                sum = nums[outer_pointer] + nums[two_p_left] + nums[two_p_right]

                if sum == 0:
                    triplet = [nums[outer_pointer], nums[two_p_left], nums[two_p_right]]
                    triplet.sort()
                    if triplet not in results:
                        results.append(triplet)
                        two_p_left += 1
                        two_p_right -= 1
                    else:
                        two_p_left += 1
                        two_p_right -= 1
                elif sum > 0:
                    two_p_right -= 1
                elif sum < 0:
                    two_p_left += 1
                
                    
            
            outer_pointer += 1

        return results
