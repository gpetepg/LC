# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [(root, 0)]
        ans = 0
        
        while queue:
            node, level = queue.pop(0)
            if node:
                if ans < level + 1:
                    ans += 1
​
                queue.append((node.left, ans))
                queue.append((node.right, ans))
        return ans
        
