# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node :
                return (0,0)
            
            l_rob, l_skip = dfs(node.left)
            r_rob, r_skip = dfs(node.right)

            rob_here = node.val + l_skip + r_skip
            skip_here = max(l_rob, l_skip) + max(r_rob, r_skip)

            return (rob_here, skip_here)
        
        return max(dfs(root))
        





            
            
        dfs(root)

        return max(money_map.values())

            
            

            
