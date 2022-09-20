key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

class Solution(object):
    def decodeMessage(self, key, message):
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        alphabet_list = list(alphabet_string)
        clean_string = "".join(dict.fromkeys(key)).replace(" ","")
        char_list = list(clean_string)
        key_dict = {}
        for i in range(len(char_list)):
            key_dict[char_list[i]] = alphabet_list[i]
        
        print(key_dict)   
        output = ""
        for char in message:
            if char != " ":
                output += key_dict[char]
            else:
                output += " "
        return output
    
a =Solution()
print(a.decodeMessage(key, message))
# print(a.decodeMessage(key2, message2))  
    
    
    
    
# alphabet_string = "abcdefghijklmnopqrstuvwxyz"
# alphabet_list = list(alphabet_string)
# clean_string = "".join(dict.fromkeys(string)).replace(" ","")
# # print(clean_string)
# char_list = list(clean_string)
# # print(char_list)
# # print(alphabet_list)
# key_dict = {}
# for i in range(len(char_list)):
#     key_dict[char_list[i]] = alphabet_list[i]

# # print(key_dict)
# output = ""
# for char in message:
#     if char != " ":
#         output += key_dict[char]
#     else:
#         output += " "

# print(output)