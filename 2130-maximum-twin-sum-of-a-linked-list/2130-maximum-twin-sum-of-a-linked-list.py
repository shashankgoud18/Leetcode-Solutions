# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        temp = head
        result = 0
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next 
        
        curr = head
        while curr:
            total = curr.val + stack.pop()
            curr = curr.next 

            result = max(total,result)
        
        return result