# def filter_anagrams(word, anagrams):
#     wo = sum([word.count(i) for i in word])
#     anagrams_count = [sum([word.count(i) for i in word])for word in anagrams]
#     final = [1,2]
#     for wor in anagrams:
#         if set(wor)==set(word):
#             for i in wor:
#                 if sum([wor.count(i) for i in wor])==wo:
#                     final.append(wor)
#     print(final)
#
# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
#
# print(filter_anagrams(word, anagrams))
