# 25 Exercises to Master Python Modules

> **Note:** The exercises below contain **no code**. Each instruction describes only what to do, which features to use, and the goal to achieve. You may implement the solution however you like, as long as you follow the spirit of the exercise.

---

## Why 25 Exercises?

To gain a solid mastery of module management in Python (reusable `.py` files), packages (folders with `__init__.py`), and imports, **25 targeted exercises** are generally enough to encounter the most common pitfalls and learn good practices. You can go further if you wish, but these exercises cover the essentials for everyday and professional use.

---

## Exercises

### 1. Creating a Module and Simple Import
- Create a new Python file containing a very simple function.
- In another script, import this module and call the function.
- Verify that it runs without errors.

**Key Points:** Creating a `.py` file, basic import, calling a function.

---

### 2. Specific Import and Alias
- In your module, add several functions or variables.
- In a separate script, import only one of them under a different name (alias).
- Show that you can call it through this alias, without exposing the rest of the module.

**Key Points:** `from ... import ... as ...`, namespace management.

---

### 3. The `__name__` Variable and Direct Execution
- In the module, print the value of the `__name__` variable.
- Run the module directly, then import it from another script.
- Observe the difference and explain why.

**Key Points:** The difference between `__main__` and the module name, script vs. library logic.

---

### 4. `if __name__ == "__main__":` Condition
- In the module, place a conditional block that runs some test or prints output only if the file is called directly.
- Make sure this test does **not** run when you import the module.

**Key Points:** Structuring a file for dual usage (script and module).

---

### 5. Module Footprint via `dir()`
- Create a module with multiple functions, classes, and variables.
- From another script, retrieve the list of names available via the `dir()` function on that module.
- Comment on which names show up, which are hidden, etc.

**Key Points:** Discovering and introspecting a module, exploring the namespace.

---

### 6. Using the `sys` Module
- Import the `sys` module.
- Print information about the Python version in use and the import search path (`sys.path`).
- Discuss how Python locates modules.

**Key Points:** Exploring `sys`, implications for imports.

---

### 7. Modifying `sys.path`
- Create a directory outside the default search path and place a module with a function there.
- Modify `sys.path` at runtime to include the new directory.
- Show that you can now import the module and call its function.

**Key Points:** Import paths, customizing import behavior, potential impacts.

---

### 8. Handling an Import Error
- Try importing a non-existent module.
- Handle the resulting exception and display a user-friendly message.
- Optionally, offer an alternative if the module is not found.

**Key Points:** `ModuleNotFoundError`, error handling, code robustness.

---

### 9. Simple Packages
- Create a folder named, for example, `my_package` and include an `__init__.py` file (even if empty).
- Add a `module_a.py` inside this folder, containing a function.
- Demonstrate how to import it from an external script.

**Key Points:** Package concept, the role of `__init__.py`.

---

### 10. Importing a Sub-module
- In the `my_package` folder, add a second file `module_b.py`.
- Have `module_a.py` use a function from `module_b.py`.
- Import only `module_a` in a script and prove that the function from `module_b` is accessible via `module_a`.

**Key Points:** Imports among modules in the same package, propagating dependencies.

---

### 11. Search Path and Organization
- Organize multiple folders (packages), for instance, an `app/` folder and a `libs/` folder.
- Place a module in `libs/` that you import from `app/`.
- Discuss how to position these folders and the possible need to modify `PYTHONPATH` or `sys.path`.

**Key Points:** More complex hierarchy, multi-folder project structure.

---

### 12. Wildcard Imports
- In a module, define several functions and variables, including some starting with an underscore.
- Perform `from my_module import *` and show what gets imported or not.
- Conclude about good practices and code readability.

**Key Points:** Wildcard imports, `_private` naming, visibility conventions, implications.

---


### 13. Using `__all__`
- In a module or an `__init__.py`
- declare a list `__all__` to control what is exported.
- Do a global import (`import *`) and confirm that only the listed entities are imported.
- Add an entity not referenced in `__all__` and note that it remains hidden.

**Key Points:** Precise export control, advanced packaging.

---

### 14. Nested Packages (Sub-packages)
- Create a main package and a sub-package (e.g., `main_pkg/` and `main_pkg/sub_pkg/`, each with its own `__init__.py`).
- Place a module in `sub_pkg/` and import it from a script at the root.
- Verify the import works and discuss the syntax (`from main_pkg.sub_pkg import ...`).

