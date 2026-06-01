from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, output = 0, 0
        currMap = defaultdict(int)

        for r in range(len(s)):
            currMap[s[r]] += 1

            maxFreq = max(currMap.values())
            while (r - l + 1) - maxFreq > k:
                currMap[s[l]] -= 1
                l += 1
                maxFreq = max(currMap.values())
            
            output = max(output, r - l + 1)

        return output