# Reference: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Sequence = 1281. Subtract the Product and Sum of Digits of an Integer
# Prepared by - Maddy Rai
import time
import functools


class Solution:
    def subtractProductAndSum(self, n):
        if n not in range(1, 100000):
            raise Exception("Unexpected range of input number.")

        lsint = list(map(int, str(n)))
        return functools.reduce((lambda x, y: x * y), lsint) - sum(lsint)


nums = 8113

tic = time.perf_counter()
result = Solution.subtractProductAndSum(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
