from collections import Counter

words_frequency = Counter()

with open("file_x.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.replace("\n","")
        words_frequency[line] += 1

print(words_frequency.most_common(n=5))