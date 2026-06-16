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
        import heapq
        #Time -> O(n*log(k))
        #Space -> O(k)
        
        dummy = ListNode(0)
        res = []
        i = 0 
        for _, sublist in enumerate(lists):
            head = sublist
            if head :
                heapq.heappush(res, (head.val, i, head))
                i += 1
         
        dummy = tail = ListNode(0)
        
        while res :      
            val,_, curr_node = heapq.heappop(res)   
            tail.next = curr_node
            if curr_node.next :
                heapq.heappush(res, (curr_node.next.val,i, curr_node.next ))
                i += 1
            
            tail = tail.next
            
            
        
        return dummy.next

        
