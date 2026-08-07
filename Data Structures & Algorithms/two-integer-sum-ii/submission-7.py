class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        l, r = 0, len(numbers) - 1



        while len(result) < 2:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                result.append(l + 1)
                result.append(r + 1)
            
        return result
            