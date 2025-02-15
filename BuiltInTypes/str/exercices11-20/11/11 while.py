user_input = input("--> ")
i = len(user_input)-1
reverse = ""
while i >= 0:
    reverse += user_input[i]
    i-=1
print(reverse)