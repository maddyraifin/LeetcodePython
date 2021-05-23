# Reference: https://leetcode.com/problems/running-sum-of-1d-array/
# Sequence = 1480, Running Sum of 1d Array
# Prepared by - Maddy Rai


class Solution:
    def runningSum(self, lsnums):
        if len(lsnums) > 1000:
            raise Exception("List cannot have more than 12 numbers.")

        if min(lsnums) < -pow(10, 6):
            raise Exception("Numbers inside the list cannot be greater than 20.")

        if max(lsnums) > pow(10, 6):
            raise Exception("Numbers inside the list cannot be greater than 20.")

        # Starting from 1 and 0 ensures no empty groups are selected
        for i in range(1, len(lsnums)):
            lsnums[i] = lsnums[i-1] + lsnums[i]

        return lsnums


nums = [1, 1, 2]
result = Solution.runningSum(None, nums.copy())
print(result)
