# Reference: https://leetcode.com/problems/third-maximum-number/
# Sequence = 414. Third Maximum Number
# Prepared by - Maddy Rai
import time


class Solution:
    def thirdMax(self, nums):
        if len(nums) not in range(1, 10000+1):
            raise Exception("Number of elements in the list out of range.")

        if min(nums) < (-2**31) or max(nums) >= (2**31):
            raise Exception("Value of elements in the list out of range.")

        nums = sorted(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]


nums = [-1,2,3]

tic = time.perf_counter()
result = Solution.thirdMax(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

