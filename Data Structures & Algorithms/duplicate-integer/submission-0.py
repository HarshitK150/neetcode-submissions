class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        seen = set()
        for element in nums:
            if element in seen:
                return True
            else:
                seen.add(element)
        return False