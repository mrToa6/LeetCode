from collections import defaultdict
class Solution:
    def repeatedCharacter(self, s):
        occurences = defaultdict(int)
        for char in s:
            occurences[char] += 1
            if occurences[char] == 2:
                return char

a = Solution()

print(a.repeatedCharacter("nxcn")) # n
print(a.repeatedCharacter("abccbaacz")) # c
print(a.repeatedCharacter("fmxwkbxugk")) # x
print(a.repeatedCharacter("regzueqr")) # e
print(a.repeatedCharacter("ohzqhozy")) # h


