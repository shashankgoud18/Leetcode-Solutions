# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstNode = None
        secondNode = None
        length = 0
        curr= head
        while curr:
            length += 1

            if secondNode:
                secondNode = secondNode.next 
            
            if(length==k):
                firstNode = curr
                secondNode = head
            curr = curr.next
        
        firstNode.val, secondNode.val= secondNode.val, firstNode.val
        return head