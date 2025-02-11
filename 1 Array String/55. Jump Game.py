from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        l=0
        while i<len(nums) and i<=l:
            l=max(l,i+nums[i])
            i+=1
        return i==len(nums)
