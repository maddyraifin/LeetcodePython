# Reference: https://leetcode.com/problems/number-of-different-integers-in-a-string/
# Sequence = 1805. Number of Different Integers in a String
# Prepared by - Maddy Rai
import time


class Solution:
    def numDifferentIntegers(self, word):
        if len(word) not in range(1, 1001):
            raise Exception("Length of string is out of range.")

        if not word.isalnum():
            raise Exception("Input string has unexpected datatype(s).")

        newword = "".join([" " if i.isalpha() else i for i in word])
        newword = newword.split()
        return len(set(map(int, newword)))


word = "a123bc34d8ef34"

tic = time.perf_counter()
result = Solution.numDifferentIntegers(None, word)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.numDifferentIntegers(None, "a123bc34d8ef34") == 3 else print('Failed')
print('Pass') if Solution.numDifferentIntegers(None, "leet1234code234") == 2 else print('Failed')
print('Pass') if Solution.numDifferentIntegers(None, "a1b01c001") == 1 else print('Failed!!')
