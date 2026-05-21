from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsMap = defaultdict(list)
        output = set()

        for i, num in enumerate(nums):
            numsMap[num].append(i)

        for i in range(len(nums)):
            target = -nums[i]

            for j in range(i+1, len(nums)):
                if (target - nums[j]) in numsMap:
                    indices = numsMap[target - nums[j]]

                    k = 0
                    while k < len(indices) and (indices[k] == i or indices[k] == j):
                            k += 1

                    if k < len(indices):
                        output.add(tuple(sorted([nums[i], nums[j], nums[indices[k]]])))
        
        return [list(triplet) for triplet in output]