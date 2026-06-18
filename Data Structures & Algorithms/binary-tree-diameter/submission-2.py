# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        
        def dfs(root, pathsum):
            nonlocal diameter
            if not root :
                return 0
            
            path_left = dfs(root.left, pathsum + 1) 
            path_right = dfs(root.right, pathsum + 1) 


            diameter = max(diameter,path_left + path_right)

            return max(path_left, path_right) + 1
        
        dfs(root, 0)

        return diameter



