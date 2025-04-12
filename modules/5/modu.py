# ### 5. Module Footprint via `dir()`
# - Create a module with multiple functions, classes, and variables.
# - From another script, retrieve the list of names available via the `dir()` function on that module.
# - Comment on which names show up, which are hidden, etc.
#
# **Key Points:** Discovering and introspecting a module, exploring the namespace.
#
# ---

# Variables
name = "Alice"
_age = 30  # starts with _ → considered "private"

# Function
def greet():
    return f"Hello, {name}!"

# Class (optional – super simple version)
class Person:
    def __init__(self, name):
        self.name = name
