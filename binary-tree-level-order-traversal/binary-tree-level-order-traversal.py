# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        # left to right so we want BFS
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            if not node:
                continue
                
            if level + 1 > len(res):
                res.append([])
                
            res[level].append(node.val)
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
            
        return res
            