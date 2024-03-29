# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = []
        
        curr = head
        
        while curr:
            if curr in seen:
                return True
            seen.append(curr)
            curr = curr.next
            
        return False
