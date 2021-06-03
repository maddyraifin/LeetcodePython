# Reference: https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Sequence = 1221. Split a String in Balanced Strings
# Prepared by - Maddy Rai
import time


class Solution:
    def balancedStringSplit(self, s):
        if len(s) not in range(1, 1001) or (s.replace('L', '').replace('R', '') != ''):
            raise Exception("Unexpected input case.")

        count = 0
        l, r = 0, 0
        for i in s:
            if i == "L":
                l = l + 1
            else:
                r = r + 1

            if l == r:
                count = count + 1
                l, r = 0, 0

        return count


s = "RLRRLLRLRL"

tic = time.perf_counter()
result = Solution.balancedStringSplit(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
