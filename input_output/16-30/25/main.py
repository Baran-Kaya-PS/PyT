with open("lines.txt","r",encoding="utf-8") as sf:
    lines = [line.strip().lower() for line in sf]

sorted_lines = sorted(lines)

with open("sorted_lines.txt","w",encoding="utf-8") as of:
    for line in sorted_lines:
        of.write(f"{line}\n")

print(sorted_lines[0:5])