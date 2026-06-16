class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import random
        distance = []

        for point in points :
            x1 = point[0]
            y1 = point[1]
            x2 = 0
            y2 = 0 

            distance.append((x1 - x2)**2 + (y1 - y2)**2)
        

        def partition(low,high):
            p = random.randrange(low,high)

            distance[p], distance[high] = distance[high], distance[p]
            points[p], points[high] = points[high], points[p]

            store = low

            for i in range(low,high):
                if distance[i] <= distance[high]:
                    distance[store], distance[i] = distance[i], distance[store]
                    points[store], points[i] = points[i], points[store]
                    store += 1
            
            distance[high], distance[store] = distance[store], distance[high]
            points[high], points[store] = points[store], points[high]

            return store
        
       
        l, h = 0 , len(points)-1
        p = None
        while l < h :
            p = partition(l, h)
        
            if k > p :
                l = p + 1
            elif k < p :
                h = p - 1
            
            else :
                break
        
        return points[:k]
            
            

            

                    

        