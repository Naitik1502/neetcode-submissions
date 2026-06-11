# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root :
            return []
        
        q = deque([root])
        level = 0 
        right_most = []

        while q :
            level += 1
            len_level = len(q)
            
            for i in range(len_level):
                node = q.popleft()
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
                if i == len_level - 1 :
                    right_most.append(node.val)
        
        return right_most

            




