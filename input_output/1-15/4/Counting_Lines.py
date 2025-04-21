with open("story.txt", 'r', encoding="utf-8") as f:
    count = 0
    for line in f:
        count = count+1
print(count)