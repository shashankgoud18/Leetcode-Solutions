# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        n = 1
        temp = head
        while temp.next:
            n += 1 
            temp = temp.next

        k = k%n
        temp.next = head

        steps = n-k-1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head


       
    