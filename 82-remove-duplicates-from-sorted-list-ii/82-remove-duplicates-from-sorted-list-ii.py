# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr = arr[::-1]
        dic = Counter(arr)
        head = None
        for key in dic:
            if dic[key]==1:
                newNode = ListNode(key)
                newNode.next = head
                head = newNode
        return head
            