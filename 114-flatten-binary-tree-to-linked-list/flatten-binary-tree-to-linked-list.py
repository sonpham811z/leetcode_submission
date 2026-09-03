# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root: Optional[TreeNode], list_nodes):
        if not root:
            return
        list_nodes.append(root)
        self.preOrder(root.left, list_nodes)
        self.preOrder(root.right, list_nodes)

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        nodes= []
        self.preOrder(root, nodes)

        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        nodes[-1].left = None
        nodes[-1].right = None
        
        
        