# 46. **Search a Substring in a List of Strings**
#     Ask the user for a list of strings.
#     Ask for a substring.
#     Filter the list to keep only those containing the substring (`sub in string`).
#     Print the result.

l = "Salut tout le monde aujourd'hui nous allons parler de".lower().split()
sub = "ou".lower()
l = sorted(([x for x in l if sub in x])) # x va représenter chaque mot un par un, si sub est dans le mot alors on garde x

print(l)

