class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupMap = new Map();

        for (const str of strs) {
            const chars = new Array(26).fill(0);
            for (const c of str) {
                chars[c.charCodeAt(0) - "a".charCodeAt(0)]++;
            }

            const charsStr = chars.join(",");
            if (groupMap.has(charsStr)) {
                groupMap.get(charsStr).push(str);
            } else {
                groupMap.set(charsStr, [str]);
            }
        }

        return [...(groupMap.values())];
    }
}
