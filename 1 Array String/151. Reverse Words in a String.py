class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.split()))







# # class Solution:
# #     def reverseWords(self, s: str) -> str:
# #         s=s.strip()
# #         l=s.split(' ')
# #         i=0
# #         while i<len(l):
# #             if l[i] == '':
# #                 l.pop(i)
# #                 i-=1
# #             i+=1
# #         l.reverse()
# #         return ' '.join(l)
    
    
# s = "   the sky is   blue"
    
# words = s.split()
# print(words)
# # Reverse the list of words
# reversed_words = reversed(words)

# # Join the reversed list of words back into a string with spaces
# reversed_sentence = ' '.join(reversed_words)

# # Return the reversed sentence
# print( reversed_sentence)
    
    
    
    
    
    
# # s = "   the sky is   blue"
# # s=s.strip()
# # l=s.split(' ')

# # print(l)
# # i=0
# # while i<len(l):
# #     if l[i] == '':
# #         l.pop(i)
# #         i-=1
# #     i+=1
    
# # print(l) 


# # l.reverse()
# # print(l) 
