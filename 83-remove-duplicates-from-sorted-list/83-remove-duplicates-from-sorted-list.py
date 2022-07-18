# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return 
        temp = head
        current_val = temp.val
        while temp.next:
            if current_val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
                current_val = temp.val
        return head