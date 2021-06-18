# Reference: https://leetcode.com/problems/excel-sheet-column-title/
# Sequence = 168. Excel Sheet Column Title
# Prepared by - Maddy Rai
import time


class Solution:
    def convertToTitle(self, columnNumber):
        if columnNumber not in range(0, 2**31):
            raise Exception("column number is out of range")

        strc = ''
        if columnNumber != 0:
            q, r = divmod(columnNumber, 26)

            if q == 0 and r != 0:
                strc = chr(64+r)
            elif q != 0 and r == 0:
                strc = Solution.convertToTitle(None, q-1) + 'Z' + strc
            else:
                strc = Solution.convertToTitle(None, q) + chr(64+r) + strc

        return strc


columnNumber = 28

tic = time.perf_counter()
result = Solution.convertToTitle(None, columnNumber)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

