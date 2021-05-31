# Reference: https://leetcode.com/problems/create-target-array-in-the-given-order/
# Sequence = 1389. Create Target Array in the Given Order
# Prepared by - Maddy Rai
import time


class Solution:
    def createTargetArray(self, nums, index):
        if len(nums) not in range(1, 101) or len(index) not in range(1, 101) or len(nums) != len(index):
            raise Exception("Unexpected input.")

        if (min(nums) < 0) or (max(nums) > 100):
            raise Exception("Min or Max values exceed the desired range.")

        target = []
        for i in range(0, len(nums)):
            if index[i] not in range(0, i+1):
                raise Exception("Unexpected indices.")

            target.insert(index[i], nums[i])

        return target


nums = [0,1,2,3,4]
index = [0,1,2,2,1]

tic = time.perf_counter()
result = Solution.createTargetArray(None, nums, index)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
