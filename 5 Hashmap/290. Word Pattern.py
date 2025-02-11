# *

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=pattern
        s2=s.split(' ')
        d={}
        s3=[]
        if len(p)!=len(s2):
            return False
        else:
            for (i,j),(k,l) in zip(enumerate(p),enumerate(s2)):                
                if j in d.keys() and d[j]!=l:
                    return False
                elif j not in d.keys() and l in d.values():
                    return False
                elif j in d.keys() and d[j]==l:
                    s3.append(k)
                elif j not in d.keys() and l not in d.values():
                    d[j]=l
                    s3.append(k)
            if len(s3)!=len(s2):
                return False
            
            return True

# class Solution:
#   def wordPattern(self, pattern: str, str: str) -> bool:
#     t = str.split()
#     return [*map(pattern.index, pattern)] == [*map(t.index, t)]













# from collections import Counter


# pattern = "abba" 
# s = "dog cat cat dog"
# p=pattern

# def wp(s,p):
#     s2=s.split(' ')

#     s3=s2.copy()
#     s4=[]
#     d={}
#     if len(p)!=len(s2):
#         return False
#     else:
#         print("In ELSE")
#         for j,(k,l) in zip(p,enumerate(s2)):                
#             if j in d.keys() and d[j]!=l:
#                 print(k,"In if 1 ",s3,d)
#                 return  False
#             elif j not in d.keys() and l in d.values():
#                 print(k,"In if 2 ",s3,d)
#                 return False
#             elif j in d.keys() and d[j]==l:
#                 s4.append(k)
#                 # s3.pop(k)
#             elif j not in d.keys() and l not in d.values():
#                 d[j]=l
#                 # s3.pop(k)
#                 s4.append(k)
#                 print(k,"In if 4 ",s3,d)
                
#         print("after for",p,s2,s3,d)
#         if len(s3)!=len(s4):
#             return False
        
#         return True

# ans=wp(s,p)
# print("\nans=",ans)















# for (i,j),(k,l) in zip(enumerate(p),enumerate(s2)):
#     if j not in d.keys() and l not in d.values():
#         d[j]=l
#         s2.pop(k)
    
        
# print(d)
    
        
        
        
        
        # vp.append(j)
        # vs.append(l)
        


# print(s2)


# print(len(s2),len(p))





# c1=Counter(p)
# c2=Counter(s2)
# print(c1.values())
# print(c2.values())