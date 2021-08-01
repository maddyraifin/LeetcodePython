# Reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Sequence = 26. Remove Duplicates from Sorted Array
# Prepared by - Maddy Rai
import time


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) not in range(0, 3*10000+1):
            raise Exception("Unexpected size/values of input(s).")

        if nums and (min(nums) < -100 or max(nums) > 100):
            raise Exception("Input list has values out of range.")

        if nums and nums != sorted(nums):
            raise Exception("Input list is not sorted")

        if not nums:
            return 0
        else:
            itr1 = 0
            itr2 = 1

            while itr2 < len(nums):
                if nums[itr1] == nums[itr2]:
                   itr2 = itr2 + 1
                elif nums[itr1] > nums[itr2]:
                   itr2 = itr2 + 1
                else:
                    if (itr2 - itr1) > 1:
                        nums[itr1+1], nums[itr2] = nums[itr2], nums[itr1+1]
                        itr1 = itr1 + 1
                        itr2 = itr1 + 1
                    else:
                        itr1 = itr1 + 1
                        itr2 = itr2 + 1

        return itr1+1


nums = [0,1,1,1,2,3]

tic = time.perf_counter()
result = Solution.removeDuplicates(None, nums)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)

# Testcases
print("----Starting Testcases-----")
print('Pass') if Solution.removeDuplicates(None, [1,1,2]) == 2 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [0,0,1,1,1,2,2,3,3,4]) == 5 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [1,1,1,2,3]) == 3 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [1,2,3]) == 3 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, []) == 0 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [1]) == 1 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [0,1,1,1,2,3,4]) == 5 else print('Failed!!')
print('Pass') if Solution.removeDuplicates(None, [0,1,1,1,2,3,4,4,4,4,6]) == 6 else print('Failed!!')
