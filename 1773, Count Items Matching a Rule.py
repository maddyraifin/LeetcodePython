# Reference: https://leetcode.com/problems/count-items-matching-a-rule/
# Sequence = 1773. Count Items Matching a Rule
# Prepared by - Maddy Rai
import time


class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        if len(items) not in range(1, 10000) or ruleKey not in ["type", "color", "name"] \
                or len(ruleKey) not in range(1, 11) or len(ruleValue) not in range(1, 11)\
                or not ruleKey.islower() or not ruleValue.islower():
            raise Exception("Unexpected input.")

        for i in range(0, len(items)):
            for j in range(0, len(items[i])):
                if len(items[i][j]) not in range(1,11):
                    raise Exception("item list strings exceed expected length.")

                if not items[i][j].islower():
                    raise Exception("item list strings is not lowercase.")

        dopt = {
            "type": 0,
            "color": 1,
            "name": 2
        }

        return sum([i[dopt[ruleKey]] == ruleValue for i in items])


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

tic = time.perf_counter()
result = Solution.countMatches(None, items, ruleKey, ruleValue)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
