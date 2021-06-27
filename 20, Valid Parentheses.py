# Reference: https://leetcode.com/problems/valid-parentheses/
# Sequence = 20. Valid Parentheses
# Prepared by - Maddy Rai
import time


# This is a Stack problem
class Solution:
    def isValid(self, s):
        if len(s) not in range(1, 10001):
            raise Exception("Unexpected size of input string.")

        # This is an important step in this process where Keys are closing parenthesis
        dictval = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in dictval and len(stack) > 0:
                if stack.pop() != dictval[char]:  # if the popped value is not the corresponding opening parenthesis
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


s = "(){[]}([]{})"

tic = time.perf_counter()
result = Solution.isValid(None, s)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.isValid(None, "()") is True else print('Failed!!')
print('Pass') if Solution.isValid(None, "()[]{}") is True else print('Failed!!')
print('Pass') if Solution.isValid(None, "(]") is False else print('Failed!!')
print('Pass') if Solution.isValid(None, "([)]") is False else print('Failed!!')
print('Pass') if Solution.isValid(None, "{[]}") is True else print('Failed!!')
