import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        c=s[::-1]
        if s=="":
            return True
        return s==c
               
               
               
               
               
# import re
# s = "A man, a plan, a canal: Panama"
# s=s.lower()
# # s=s.split()
# s = re.sub(r'[^a-zA-Z0-9]', '', s)
# c=str(reversed(s))
# print(s==c)
# print(s,c)