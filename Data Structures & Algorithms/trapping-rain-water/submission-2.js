class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let water = 0;
        let lMax = height[0], rMax = height[height.length - 1];
        let l = 0, r = height.length - 1;

        while (l < r - 1) {
            if (lMax < rMax) {
                lMax = Math.max(lMax, height[++l]);
                water += lMax - height[l];
            } else {
                rMax = Math.max(rMax, height[--r]);
                water += rMax - height[r];
            }
        }
        return water;
    }
}
