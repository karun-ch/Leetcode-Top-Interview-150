class Solution:
    def romanToInt(self, s: str) -> int:
        ri = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        c=0
        for i in range(len(s)-1):
            if ri[s[i]]<ri[s[i+1]]:
                c-=ri[s[i]]
            else: c+=ri[s[i]]
        return c+ri[s[-1]]
        







# roman_to_int = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
# ri=roman_to_int
# c=0
# s="VIII"
# for i in range(len(s)):
#     c+=ri[s[i]]
# print(c)

