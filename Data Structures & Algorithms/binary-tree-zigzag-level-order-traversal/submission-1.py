# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []

        q = deque()
        q.append(root)

        every_level = 0
        level = 0
        order = 1
        
        res = []
        while q :
            every_level = len(q)
            level += 1
            
            level_vals = []
            for i in range(every_level):
                
                
                curr = q.popleft()
                level_vals.append(curr.val)
              
                if curr.left :
                    q.append(curr.left)
                if curr.right :
                    q.append(curr.right)
           
                    
            print(level_vals)
            res.append(level_vals) if order == 1 else res.append(level_vals[::-1])
            if order == 1 : order = 0 
            else : order =1

        return res
                
        

            


        