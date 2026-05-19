class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            letters = [0] * 26
            for c in word:
                letters[ord(c) - ord('a')] += 1
            
            if tuple(letters) in groups:
                groups[tuple(letters)].append(word)
            else:
                groups[tuple(letters)] = [word]

        return list(groups.values())