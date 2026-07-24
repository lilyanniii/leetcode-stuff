class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuple_array = list(zip(position, speed))
        ordered_arr = sorted(tuple_array, reverse=True)
        stack = []

        for pos, speed in ordered_arr:
            meet_point = (target - pos) / speed

            if not stack or meet_point > stack[-1]:
                stack.append(meet_point)
            
        return len(stack)
