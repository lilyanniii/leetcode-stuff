# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def height(node1):
            if not node1: return 0

            left = height(node1.left)
            right = height(node1.right)

            if abs(left - right) > 1:
                self.res = False

            return 1 + max(left, right)

        height(root)

        return self.res


