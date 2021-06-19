# Reference: https://leetcode.com/problems/length-of-last-word/
# Sequence = 58. Length of Last Word
# Prepared by - Maddy Rai
import time


class Solution:
    def lengthOfLastWord(self, s):
        if len(s) not in range(1, 10000):
            raise Exception("Length of string is out of range")

        if not s.isalpha():
            if s.find(" ") == -1:
                raise Exception("Input string is not alphabet-only.")

        lss = s.split()
        return len(lss[-1]) if lss else 0


s = "Hello World"

tic = time.perf_counter()
result = Solution.lengthOfLastWord(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

