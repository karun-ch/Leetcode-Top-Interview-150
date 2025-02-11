from typing import Counter


s = "anagram"
t = "nagaram"

print(Counter(s),Counter(t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        