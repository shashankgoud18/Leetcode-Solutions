# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])

        ans = []
        zigzag = False
        while q:
            length = len(q)
            level = []

            for i in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                level.append(node.val)
            if zigzag:
                ans.append(level[::-1])
            else:
                ans.append(level)
            zigzag = not zigzag   
        
        return ans

        