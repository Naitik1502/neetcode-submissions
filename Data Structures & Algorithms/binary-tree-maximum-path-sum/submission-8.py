# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root :
            return 0


        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum

            if not root :
                return 0 
            
            l_gain = max(dfs(root.left),0)
            r_gain = max(dfs(root.right),0)

            max_sum =  max(root.val + l_gain + r_gain, max_sum)

            return root.val + max(l_gain, r_gain)
        
        dfs(root)

        return max_sum