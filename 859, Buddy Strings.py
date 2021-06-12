# Reference: https://leetcode.com/problems/buddy-strings/
# Sequence = 859. Buddy Strings
# Prepared by - Maddy Rai
import time


class Solution:
    def buddyStrings(self, s, goal):
        if len(s) not in range(1, 2*104+1) or len(goal) not in range(1, 2*104+1):
            raise Exception("Length of input(s) out of range.")

        if not s.islower():
            raise Exception("First string is not lower case.")

        if not goal.islower():
            raise Exception("Goal string is not lower case.")

        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(goal):
            return True

        # if more than 2 positions differ, solution does not exist
        lstf = [s[i] != goal[i] for i in range(0, len(s))]
        if sum(lstf) == 2:
            lsidx = []
            for i in range(0, len(lstf)):
                if lstf[i]:
                    lsidx.append(i)
            if s[lsidx[1]] + s[lsidx[0]] == goal[lsidx[0]] + goal[lsidx[1]]:
                return True

        return False


s = "aaabcde"
goal = "aaacbde"

tic = time.perf_counter()
result = Solution.buddyStrings(None, s, goal)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
