# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        valid = True
        def dfs(node, minNum, maxNum):
            nonlocal valid

            if not node or not valid:
                return 

            if not (minNum < node.val < maxNum):
                valid = False
                

            if not valid:
                return


            dfs(node.left, minNum, node.val)
            dfs(node.right, node.val, maxNum)

            return
            

        dfs(root, -math.inf, math.inf)

        return valid
        