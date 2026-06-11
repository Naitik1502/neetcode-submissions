# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        val = []

        def dfs_inorder(root):
            nonlocal val
            if not root :
                return 
            
            dfs_inorder(root.left)
            val.append(root.val)
            dfs_inorder(root.right)

            return
        dfs_inorder(root)
        
        return val[k-1]




        