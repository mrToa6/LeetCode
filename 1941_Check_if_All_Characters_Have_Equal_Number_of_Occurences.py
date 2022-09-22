from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return True if len(list(dict.fromkeys(list(Counter(s).values())))) == 1 else False
      

string = "abcdeasdfsdcvbfdgaec"
string2 = "aabbccddeeffgg"
a = Solution()
print(a.areOccurrencesEqual(string))
print(a.areOccurrencesEqual(string2))