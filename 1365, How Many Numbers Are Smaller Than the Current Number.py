# Reference: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Sequence = 1365. How Many Numbers Are Smaller Than the Current Number
# Prepared by - Maddy Rai
import time


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        if len(nums) not in range(2, 501):
            raise Exception("Unexpected size of input list.")

        if (min(nums) < 0) or (max(nums) > 100):
            raise Exception("Min or Max values exceed the desired range.")

        sortnums = sorted(nums)
        return [sortnums.index(x) for x in nums]  # in case of a tie, index returns the first pos


nums = [8,1,2,2,3]

tic = time.perf_counter()
result = Solution.smallerNumbersThanCurrent(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
