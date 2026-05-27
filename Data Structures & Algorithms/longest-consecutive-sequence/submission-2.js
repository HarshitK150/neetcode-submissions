class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numsSet = new Set(nums);
        let output = 0;

        for (let num of numsSet) {
            if (!numsSet.has(num - 1)) {
                let length = 1;
                while (numsSet.has(++num)) {
                    length++;
                }

                output = Math.max(output, length);
            }
        }
        return output;
    }
}
