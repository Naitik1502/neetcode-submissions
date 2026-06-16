from _heapq import heapify
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        res = []
        for inter in intervals:
            s = inter.start
            e = inter.end
            heapq.heappush(res, (s,e))

        prev = [] 
        meetingroom = 0

        while res :
            print(prev)
            s, e = heapq.heappop(res)
            if not prev :
                meetingroom += 1
                heapq.heappush(prev, e)
                continue
            
            fast_ending = heapq.heappop(prev)

            if s >= fast_ending :
                heapq.heappush(prev, e)
            
            else :
                meetingroom += 1
                heapq.heappush(prev, fast_ending)
                heapq.heappush(prev, e)

        return meetingroom

        





        