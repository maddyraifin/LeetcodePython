# Reference: https://leetcode.com/problems/remove-element/
# Sequence = 27. Remove Element
# Prepared by - Maddy Rai
import time


class Solution:
    def removeElement(self, nums, val):
        if len(nums) not in range(0, 101) or val not in range(0, 101):
            raise Exception("Unexpected size/values of input(s).")

        if nums and (min(nums) < 0 or max(nums) > 50):
            raise Exception("Input list has values out of range.")

        itr1 = 0
        itr2 = len(nums)-1
        while itr1 < len(nums) and itr2 > itr1:
            if nums[itr2] == val:
                while itr2 > 0:
                    if nums[itr2] != val:
                        break
                    else:
                        itr2 = itr2 - 1

            if itr2 > itr1:
                if nums[itr1] == val:
                    nums[itr1], nums[itr2] = nums[itr2], nums[itr1]
                    itr2 = itr2 - 1
                itr1 = itr1 + 1

        if not nums:
            return 0
        elif val in nums:
            return nums.index(val)
        else:
            return len(nums)


nums = [3,1,3,3,3]
val = 3

tic = time.perf_counter()
result = Solution.removeElement(None, nums, val)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.removeElement(None, [3,2,2,3], 3) == 2 else print('Failed!!')
print('Pass') if Solution.removeElement(None, [0,1,2,2,3,0,4,2], 2) == 5 else print('Failed!!')
print('Pass') if Solution.removeElement(None, [0,1,2,2,3,3,3,3], 3) == 4 else print('Failed!!')
print('Pass') if Solution.removeElement(None, [0,1,2,2,3,3,3,3], 9) == 8 else print('Failed!!')
print('Pass') if Solution.removeElement(None, [4,2,0,2,2,1,4,4,1,4,3,2], 4) == 8 else print('Failed!!')
print('Pass') if Solution.removeElement(None, [3,1,3,3,3], 3) == 1 else print('Failed!!')
