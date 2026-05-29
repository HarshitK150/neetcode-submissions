class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);

        const output = [];
        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) {
                continue;
            }

            const target = -nums[i];

            let l = i + 1, r = nums.length - 1;
            while (l < r) {
                const sum = nums[l] + nums[r];
                if (sum < target || 
                    (l > i+1 && nums[l - 1] === nums[l])) {
                    l++;
                } else if (sum > target) {
                    r--;
                } else {
                    output.push([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                }
            }
        }
        return output;
    }
}
