# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_len = float('-inf')

        def dfs(root) :
            nonlocal max_len

            if not root :
                return 0
            
            l_gain = max(dfs(root.left),0)
            r_gain = max(dfs(root.right),0)

            new_sub_tree = l_gain + r_gain + root.val

            l_tree = root.val + l_gain

            r_tree = root.val + r_gain

            max_len = max(new_sub_tree, l_tree, r_tree, max_len)
        

            return max(l_tree, r_tree)
        
        dfs(root)

        return int(max_len)






        