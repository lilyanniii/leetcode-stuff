class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #choices: all numbers in nums
        #constraint: numbers must sum to target
        #base case: when sum == target
        #backtrack step: pop the last num from path(undo choice)
        #prune: if sum > target, don't recurse further down this branch

        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j, cur, total + nums[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return res