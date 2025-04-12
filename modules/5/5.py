# ### 5. Module Footprint via `dir()`
# - Create a module with multiple functions, classes, and variables.
# - From another script, retrieve the list of names available via the `dir()` function on that module.
# - Comment on which names show up, which are hidden, etc.
#
# **Key Points:** Discovering and introspecting a module, exploring the namespace.
#
# ---

import modu

print(dir())
print(dir(modu))