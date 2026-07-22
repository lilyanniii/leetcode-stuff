class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        

        while t <= b:
            mid_r = (t+b) // 2

            if matrix[mid_r][-1] < target:
                t = mid_r + 1
            elif matrix[mid_r][0] > target:
                b = mid_r - 1
            else:
                row = mid_r
        
                l, r = 0, len(matrix[mid_r]) - 1
        
                while l <= r:
                    mid_c = (l + r) // 2
                    if matrix[mid_r][mid_c] == target:
                        return True
                    elif matrix[mid_r][mid_c] < target:
                        l = mid_c + 1
                    else:
                        r = mid_c - 1
                return False        
        return False


