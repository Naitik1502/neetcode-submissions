class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = [(-v, k) for k, v in freq.items()]
        heapq.heapify(freq)

        res = []

        while k :
            _, element = heapq.heappop(freq)
            res.append(element)
            k -= 1

        return res