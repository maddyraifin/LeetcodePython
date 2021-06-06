# Reference: https://leetcode.com/problems/count-the-number-of-consistent-strings/
# Sequence = 1684. Count the Number of Consistent Strings
# Prepared by - Maddy Rai
import time


class Solution:
    def countConsistentStrings(self, allowed, words):

        if len(words) not in range(1, 105) or len(allowed) not in range(1, 27) or not allowed.islower():
            raise Exception("Unexpected inputs.")

        for word in words:
            if len(word) not in range(1, 11):
                raise Exception("List of string is out of range.")

            if not word.islower():
                raise Exception("String exceeds the max allowed length.")

        tempset = set(allowed)

        if len(tempset) != len(allowed):
            raise Exception("Allowed characters are not unique.")

        return sum(set(word).issubset(tempset) for word in words)  # is word a subset of tempset


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

tic = time.perf_counter()
result = Solution.countConsistentStrings(None, allowed, words)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
