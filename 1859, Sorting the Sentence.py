# Reference: https://leetcode.com/problems/sorting-the-sentence/
# Sequence = 1859. Sorting the Sentence
# Prepared by - Maddy Rai
import time


class Solution:
    def sortSentence(self, s):
        if len(s) not in range(2, 201):
            raise Exception("string length out of range.")

        lsarr = s.split()
        if len(lsarr) not in range(1, 10):
            raise Exception("Number of words in the string out of range.")

        lstemp = [None] * len(lsarr)

        for i in lsarr:
            lstemp[int(i[-1])-1] = i[0:-1]

        return ' '.join(lstemp)


s = "is2 sentence4 This1 a3"

tic = time.perf_counter()
result = Solution.sortSentence(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
