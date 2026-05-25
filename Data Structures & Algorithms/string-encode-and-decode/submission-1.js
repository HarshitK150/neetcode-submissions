class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = "";
        for (const str of strs) {
            encoded += String(str.length) + "_" + str
        }

        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const decoded = [];
        let i = 0;
        while (i < str.length) {
            let j = i;
            while (str[j] >= "0" && str[j] <= "9") {
                j++;
            }
            const len = parseInt(str.slice(i, j));
            j++;

            decoded.push(str.slice(j, j+len));
            i = j+len;
        }

        return decoded;
    }
}
