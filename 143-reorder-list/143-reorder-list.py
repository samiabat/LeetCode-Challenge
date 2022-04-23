# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        arr = arr[ceil(len(arr)/2):]
        temp = head
        turn = 1
        while arr:
            if turn:
                turn = 0
                top = arr.pop()
                t1 = temp.next
                node = ListNode(top)
                temp.next = node
                node.next = t1
            else:
                turn = 1
            temp = temp.next
        if not n%2:
            if temp:
                temp.next = None
        else:
            if temp:
                if temp.next:
                    temp.next.next = None
                
                
            
                
        