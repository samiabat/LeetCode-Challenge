# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        arr = sorted(arr)[::-1]
        head = None
        for i in arr:
            newNode = ListNode(i)
            newNode.next = head
            head = newNode
        return head
        