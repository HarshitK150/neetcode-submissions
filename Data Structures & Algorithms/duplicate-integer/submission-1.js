class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsSet = new Set()
        for (const n of nums) {
            if (numsSet.has(n)) {
                return true
            } else {
                numsSet.add(n)
            }
        }
        return false
    }
}
