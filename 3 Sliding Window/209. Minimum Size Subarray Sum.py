from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sn=sum(nums)
        if sn<target:
            return 0
        sn=0
        l=0
        ml=len(nums)+1
        for r in range(len(nums)):
            sn+=nums[r]

            while sn>=target:
                ml=min(ml,r-l+1)
                sn-=nums[l]
                l+=1
        return ml if ml<=len(nums) else 0