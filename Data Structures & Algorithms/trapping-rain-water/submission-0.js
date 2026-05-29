class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const left = new Array(height.length).fill(0);
        const right = new Array(height.length).fill(0);

        for (let i = 1; i < height.length; i++) {
            left[i] = Math.max(left[i - 1], height[i - 1]);
        }

        for (let i = height.length - 2; i >= 0; i--) {
            right[i] = Math.max(right[i + 1], height[i + 1]);
        }

        let output = 0;
        for (let i = 0; i < height.length; i++) {
            if (height[i] <= left[i] && height[i] <= right[i]) {
                output += Math.min(left[i], right[i]) - height[i];
            }
        }
        return output;
    }
}
