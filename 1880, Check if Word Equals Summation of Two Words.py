# Reference: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# Sequence = 1880. Check if Word Equals Summation of Two Words
# Prepared by - Maddy Rai
import time


class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        if len(firstWord) not in range(1, 9) or len(secondWord) not in range(1, 9) or len(targetWord) not in range(1, 9):
            raise Exception("Unexpected length of inputs.")

        dictm = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}

        s1 = ''.join([dictm[i] for i in firstWord])
        s2 = ''.join([dictm[i] for i in secondWord])
        s3 = ''.join([dictm[i] for i in targetWord])

        if (int(s1) + int(s2)) == int(s3):
            return True
        else:
            return False


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

tic = time.perf_counter()
result = Solution.isSumEqual(None, firstWord, secondWord, targetWord)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
