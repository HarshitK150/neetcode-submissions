class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}       # integer -> index

        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_map and i != nums_map[diff]:
                return [i, nums_map[diff]]
        
        return None