# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Brute Force
        # temp = head
        # stack = []
        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next
        # temp = head
        # while temp is not None:
        #     temp.val = stack.pop()
        #     temp = temp.next
        
        # return head

        #Optimal
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev