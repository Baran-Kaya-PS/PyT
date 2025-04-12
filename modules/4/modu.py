# ### 4. `if __name__ == "__main__":` Condition
# - In the module, place a conditional block that runs some test or prints output only if the file is called directly.
# - Make sure this test does **not** run when you import the module.
#
# **Key Points:** Structuring a file for dual usage (script and module).
#
# ---

if __name__ == "__main__": #
    print("you can only see this on mody.py")