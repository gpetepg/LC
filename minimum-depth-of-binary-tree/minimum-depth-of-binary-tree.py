# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        res, queue = 0, [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if not node:
                continue
                
            if res < level + 1:
                res += 1
                
            if not node.left and not node.right:
                return res
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        
