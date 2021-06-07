# Reference: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Sequence = 1832. Check if the Sentence Is Pangram
# Prepared by - Maddy Rai
import time
import collections

class Solution:
    def checkIfPangram(self, sentence):
        if len(sentence) not in range(1, 1001) or not sentence.islower():
            raise Exception("Unexpected input.")

        return len(collections.Counter(sentence)) == 26


sentence = "thequickbrownfoxjumpsoverthelazydog"

tic = time.perf_counter()
result = Solution.checkIfPangram(None, sentence)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
