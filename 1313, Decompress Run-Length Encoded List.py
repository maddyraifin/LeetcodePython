
# Reference: https://leetcode.com/problems/decompress-run-length-encoded-list/
# Sequence = 1313. Decompress Run-Length Encoded List
# Prepared by - Maddy Rai
import time
import itertools


class Solution:
    def decompressRLElist(self, nums):
        if len(nums) not in range(2, 101):
            raise Exception("Unexpected size of input list.")

        if len(nums) % 2 != 0:
            raise Exception("Size of input list not divisible by 2.")

        if (min(nums) < 1) or (max(nums) > 100):
            raise Exception("Min or Max values exceed the desired range.")

        return list(itertools.chain.from_iterable([nums[2*i+1]] * nums[2*i] for i in range(0, int(len(nums)/2))))


nums = [1,1,2,3]

tic = time.perf_counter()
result = Solution.decompressRLElist(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
