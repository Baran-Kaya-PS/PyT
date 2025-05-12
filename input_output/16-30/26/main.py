import re


def isComment(line):
    if '#' in line:
        return True
    return False

def extractComment(line):
    if isComment(line):
        if line.startswith("#"):
            return line
        else:
            idx = line.index('#')
            return line[idx::]
    else:
        return None

def isVariable(line):
    if '=' in line :
        return True
    return False

def extractVariable(line):
    if isVariable(line):
        if isComment(line):
            comment = extractComment(line)
            line = re.sub(re.escape(comment),"",line)
            return line
        return line
    else:
        return None
# with open("data.txt","r",encoding="utf-8") as f: