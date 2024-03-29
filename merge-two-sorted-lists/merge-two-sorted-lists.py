# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            
        answer = ListNode()
        temp = answer

        while l1 and l2:

            if l1.val > l2.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next

            else:
                temp.next = ListNode(l1.val)
                l1 = l1.next

            temp = temp.next

        temp.next = l1 or l2
        return answer.next