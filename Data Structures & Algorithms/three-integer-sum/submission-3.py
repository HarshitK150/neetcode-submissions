from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        
        for i in range(len(nums)):
            target = -nums[i]

            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum < target or i == l:
                    l += 1
                elif currSum > target or i == r:
                    r -= 1
                else:
                    output.add(tuple(sorted((nums[i], nums[l], nums[r]))))
                    l += 1
                    r -= 1

        return [list(triplet) for triplet in output]