**Key Points:** Complex hierarchies, exploring package structure.

---

### 15. Alias for Sub-packages
- In your main script, import a sub-package with a shorter alias.
- Use that alias to call the function or class defined in the sub-package.
- Argue why it helps reduce verbosity in the code.

**Key Points:** Sub-package aliasing, code readability, naming conventions.

---

### 16. Running a Package as a Script
- In a sub-package, place instructions that print text only if `__name__ == "__main__"`.
- Test it with direct command-line execution (if allowed in your environment).
- Compare with simply importing the sub-package.

**Key Points:** Differences between direct execution and imports, making a package “runnable.”

---

### 17. Investigating `__pycache__`
- Import a module and note that a `__pycache__/` folder is created.
- Modify the module, re-import it, and observe the updated cache files.
- Explain why this compilation mechanism exists and how it affects performance.

**Key Points:** `.pyc` compilation, caching mechanism, reloading.

---

### 18. Dynamic Reload
- After importing a module, change its content (e.g., a variable).
- Use a dynamic reload mechanism (via appropriate tools) to refresh it without restarting the interpreter.
- Verify the new value is in effect.

**Key Points:** Partial or complete module reload, debugging, limitations.

---

### 19. Circular Import
- Create two modules that import each other.
- Show how it can lead to errors or partially initialized objects.
- Fix the situation (e.g., by reorganizing or using local imports) and explain the solution.

**Key Points:** Detecting and resolving circular dependencies, a tricky aspect of Python architecture.

---

### 20. Alias for Conflict Resolution
- Simulate two modules with the same name (e.g., `config.py` in different directories).
- Import them with distinct aliases in a script.
- Prove that you can access each one via its alias.

**Key Points:** Multiple homonymous modules, aliasing, naming management.

---

### 21. Advanced System Functions
- Look into standard modules (like `os`, `pathlib`, etc.) that can interact with your project structure.
- Implement logic to check if a module exists (without actually importing it).
- Argue when to use these functions for managing imports or packages.

**Key Points:** More advanced exploration, OS–Python interactions.

---

### 22. Basic “Plugin System”
- Organize a `plugins/` folder with multiple sub-modules.
- Each sub-module exposes a `register()` function or similar behavior.
- Write a script that detects and imports all plugins in this folder, then calls their `register()` function.

**Key Points:** Dynamic loading, plugin pattern, modular architecture.

---

### 23. CLI Scripts and Modules
- Write a script that can be used on the command line to do a simple task (e.g., addition, string concatenation).
- Put your main logic in a dedicated module so you can also use it normally via import.
- Show the advantage of separating business logic from the CLI interface.

**Key Points:** Modular approach, using as both command and library.

---

### 24. Partial Distribution (.pyc Only)
- Compile a module to produce a `.pyc` file.
- Remove the `.py` file.
- Confirm that you can still import it from a script.
- Explain possible use cases and limitations of this distribution method.

**Key Points:** Distributing without source code, `.pyc` only, portability concerns.

---

### 25. Advanced Project Structure
- Create a more complex tree (for example, a main folder, multiple sub-packages, a separate `tests/` folder, etc.).
- Describe the role of each `__init__.py`, how you import from one sub-package to another, and what each module does.
- Ensure at least one script orchestrates the whole thing (reading/writing data or launching a small service).

**Key Points:** Comprehensive practice, managing larger codebases, final organization.

---

## Summary of Skills Developed

By completing these exercises, you will have:

1. **Understood the basics** of creating and importing modules (`.py` files).
2. **Built structured packages** (`__init__.py`, sub-packages) and mastered navigation through hierarchy.
3. **Manipulated `sys.path`**, the `__name__` variable, and the intricacies of `if __name__ == "__main__"`.
4. **Learned to handle name conflicts** via aliases, package structures, and wildcard imports.
5. **Explored advanced concepts** like dynamic reloading, circular imports, `.pyc` distribution, and running a package as a script.
6. **Reflected on best practices**: avoiding conflicts, clarifying code, organizing professional projects with coherent hierarchies.
7. **Understood plugin logic** and modular dynamic loading for extensible projects.

By tackling these 25 progressive exercises, you’ll cover the essential aspects of **Python Modules**. Happy coding and development!
