def isComment(line):
    if '#' in line:
        return True
    return False

def extractComment(line):
    if isComment(line):
        if line.startswith("#"):
            return line
        else:
            idx = line.index('#') + 1
            return line[idx::]
    else:
        return None

def isVariable(line):
    if '=' in line :
        return True
    return False

# with open("data.txt","r",encoding="utf-8") as f: