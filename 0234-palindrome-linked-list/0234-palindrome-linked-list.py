# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next 
        temp = head
        while temp:
            if temp.val == stack.pop():
                temp = temp.next
            else:
                return False
        return True