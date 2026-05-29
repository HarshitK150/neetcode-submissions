class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0, r = heights.length - 1, output = 0;
        while (l < r) {
            output = Math.max(
                output,
                Math.min(heights[l], heights[r]) * (r - l)
            );

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return output;
    }
}
