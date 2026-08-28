# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)

        def subTree(node1, node2):
            if not node1: return False

            if sameTree(node1, node2):
                return True

            return subTree(node1.left, node2) or subTree(node1.right, node2) 

        return subTree(root, subRoot)