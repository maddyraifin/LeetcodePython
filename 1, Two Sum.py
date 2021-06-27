# Reference: https://leetcode.com/problems/two-sum/
# Sequence = 1. Two Sum
# Prepared by - Maddy Rai
import time


class Solution:
    def twoSum(self, nums, target):
        if len(nums) not in range(2, 10001):
            raise Exception("Unexpected size of input numbers.")

        if min(nums) < -10**9 or max(nums) > 10**9 or target < -10**9 or target > 10**9:
            raise Exception("Values are out of range.")

        mapval = {}
        for i in range(0, len(nums)):
            numfind = target - nums[i]
            if numfind in mapval:
                return [mapval[numfind], i]
            else:
                mapval[nums[i]] = i


nums = [2,7,11,15]
target = 9

tic = time.perf_counter()
result = Solution.twoSum(None, nums, target)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.twoSum(None, [2,7,11,15], 9) == [0, 1] else print('Failed!!')
print('Pass') if Solution.twoSum(None, [3,2,4], 6) == [1, 2] else print('Failed!!')
print('Pass') if Solution.twoSum(None, [3,3], 6) == [0, 1] else print('Failed!!')
