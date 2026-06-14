# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        

        def bfs(root):

            if not root :
                return []
            
            q = deque()

            q.append((root,0))

            pre_res = defaultdict(list)

            while q :
                level_len = len(q)
                node, d = q.popleft()
                pre_res[d].append(node.val)

                if node.left : q.append((node.left,d-1))
                if node.right : q.append((node.right,d+1))

                for i in range(1, level_len):
                    node, d = q.popleft()
                    pre_res[d].append(node.val)

                    if node.left : q.append((node.left,d-1))
                    if node.right : q.append((node.right,d+1))


            return [sub_list for _, sub_list in sorted(pre_res.items())]
        

        return bfs(root)


