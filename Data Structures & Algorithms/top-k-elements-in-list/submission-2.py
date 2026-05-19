import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        largest_freq = 0
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            largest_freq = max(largest_freq, frequency[num])

        bucket = [[] for i in range(largest_freq + 1)]

        for key, val in frequency.items():
            bucket[val].append(key)

        output = []
        for j in reversed(bucket):
            for m in j:
                output.append(m)
                if len(output) == k:
                    return output

        return None