"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    from collections import deque
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node :
            return None

        q = deque([node])
        root = None

        node_map = {node: Node(node.val)}

        while q :
            curr_node = q.popleft()
            
            
            for nei_node in curr_node.neighbors:
                if  nei_node not in node_map :
                    node_map[nei_node] = Node(nei_node.val)
                    q.append(nei_node)
                
                node_map[curr_node].neighbors.append(node_map[nei_node])
                    
        
        return node_map[node]
            
            

        

        