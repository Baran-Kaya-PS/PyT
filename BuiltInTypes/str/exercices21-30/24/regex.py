import re

banned_list = {"spam", "fake", "scam", "fraud", "cheat", "virus", "hack", "phishing"}
to_replace = [",",".",";","!","?"]

test_cases = [
    "This message contains spam.",            # ✅ Contient "spam"
    "Be careful, this is a phishing attempt!", # ✅ Contient "phishing"
    "You have won a prize! Claim now, no scam!", # ✅ Contient "scam"
    "This email might contain a virus, don't open it.", # ✅ Contient "virus"
    "Beware of fraud calls, do not share OTP." # ✅ Contient "fraud"
]

test_cases_no_banned = [
    "Hello, how are you?",      # ❌ Aucun mot interdit
    "Python is a great language!", # ❌ Aucun mot interdit
    "Let's meet at the café for coffee.", # ❌ Aucun mot interdit
    "Technology is evolving rapidly.", # ❌ Aucun mot interdit
    "I love programming challenges." # ❌ Aucun mot interdit
]

def remove_punctuation(sentence):
    for ch in to_replace:
        sentence = sentence.replace(ch, " ")
    return sentence

def construct_regex(banned_words):
    return r"\b("+"|".join(banned_words)+ r")\b"

def banned_word(banned_words,words):
    sentence = remove_punctuation(words).lower()
    regx = construct_regex(banned_words)
    if re.search(regx,sentence):
        return True
    return False

for test in test_cases:
    print(banned_word(banned_list,test))

for test in test_cases_no_banned:
    print(banned_word(banned_list,test))