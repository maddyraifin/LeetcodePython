# Reference: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Sequence = 1431. Kids With the Greatest Number of Candies
# Prepared by - Maddy Rai
import time


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        if len(candies) not in range(2, 101):
            raise Exception("Number of elements in the list is out of range.")

        if extraCandies not in range(1, 51):
            raise Exception("Extra number of candies is out of range.")

        if min(candies) < 1:
            raise Exception("Min number in the list is out of range.")

        nummax = max(candies)
        if nummax > 100:
            raise Exception("Max number in the list is out of range.")

        return [candy >= nummax-extraCandies for candy in candies]


candies = [4,2,1,1,2]

tic = time.perf_counter()
result = Solution.kidsWithCandies(None, candies, 1)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
