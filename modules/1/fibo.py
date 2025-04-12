# ### 1. Création de Module et Import Simple
# - Créez un nouveau fichier Python et placez-y une fonction très simple.
# - Dans un autre script, importez ce module et appelez la fonction.
# - Vérifiez que vous pouvez l’exécuter sans erreur.

def fib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib(500))