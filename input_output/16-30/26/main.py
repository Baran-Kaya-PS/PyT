import re

def containsError(line):
    c_line = line
    if containsComment(c_line):
        c_line = re.sub(extractComment(c_line),"",c_line).strip()
    if c_line.startswith("[") and (not c_line.endswith("]")):
        return True
    if '=' in c_line and c_line[c_line.index("=")::].strip() == "":
        return True
    return False

def containsOnlyText(line):
    if not (containsComment(line) or isVariable(line) or isSection(line)):
        return True
    return False

def extractText(line):
    if containsOnlyText(line):
        return line
    return False

def containsComment(line):
    if '#' in line:
        return True
    return False

def extractComment(line):
    if containsComment(line):
        if line.startswith("#"):
            return line
        else:
            idx = line.index('#')
            return line[idx::].strip()
    else:
        return None

def isVariable(line):
    if '=' in line:
        return True
    return False

def extractVariable(line):
    if isVariable(line):
        if containsComment(line):
            comment = extractComment(line)
            line = re.sub(re.escape(comment),"",line).strip()
            return line
        return line
    else:
        return False

def isSection(line):
    if line.startswith("[") and line.endswith("]"):
        return True
    return False

def extractSection(line):
    if isSection(line):
        if containsComment(line):
            comment = extractComment(line)
            line = re.sub(re.escape(comment),"",line).strip()
            return line[1:-1]
    return line[1:-1]


def parse_file(path):
    comments     = []   # [(line_no, text), …]
    sections     = {}   # { section_name: { start_line: int, entries: {key: (value, line_no), …} }, … }
    free_lines   = []   # [(line_no, text), …]
    errors       = []   # [(line_no, text, description), …]

    curr_section = None

    sections["Global"] = {"start_line":0,"entries":{}}

    with open(path,"r",encoding="utf-8") as f:
        for lineno,raw in enumerate(f,start=1):
            line = raw.rstrip("\n").strip()
