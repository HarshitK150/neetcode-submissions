import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        heap = []
        for key, v in frequency.items():
            heap.append((-v, key))

        heapq.heapify(heap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output