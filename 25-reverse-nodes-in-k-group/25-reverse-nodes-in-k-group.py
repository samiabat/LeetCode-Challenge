# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left = 0
        right = k-1
        while right<len(arr):
            t = right
            while left<t:
                arr[left], arr[t]= arr[t],arr[left]
                left+=1
                t-=1
            left = right+1
            right = left+k-1
        arr = arr[::-1]
        head = None
        for i in arr:
            newNode = ListNode(i)
            newNode.next = head
            head = newNode
        return head