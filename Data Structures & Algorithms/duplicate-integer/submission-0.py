class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_List = {}
        for num in nums:
            if num in number_List:
                return True
            else: 
                number_List[num] = 1
        return False 