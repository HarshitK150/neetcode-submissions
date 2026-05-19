class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if num in nums_map:
                nums_map[num].append(i)
            else:
                nums_map[num] = [i]

        for i, num in enumerate(nums):
            if (target - num) in nums_map:
                indices = nums_map[target - num]
                if i != indices[0]:
                    return sorted([i, indices[0]])
                elif len(indices) > 1:
                    return sorted([i, indices[1]])