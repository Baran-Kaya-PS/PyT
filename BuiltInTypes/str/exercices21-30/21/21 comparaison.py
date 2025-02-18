def is_number(s):
    return set(s).issubset("0123456789")

print(is_number(input("--> ")))