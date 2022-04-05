# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i = 0
        arr.sort()
        arr = arr[::-1]
        while i<len(arr):
            newNode = ListNode(arr[i])
            newNode.next = head
            head = newNode
            i+=1
        return head
            