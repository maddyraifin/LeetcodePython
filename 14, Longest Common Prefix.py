# Reference: https://leetcode.com/problems/longest-common-prefix/
# Sequence = 14. Longest Common Prefix
# Prepared by - Maddy Rai
import time


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) not in range(1, 201):
            raise Exception("Unexpected size of input List.")

        nummin = min([len(s) for s in strs])

        strout = ""
        for i in range(0, nummin):
            setchar = set()
            for j in strs:
                if len(j) not in range(0, 201):
                    raise Exception("Unexpected size of a string.")

                if j.islower() is False:
                    raise Exception("A string has an uppercase character.")

                setchar.add(j[i])

                if len(setchar) > 1:
                    break

            if len(setchar) == 1:
                strout = strout + setchar.pop()
            else:
                break

        return strout


strs = ["cir","car"]

tic = time.perf_counter()
result = Solution.longestCommonPrefix(None, strs)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.longestCommonPrefix(None, ["flower","flow","flight"]) == "fl" else print('Failed!!')
print('Pass') if Solution.longestCommonPrefix(None, ["dog","racecar","car"]) == "" else print('Failed!!')
print('Pass') if Solution.longestCommonPrefix(None, ["flo","flo","flo"]) == "flo" else print('Failed!!')
print('Pass') if Solution.longestCommonPrefix(None, ["cir","car"]) == "c" else print('Failed!!')