# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0


        def dfs(node):
            nonlocal max_d
            if node is None:
                return 0
            
            l1 = dfs(node.left)
            l2 = dfs(node.right)

            max_d = max(max_d, l1+l2)

            return max(l1,l2)+1
        
        dfs(root)
        return max_d
        