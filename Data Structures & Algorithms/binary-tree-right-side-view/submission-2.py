class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            last_val = None
            for i in range(len(queue)):
                node = queue.popleft()
                last_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(last_val)
        
        return result