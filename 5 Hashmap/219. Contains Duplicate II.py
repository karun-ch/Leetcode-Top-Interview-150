from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexmap={}
        
        for i,n in enumerate(nums):
            if n in indexmap and i-indexmap[n]<=k:
                return True
            indexmap[n]=i
        return False





# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     if abs(i-j)<=k:
#                         return True
#         return False