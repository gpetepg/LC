# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # DFS
        
        stack = [(root, False)]
        left_sum = 0
        
        while stack:
            node, is_left = stack.pop()
            
            if not node:
                continue
            
            if not node.left and not node.right:
                if is_left:
                    left_sum += node.val
                    
            stack.append((node.left, True))
            stack.append((node.right, False))
            
        return left_sum