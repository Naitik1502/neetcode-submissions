class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(p1, p2):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
           
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        res = []

        for point in points:
            heapq.heappush(res, (distance(point, [0,0]), point))
        final = []
        for i in range(k):
            final.append(heapq.heappop(res)[-1])
        return final

        