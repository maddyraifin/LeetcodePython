# Reference: https://leetcode.com/problems/jewels-and-stones/
# Sequence = 771. Jewels and Stones
# Prepared by - Maddy Rai
import time


class Solution:
    def numJewelsInStones(self, jewels, stones):
        if len(jewels) not in range(1, 51) or len(stones) not in range(1, 51)\
                or not jewels.isalpha() or not stones.isalpha():
            raise Exception("Unexpected input case.")

        if len(set(jewels)) != len(jewels):
            raise Exception("Jewels string does not has unique characters.")

        return sum(s in jewels for s in stones)


jewels = "aA"
stones = "aAAbbbb"

tic = time.perf_counter()
result = Solution.numJewelsInStones(None, jewels, stones)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
