# ### 7. Modifying `sys.path`
# - Create a directory outside the default search path and place a module with a function there.
# - Modify `sys.path` at runtime to include the new directory.
# - Show that you can now import the module and call its function.
#
# **Key Points:** Import paths, customizing import behavior, potential impacts.
#
# ---

import sys
path = r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\external modules"
sys.path.append(path)
import bonus
bonus.surprise()