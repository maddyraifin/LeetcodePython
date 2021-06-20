# Reference: https://leetcode.com/problems/valid-mountain-array/
# Sequence = 941. Valid Mountain Array
# Prepared by - Maddy Rai
import time


class Solution:
    def validMountainArray(self, arr):
        if len(arr) not in range(1, 10001):
            raise Exception("Length of list is out of range.")

        if min(arr) < 0 or max(arr) > 10000:
            raise Exception("Array elements are out of bounds.")

        boolmt = False

        if len(arr) >= 3:
            if arr[0] == max(arr) or arr[-1] == max(arr):
                boolmt = False
            else:
                idxmax = arr.index(max(arr))

                #Check the first part is increasing
                boolmt = all([arr[i] < arr[i+1] for i in range(0, len(arr[:idxmax]))]) and\
                        all([arr[i] > arr[i + 1] for i in range(len(arr[:idxmax]), len(arr)-1)])

        return boolmt

arr = [1,4,5,6,4,2]

tic = time.perf_counter()
result = Solution.validMountainArray(None, arr)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

