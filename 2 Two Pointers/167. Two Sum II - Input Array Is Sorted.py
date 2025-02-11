from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            if numbers[l]+numbers[r]<target:
                l+=1
            else: r-=1













#  brute force
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(1,len(numbers)):
#                 if j!=i:
#                     if numbers[i]+numbers[j]==target:
#                         return [i+1,j+1]