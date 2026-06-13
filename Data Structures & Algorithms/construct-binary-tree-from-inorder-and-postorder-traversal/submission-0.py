# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        in_map = {val : i for i, val in enumerate(inorder)}
        self.post_ind = len(postorder) - 1

        def build(l, r):
            if l > r :
                return 
            
            # print(self.post_ind)
            mid = in_map[postorder[self.post_ind]]
            self.post_ind -= 1

            node = TreeNode(inorder[mid])
            
            node.right = build(mid+1 , r)
            node.left = build(l, mid-1)
            
            return node
        
        return build(0, len(postorder)-1)
        