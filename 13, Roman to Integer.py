# Reference: https://leetcode.com/problems/roman-to-integer/
# Sequence = 13. Roman to Integer
# Prepared by - Maddy Rai
import time


class Solution:
    def romanToInt(self, s):
        if len(s) not in range(1, 16):
            raise Exception("Unexpected size of input string.")

        mapval = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        mapexcp = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        numout = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i] + s[i+1] in mapexcp:
                numout = numout + mapexcp[s[i] + s[i+1]]
                i = i + 1
            else:
                numout = numout + mapval[s[i]]
            i = i + 1

        return numout


s = "IV"

tic = time.perf_counter()
result = Solution.romanToInt(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.romanToInt(None, "III") == 3 else print('Failed!!')
print('Pass') if Solution.romanToInt(None, "IV") == 4 else print('Failed!!')
print('Pass') if Solution.romanToInt(None, "IX") == 9 else print('Failed!!')
print('Pass') if Solution.romanToInt(None, "LVIII") == 58 else print('Failed!!')
print('Pass') if Solution.romanToInt(None, "LIX") == 59 else print('Failed!!')
print('Pass') if Solution.romanToInt(None, "MCMXCIV") == 1994 else print('Failed!!')
