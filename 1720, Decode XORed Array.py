# Reference: https://leetcode.com/problems/decode-xored-array/
# Sequence = 1720. Decode XORed Array
# Prepared by - Maddy Rai
import time
import itertools


class Solution:
    def decode(self, encoded, first):
        if len(encoded) not in range(2-1, 105-1):
            raise Exception("Unexpected size of input list.")

        if (min(encoded) < 0) or (max(encoded) > 105):
            raise Exception("Min or Max values exceed the desired range.")

        if first not in range(0, 106):
            raise Exception("first digit out of range.")

        lsfinal = [first]
        for i in encoded:
            lsfinal.append(lsfinal[-1] ^ i)
        return lsfinal

encoded = [1,2,3]

tic = time.perf_counter()
result = Solution.decode(None, encoded, 1)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
