# Reference: https://leetcode.com/problems/shuffle-string/
# Sequence = 1528. Shuffle String
# Prepared by - Maddy Rai
import time
import functools


class Solution:
    def restoreString(self, s, indices):
        if len(indices) not in range(1, 101):
            raise Exception("Unexpected size of indices list.")

        if len(s) != len(indices):
            raise Exception("String and indices size do not match.")

        if (min(indices) < 0) or (max(indices) > 100):
            raise Exception("Min or Max values exceed the desired range.")

        if not s.islower():
            raise Exception("string has uppercase letters.")

        if sorted(indices) != list(range(0, len(indices))):
            raise Exception("Unexpected indices.")

        sortidx = sorted(indices)
        return ''.join([s[indices.index(x)] for x in sortidx])


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

tic = time.perf_counter()
result = Solution.restoreString(None, s, indices)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
