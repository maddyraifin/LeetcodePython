# Reference: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Sequence = 1290. Convert Binary Number in a Linked List to Integer
# Prepared by - Maddy Rai
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

        if val not in (0, 1):
            raise Exception("Unexpected value.")

class Solution:
    def getDecimalValue(self, head):
        count = 0
        num = 0
        while head:
            num = 2*num + head.val
            count = count+1
            head = head.next

        if count > 30:
            raise Exception("Unexpected number of nodes.")

        return num


n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15 = \
    ListNode(1), ListNode(0), ListNode(0), ListNode(1), ListNode(0), ListNode(0), ListNode(1), ListNode(1)\
    , ListNode(1), ListNode(0), ListNode(0), ListNode(0), ListNode(0), ListNode(0), ListNode(0)
n1.next, n2.next, n3.next, n4.next, n5.next, n6.next, n7.next, n8.next, n9.next, n10.next, n11.next, n12.next, \
    n13.next, n14.next = n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15

tic = time.perf_counter()
result = Solution.getDecimalValue(None, n1)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
