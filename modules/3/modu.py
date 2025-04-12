# ### 3. The `__name__` Variable and Direct Execution
# - In the module, print the value of the `__name__` variable.
# - Run the module directly, then import it from another script.
# - Observe the difference and explain why.
#
# **Key Points:** The difference between `__main__` and the module name, script vs. library logic.
#
# ---

var1 = 3
l = "Baran James Christian".split()

def b():
    for v in l:
        print(v)

print(__name__) # useful for debug