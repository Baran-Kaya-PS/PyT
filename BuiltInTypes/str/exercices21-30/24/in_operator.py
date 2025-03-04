# Vérifie si une phrase contient un mot interdit dans une liste donnée.
to_replace = [",",".",";","!","?"]
banned_list = ["spam", "fake", "scam", "fraud", "cheat", "virus", "hack", "phishing"]


def banned_words(banned_words,words):
    words = remove_ponctuation(words)
    for word in words.split():
        if word in banned_words:
            return True
    return False


def remove_ponctuation(words):
    for ch in to_replace:
        words = words.replace(ch, " ")
    return words


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

for test in test_cases:
    print(banned_words(banned_list,test))

for test in test_cases_no_banned:
    print(banned_words(banned_list,test))

