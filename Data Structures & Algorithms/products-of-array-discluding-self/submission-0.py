class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n

        for i in range(n):
            if i > 0:
                prefix[i] *= prefix[i-1] * nums[i-1]
            
            if ((n - 1) - i) < n - 1:
                postfix[(n - 1) - i] *= postfix[n-i] * nums[n-i]

        return [prefix[i] * postfix[i] for i in range(n)]