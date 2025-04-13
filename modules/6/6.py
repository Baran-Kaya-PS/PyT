# ### 6. Using the `sys` Module
# - Import the `sys` module.
# - Print information about the Python version in use and the import search path (`sys.path`).
# - Discuss how Python locates modules.
#
# **Key Points:** Exploring `sys`, implications for imports.

import sys

for path in sys.path: #sys.path is a list
    print(path)

# use case is sys.path.append(path) to dynamically import modules

# use case exemple
# import os
# import sys
#
# DB_EXISTS = os.path.exists("data/my_database.db")
#
# if not DB_EXISTS:
#     # ➕ Ajouter dynamiquement le dossier contenant ton module de setup
#     sys.path.append("setup_utils")
#
#     # 🧠 Importer et exécuter le setup
#     import db_initializer
#     db_initializer.create_database()
#
#     # 🧼 Nettoyer le namespace si tu veux
#     sys.path.remove("setup_utils")
#     del db_initializer