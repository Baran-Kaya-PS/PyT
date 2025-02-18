import re

if (re.fullmatch("[\d]*",input("-->"))) is None:
    print("is not digit")
else :
    print("is digit")