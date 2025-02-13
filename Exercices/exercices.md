Voici une série de 10 exercices par section principale du tutoriel Python, conçus pour un·e programmeur·euse expérimenté·e qui découvre la syntaxe et les particularités de Python. Les énoncés sont en français, et chaque ensemble d’exercices met l’accent sur les points clés abordés dans la section concernée. Les exercices supposent déjà une compréhension générale de la programmation, mais visent à familiariser avec la grammaire et l’« idiome » Python.

---

## 1. Whetting Your Appetite

1. **Hello, Python!**  
   Écrivez un script Python minimal qui affiche « Bonjour Python ! ». Comparez la syntaxe et l’exécution à un « Hello World » dans un autre langage que vous maîtrisez.

2. **Calcul rapide**  
   Dans un shell interactif, faites quelques opérations mathématiques simples (addition, multiplication, division) pour vous familiariser avec l’interpréteur Python. Observez comment Python gère la division par défaut (opérateur `/` vs `//`).

3. **Petite fonction**  
   Définissez une fonction `bonjour(nom)` qui prend un nom en paramètre et affiche un message de bienvenue. Testez-la dans l’interpréteur.

4. **Import rapide**  
   Testez l’importation d’un module standard (par exemple `math`) dans l’interpréteur et utilisez une fonction (`math.sqrt`, `math.sin`, etc.) pour vous familiariser avec l’appel de fonctions de bibliothèques.

5. **Exécution de script**  
   Créez un fichier `test.py` contenant une instruction `print("Exécuter en script")`. Exécutez-le depuis la ligne de commande avec `python test.py`. Comparez avec l’exécution en mode interactif.

6. **Comparaison de types**  
   Testez différentes affectations de variables en Python : entiers, flottants, chaînes, booléens. Vérifiez le type de chaque variable avec `type()`.

7. **Docstring**  
   Écrivez une courte fonction avec un docstring. Utilisez `help(ma_fonction)` dans l’interpréteur pour voir comment Python affiche la documentation.

8. **Installation d’un package**  
   Installez un package tiers (par ex. `requests`, si vous le pouvez) et lancez un script minimal qui l’importe et affiche la version installée (`requests.__version__`). Appropriez-vous l’outil `pip`.

9. **Experimentation**  
   Jouez avec le mode interactif pour convertir des types (ex. `float -> int`, `str -> int`) et observez les résultats ou erreurs éventuelles.

10. **Première impression**  
   Discutez brièvement (dans un commentaire ou un petit fichier Markdown) de vos premières impressions sur Python par rapport à d’autres langages que vous connaissez déjà.

---

## 2. Using the Python Interpreter

### 2.1. Invoking the Interpreter

1. **Ligne de commande**  
   Lancez l’interpréteur Python sans arguments (`python`) et exécutez quelques lignes. Ensuite, lancez-le avec l’option `-i` sur un script qui fait un `print("Hello")` pour rester en mode interactif après l’exécution du script.

2. **Option -c**  
   Utilisez `python -c` pour exécuter une ligne Python qui affiche « Bonjour » et qui calcule un petit résultat (p. ex. `python -c "print('Bonjour', 2+2)"`).

3. **Fichier vs. Interactif**  
   Comparez le comportement d’une variable `a = 10` définie dans un script et le comportement de la même variable en mode interactif.

4. **Script shell**  
   Créez un petit script exécutable (sur Linux/macOS, en ajoutant `#!/usr/bin/env python3` en en-tête) et lancez-le directement (`./mon_script.py`). Vérifiez les permissions d’exécution.

5. **Arguments**  
   Écrivez un script qui lit `sys.argv` et affiche les arguments passés en ligne de commande. Testez-le avec différents arguments.

6. **Version**  
   Utilisez la commande `python --version` pour afficher la version de Python. Essayez aussi `python -V` sur votre machine.

7. **Changement de version**  
   Si vous avez plusieurs versions installées (ex. `python3.9` et `python3.10`), testez l’invocation de la version spécifique (`python3.9`, `python3.10`, etc.) et observez la différence.

8. **Help**  
   Lancez `python` et tapez `help()`. Parcourez le système d’aide interactif, puis quittez-le.

9. **Profil simple**  
   Exécutez un petit script avec `python -m cProfile mon_script.py` pour avoir un aperçu de temps d’exécution et de profilage.

10. **Exécution depuis un éditeur**  
   Configurez un éditeur ou un IDE (VSCode, PyCharm, Vim, etc.) pour exécuter directement un script Python et comparez l’expérience avec la ligne de commande.

### 2.2. The Interpreter and Its Environment

1. **ENCODAGE**  
   Créez un fichier Python avec des caractères accentués ou des symboles Unicode. Spécifiez l’encodage en en-tête (`# -*- coding: utf-8 -*-`) et exécutez le script. Vérifiez le comportement.

2. **sys.path**  
   Affichez la variable `sys.path` dans l’interpréteur et expliquez brièvement son rôle. Rajoutez un répertoire personnalisé et importez un module qui s’y trouve.

3. **Variables d’environnement**  
   Expérimentez avec la variable d’environnement `PYTHONPATH`. Ajoutez un dossier à `PYTHONPATH` et importez un module qui s’y trouve sans le copier dans le projet principal.

4. **Quitter l’interpréteur**  
   Comparez différentes façons de quitter l’interpréteur (`quit()`, `exit()`, Ctrl+D/Ctrl+Z suivant l’OS). Prenez note des différences éventuelles.

5. **Fonction dir()**  
   Dans l’interpréteur, importez quelques modules (`math`, `os`, `sys`) et utilisez `dir(module)` pour lister leur contenu.

6. **Objets spéciaux**  
   Dans le mode interactif, tapez `__name__`, `__doc__` et notez la différence entre l’espace global de l’interpréteur et celui d’un script.

7. **help(module)**  
   Sur un module standard (ex. `random`), exécutez `help(random)` et explorez quelques fonctions (ex. `randint`, `choice`).

8. **Exécution conditionnelle**  
   Créez un script qui exécute un code uniquement si `__name__ == "__main__"` et un autre code sinon. Lancez-le directement puis importez-le comme module pour voir la différence.

