class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }
        
        const sMap = new Map();
        const tMap = new Map();

        for (const c of s) {
            sMap.set(c, (sMap.get(c) || 0) + 1);
        }

        for (const c of t) {
            tMap.set(c, (tMap.get(c) || 0) + 1);
        }

        for (const [key, val] of sMap) {
            if (!tMap.has(key) || tMap.get(key) !== val) {
                return false;
            }
        }

        return true;
    }
}
