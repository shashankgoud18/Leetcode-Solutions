
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        stack1 = []
        stack2 = []
        temp1 = l1
        temp2 = l2 

        while temp1 is not None:
            stack1.append(temp1.val)
            temp1 = temp1.next 
        
        while temp2 is not None:
            stack2.append(temp2.val)
            temp2 = temp2.next
        
        carry = 0

        while stack1 or stack2 or carry:
            total = carry
            total += (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0)
            digit = total%10
            carry = total // 10

            new_node = ListNode(digit)
            new_node.next = dummy.next
            dummy.next = new_node
        if carry > 0:
            new_node = ListNode(carry)
            new_node.next = dummy.next
            dummy.next = new_node
        
        return dummy.next