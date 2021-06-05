# Reference: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Sequence = 1588. Sum of All Odd Length Subarrays
# Prepared by - Maddy Rai
import time


class Solution:
    def sumOddLengthSubarrays(self, arr):
        if len(arr) not in range(1, 101):
            raise Exception("Number of elements in the list is out of range.")

        if min(arr) < 1 or max(arr) > 1000:
            raise Exception("Array elements are out of range.")

        count = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i+1):
                if (j+i) <= len(arr):
                    count = count + sum(arr[j:j+i])

        return count


arr = [1,4,2,5,3]

tic = time.perf_counter()
result = Solution.sumOddLengthSubarrays(None, arr)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
