class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numsMap = new Map();
        for (const num of nums) {
            numsMap.set(num, (numsMap.get(num) || 0) + 1);
        }

        const arr = Array.from({length: nums.length + 1}, () => []);
        for (const [key, val] of numsMap) {
            arr[val].push(key);
        }
        
        const output = [];
        for (const numbers of arr.reverse()) {
            for (const num of numbers) {
                output.push(num);

                if (output.length === k) {
                    return output
                }
            }
        }
        return []
    }
}