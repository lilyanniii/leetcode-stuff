class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0

        l = 0

        while l < len(heights):
            r = len(heights) - 1
            while r > l:
                width = r - l
                height = min(heights[l], heights[r])

                contain_w = width * height

                if contain_w > max_w:
                    max_w = contain_w
                r -= 1
            l += 1
        
        return max_w