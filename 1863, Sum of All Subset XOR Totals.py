# Reference: https://leetcode.com/problems/sum-of-all-subset-xor-totals
# Sequence = 1863,  Title = Sum of All Subset XOR Totals
# Prepared by - Maddy Rai

import itertools
import functools


class Solution:
    def subsetXORSum(self, lsnum):
        if len(nums) > 12:
            raise Exception("List cannot have more than 12 numbers.")

        if max(nums) > 20:
            raise Exception("Numbers inside the list cannot be greater than 20.")

        sumall = 0

        # Starting from 1 and 0 ensures no empty groups are selected
        for grp in range(1, len(lsnum)+1):
            for lssubset in itertools.combinations(lsnum, grp):
                xorval = functools.reduce(lambda x, y: x ^ y, lssubset)
                sumall = sumall + xorval

        return sumall


nums = [3, 4, 5, 6, 7, 8]
result = Solution.subsetXORSum(None, nums)
print(result)
