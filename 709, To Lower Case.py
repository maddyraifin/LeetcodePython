# Reference: https://leetcode.com/problems/to-lower-case/
# Sequence = 709. To Lower Case
# Prepared by - Maddy Rai
import time


class Solution:
    def toLowerCase(self, s):
        if len(s) not in range(1, 101):
            raise Exception("Unexpected inputs.")

        return s.lower()


s = "Hello"

tic = time.perf_counter()
result = Solution.toLowerCase(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
