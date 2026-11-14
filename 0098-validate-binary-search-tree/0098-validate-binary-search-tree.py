# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, maxi = float("inf"), mini = float("-inf")) -> bool:
        if not root:
            return True

        if not mini < root.val < maxi:
            return False
        
        return self.isValidBST(root.left, root.val, mini) and self.isValidBST(root.right, maxi,root.val)