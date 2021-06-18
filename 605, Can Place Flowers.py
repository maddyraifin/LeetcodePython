# Reference: https://leetcode.com/problems/can-place-flowers/
# Sequence = 605. Can Place Flowers
# Prepared by - Maddy Rai
import time


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) not in range(1, 20001):
            raise Exception("Number of elements in the list out of range.")

        if n not in range(0, len(flowerbed)+1):
            raise Exception("Integer n is out of range.")

        intc = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            intc = intc + 1
        elif len(flowerbed) == 2 and (flowerbed == [0, 0]):
            intc = intc + 1
        elif len(flowerbed) >= 3:
            # head edge case
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                intc = intc+1

            # tail edge case
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                intc = intc+1

            for i in range(0, len(flowerbed)-3):
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                    flowerbed[i+1] = 1
                    intc = intc+1
                    i = i+2

        return True if n <= intc else False


flowerbed = [0,0,1]
n = 1

tic = time.perf_counter()
result = Solution.canPlaceFlowers(None, flowerbed, n)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

