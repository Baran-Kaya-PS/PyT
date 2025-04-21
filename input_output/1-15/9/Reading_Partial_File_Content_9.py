with open("file_x.txt", 'r', encoding="utf_8") as tf:
    chars = []
    while len(chars) < 50:
        ch = tf.read(1)
        if ch != '\n':
            chars.append(ch)
print(chars)
print(len(chars))