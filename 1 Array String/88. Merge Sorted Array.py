from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=len(nums2)  # noqa: E741
        for i in range(l):
            nums1[m+i] = nums2[i]
        nums1.sort()
