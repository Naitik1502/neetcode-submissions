# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []

        q = deque([root])
        res = []

        while q :
            len_level = len(q)
            
            each_level = []

            for i in range(len_level):
                node = q.popleft()
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
                each_level.append(node.val)
            
            res.append(each_level)
        
        return res