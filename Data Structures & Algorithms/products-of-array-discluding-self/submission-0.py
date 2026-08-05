class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 0

        output = []

        while l <= len(nums) - 1:
            sum = 1
            r = 0
            while r <= len(nums) - 1:
                if r == l:
                    r += 1
                else:
                    sum *= nums[r]
                    r += 1
            output.append(sum)
            l += 1
        
        return output
            

            