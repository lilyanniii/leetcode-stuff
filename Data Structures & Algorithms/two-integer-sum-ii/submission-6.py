class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while len(result) < 2:
            if left_pointer < right_pointer:
                if numbers[left_pointer] + numbers[right_pointer] == target:
                    result.append(left_pointer + 1)
                    result.append(right_pointer + 1)
                else:
                    right_pointer -= 1
            else:
                left_pointer += 1
                right_pointer = len(numbers) - 1

        return result
            