9. **Documentation en ligne**  
   Ouvrez la documentation officielle Python (https://docs.python.org/) pour un module standard et comparez avec la sortie de `help()`.

10. **Histoire des commandes**  
   En mode interactif, exécutez plusieurs commandes, puis utilisez les flèches haut/bas pour naviguer dans l’historique. Expérimentez avec `ctrl+r` (ou l’équivalent) s’il est disponible pour la recherche dans l’historique.

---

## 3. An Informal Introduction to Python

### 3.1. Using Python as a Calculator

1. **Opérations arithmétiques**  
   Expérimentez avec les opérateurs `+`, `-`, `*`, `/`, `//`, `%`, `**`. Notez les différences (par exemple `7/2` vs `7//2`).

2. **Priorité des opérateurs**  
   Testez des expressions combinées (ex. `3 + 4 * 2`, `(3 + 4) * 2`, `3 ** 2 * 2`, etc.) pour vérifier la priorité des opérateurs en Python.

3. **Nombres complexes**  
   Python gère nativement les complexes. Testez `a = 2+3j` et faites quelques opérations (`a.real`, `a.imag`, `abs(a)`, etc.).

4. **Arrondi et conversion**  
   Jouez avec la fonction `round()` et la conversion `int()` sur différents flottants, par exemple `3.14159`, `3.5`, `-2.7`, etc.

5. **Variables vs Expressions**  
   Stockez des expressions dans des variables et observez la différence entre l’affectation et l’évaluation (ex. `x = 2 + 3`, puis `x = x * 2`).

6. **Division par zéro**  
   Essayez d’effectuer une division par zéro pour voir l’erreur retournée par Python et comment elle se nomme.

7. **Convertisseur simple**  
   Écrivez une mini-fonction `convertir_euros_en_dollars(euros, taux=1.10)` qui renvoie la valeur en dollars. Testez plusieurs appels.

8. **Opérations de module**  
   Importez le module `math` et expérimentez avec `math.sqrt()`, `math.factorial()`, `math.log()`, etc.

9. **Chiffres hexadécimaux, octaux, binaires**  
   Expérimentez avec la notation Python pour ces bases (`0x1F`, `0o12`, `0b1010`) et convertissez-les (via `int('0x1F', 16)` par exemple).

10. **Écriture lisible**  
   Pour un nombre comme un million, utilisez le séparateur `_` dans le littéral (ex. `1_000_000`) et confirmez que Python le gère correctement.

### 3.1.2. Text

1. **Chaînes**  
   Expérimentez avec des chaînes entre guillemets simples, doubles, triples. Testez les guillemets triples pour multi-lignes.

2. **Échappement**  
   Essayez les séquences d’échappement `\n`, `\t`, `\\`. Ensuite, testez les chaînes brutes (`r"texte \n brut"`).

3. **Opérations sur les chaînes**  
   Faites de la concaténation (`+`) et de la répétition (`*`). Par exemple, `"py" + "thon"` et `"ha" * 3`.

4. **Indexation et slicing**  
   Prenez une chaîne, par exemple `"Python"`. Affichez `s[0]`, `s[1:3]`, `s[-1]`, etc. Notez la différence entre slicing et indexation.

5. **Immutabilité des chaînes**  
   Tentez de modifier un caractère d’une chaîne (ex. `s[0] = 'J'`) et observez l’erreur. Expliquez pourquoi en commentaire.

6. **Méthodes de chaîne**  
   Testez des méthodes comme `split()`, `strip()`, `upper()`, `replace()`. Créez une phrase et manipulez-la.

7. **Formatage**  
   Expérimentez l’interpolation de chaînes f-string. Ex. `nom = "Alice"; print(f"Bonjour {nom}, 2+2={2+2}")`.

8. **Encodage**  
   Prenez une chaîne avec des caractères spéciaux et encodez-la en UTF-8 (`my_str.encode('utf-8')`). Observez ce que vous obtenez.

9. **Comptage**  
   Écrivez un script qui compte le nombre d’occurrences d’une sous-chaîne dans une chaîne donnée (ex. `count('banana', 'a')` renvoie 3).

10. **Réverser une chaîne**  
   Utilisez le slicing avec pas négatif (`[::-1]`) pour renverser une chaîne. Ex. `"Python"[::-1] -> "nohtyP"`.

### 3.1.3. Lists

1. **Création de liste**  
   Créez une liste de nombres, de chaînes, et mélangez les types. Observez que Python permet l’hétérogénéité.

2. **Index, slicing**  
   Sur la liste `[10, 20, 30, 40, 50]`, accédez à `lst[0]`, `lst[1:3]`, `lst[-2:]`, etc.

3. **Mutation**  
   Remplacez un sous-ensemble de la liste par un autre (ex. `lst[1:3] = [200, 300]`). Comparez la longueur.

4. **Méthodes de liste**  
   Testez `append()`, `extend()`, `insert()`, `pop()`, `remove()`. Vérifiez comment la liste change après chaque opération.

5. **Listes imbriquées**  
   Créez une liste imbriquée (par ex. `[1, [2, 3], 4]`). Accédez à l’élément `3` via une double indexation.

6. **Copie de liste**  
   Comparez une copie par référence (`copie_ref = lst`) et une copie via slicing (`copie_slice = lst[:]`) ou la fonction `copy()`. Montrez comment la première modifie aussi l’original.

7. **List comprehension**  
   Créez une liste de carrés de 0 à 9 en utilisant une list comprehension. Ex. `[i**2 for i in range(10)]`.

8. **Tri**  
   Créez une liste de mots mélangés, puis triez-la avec `sorted()` et la méthode `list.sort()`. Comparez les deux approches.

9. **max, min, sum**  
   Sur une liste numérique, expérimentez ces fonctions intégrées pour trouver la valeur minimale, maximale et la somme.

10. **Conversion**  
   Convertissez un objet itérable en liste, par exemple `tuple`, `range`, ou un générateur, et observez le résultat.

### 3.2. First Steps Towards Programming

1. **Script simple**  
   Écrivez un script qui lit une valeur depuis l’entrée (`input()`), la convertit en entier, l’incrémente de 1, puis l’affiche.

2. **Boucle while**  
   Implémentez une boucle `while` qui compte de 0 à 4, puis s’arrête. Affichez chaque valeur.

3. **Condition simple**  
   Demandez un nombre à l’utilisateur. S’il est positif, affichez « Positif », sinon « Négatif ou nul ». Utilisez `if-else`.

4. **Multiplication continue**  
   Demandez à l’utilisateur de saisir des nombres (dans une boucle infinie). Accumulez le produit. Arrêtez-vous et affichez le résultat lorsque l’utilisateur entre « stop ».

5. **Petite calculatrice**  
   Avec un `while True:`, lisez une opération sous forme de chaîne (ex. `2 + 3`) et évaluez-la (via `eval()` ou en parsant vous-même). Quittez si la chaîne est vide.

6. **Trouver la voyelle**  
   Demandez une lettre à l’utilisateur et affichez si c’est une voyelle ou une consonne. Gérez le cas majuscule/minuscule.

7. **Fonctions de base**  
   Écrivez une fonction `afficher_table_multiplication(n)` qui imprime la table de multiplication de `n`. Testez avec `n=5`.

8. **Docstring**  
   Ajoutez un docstring à votre fonction précédente et testez `help(afficher_table_multiplication)`.

9. **Commentaires**  
   Commentez votre code pour expliquer brièvement chaque bloc. Comparez la lisibilité à des codes non commentés.

10. **Expérience**  
   Combinez plusieurs fonctionnalités (input, conversion, condition, boucle) pour créer un petit jeu de devinette qui demande à l’utilisateur de trouver un nombre secret.  

---

## 4. More Control Flow Tools

### 4.1. if Statements

1. **Conditions multiples**  
   Écrivez un script qui lit un entier et affiche :  
   - « Négatif » si < 0  
   - « Zéro » si == 0  
   - « Positif » si > 0  

2. **Condition imbriquée**  
   Implémentez un test imbriqué : si un nombre est pair, affichez « Pair », sinon si c’est un multiple de 3, affichez « Multiple de 3 », sinon « Autre ».

3. **if court**  
   Utilisez l’opérateur ternaire Python pour affecter une variable en fonction d’une condition (ex. `parite = "pair" if x % 2 == 0 else "impair"`).

4. **Comparaison chaînes**  
   Demandez une saisie utilisateur. Si c’est `"python"`, affichez « Correct », sinon « Mauvais mot ». Comparez la casse (majuscule/minuscule) à l’aide de `lower()`.

5. **Refactor**  
   Prenez un bloc `if-elif-else` et transformez-le en plusieurs blocs if séparés, si logique. Observez la différence dans l’exécution.

6. **Opérateurs logiques**  
   Testez `and`, `or`, `not` avec plusieurs conditions (ex. `if x > 0 and x < 10:`).

7. **Comparaisons enchaînées**  
   Python permet des comparaisons enchaînées : `0 < x < 10`. Vérifiez que ça fonctionne comme attendu.

8. **None**  
   Mettez une variable à `None` et testez la condition `if ma_var is None: ...`. Comparez avec `== None`.

9. **Validation**  
   Écrivez un script qui valide un email rudimentaire. Affichez « valide » si la chaîne contient un `@` et un `.`, sinon « non valide ».

10. **Bonne pratique**  
   Mettez en évidence le respect de la PEP8 dans vos `if` : indentation, espaces, etc.

### 4.2. for Statements

1. **Itération sur une liste**  
   Créez une liste de prénoms et itérez dessus avec `for`. Affichez chaque prénom.

2. **Itération sur une chaîne**  
   Pour la chaîne `"Python"`, utilisez `for c in "Python":` et affichez chaque caractère.

3. **Accumulation**  
   À partir d’une liste de nombres, calculez la somme totale via une boucle `for`. Comparez ensuite avec `sum(liste)`.

4. **Modification d’une liste en itérant**  
   Testez la modification d’une liste en direct dans une boucle for (ajouter/enlever des éléments) et observez les anomalies. Proposez une solution en faisant une copie de la liste ou en construisant une nouvelle liste.

5. **Continue**  
   Dans une boucle for, sautez l’itération courante si la valeur est négative (avec `continue`), sinon affichez-la.

6. **Break**  
   Dans une boucle for, arrêtez tout si vous rencontrez la valeur 0 (avec `break`), sinon affichez la valeur courante.

7. **range**  
   Utilisez `range(10)`, `range(5, 15)`, `range(0, 10, 2)` pour afficher des suites de nombres. Comparez le résultat.

8. **Loop else**  
   Créez une boucle for qui recherche un élément particulier dans une liste. S’il est trouvé, utilisez `break`. Sinon, exécutez le bloc `else` (qui n’est exécuté que si on n’a pas fait de `break`).

9. **Nested loops**  
   Faites deux boucles for imbriquées (ex. pour afficher les paires (i, j) avec i de 0 à 2 et j de 0 à 2).

10. **List comprehension**  
   Transformez une boucle for qui construit une liste en une list comprehension. Comparez la lisibilité.

### 4.3. The range() Function

1. **Itération sur range()**  
   Affichez chaque élément de `range(5)`. Comparez avec `list(range(5))`.

2. **Sauts**  
   Utilisez `range(0, 20, 3)` pour afficher les multiples de 3 inférieurs à 20.

3. **négatif**  
   Utilisez `range(10, 0, -1)` pour compter à rebours.

4. **Opérations**  
   Trouvez la somme de tous les nombres pairs de 0 à 100 en utilisant `range(start, end, step)`.

5. **Indices de liste**  
   Créez une liste de chaînes, puis parcourez-la en utilisant la forme `for i in range(len(liste)):` pour afficher index + valeur.

6. **Effet mémoire**  
   Montrez que `range` ne génère pas la liste en mémoire (testez la taille via `sys.getsizeof(range(...))` vs `sys.getsizeof(list(range(...)))`).

7. **Boucle vide**  
   Testez `range(5, 1)` et observez qu’il n’y a pas d’itération si le step est positif.

8. **Boucle flexible**  
   Écrivez une fonction qui affiche les nombres de `start` à `end` (non inclus) avec un pas `step`, en utilisant `range`.

9. **Comparaison**  
   Comparez la performance (temps d’exécution) d’une boucle `for i in range(...)` vs `while` équivalent.

10. **Indexation créative**  
   Utilisez `enumerate(liste, start=1)` pour afficher un index qui commence à 1 au lieu de 0, en lien avec `range(len(liste))`.

### 4.4. break and continue Statements

1. **Recherche**  
   Dans une liste `[1, 5, 3, 9, 2]`, utilisez une boucle for pour trouver la première occurrence de 9 et faites un `break`.

2. **Filtrage**  
   Dans la même liste, sautez (continue) toute valeur impaire et affichez uniquement les paires.

3. **Mot magique**  
   Demandez des mots à l’utilisateur dans une boucle while. Si l’utilisateur tape « magie », faites un `break`.

4. **Mots interdits**  
   Ayez une liste de mots interdits. Lisez des mots dans un fichier ou en input, si vous en rencontrez un, faites un `break`.

5. **Division protégée**  
   Parcourez une liste de valeurs. Si vous tombez sur 0, ignorez-le (`continue`). Sinon, divisez un nombre donné par cet élément.

6. **Recherche partielle**  
   Dans une liste de chaînes, continuez tant que la chaîne ne contient pas la lettre `"a"`. Dès que vous trouvez une chaîne avec `"a"`, affichez-la et arrêtez (`break`).

7. **Prime**  
   Ecrivez une boucle qui identifie si un nombre est premier. Arrêtez dès qu’on trouve un diviseur (break), sinon c’est premier.

8. **Valeur sentinelle**  
   Dans une boucle while, lisez des entrées utilisateur jusqu’à ce que la valeur « stop » apparaisse (break). Stockez ce qui est saisi dans une liste.

9. **Validation continue**  
   Si une donnée n’est pas valide (ex. pas convertible en float), utilisez `continue` pour redemander la saisie.

10. **Extraction**  
   Dans un texte, parcourez chaque caractère. Si c’est une ponctuation (ex. `, . ; ! ?`), passez (continue). Concaténez les autres dans une nouvelle chaîne.

### 4.5. else Clauses on Loops

1. **Recherche non aboutie**  
   Faites une boucle for pour chercher un élément dans une liste. S’il n’est pas trouvé, exécutez le `else` et affichez « Introuvable ».

2. **Boucle while + else**  
   Comptez un compteur à la baisse jusqu’à 0 dans une boucle `while`. Si le compteur atteint -1 (sortie normale), exécutez `else`.

3. **Question**  
   Expliquez dans un commentaire la différence entre `else` sur une boucle et `else` sur un `if`.

4. **Avertissement**  
   Dans une boucle cherchant un nom, si `break` n’a pas lieu, affichez un message. Sinon, affichez « Trouvé et break ».

5. **Parité**  
   Testez si tous les nombres d’une liste sont pairs. Si vous rencontrez un nombre impair, `break`. Sinon, l’`else` indique « Tous pairs ».

6. **Somme d’un intervalle**  
   Additionnez les nombres de 1 à n dans une boucle for. Si la somme dépasse 100, `break`. Sinon, le `else` affiche la somme finale (<=100).

7. **Boucle infinie**  
   Dans une boucle `while True:`, utilisez `break` si une condition se remplit. Sinon, exécutez un `else`. Analysez pourquoi le `else` se déclenche ou pas.

8. **Recherche string**  
   Parcourez les caractères d’une chaîne. Cherchez `'x'`. Si trouvé, `break`. Sinon (si pas trouvé), `else` signale « Pas de x ».

9. **Verrouillage**  
   Imaginez un code de verrou. Dans une boucle (3 tentatives), si l’utilisateur saisit le bon code, `break`. Sinon, `else` après 3 échecs dit « Verrouillé ».

10. **Question sur l’usage**  
   Discutez dans un commentaire : « Dans quels cas l’`else` sur une boucle est-il réellement utile ? ».

### 4.6. pass Statements

1. **if pass**  
   Écrivez un `if` qui détecte si une variable est négative ou positive, mais dans chaque bloc, mettez simplement `pass`. Vérifiez que le script s’exécute sans erreur.

2. **Boucle while**  
   Dans une boucle `while x < 5: pass`, incrementant x dans un autre thread ou manuellement (si possible) pour simuler un bloc vide.

3. **Boucle for**  
   Parcourez une liste, mais ne faites rien pour chaque élément. Utilisez `pass`.

4. **Structure squelette**  
   Créez le squelette d’une classe `MyClass` avec une méthode `methode()` qui ne fait rien (juste `pass` à l’intérieur).

5. **Placeholder**  
   Utilisez `pass` pour marquer un endroit où vous prévoyez d’ajouter une fonctionnalité plus tard.

6. **Exemple concret**  
   Montrez un cas où vous pouvez utiliser `pass` pour contourner temporairement une exception sans casser la logique du script.

7. **Fonction vide**  
   Définissez une fonction `todo()` qui ne fait rien, juste `pass`. Affichez `todo()` dans un script.

8. **if-elif-else**  
   Implémentez un if-elif-else mais placez `pass` dans chaque bloc. Vérifiez qu’il n’y a pas d’erreur.

9. **Debugger**  
   Montrez comment `pass` peut aider à poser un breakpoint (`import pdb; pdb.set_trace()`) en plein milieu d’un bloc plus vaste.

10. **Équivalent**  
   Identifiez et discutez de l’équivalent de `pass` dans un autre langage (parfois un commentaire vide, ou `{}`).

### 4.7. match Statements (Python 3.10+)

1. **Match simple**  
   Utilisez un `match x:` avec des `case` pour comparer x à plusieurs constantes.

2. **Match tuple**  
   Si x est un tuple `(a, b)`, utilisez `match (a, b): case (0, _): ... case (_, 0): ... etc.`.

3. **Match structuré**  
   Créez un petit dictionnaire `person = {"name": "Alice", "age": 30}` et utilisez `match person:` pour extraire `name` et `age`.

4. **Match ou if-elif**  
   Comparez un match statement à un enchaînement if-elif-else classique. Rédigez deux versions du même code.

5. **Wildcard**  
   Dans un `match`, utilisez `_` comme wildcard, par exemple pour un cas par défaut.

6. **Patern binding**  
   Montrez un exemple où vous faites `case {"name": nom, "age": age}: ...` et réutilisez `nom`, `age` dans le bloc.

7. **Match guard**  
   Utilisez `case {"age": int(x)} if x >= 18:` pour distinguer un adulte d’un mineur.

8. **Liste variable**  
   Faites un match d’une liste de longueur variable, ex. `case [first, *rest]: ...`.

9. **Exhaustivité**  
   Faites un match sur quelques valeurs d’une variable. Ajoutez un `case _:` pour gérer tous les autres cas.

10. **Limitations**  
   Discutez en commentaire : dans quel cas `match` est-il préférable à un if-elif-else ?

### 4.8. Defining Functions

1. **Basique**  
   Définissez une fonction `saluer(nom)` qui affiche « Bonjour nom ! » et testez-la.

2. **Retour**  
   Définissez une fonction `carré(x)` qui renvoie x². Appelez-la et affichez le résultat.

3. **Plusieurs arguments**  
   Écrivez une fonction `somme(a, b, c)` qui renvoie la somme des trois. Testez avec différentes valeurs.

4. **Valeur par défaut**  
   Créez une fonction `exposant(base, puissance=2)` qui calcule base^puissance. Testez-la avec un seul argument ou deux arguments.

5. **Nom des arguments**  
   Dans une fonction `creer_utilisateur(nom, age=20, ville="Paris")`, testez l’appel en utilisant des arguments nommés (ex. `creer_utilisateur(age=30, nom="Bob")`).

6. **Docstring**  
   Écrivez une fonction avec un docstring expliquant son usage. Vérifiez en exécutant `help(ma_fonction)`.

7. **Commentaires vs docstring**  
   Comparez un commentaire classique #… et un docstring """…""". Décrivez leurs usages respectifs.

8. **Scope**  
   Montrez un exemple où une variable locale masque une variable globale du même nom. Expliquez comment éviter les conflits.

9. **Fonctions anonymes**  
   Définissez rapidement une fonction lambda pour calculer le carré d’un nombre, ex. `lambda x: x*x`. Passez-la en argument d’une fonction `map`.

10. **Fonction factorielle**  
   Codez une fonction récursive `factorielle(n)`. Testez sur quelques valeurs.

---

## 5. Data Structures

### 5.1. More on Lists

1. **Stack**  
   Utilisez une liste comme pile (`append()` et `pop()`). Empilez quelques nombres, dépilez-en et affichez le résultat.

2. **Queue**  
   Utilisez une liste comme file d’attente (`pop(0)`). Montrez le coût de cette opération sur des grandes listes et parlez de `collections.deque`.

3. **List comprehension**  
   Construisez une liste `[i*2 for i in range(10)]`. Comparez avec la même chose en boucle for.

4. **Nested list comprehension**  
   Créez une liste de paires `(i, j)` pour i dans [1,2,3] et j dans [4,5,6].

5. **del**  
   Supprimez un élément d’une liste par son index (ex. `del liste[2]`) et affichez la liste résultante.

6. **Tri**  
   Créez une liste mixte de chaînes. Triez-la avec `sorted(liste, key=len)` pour classer par longueur de chaîne.

7. **Index**  
   Trouvez l’index d’un élément particulier avec `liste.index(x)`. Gérez le cas où x n’est pas présent (try/except).

8. **Reversed**  
   Utilisez `reversed(liste)` pour parcourir la liste à l’envers sans la modifier définitivement.

9. **Copie profonde**  
   Créez une liste de listes (ex. `[[1,2],[3,4]]`) et utilisez `copy.deepcopy()` pour en faire une copie. Montrez que modifier l’original n’affecte pas la copie.

10. **Liste => Chaîne**  
   Transformez une liste de mots en une seule chaîne séparée par des virgules (`",".join(liste_mots)`).

### 5.2. The del statement

1. **del sur variable**  
   Définissez `x = 10`, puis `del x`. Tentez d’afficher `x` après. Observez l’erreur.

2. **del sur liste**  
   Créez une liste `[10, 20, 30, 40]`. Supprimez l’élément index 2 via `del`. Affichez la liste.

3. **Slice**  
   Supprimez un sous-ensemble d’une liste (ex. `del liste[1:3]`) et affichez le résultat.

4. **Effacer la liste entière**  
   Testez `del liste[:]` pour vider la liste, puis `print(liste)`.

5. **del sur dictionnaire**  
   Dans un dictionnaire `d = {"a": 1, "b": 2}`, faites `del d["b"]`. Vérifiez qu’il ne reste plus que `{"a": 1}`.

6. **Classe**  
   Créez une classe avec un attribut, instanciez-la, puis `del instance.attribut`. Vérifiez que l’attribut n’existe plus.

7. **Nom multiple**  
   Faites `a = [1,2,3]`, `b = a`. Puis `del a`. Vérifiez si `b` continue de référencer la liste.

8. **del vs. remove**  
   Comparez `del liste[0]` et `liste.remove(liste[0])`. Dans quel cas l’utiliser ?

9. **Garbage collector**  
   Expliquez en commentaire comment `del` affecte (ou pas) le ramasse-miettes de Python.

10. **Exemple concret**  
   Donnez un scénario où on doit vraiment utiliser `del` pour éviter des références inutiles en mémoire.

### 5.3. Tuples and Sequences

1. **Création de tuple**  
   Créez un tuple `(1, 2, 3)`. Affichez ses éléments.

2. **Immutabilité**  
   Essayez de modifier un élément du tuple. Observez l’erreur.

3. **Unpacking**  
   Faites `a, b, c = (1, 2, 3)` et vérifiez les variables.

4. **Retour multiple**  
   Écrivez une fonction qui renvoie un tuple `(valeur, statut)`. Récupérez les deux dans des variables distinctes.

5. **Swapping**  
   Définissez `a = 10, b = 20`. Échangez-les via `a, b = b, a`.

6. **Indexation**  
   Sur un tuple `t = (4, 5, 6)`, accédez à `t[1]`. Essayez `t[1] = 7` et notez l’erreur.

7. **Constructeur**  
   Créez un tuple à partir d’une liste ou d’une range (ex. `tuple(range(5))`).

8. **In**  
   Testez si un élément est dans un tuple : `if 3 in t: ...`.

9. **Tuple vide**  
   Créez un tuple vide `()`. Vérifiez son type.

10. **Avantage**  
   Dans un commentaire, discutez des cas où un tuple est préférable à une liste.

### 5.4. Sets

1. **Création**  
   Créez un set `s = {1, 2, 3}` et affichez-le.

2. **Duplication**  
   Ajoutez des éléments dupliqués (ex. `s.add(2)`) et vérifiez la structure unique du set.

3. **Opérations ensemblistes**  
   Créez deux sets et faites `union`, `intersection`, `difference`, `symmetric_difference`.

4. **Ajout / Retrait**  
   Testez `s.add(4)`, `s.remove(2)` et affichez le set résultant.

5. **Iter**  
   Parcourez le set dans une boucle for. Notez l’ordre d’affichage (non garanti).

6. **Frozenset**  
   Créez un `frozenset([1,2,3])` et essayez de le modifier (erreur).

7. **in**  
   Vérifiez la présence d’un élément : `if 1 in s:`.

8. **Set comprehension**  
   Créez un set `{i*i for i in range(5)}`. Comparez avec une list comprehension.

9. **Égalité**  
   Comparez deux sets avec `==`. Ex. `{1,2,3} == {3,2,1}`.

10. **Cas d’usage**  
   Décrivez (en commentaire) une situation où l’utilisation d’un set est plus efficace que d’autres structures.

### 5.5. Dictionaries

1. **Création**  
   Créez un dictionnaire `d = {"nom": "Alice", "age": 30}` et affichez `d["nom"]`.

2. **Ajouter / modifier**  
   Ajoutez une nouvelle clé `d["ville"] = "Paris"`. Modifiez `d["age"] = 31`.

3. **Suppression**  
   Utilisez `del d["age"]` et vérifiez que l’élément est parti.

4. **.get()**  
   Utilisez `d.get("age", 0)` pour retourner 0 si la clé n’existe pas.

5. **.items()**  
   Parcourez le dictionnaire avec `for k, v in d.items(): ...`.

6. **.keys() / .values()**  
   Affichez toutes les clés (`.keys()`) et toutes les valeurs (`.values()`).

7. **Constr. alternative**  
   Créez un dict via `dict(nom="Bob", age=25)`. Comparez avec la syntaxe accolades.

8. **Defaultdict / Counter**  
   Montrez un exemple simple d’utilisation de `collections.defaultdict(int)` ou `collections.Counter`.

9. **Tri par clé**  
   Créez un dict, puis récupérez une liste de paires `(clé, valeur)` triées par clé. Ex. `sorted(d.items())`.

10. **Mise à jour**  
   Fusionnez deux dictionnaires (ex. `d.update(d2)`). Comparez avec l’opérateur `|` (Python 3.9+).

### 5.6. Looping Techniques

1. **.items()**  
   Faites une boucle `for clé, valeur in d.items(): print(clé, valeur)` sur un dict.

2. **.enumerate()**  
   Sur une liste de noms, utilisez `enumerate()` pour afficher indice + nom.

3. **zip**  
   Avec deux listes, zippez-les pour créer des paires. Itérez et affichez ces paires.

4. **renversé**  
   Utilisez `reversed()` sur une liste ou un range pour itérer en sens inverse.

5. **Tri personnalisé**  
   Triez une liste d’objets par un critère (longueur de string, par ex.) en utilisant `sorted(liste, key=...)`.

6. **Dictionnaire trié**  
   Itérez sur les clés triées d’un dictionnaire. Ex. `for k in sorted(d): ...`.

7. **zip + enumerate**  
   Combinez `enumerate` et `zip` pour parcourir plusieurs listes en même temps avec des indices.

8. **Compréhension**  
   Créez un dict via dict comprehension : `{x: x*x for x in range(5)}`.

9. **inversion dict**  
   Pour un dict `{1:'a', 2:'b'}`, utilisez un dict comprehension pour inverser : `{'a':1, 'b':2}`.

10. **Nom de variable**  
   Parlez de la convention PEP8 pour nommer l’itérateur (`for i in range(...)`) vs. plus explicite (`for index in range(...)`).

### 5.7. More on Conditions

1. **Comparaisons multiples**  
   Testez `x in liste` vs `x not in liste`. Testez `if x is None:` vs `if x == None:`.

2. **Opérateurs chainés**  
   Expérimentez `0 < x < 10`, `x == 0 or x == 10`, etc.

3. **is vs ==**  
   Montrez la différence entre égalité de valeur et égalité d’identité (avec de petits entiers ou petits strings).

4. **bool()**  
   Vérifiez la valeur booléenne de listes vides, chaînes vides, 0, None, etc.

5. **any / all**  
   Sur une liste de booléens, testez `any(liste)` et `all(liste)`.

6. **Comparaison mixte**  
   Comparez des types différents (ex. `"3" < 4`) pour voir si Python l’autorise ou lève une exception.

7. **Condition courte**  
   Utilisez l’opérateur ternaire : `result = "ok" if x > 0 else "nok"`.

8. **Conditions successives**  
   Montrez comment factoriser plusieurs conditions (if-elif-else) en expressions plus simples.

9. **None**  
   Faites un test explicite pour None : `if variable is not None:`.

10. **PEP 8**  
   Discutez dans un commentaire : comment la PEP 8 recommande-t-elle de gérer les espaces autour des opérateurs de comparaison ?

### 5.8. Comparing Sequences and Other Types

1. **Listes**  
   Comparez `[1,2,3] < [1,2,4]`. Expliquez pourquoi.

2. **Longueur différente**  
   Comparez `[1,2,3] < [1,2,3,4]`. Résultat ?

3. **Chaînes**  
   Comparez `"abc" < "abd"` et `"abc" < "abcd"`.

4. **Tuples**  
   Comparez `(1,2) < (1,3)` et `(1,2) < (1,2,0)`.

5. **Hétérogène**  
   Essayez de comparer `[1,2] < "abc"`. Python 3 refuse la comparaison entre types incompatibles (TypeError).

6. **Tri mixte**  
   Créez une liste de tuples (ex. `[(1, 'b'), (1, 'a'), (0, 'c')]`) et triez-la par ordre naturel. Observez la priorité.

7. **Tri multiple**  
   Triez la même liste avec un `key` personnalisé : d’abord par la première valeur, ensuite la deuxième.

8. **min / max**  
   Calculez `min` et `max` sur une liste de chaînes ou de tuples. Observez le résultat.

9. **égalité**  
   Vérifiez `[1,2,3] == [1,2,3]` et `[1,2,3] == [1,3,2]`.

10. **Exemple**  
   Décrivez un cas où la comparaison lexicographique est utile (ex. tri de versions, tri de mots, etc.).

---

## 6. Modules

### 6.1. More on Modules

1. **Module perso**  
   Créez un fichier `mon_module.py` avec une fonction `salut()`. Importez-le dans un autre fichier `main.py` et exécutez.

2. **Exécution directe**  
   Ajoutez une section `if __name__ == "__main__":` dans `mon_module.py`. Faites-le s’exécuter en script et importez-le pour constater la différence.

3. **Recherche du module**  
   Affichez `sys.path` dans `main.py`. Vérifiez que votre module se trouve dans l’un de ces chemins ou dans le répertoire courant.

4. **pyc**  
   Exécutez votre module. Cherchez les fichiers `.pyc` dans `__pycache__`. Expliquez leur rôle.

5. **Alias d’import**  
   Importez `mon_module` sous un alias `import mon_module as mm`. Appelez `mm.salut()`.

6. **from … import**  
   Faites `from mon_module import salut`. Appelez directement `salut()`.

7. **Import circulaire**  
   Créez deux modules qui s’importent mutuellement. Observez le problème et discutez d’une solution.

8. **Ré-exécution**  
   Après avoir importé un module, modifiez son code. Réimportez-le. Notez que le code ne se re-charge pas automatiquement (il faut redémarrer l’interpréteur ou reloader).

9. **dir()**  
   Utilisez `dir(mon_module)` pour afficher le contenu exporté. Comparez avec `__all__` si vous l’avez défini.

10. **Doc module**  
   Placez une docstring au début de `mon_module.py`. Consultez-la via `mon_module.__doc__`.

### 6.2. Standard Modules

1. **math**  
   Importez `math` et testez `math.sin(0)`, `math.sqrt(16)`. Lisez rapidement la doc.

2. **random**  
   Générez un nombre aléatoire entre 1 et 10 via `random.randint(1, 10)`. Générez une liste mélangée via `random.shuffle(...)`.

3. **statistics**  
   Calculez la moyenne et l’écart-type d’une liste de nombres via `statistics.mean()` et `statistics.pstdev()`.

4. **os**  
   Affichez le répertoire courant via `os.getcwd()`, listez les fichiers avec `os.listdir()`.

5. **sys**  
   Affichez `sys.platform`, `sys.version`, `sys.argv`, etc. Comparez à votre environnement.

6. **time**  
   Mesurez le temps d’exécution d’une boucle en microsecondes. Comparez avec `time.perf_counter()`.

7. **datetime**  
   Obtenez la date et l’heure actuelles. Formatez-les en chaîne (`strftime`).

8. **json**  
   Sérialisez un dictionnaire en JSON (`json.dumps`) puis désérialisez (`json.loads`).

9. **pathlib**  
   Testez la manipulation de chemins et de fichiers via `pathlib.Path`.

10. **import this**  
   Dans l’interpréteur, tapez `import this` pour lire le Zen de Python.  

### 6.3. The dir() Function

1. **dir sur module**  
   Appliquez `dir(math)` et inspectez quelques fonctions.

2. **dir sans argument**  
   Lancez `dir()` dans l’interpréteur pour voir les variables globales.

3. **Filtrage**  
   Convertissez la liste retournée par `dir(...)` en un tri alphabétique et cherchez un nom précis.

4. **Attribut spécial**  
   Dans un module perso, définissez `__all__ = ["salut"]` et comparez `dir(mon_module)` avec et sans `__all__`.

5. **Inspect**  
   Combinez `dir(math)` et `help(math.sqrt)` pour comprendre un module en profondeur.

6. **Objet custom**  
   Créez une classe avec quelques méthodes. Instanciez-la et faites `dir(instance)` pour voir les attributs/méthodes.

7. **Objet standard**  
   Faites `dir("chaîne")`. Comparez la liste de méthodes à la doc officielle.

8. **dir vs vars**  
   Testez `vars()` (qui renvoie un dict local) et comparez avec `dir()`.

9. **dir sur builtins**  
   Faites `import builtins` et `dir(builtins)`. Voyez toutes les fonctions intégrées.

10. **Exploration**  
   Décrivez un scénario où `dir()` vous a aidé à découvrir le contenu d’un module inconnu.

### 6.4. Packages

1. **Création package**  
   Créez une arborescence avec un dossier `mon_paquet/`, un fichier `__init__.py` à l’intérieur, et un module `module_a.py`. Importez ce package.

2. **Import ***  
   Dans `__init__.py`, importez et exportez certaines fonctions via `__all__`. Vérifiez `from mon_paquet import *`.

3. **Intra-package**  
   Dans `module_b.py`, importez `module_a` via une import relative (`from . import module_a`) et appelez une fonction.

4. **Arborescence multiple**  
   Créez `mon_paquet/sous_paquet/__init__.py` avec un module dedans. Importez-le depuis l’extérieur.

5. **Exécution**  
   Lancez un module package en script : `python -m mon_paquet.module_a`. Comparez `__name__`.

6. **Organisation**  
   Ajoutez un package `utils` et `models`. Discutez dans un commentaire de l’organisation de code en Python.

7. **__main__.py**  
   Dans un package, créez un `__main__.py`. Lancez-le avec `python -m mon_paquet`. Notez le comportement.

8. **Données partagées**  
   Faites un fichier `config.py` dans le package. Importez-le depuis deux modules du package pour y stocker/partager des variables.

9. **Chemins**  
   Ajoutez un chemin personnalisé. Utilisez `PYTHONPATH` ou modifiez `sys.path` dans un script. Importez votre package depuis cet emplacement.

10. **Setup**  
   Discutez brièvement de la création d’un paquet installable (avec `setup.py` ou `pyproject.toml`) pour distribution.

---

## 7. Input and Output

### 7.1. Fancier Output Formatting

1. **f-string**  
   Formatez un message avec des variables `nom` et `âge`. Utilisez `f"Bonjour {nom}, tu as {âge} ans"`.

2. **format()**  
   Reprenez l’exercice précédent avec `"Bonjour {}, tu as {} ans".format(nom, âge)`.

3. **Alignement**  
   Affichez un tableau avec colonnes alignées. Ex. `f"{valeur:10} | {carré:10}"`.

4. **Précision**  
   Affichez un flottant avec 2 décimales : `f"{3.14159:.2f}"`.

5. **Remplissage**  
   Testez la syntaxe `f"{nombre:05d}"` pour afficher un entier sur 5 digits, complété de zéros.

6. **Ancien format**  
   Comparez l’usage de l’opérateur `%` : `"%s - %d" % ("Texte", 10)`. Discutez des inconvénients.

7. **Largeur dynamique**  
   Avec `format()`, testez `"{:{}d}".format(42, 5)` pour un padding dynamique. Ou en f-string : `f"{42:{5}d}"`.

8. **Nom des champs**  
   Utilisez `"Coordonnées: x={x}, y={y}".format(x=10, y=20)` pour clarifier l’association.

9. **Conversion**  
   Montrez l’usage de `!r`, `!s`, `!a` dans une f-string pour afficher la représentation brute, etc.

10. **Table**  
   Créez un tableau formaté de la multiplication de 1 à 5, aligné en colonnes.

### 7.2. Reading and Writing Files

1. **Écriture simple**  
   Ouvrez un fichier en écriture (`with open("test.txt", "w") as f:`) et écrivez quelques lignes.

2. **Lecture**  
   Lisez ce fichier et affichez son contenu ligne par ligne.

3. **Append**  
   Ouvrez le fichier en mode append et ajoutez une nouvelle ligne. Relisez pour vérifier.

4. **Modes binaire**  
   Ouvrez un fichier image en binaire (`"rb"`) et lisez quelques octets. Affichez-les en hexadécimal.

5. **Gestion d’erreur**  
   Tentez d’ouvrir un fichier inexistant en lecture. Gérez l’exception `FileNotFoundError`.

6. **Encodage**  
   Écrivez un fichier texte en UTF-8 contenant des accents. Rélisez-le pour vérifier que tout est correct.

7. **Json**  
   Sérialisez un dictionnaire en JSON dans un fichier. Puis désérialisez-le pour récupérer vos données.

8. **Boucle sur fichier**  
   Lisez le fichier ligne par ligne dans une boucle `for line in f:`. Comptez le nombre de lignes.

9. **Flush**  
   Testez l’écriture bufferisée (sans close). Utilisez `f.flush()` et vérifiez la taille du fichier après.

10. **Context manager**  
   Expliquez pourquoi on utilise `with open("fichier.txt") as f:` plutôt que d’ouvrir/fermer manuellement.

---

*(La suite suivra le même principe : 10 exercices par grande section. Étant donné le volume important, vous trouverez ci-dessous les grandes lignes d’exercices pour les sections 8 à 16. Pour un document encore plus détaillé, vous pourrez extrapoler de la même façon.)*

---

## 8. Errors and Exceptions

1. **Syntax Error**  
   Provoquez une syntax error (oubliez une parenthèse). Exécutez le script, notez le message.
2. **Try-Except**  
   Écrivez un bloc try-except pour gérer un ZeroDivisionError.
3. **Except multiples**  
   Gérez plusieurs exceptions (ValueError, TypeError) dans le même bloc.
4. **Else**  
   Utilisez `else` dans un bloc try-except, exécuté si pas d’exception.
5. **Finally**  
   Ajoutez un bloc `finally` pour nettoyer des ressources (fichier, connexion).
6. **Raise**  
   Levez une exception personnalisée via `raise Exception("Message")`.
7. **Assertion**  
   Utilisez `assert condition, "Message"` pour vérifier une hypothèse.
8. **Chainage**  
   Gérez un bloc qui re-lance une exception après l’avoir interceptée (`raise e`).
9. **Custom Exception**  
   Créez une classe d’exception perso `class MyError(Exception): pass`.
10. **Exception Note** (3.11+)  
   Ajoutez une note via `e.add_note("Contexte supplémentaire")` et inspectez la.

---

## 9. Classes

1. **Classe simple**  
   Créez une classe `Person` avec un constructeur `__init__(self, nom, age)`.
2. **Méthode**  
   Ajoutez une méthode `se_presenter()` qui affiche les infos de la personne.
3. **Attributs**  
   Modifiez un attribut (`self.age`) depuis l’extérieur. Vérifiez que c’est autorisé.
4. **Héritage**  
   Créez une sous-classe `Etudiant(Person)`. Ajoutez-lui un champ `ecole`.
5. **Méthode redéfinie**  
   Redéfinissez `se_presenter()` dans `Etudiant`. Appelez le parent via `super()`.
6. **Propriétés**  
   Ajoutez une property `age` pour contrôler la valeur (pas négative).
7. **Méthodes statiques / de classe**  
   Définissez `@staticmethod` ou `@classmethod` pour créer une instance à partir d’un dict.
8. **Méthodes spéciales**  
   Implémentez `__str__` ou `__repr__` pour afficher la personne.
9. **Opérateur**  
   Implémentez `__eq__` pour comparer deux `Person`.
10. **Itérateur**  
   Créez une classe qui implémente `__iter__` et `__next__` pour itérer sur une collection interne.

---

## 10. Brief Tour of the Standard Library

1. **subprocess**  
   Lancez une commande système via `subprocess.run(["ls"])` ou équivalent Windows.
2. **glob**  
   Listez tous les fichiers `.py` dans le répertoire courant.
3. **sys.exit**  
   Testez la fin de programme via `sys.exit(0)`.
4. **re**  
   Recherchez tous les mots commençant par `p` dans une phrase via `re.findall(r"\bp\w+", texte)`.
5. **math**  
   Calculez la racine carrée, la factorielle et la fonction exp/log.
6. **urllib**  
   Téléchargez le contenu HTML d’une page (si autorisé) via `urllib.request.urlopen`.
7. **datetime**  
   Calculez la différence entre deux dates.
8. **gzip**  
   Compressez un fichier texte en gzip, puis décompressez-le.
9. **timeit**  
   Mesurez le temps d’exécution d’une petite fonction via `python -m timeit`.
10. **unittest**  
   Écrivez un test unitaire minimal avec le module `unittest`.

---

## 11. Brief Tour of the Standard Library — Part II

1. **string**  
   Utilisez `string.capwords` pour mettre en majuscule la première lettre de chaque mot.
2. **tpllib / jinja2**  
   Si vous avez `jinja2`, testez un petit template. Sinon, utilisez `string.Template`.
3. **struct**  
   Manipulez des données binaires en pack/unpack avec `struct`.
4. **threading**  
   Créez deux threads qui affichent des compteurs.
5. **logging**  
   Configurez un logger de base et loggez quelques messages d’info et d’erreur.
6. **weakref**  
   Expérimentez les références faibles sur un objet pour voir quand il est collecté.
7. **functools**  
   Essayez `functools.lru_cache` sur une fonction récursive.
8. **itertools**  
   Utilisez `itertools.product` pour cartésien, `itertools.permutations`, etc.
9. **decimal**  
   Comparez les calculs en `decimal.Decimal` vs float (par ex. 0.1+0.2).
10. **fractions**  
   Utilisez `Fraction` pour manipuler des rationnels exacts.

---

## 12. Virtual Environments and Packages

1. **Création venv**  
   Créez un environnement virtuel `python -m venv env`. Activez-le.
2. **pip freeze**  
   Installez un package dans l’environnement. Utilisez `pip freeze` pour lister.
3. **Désactivation**  
   Désactivez l’environnement virtuel. Vérifiez que `which python` pointe à la version système.
4. **requirements**  
   Générez un fichier `requirements.txt`. Testez l’installation dans un nouvel env.
5. **Package local**  
   Installez un package local (`pip install -e .`) depuis un setup minimal.
6. **Mise à jour**  
   Mettez à jour un package (ex. `pip install --upgrade`).
7. **Désinstallation**  
   Désinstallez un package via `pip uninstall`.
8. **conda**  
   (Optionnel) Si vous utilisez conda, créez un env conda et comparez.
9. **Poetry**  
   (Optionnel) Testez la création d’un projet avec Poetry. Comparez à venv classique.
10. **ISOlation**  
   Discutez en commentaire : pourquoi l’isolation d’un venv est-elle cruciale en Python ?

---

## 13. What Now?

1. **Documentation**  
   Trouvez 2 ressources officielles ou livres recommandés pour aller plus loin.
2. **Projets perso**  
   Listez 2 idées de projets perso en Python.
3. **Frameworks**  
   Choisissez un framework Web (Django, Flask) à explorer ensuite.
4. **Data Science**  
   Si intérêt, essayez d’installer `numpy`, `pandas` et de tester un script minimal.
5. **Open Source**  
   Identifiez un projet open source Python auquel contribuer.
6. **Coding style**  
   Installez un linter (flake8, black) et essayez-le sur un de vos scripts.
7. **Tests**  
   Explorez la documentation de `pytest`.
8. **CI**  
   Configurez un pipeline GitHub Actions ou GitLab CI pour vos projets Python.
9. **Packaging**  
   Créez un petit package et publiez-le sur TestPyPI.
10. **Communauté**  
   Rejoignez une communauté Python locale ou en ligne (Meetup, Discord, etc.).

---

## 14. Interactive Input Editing and History Substitution

1. **rlwrap**  
   Sur certains systèmes, lancez Python avec `rlwrap python` pour l’édition en ligne (si besoin).
2. **Tab completion**  
   Activez la complétion tab (dans un shell supporté). Tapez une variable partielle et appuyez Tab.
3. **History**  
   Naviguez dans l’historique avec les flèches. Modifiez une commande précédente.
4. **.pythonrc**  
   Créez un fichier `~/.pythonrc` avec quelques alias ou import automatiques. Lancez Python pour voir l’effet.
5. **readline**  
   Vérifiez si votre Python est compilé avec libreadline pour l’historique.
6. **IPython**  
   Installez IPython. Comparez l’expérience d’édition, d’historique et de complétion.
7. **bpython**  
   Testez `bpython` comme alternative interactive.
8. **Magic commands**  
   Si IPython, essayez `%run`, `%time`, `%whos`.
9. **Multiline**  
   Dans IPython/bpython, éditez une fonction multiline interactivement. Comparez au shell standard.
10. **Configuration**  
   Creusez la configuration d’IPython dans `~/.ipython/` (ou autre). Ajoutez des raccourcis ou extensions.

---

## 15. Floating-Point Arithmetic: Issues and Limitations

1. **0.1 + 0.2**  
   Calculez `0.1 + 0.2`. Comparez le résultat à `0.3`.
2. **Affichage**  
   Affichez 0.3 avec 20 décimales (`f"{0.3:.20f}"`).
3. **Decimal**  
   Répétez l’opération `0.1 + 0.2` avec `decimal.Decimal`, comparez.
4. **Erreur d’arrondi**  
   Montrez un exemple concret où l’erreur d’arrondi s’accumule dans une boucle.
5. **EPS**  
   Trouvez la plus petite différence détectable, par ex. `import sys; sys.float_info.epsilon`.
6. **Forme exponentielle**  
   Expérimentez des grands nombres (`1e308`) et regardez le dépassement (`inf`).
7. **Comparaison**  
   Implémentez une fonction `float_equals(a, b, tol=1e-9)` pour comparer deux floats.
8. **Fraction**  
   Comparez `Fraction(1, 3)` avec 0.3333…  
9. **Binary floating**  
   Expliquez brièvement pourquoi 0.1 n’a pas de représentation binaire exacte.
10. **Bonnes pratiques**  
   Discutez quand préférer `decimal` ou `fractions` à float.

---

## 16. Appendix

### 16.1. Interactive Mode

1. **Options**  
   Testez `python -i script.py` pour rester en interactif après un script.
2. **Erreur**  
   Dans l’interpréteur, provoquez une erreur, lisez la traceback.  
3. **Exécutable**  
   Créez un script avec le shebang `#!/usr/bin/env python3`, rendez-le exécutable et lancez-le.
4. **Startup file**  
   Définissez `PYTHONSTARTUP` pointant vers un script d’initialisation (ex. `.pythonrc`).
5. **Customization modules**  
   Découvrez `sitecustomize` ou `usercustomize`.  
6. **sys.ps1**  
   Personnalisez l’invite Python (`sys.ps1 = ">>> "`) en interactif.  
7. **Automatisation**  
   Appelez un script Python depuis un autre script shell. Comparez `subprocess`.  
8. **Quit**  
   Testez les différentes manières de quitter (`exit()`, `quit()`, Ctrl+D).  
9. **Historique**  
   Montrez où Python stocke l’historique (`~/.python_history`).  
10. **Limites**  
   Discutez quand il vaut mieux passer en script ou IPython qu’en mode interactif pur.

---

### Remarques finales

- Vous avez désormais 10 exercices par section (et sous-section principale) pour vous entraîner. Certains sont plus conceptuels (discussion, comparaison) et d’autres plus pratiques (implémentation directe).  
- En tant que développeur expérimenté venant d’un autre langage, ces exercices vous permettront de prendre en main les particularités de Python (syntaxe, écosystème, outillage).  
- N’hésitez pas à adapter les exercices à vos centres d’intérêt (Data Science, Web, automatisation système, etc.).  
- Bonne pratique !