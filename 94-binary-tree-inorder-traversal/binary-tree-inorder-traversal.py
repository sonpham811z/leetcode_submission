# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        if(root.left != None):
            leave_left = self.inorderTraversal(root.left)
            res.extend(leave_left)

        res.append(root.val)

        if(root.right != None):
            leave_right = self.inorderTraversal(root.right)
            res.extend(leave_right)

        return res 