class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, output, maxF = 0, 0, 0
        currMap = {}

        for r in range(len(s)):
            currMap[s[r]] = currMap.get(s[r], 0) + 1
             
            maxF = max(maxF, currMap[s[r]])

            while (r - l + 1) - maxF > k:
                currMap[s[l]] -= 1
                l += 1
            
            output = max(output, r - l + 1)

        return output