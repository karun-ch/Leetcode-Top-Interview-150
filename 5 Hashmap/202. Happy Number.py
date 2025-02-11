class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))        
        return n == 1



class Solution:
    def isHappy(self, n: int) -> bool:
        l=list(str(n))
        d={}
        s=0
        count=0
        while s!=1 and count<100:
            s=0
            for i in l:
                d[i]=int(i)**2
                s+=d[i]
            l=list(str(s))            
            if s==1:
                return True
            count+=1
        return False







# def isHappy(n):
#     l=list(str(n))
#     print(l)
#     if len(l)==1 and n!=1:
#         print("in 1st if")
#         return False
#     d={}
#     s=0
#     count=0
#     while s!=1 and count<100:
#         s=0
#         for i in l:
#             print("i in for",i)
#             d[i]=int(i)**2
#             print(d)
#             s+=d[i]
#             print(s)
#         l=list(str(s))
#         if s==1:
#             return True
#         count+=1
#     return False


# n=19
# print(isHappy(n))