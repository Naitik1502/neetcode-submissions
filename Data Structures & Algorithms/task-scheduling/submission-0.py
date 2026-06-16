class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c_map = Counter(tasks)
        freq = [-c for _, c in c_map.items()]

        heapq.heapify(freq)
        q = deque()
        time = 0
        
        while freq or q :
            time += 1
            if freq :
                most_freq = heapq.heappop(freq)

                most_freq += 1

                if most_freq != 0 :
                    q.append((time+n,most_freq))
            
            if q and q[0][0] == time :
                heapq.heappush(freq, q.popleft()[1])
        
        return time
