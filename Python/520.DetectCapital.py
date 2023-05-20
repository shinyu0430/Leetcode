
# solution1
# def captial(self,char):
#     if ord(char)<91:
#         return True
# def detectCapitalUse(self, word: str) -> bool:
#     l = len(word)
#     if l == 1 :
#         return True

#     result = True
#     if not self.captial(word[0]):
#         for i in range(1,l):
#             if(self.captial(word[i]) and result):
#                 result = False
#     else:
#         flag,result = 0, True
#         if self.captial(word[1]):
#             flag = 1

#         for i in range(2, l):
#             if (flag and not self.captial(word[i])) or (not flag and self.captial(word[i])):
#                 result = False
#                 break

#     return result

# solution2: more clever way
def detectCapitalUse(self, word: str) -> bool:
    cnt = 0
    for i in range(len(word)):
        if word[i] <= 'Z':
            cnt += 1
    return cnt == len(word) or cnt == 0 or (cnt == 1 and word[0] <= 'Z')

# solution3: using python's string method
def detectCapitalUse(self, word: str) -> bool:
    if word.upper() == word or word.lower() == word or word.capitalize() == word:
        return True
    return False
