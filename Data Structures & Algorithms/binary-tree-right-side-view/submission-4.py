# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)

        res = []
        
        while q :
            len_level = len(q)

            for i in range(0, len_level):
                curr_node = q.popleft()

                if curr_node and i == 0 :
                    res.append(curr_node.val)

                if curr_node and curr_node.right :
                    q.append(curr_node.right)
                if curr_node and curr_node.left :
                    q.append(curr_node.left)
        
        return res


        