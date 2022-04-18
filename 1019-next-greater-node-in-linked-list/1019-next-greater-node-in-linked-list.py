# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp= temp.next
        ans = [0]*count
        i=0
        
        
        
        temp = head
        stack = []
        
        while temp:
            count = 0
            if not stack or temp.val<stack[-1][1]:
                stack.append((i, temp.val))
            else:
                while stack and temp.val>stack[-1][1]:
                    ans[stack[-1][0]]=temp.val
                    stack.pop()
            stack.append((i, temp.val))
            temp = temp.next
            i+=1
        return ans