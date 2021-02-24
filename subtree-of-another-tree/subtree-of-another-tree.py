# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check_same(p, q):
            stack = [(p, q)]
            while stack:
                l, r = stack.pop()
                if not l and not r:
                    continue

                if not l or not r:
                    return False

                if l.val != r.val:
                    return False

                stack.append((l.left, r.left))
                stack.append((l.right, r.right))

            return True
        
        nodes = []
        stack = [s]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            nodes.append(node)
            stack.append(node.left)
            stack.append(node.right)
        
        for node in nodes:
            if check_same(node, t):
                return True
            
        return False
        
                
                
            
        
        