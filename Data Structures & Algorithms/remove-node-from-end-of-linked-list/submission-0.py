# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def move(node):
            if not node :
                return None, 0
            node.next, step = move(node.next) 
            step += 1
            if step == n :
                # print("#")
                # print(node.val)
                # print(step)
                
                if not node.next :
                    return None, step
                # print(node.next.val)
                return node.next, step  
            return node, step
        
        return move(head)[0]

        