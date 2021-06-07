# Reference: https://leetcode.com/problems/xor-operation-in-an-array/
# Sequence = 1486. XOR Operation in an Array
# Prepared by - Maddy Rai
import time
import functools


class Solution:
    def xorOperation(self, n, start):
        if n not in range(1, 1001) or start not in range(0, 1001):
            raise Exception("Unexpected inputs.")

        return functools.reduce(lambda x, y: x ^ y, [start + 2*i for i in range(0, n)])


n = 5
start = 0

tic = time.perf_counter()
result = Solution.xorOperation(None, n, start)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
