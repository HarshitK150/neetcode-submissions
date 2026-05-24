class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numsMap = new Map();

        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i];
            if (numsMap.has(diff)) {
                return [numsMap.get(diff), i];
            } else {
                numsMap.set(nums[i], i);
            }
        }
        return []
    }
}
