# Reference: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Sequence = 914. X of a Kind in a Deck of Cards
# Prepared by - Maddy Rai
import time
import collections


class Solution:
    def hasGroupsSizeX(self, deck):
        if len(deck) not in range(1, 10001):
            raise Exception("Length of list is out of range.")

        if min(deck) < 0 or max(deck) > 10000:
            raise Exception("Array elements are out of bounds.")

        if len(deck) < 2:
            return False

        lscounts = list(dict(collections.Counter(deck)).values())
        if len(lscounts) == 1:
            return True

        minval = min(lscounts)
        if minval == 1:
            return False

        # Starting with number 2 to minval/2, check if there is any common divisor
        for i in range(2, int(minval/2)+1):
            if all(j % i == 0 for j in lscounts):
                return True

        # Check if the minval itself is a common divisor (if it is a prime number)
        if all(i % minval == 0 for i in lscounts):
            return True
        else:
            return False


deck = [1,1,1,1,2,2,2,2,2,2]#[1,1,1,1,1,1,1,1,1]

tic = time.perf_counter()
result = Solution.hasGroupsSizeX(None, deck)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,1,1,1,1,1,1,1]) is True else print('Failed')
print('Pass') if Solution.hasGroupsSizeX(None, [1,2,3,4,4,3,2,1]) is True else print('Failed')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,1,2,2,2,3,3]) is False else print('Failed!!')
print('Pass') if Solution.hasGroupsSizeX(None, [1]) is False else print('Failed!!')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1]) is True else print('Failed')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,2,2,2,2]) is True else print('Failed')
print('Pass') if Solution.hasGroupsSizeX(None, [1,2,3]) is False else print('Failed!!')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]) is True else print('Failed!!')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,1,1,2,2,2,2,2,2]) is True else print('Failed!!')
print('Pass') if Solution.hasGroupsSizeX(None, [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) is True else print('Failed!!')

