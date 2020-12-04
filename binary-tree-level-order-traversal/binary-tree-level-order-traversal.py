# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res, queue = [], [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if not node:
                continue
                
            if len(res) < level + 1:
                res.append([])
                
            res[level].append(node.val)
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        
        return res
        
