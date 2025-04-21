dict_ = { "Alice": 24, "Bob": 19, "Charlie": 30 }
for k,v in dict_.items():
    pass
    #print("{:>10}{:>5}".format(k,v))

max_key = max([len(name) for name in dict_.keys()])

for name,age in dict_.items():
    header = name.ljust(max_key+2) + str(age).rjust(3)
    sep = "-"*len(header)
    print(header)
    print(sep)