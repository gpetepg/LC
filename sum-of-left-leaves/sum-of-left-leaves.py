# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Leaf has no left or right
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
        
