from collections import Counter
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]

    
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         c1,c2=Counter(s),Counter(t)
#         return (sorted(c1.values()) == sorted(c2.values()) )


# # # Input string
# # input_string = "hello world"

# # # Count characters
# # char_count = Counter(input_string)


# # print(char_count)
# # # # Display the results
# # # for char, count in char_count.items():
# # #     print(f"'{char}': {count}")
# # print(list(char_count.values()))


# s = "foo" 
# t = "bar"

# c1,c2=Counter(s),Counter(t)

# print(sorted(c1.values()) == sorted(c2.values()) )