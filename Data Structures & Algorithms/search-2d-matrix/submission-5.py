class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            mid = (t + b) // 2

            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][-1] < target:
                t = mid + 1
            else:
                row = mid

                l, r = 0, len(matrix[mid]) - 1

                while l <= r:
                    mid_c = (l + r) // 2

                    if matrix[row][mid_c] == target:
                        return True
                    elif matrix[row][mid_c] < target:
                        l = mid_c + 1
                    else:
                        r = mid_c - 1
                
                return False
        
        return False