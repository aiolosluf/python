# vowels = ['a', 'e', 'i', 'o', 'u']
# # word = input("Provide a word to search for vowels: ")
# word = "i have to know the truth"
# found = {'a': 0,'u': 0, 'e': 0,'i': 0,'o': 0}
# for letter in word:
#     if letter in vowels:
#         # if letter not in found:
#         #     found.append(letter)
#         found[letter] += 1
# # for vowel in found:
# #     print(vowel)
# print(found)
# print(sorted(found.items()))
# for k in found:
#     print(k, 'was found',found[k],'time(s).')
# for k,v in sorted(found.items()):
#     print(k, 'was found',v,'time(s).')

#
# def findvowels(word:str)->set:
#     """try this out"""
#     vowels = set('aeiou')
#     found = vowels.intersection(word)
#     return ''.join(found)
#
#
# print(findvowels("word is a word"))
#
# help(findvowels)

import vsearch

found = vsearch.search4letters('this is not a sentence.')
for everything in found:
    print(everything)