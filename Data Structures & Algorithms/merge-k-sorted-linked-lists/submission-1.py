# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return 
        if lists == [[]]:
            return 
        
        dummy = ListNode(0)
        res = []
        i = 0 
        for _, sublist in enumerate(lists):
            head = sublist
            while head :
                # print(head.val)
                res.append((head.val, i, ListNode(head.val)))
                head = head.next
                i += 1
        
        heapq.heapify(res)
        # print(res)
        prev = ListNode(0)

        i = 0
        
        while res :
            # print(heapq.heappop(res))
            _,_, curr_node = heapq.heappop(res)
            # print(curr_node.val)
            prev.next = curr_node
            if i == 0 :
                dummy = ListNode(0, curr_node)
                i += 1
            prev = prev.next
        
        return dummy.next

        
