class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #choices - all the other numbers
        #constraints - if i ever goes out of bounds
        #base case - if the total >= target
        #backtrack - ignore the number 
        candidates.sort()
        res = []
        combo = []

        def dfs(start, current_sum):

            if current_sum == target:
                res.append(combo.copy())
                return

            for j in range(start, len(candidates)):
                if current_sum + candidates[j] > target:
                    break
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                
                combo.append(candidates[j])
                dfs(j + 1, current_sum + candidates[j])
                combo.pop()

        
        dfs(0, 0)
        return res