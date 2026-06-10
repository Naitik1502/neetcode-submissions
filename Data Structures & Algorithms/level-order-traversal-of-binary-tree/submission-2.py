# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []
        
        res = []
        q = deque()

        q.append((root, 1))

        prev_level = 1
        each_level = []

        while q :


            node, level = q.popleft()

            print(node.val)
            print(level)
            print(prev_level)

            if prev_level < level : 
                res.append(each_level.copy())
                each_level.clear()
                each_level.append(node.val)
                prev_level = level
            else :
                each_level.append(node.val)

            
            if node.left : q.append((node.left, level + 1))
            if node.right : q.append((node.right, level + 1))
        
        if each_level :
            res.append(each_level)
            
        
        return res
           



        