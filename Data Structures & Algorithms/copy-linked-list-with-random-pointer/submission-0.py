"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        dummy = Node(0, head)
        dummy = dummy.next

        orig_to_new_mapping = {}

        while dummy :
            new_node = Node(dummy.val)
            orig_to_new_mapping[dummy] = new_node
            dummy = dummy.next
        
        dummy = Node(0, head)
        dummy = dummy.next

        while dummy :
            orig_to_new_mapping[dummy].next = orig_to_new_mapping.get(dummy.next)
            orig_to_new_mapping[dummy].random = orig_to_new_mapping.get(dummy.random)
            dummy = dummy.next

        return orig_to_new_mapping[head]
        

        



        