# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._helper(root, res)
        return res
        
    def _helper(self, node, res):
        if node:
            self._helper(node.left, res)
            res.append(node.val)
            self._helper(node.right, res)

    