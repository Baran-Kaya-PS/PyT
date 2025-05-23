with open("lines.txt","r",encoding="utf-8") as sf:
    lines = [line.strip().lower() for line in sf] # tableau qui récupère chaque ligne

sorted_lines = sorted(lines) # tri des lignes

with open("sorted_lines.txt","w",encoding="utf-8") as of:
    for line in sorted_lines:
        of.write(f"{line}\n")

print(sorted_lines[0:5])