# Reference: https://leetcode.com/problems/palindrome-number/
# Sequence = 9. Palindrome Number
# Prepared by - Maddy Rai
import time


class Solution:
    def isPalindrome(self, x):
        if x not in range(-2**31, 2**31):
            raise Exception("Input number is out of range.")

        return str(x) == str(x)[::-1]


x = 2

tic = time.perf_counter()
result = Solution.isPalindrome(None, x)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.isPalindrome(None, -121) is False else print('Failed')
print('Pass') if Solution.isPalindrome(None, 10) is False else print('Failed')
print('Pass') if Solution.isPalindrome(None, -101) is False else print('Failed!!')
print('Pass') if Solution.isPalindrome(None, 123321) is True else print('Failed!!')
