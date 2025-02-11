from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3 :
            return []
        if len(nums)==3 and sum(nums)!=0:
            return[]
        ans=[]
        nl=len(nums)
        nums.sort()
        
        for i in range(nl-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,nl-1
            while l<r:
                cs=nums[i]+nums[r]+nums[l]
                if cs==0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                elif cs<0:
                    l+=1
                else :
                    r-=1                                                            
        return ans