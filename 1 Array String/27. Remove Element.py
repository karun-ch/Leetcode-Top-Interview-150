class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for num in nums:
      if num != val:
        nums[i] = num
        i += 1
    return i


















# nums = [3, 2, 2, 3]
# val = 3
# n = []
# l = len(nums)
# i = 0

# while i < l:
#     if nums[i] == val:
#         nums.pop(i)
#         n.append("_")
#         l -= 1
#     else:
#         i += 1

# print(nums)
# # print(n)
# for i in n:
#     nums.append(i)

# print(nums)





# # nums = [3,2,2,3]
# # val = 3
# # n=nums
# # a=[]
# # c=[]
# # l=len(nums)
# # for i in range(l):
# #     if nums[i]==val:
# #         # n.pop(i)
# #         a.append("_")
# #     else: c.append(nums[i])

# # print(nums)
# # print(c)
# # c.append(''.join(a))
# # print(c)
