# Reference: https://leetcode.com/problems/defanging-an-ip-address/
# Sequence = 1108, Defanging an IP Address
# Prepared by - Maddy Rai
import time


class Solution:
    def defangIPaddr(self, tempstr):
        # Following is faster than using FOR loop,
        # or SPLITTING to list and then joining
        return tempstr.replace('.', '[.]')


address = "1.1.1.1"

tic = time.perf_counter()
result = Solution.defangIPaddr(None, address)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)





