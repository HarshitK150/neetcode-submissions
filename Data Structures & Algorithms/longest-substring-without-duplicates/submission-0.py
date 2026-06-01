class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        currSet = set()
        l, output = 0, 0

        for r in range(len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1

            currSet.add(s[r])
            output = max(output, len(currSet))
            
        return output