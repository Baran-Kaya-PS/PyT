# ### 21. Advanced System Functions
# - Look into standard modules (like `os`, `pathlib`, etc.) that can interact with your project structure.
# - Implement logic to check if a module exists (without actually importing it).
# - Argue when to use these functions for managing imports or packages.
#
# **Key Points:** More advanced exploration, OS–Python interactions.
#
# ---
import importlib.util
import os # https://docs.python.org/3.11/library/os.html
import pkgutil
from pathlib import Path # https://docs.python.org/3.11/library/pathlib.html
pat = r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\modules\21"
print(os.path.exists(pat))

print(importlib.util.find_spec("lib1.modu_a"))

import pkgutil

for importer, modname, ispkg in pkgutil.iter_modules([pat]):
    print(f"Nom du module: {modname}, est un package: {ispkg}")


