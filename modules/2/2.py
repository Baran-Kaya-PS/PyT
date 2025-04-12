# ### 2. Import Spécifique et Alias
# - Dans votre module, ajoutez plusieurs fonctions ou variables.
# - Dans un script séparé, importez-en une seule sous un autre nom (alias).
# - Montrez que vous pouvez l’appeler via cet alias, sans exposer le reste du module.
#
# **Points clés :** `from ... import ... as ...`, gestion du namespace.

from modu import var1,l as names, b as printnames

names.append("Jean")

printnames()