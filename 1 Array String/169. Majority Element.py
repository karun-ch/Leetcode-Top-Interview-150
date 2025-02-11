nums = [2, 2, 1, 1, 1, 2, 2]
counts = {}

for num in nums:
    counts[num] = counts.get(num, 0) + 1

print(counts)
max_num = max(counts, key=counts.get)













# from itertools import count
# nums = [2,2,1,1,1,2,2]
# a=[]
# c=0
# for i in nums:
#     if i not in a:
#         cnt=nums.count(i)
#         if c<cnt:
#             c=cnt