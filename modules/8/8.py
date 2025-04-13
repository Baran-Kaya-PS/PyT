# ### 8. Handling an Import Error
# - Try importing a non-existent module.
# - Handle the resulting exception and display a user-friendly message.
# - Optionally, offer an alternative if the module is not found.
#
# **Key Points:** `ModuleNotFoundError`, error handling, code robustness.
#
# ---

import sys
path = r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\external modules"
sys.path.append(path)
try :
    import nonexistantmodule
except:
    print("L'import n'existe pas")

print("suite du programme")