# Reference: https://leetcode.com/problems/reverse-integer/
# Sequence = 7. Reverse Integer
# Prepared by - Maddy Rai
import time


class Solution:
    def reverse(self, x):
        if x not in range(-2**31, 2**31):
            raise Exception("Input number is out of range.")

        if x < 0:
            numrev = -int(str(abs(x))[::-1])
        else:
            numrev = int(str(abs(x))[::-1])

        return numrev if numrev in range(-2**31, 2**31) else 0


x = -123

tic = time.perf_counter()
result = Solution.reverse(None, x)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
