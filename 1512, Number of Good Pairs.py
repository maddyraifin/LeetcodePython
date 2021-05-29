# Reference: https://leetcode.com/problems/number-of-good-pairs/
# Sequence = 1512. Number of Good Pairs
# Prepared by - Maddy Rai
import time
import itertools
import collections


class Solution:
    def numIdenticalPairs(self, nums):
        if len(nums) not in range(1, 101):
            raise Exception("Unexpected size of input list.")

        if (min(nums) < 1) or (max(nums) > 100):
            raise Exception("Min or Max values exceed the desired range.")

        return int(sum(k * (k - 1) / 2 for k in collections.Counter(nums).values()))


nums = [1,2,3,1,1,3]

tic = time.perf_counter()
result = Solution.numIdenticalPairs(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
