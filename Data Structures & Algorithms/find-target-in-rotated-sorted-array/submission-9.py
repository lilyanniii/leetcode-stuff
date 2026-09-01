class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                #target is on left or target is on right
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return res