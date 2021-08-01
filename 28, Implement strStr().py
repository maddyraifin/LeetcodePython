# Reference: https://leetcode.com/problems/implement-strstr/
# Sequence = 28. Implement strStr()
# Prepared by - Maddy Rai
import time


class Solution:
    def strStr(self, haystack, needle):
        if len(haystack) not in range(0, (5*104)+1) or len(needle) not in range(0, (5*104)+1):
            raise Exception("Unexpected size of input strings.")

        if (len(haystack) != 0 and not haystack.islower()) or (len(needle) != 0 and not needle.islower()):
            raise Exception("Input strings are not fully lowercase.")

        return 0 if needle == "" else haystack.find(needle)


haystack = "hello"
needle = "ll"

tic = time.perf_counter()
result = Solution.strStr(None, haystack, needle)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.strStr(None, "hello", "ll") == 2 else print('Failed!!')
print('Pass') if Solution.strStr(None, "aaaaa", "bba") == -1 else print('Failed!!')
print('Pass') if Solution.strStr(None, "", "") == 0 else print('Failed!!')
