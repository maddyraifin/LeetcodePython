# Reference: https://leetcode.com/problems/count-primes/
# Sequence = 204. Count Primes
# Prepared by - Maddy Rai
import time
import math


class Solution:
    def countPrimes(self, n):
        if n not in range(0, 5000001):
            raise Exception("Input number is out of range")

        if n <= 2:
            lsprime = []
        else:
            lsprime = [0, 0] + [i for i in range(2, n)]

            p = 2
            while p**2 <= n:
                if lsprime[p] != 0:
                    for i in range(p*2, n, p):
                        lsprime[i] = 0
                p = p+1

        return sum([1 for i in lsprime if i != 0])


n = 25 #499979

tic = time.perf_counter()
result = Solution.countPrimes(None, n)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

