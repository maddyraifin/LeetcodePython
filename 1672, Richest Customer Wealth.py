# Reference: https://leetcode.com/problems/richest-customer-wealth/
# Sequence = 1672. Richest Customer Wealth
# Prepared by - Maddy Rai
import time


class Solution:
    def maximumWealth(self, accounts):
        if len(accounts) not in range(1, 51):
            raise Exception("Unexpected number of accounts.")

        # Following solution is simple but does not check on constraints
        #nummax = max([sum(accounts[i]) for i in range(0, len(accounts))])
        #return nummax

        nummax = 0
        for i in range(0, len(accounts)):
            if len(accounts[i]) not in range(1, 51):
                raise Exception("Unexpected number of accounts for a single holder.")

            if (min(accounts[i]) < 1) or (max(accounts[i]) > 100):
                raise Exception("Account values for a single holder is out of range.")

            if sum(accounts[i]) > nummax:
                nummax = sum(accounts[i])

        return nummax


accounts = [[1,2,3],[3,2,1]]

tic = time.perf_counter()
result = Solution.maximumWealth(None, accounts)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
