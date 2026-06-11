# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = None

        if p.val > q.val :
            temp = q.val
            q.val = p.val
            p.val = temp
        
        def dfs(root):
            nonlocal res

            if not root :
                return 
            
            if root.val < p.val and root.val < q.val :
                dfs(root.right)
            elif p.val <= root.val <= q.val :
                res = root
            else :
                dfs(root.left)
            return
        
        dfs(root)
        # print(res)
            
        return res

            
                

            


            
            
            
        