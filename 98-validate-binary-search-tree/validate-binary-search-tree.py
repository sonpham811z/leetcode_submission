# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, root, min_value, max_value):
        if not root:
            return True
        if root.val <= min_value or root.val >= max_value:
            return False
        
        return self.validate(root.left, min_value, root.val) and self.validate(root.right, root.val, max_value)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_value = 10000000
        min_value = -10000000

        return self.validate(root, float('-inf'), float('inf'))        


    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []

    #     if not root:
    #         return res

    #     if(root.left != None):
    #         leave_left = self.inorderTraversal(root.left)
    #         res.extend(leave_left)

    #     res.append(root.val)

    #     if(root.right != None):
    #         leave_right = self.inorderTraversal(root.right)
    #         res.extend(leave_right)

    #     return res 

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.inorderTraversal(root)

        for i in range(len(res)-1):
            if(res[i] >= res[i+1]):
                return False
            
        return True
