class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        t, b = 0, len(matrix) - 1

        while t <= b:
            mid = (t + b) // 2

            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                row = mid
            

                l, r = 0, len(matrix[mid]) - 1

                while l <= r:
                    mid_c = (l + r) // 2
                    if target == matrix[mid][mid_c]:
                        return True
                    if target < matrix[mid][mid_c]:
                        r = mid_c - 1
                    elif target > matrix[mid][mid_c]:
                        l = mid_c + 1
                return False
        return False
                
            
            
            
        
