# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res, path, stack = [], [], [(root, 0)]
        
        while stack:
            node, _sum = stack.pop()
            
            if not node:
                continue
            
            path.append(node.val)
            _sum += node.val
            
            if not node.left and not node.right:
                res.append(_sum)
                _sum -= node.val
            
            stack.append((node.left, _sum))
            stack.append((node.right, _sum))
            
        print(res)
            
        if sum in res:
            return True
        
        return False
        
