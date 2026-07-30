class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r-l
            height = min(heights[l], heights[r])
            container_w = width * height

            if container_w > max_w:
                max_w = container_w
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
            
        return max_w
            