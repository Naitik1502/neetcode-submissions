# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total = 0

        def dfs(root, s):
            nonlocal total
            if not root :
                return
            
            s += str(root.val)

            if root.left == None and root.right == None :
                total += int(s)
            

            dfs(root.left, s)
            dfs(root.right, s)

            s = s[:-1]

            return
        
        dfs(root, "")

        return total



        