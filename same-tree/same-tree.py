# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p,q)]
        
        while stack:
            l, r = stack.pop()
            
            if not r and not l:
                continue
                
            if not r or not l:
                return False
            
            if r.val != l.val:
                return False
            
            stack.append((r.left, l.left))
            stack.append((r.right, l.right))
            
            
        return True