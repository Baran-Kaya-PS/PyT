def isVowel(char):
    return char in 'aeiouAEIOU'


# 38. **Set Comprehension**
#     Take a string with duplicates.
#     Build a set comprehension to extract only unique letters that are, for instance, vowels.
#     Print the resulting set.

str1 = "abcd efg salut à tous"
str2 = "abcd efg cette fois c'est différent"

# récupérer les lettres uniques qui sont des voyelles

unique_letters = {c1 for c1 in str1 + str2 if isVowel(c1)}

print(unique_letters)