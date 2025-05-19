ui = input()
while '@' not in ui:
    ui = input()

with open("emails.txt","a",encoding="utf-8") as f:
    f.write(f"{ui}\n")

with open("emails.txt", "r", encoding="utf-8") as f:
    total = len(f.readlines())

print(f"Total emails in file: {total}")