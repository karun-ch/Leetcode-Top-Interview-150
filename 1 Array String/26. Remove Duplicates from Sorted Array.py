from cmath import inf
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=[-inf]
        for i in range(len(nums)):
            if nums[i]!=n[-1]:
                n.append(nums[i])
        n.pop(0)
        # nums=n
        for i in range(len(n)):
            nums[i] = n[i]
        return len(n)







# from cmath import inf


# nums = [1,1,2]

# n=[-inf]
# for i in range(len(nums)):
#     if nums[i]!=n[-1]:
#         n.append(nums[i])
# n.pop(0)
# print(n)