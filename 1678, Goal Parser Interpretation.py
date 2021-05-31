# Reference: https://leetcode.com/problems/goal-parser-interpretation/
# Sequence = 1678. Goal Parser Interpretation
# Prepared by - Maddy Rai
import time


class Solution:
    def interpret(self, command):
        if len(command) not in range(1, 101):
            raise Exception("Unexpected input.")

        return command.replace("()", "o").replace("(al)", "al")


command = "G()(al)"

tic = time.perf_counter()
result = Solution.interpret(None, command)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
