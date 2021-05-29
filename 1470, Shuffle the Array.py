# Reference: https://leetcode.com/problems/shuffle-the-array/
# Sequence = 1470. Shuffle the Array
# Prepared by - Maddy Rai
import time


class Solution:
    def shuffle(self, nums, n):
        if n not in range(1, 501):
            raise Exception("n is out of range.")

        if len(nums) != 2*n:
            raise Exception("Unexpected size of input list.")

        if (min(nums) < 1) or (max(nums) > 1000):
            raise Exception("Min or Max values exceed the desired range.")

        lsans = len(nums) * [None]
        for i in range(0, n):
            lsans[i*2] = nums[i]
            lsans[i*2+1] = nums[n]
            n += 1

        return lsans


nums = [1,2,3,4,5,6,7,8,9,10]
n = 5

tic = time.perf_counter()
result = Solution.shuffle(None, nums, n)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

