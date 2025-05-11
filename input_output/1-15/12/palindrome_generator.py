#https://stackoverflow.com/questions/17435448/palindrome-generator

from itertools import count

from wheel.cli.convert import convert

def numberToChar(val):
    char = chr(ord("a")+val)

def getPalindrome():
    """
        Generator for palindromes.
        Generates palindromes, starting with 0.
        A palindrome is a number which reads the same in both directions.
    """
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])

def allPalindromes(minP, maxP):
    """Get a sorted list of all palindromes in intervall [minP, maxP]."""
    palindromGenerator = getPalindrome()
    palindromeList = []
    for palindrome in palindromGenerator:
        if palindrome > maxP:
            break
        if palindrome < minP:
            continue
        palindromeList.append(palindrome)
    return palindromeList

if __name__ == "__main__":
    print(allPalindromes(4456789, 5000000))

