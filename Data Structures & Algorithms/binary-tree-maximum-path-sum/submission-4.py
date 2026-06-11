# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_len = float('-inf')

        def dfs(root, pathsum) :
            nonlocal max_len

            if not root :
                return 0
            
            l_gain = dfs(root.left, pathsum)
            r_gain = dfs(root.right, pathsum)

            new_sub_tree = max(l_gain,0) + max(r_gain,0) + root.val

            l_tree = root.val + max(l_gain,0)

            r_tree = root.val + max(r_gain,0)

            # print('#')
            # print(new_sub_tree, l_tree, r_tree)
            max_len = max(new_sub_tree, l_tree, r_tree, max_len)
            # print(max_len)

            
            # print(root.val)
            # print(l_gain)
            # print(r_gain)
            # print(l_tree)
            # print(r_tree)
            

            return max(l_tree, r_tree)
        
        dfs(root, 0)

        return int(max_len)






        