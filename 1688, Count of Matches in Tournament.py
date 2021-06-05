# Reference: https://leetcode.com/problems/count-of-matches-in-tournament/
# Sequence = 1688. Count of Matches in Tournament
# Prepared by - Maddy Rai
import time


class Solution:
    def numberOfMatches(self, n):
        if n not in range(1, 201):
            raise Exception("Input number is out of range out of range.")

        return n-1


n = 7

tic = time.perf_counter()
result = Solution.numberOfMatches(None, n)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
