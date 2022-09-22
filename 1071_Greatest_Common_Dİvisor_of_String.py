from itertools import combinations

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str_combs = []
        if len(str1) < len(str2):
            for i in range(len(str1)):
                str_combs.append(str1[:i+1])
        else:
            for i in range(len(str2)):
                str_combs.append(str2[:i+1])
        result = ""
        for comb in str_combs:
            n = len(comb)
            substringA = [str1[i:i+n] for i in range(0,len(str1),n)]
            substringB = [str2[i:i+n] for i in range(0,len(str2),n)]
            
            no_dup_A = list(set(substringA))
            no_dup_B = list(set(substringB))
            
            if len(no_dup_A) == 1 and len(no_dup_B) == 1 and no_dup_A == no_dup_B:
                result = comb
        return result
        
a = Solution()
str1 = "ABABAB" 
str2 = "ABAB"
str3 = "ABCABC"
str4 = "ABC"
str5 = "LEET"
str6 = "CODE"
print(a.gcdOfStrings(str1, str2))
print(a.gcdOfStrings(str3, str4))
print(a.gcdOfStrings(str5, str6))