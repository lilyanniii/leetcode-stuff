# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = collections.deque()

        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                val = queue.popleft()
                if val:
                    queue.append(val.left)
                    queue.append(val.right)
                    level.append(val.val)
            if level:
                res.append(level)
        
        return res