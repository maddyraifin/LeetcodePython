# Reference: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3837/
# Sequence = 90. Subsets II
# Prepared by - Maddy Rai
import time
import itertools


class Solution:
    def subsetsWithDup(self, nums):
        if len(nums) not in range(1, 11):
            raise Exception("Unexpected size of input(s).")

        if nums and (min(nums) < -10 or max(nums) > 10):
            raise Exception("Input list has values out of range.")

        lslsfinal = []
        for i in range(0, len(nums)+1):
            for subset in itertools.combinations(nums, i):
                subset = sorted(list(subset))
                if subset not in lslsfinal:
                    lslsfinal = lslsfinal + [subset]

        return lslsfinal


nums = [4,4,4,1,4]

tic = time.perf_counter()
result = Solution.subsetsWithDup(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.subsetsWithDup(None, [1,2,2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]] else print('Failed!!')
print('Pass') if Solution.subsetsWithDup(None, [0]) == [[],[0]] else print('Failed!!')
