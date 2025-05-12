def isComment(line):
    if '#' in line:
        return True
    return False
def extractComment(line):
    if isComment(line):
        if line.startswith("#"):
            return line
        else:
            return line[line.index('#')::]
    else:
        return None
# with open("data.txt","r",encoding="utf-8") as f: