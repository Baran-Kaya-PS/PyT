# 50 Exercises Inspired by Python Data Structures (in English)

Drawing inspiration from the previous list of exercises and the topics covered in [Section 5 of the Python Tutorial](https://docs.python.org/3/tutorial/datastructures.html), here are **50 exercises** focusing on lists, tuples, sets, dictionaries, comprehensions, and more. Each exercise addresses one or more points mentioned in that section (using lists as stacks/queues, slicing, list comprehensions, set/dict comprehensions, the `del` statement, tuples, sets, etc.). The exercises are split into three categories – **Easy**, **Medium**, and **Hard** – ending with challenging tasks where you should also practice writing **functions** that utilize these data structures.

---

## 🌱 EASY (1–15)

1. **List and `append()`**  
   Write a function that creates an empty list.
   Ask the user for five values.
   Use `list.append()` to add each value.
   Print the final list.

2. **Insertion and Deletion**  
   Write a function that asks the user for a list of numbers.
   Insert a chosen number at index 0 with `list.insert()`.
    Remove the last element with `list.pop()`.
    Print the result.

3. **Cleaning a List**  
    Write a function that creates a list with duplicate values.
    Use `list.remove()` to delete the first occurrence of an element specified by the user.
    Then call `list.clear()` to empty the entire list.
    Show each step.

4. **Simple Stack**  
    Implement a stack using a list.
    Push several elements (using `append`) and pop one element (using `pop`).
    Show the stack state at each operation.

5. **Queue with `deque`**  
    Import `collections.deque` in your function.
    Create a queue with a few elements (“first in, first out”).
    For each removal (via `popleft()`), print the element removed.
    Display the final data structure.

6. **Using `del` on a List**  
    Write a function that requests a list from the user.
    Delete a specific element by index using `del my_list[index]`.
    Then delete a slice of the list (e.g., the last 2 elements).
    Print the list after each deletion.

7. **Create and Display a Tuple**  
    Ask the user for three values inside a function.
    Build a tuple with these three values.
    Print the tuple and demonstrate it is **immutable**.

8. **Conditional Addition with `in`**  
    Start with an existing list.
    Request an element from the user.
    Check if it is not already in the list (`if x not in my_list`).
    If it isn’t, add it (with `append`); otherwise, do nothing.
    Print the final list.

9. **Creating a Set and Testing Membership**  
    Ask the user for multiple elements (numbers or strings).
    Convert them into a `set`.
    Check whether a particular element is in the set (`in` operator).
    Print the size of the final set (`len(the_set)`).

10. **Simple Dictionary**  
    Create a small dictionary (3 or 4 keyvalue pairs).
    Ask the user for a key and print the corresponding value if the key exists.
    Otherwise, print “Unknown key.”

11. **List of Squares (List Comprehension)**  
    Ask the user for an integer `n` in a function.
    Build a list of squares via `[x*x for x in range(n)]`.
    Print the result.

12. **Filter a List (List Comprehension)**  
    Create a list of both positive and negative numbers.
    Use a list comprehension to build a new list containing only positive ones.
    Print that filtered list.

13. **Slice Extraction**  
    Ask the user for any list.
    Print a slice of elements from index 2 to 5.
    Also print a slice of elements at even indices (`[::2]` or another approach).

14. **Reversing a List**  
    Request a list from the user.
    Reverse it using slicing `[::1]`.
    Print the reversed list.

15. **Compare Two Lists**  
    Ask the user for two lists.
    Convert them to tuples and compare them using `<`, `>`, and `==`.
    Print the result of the lexicographical comparison.



## ⚡ MEDIUM (16–30)

16. **Shallow Copy vs. Deep Copy**  
    Create a list that itself contains a sublist.
    Perform `copy_1 = my_list.copy()` and modify an element inside the sublist.
    Show that the change appears in `copy_1`.
    Discuss the difference between shallow and deep copies (without necessarily coding deep copy).

17. **Multiple Push and Pop**  
    Simulate multiple pushes in a list (like a stack).
    Then pop several elements in a row, printing each popped element.
    Print the final state of the list.

18. **Concatenation**  
    Ask the user for two lists.
    Concatenate them using the `+` operator.
    Print the resulting list.  
    Discuss that this does not modify the original lists.

19. **Insert at Multiple Positions**  
    Request an initial list.
    Insert a new element at index 0 and another at the last position (`insert(len(my_list), elem)`).
    Print the list after each insertion.

20. **Index Search**  
    Create a list of strings.
    Ask the user for a word to search.
    Attempt to find its index with `list.index()`.
    If not found, catch the `ValueError` exception and display an appropriate message.

21. **Count Occurrences**  
    Have a list of objects, with some repeats.
    Ask the user which object to count.
    Use `list.count()` to show how many times it occurs.
    Confirm that this method does not alter the list.

22. **Sort and Reverse**  
    Request a list of numbers.
    Call `list.sort()` and then `list.reverse()` to display them in reverse.
    Compare that result with `sorted(my_list, reverse=True)`.

23. **Slice Deletion**  
    Create a list of multiple elements.
    Use `del my_list[1:4]` to remove a slice.
    Print the list.
    Then delete the entire list content with `del my_list[:]` and print it again.

24. **Tuples: Packing and Unpacking**  
    Ask for four values.
    Assign them to variables simultaneously (unpacking).
    Combine them into one tuple (packing).
    Print both the variables and the final tuple.

25. **Creating and Intersecting Sets**  
    Ask the user for two sets of values (split by spaces).
    Convert each set of values to an actual Python set.
    Print their intersection (`set1 & set2`).

26. **Difference and Union of Sets**  
    Reuse the sets from the previous exercise.
    Print their difference (`set1  set2`), union (`set1 | set2`), and symmetric difference (`set1 ^ set2`).

27. **Dictionary: Add and Remove**  
    Create a simple dictionary (a few keyvalue pairs).
    Add a new pair (key/value) given by the user.
    Remove an existing key with `del d[key]`.
    Print the final dictionary.

28. **Loops and Enumeration**  
    Have a list of data.
    Loop over it with `enumerate()` and print both index and value for each element.
    Briefly explain the advantage of using `enumerate()`.

29. **Zip Two Sequences**  
    Ask the user for two lists of equal length.
    Iterate them in parallel with `zip()`.
    Print each pair of elements.

30. **Reverse Iteration**  
    Ask the user for a list (or range).
    Iterate in reverse order with `reversed()`.
    Print the elements in that order.



## 🔥 HARD (31–50) — Challenge at the End

31. **Queue with `list`**  
    Discuss the inefficiency of `pop(0)` in a list.
    Show a queue implementation using a list (removing from index 0).
    Display the impact on the list size if you do many operations.

32. **List of Lists and Nested List Comprehensions**  
    Create a list of lists (a small matrix).
    Using a **nested list comprehension**, extract only the even elements.
    Print the result

33. **Matrix Transposition**  
    Reuse the concept of a matrix (e.g., 3×4).
    Transpose it with `[[row[i] for row in matrix] for i in range(...)]`.
    Compare that with `zip(*matrix)`.

34. **Advanced Filtering**  
    Make a list of numbers that includes some `None` values and negative numbers.
    Use a list comprehension to filter out only the non`None` and positive ones.
    Print the final filtered list.

35. **Custom Sort with `key`**  
    Have a list of tuples `(name, age)`.
    Sort it by age using `list.sort(key=lambda x: x[1])`.
    Print the list after sorting.

36. **Looping Through Dictionaries**  
    Create a dictionary (e.g. `product > price`).
    Loop over it with `items()` to print each key/value pair.
    Then print only the keys (`keys()`) and only the values (`values()`).

37. **Sort a Dictionary by Value**  
    Reuse a dictionary (e.g. `name > score`).
    Convert it to a list of tuples with `items()`.
    Sort the list of tuples by the score (the value).
    Rebuild a new dictionary sorted by that criterion.

38. **Set Comprehension**  
    Take a string with duplicates.
    Build a set comprehension to extract only unique letters that are, for instance, vowels.
    Print the resulting set.

39. **Error Handling with `list.index()`**  
    Have a list.
    Ask the user for a value to find.
    Use a `try/except` block for `list.index()`.
    If found, print the index; if not, display an error message.

40. **Conditional Deletion in a List**  
    Have a list of numbers.
    Loop and remove every negative number.
    Discuss the trap of modifying the list while iterating.
    Show why it’s safer to build a new filtered list instead.

41. **Create a Small Inventory (Dictionary)**  
    Request multiple pairs `(item_name, quantity)` from the user.
    Store them in a dictionary, adding up the quantities if the item name already exists.
    Print the final dictionary.

42. **List of Tuples and MultiLevel Sorting**  
    Have tuples `(title, price, quantity)`.
    First sort by `price`, then by `quantity` if prices are equal.
    Use an appropriate `lambda` or a function returning `(price, quantity)`.

43. **ShortCircuiting with `and` / `or`**  
    Create two functions that print a message when called and return a boolean (True/False).
    Construct a condition like `if f1() and f2(): ...`.
    Demonstrate how Python shortcircuits the evaluation.

44. **List Copy via Slicing**  
    Have a list of numbers.
    Do `list2 = my_list[:]` for copying.
    Modify `list2` and show that `my_list` is unaffected.
    Compare it with a simple assignment `list2 = my_list`.

45. **Comparing Tuples**  
    Create two tuples.
    Compare them with `<`, `>`, `==`.
    Show how Python compares them element by element (lexicographically).

46. **Search a Substring in a List of Strings**  
    Ask the user for a list of strings.
    Ask for a substring.
    Filter the list to keep only those containing the substring (`sub in string`).
    Print the result.

47. **Splitting a List into Sublists**  
    Create a list with at least 10 elements.
    Divide it into 2 or 3 sublists of approximately equal size with slicing.
    Print each sublist.

48. **Dictionary Comprehension**  
    Ask the user for an integer `n`.
    Build a dictionary `{x: x*x for x in range(n)}`.
    Print it.

49. **Using `zip()` with Multiple Arguments**  
    Have three lists of the same length.
    Loop over them simultaneously with `zip(l1, l2, l3)`.
    For each index, print the combination of the three elements.

50. **Manually Merging Multiple Sets**  
    Request three sets from the user (typed as spaceseparated strings).
    Convert them all to Python `set` objects.
    Print the final merged set (`set1 | set2 | set3`).
    Optionally show the global intersection, too.

---

**Good luck!**  
These 50 exercises explore various features described in [The Python Tutorial – Section 5: Data Structures](https://docs.python.org/3/tutorial/datastructures.html). Learn to manipulate **lists**, **tuples**, **sets**, and **dictionaries** effectively, and practice **comprehensions** as well as the `del` statement to become more comfortable with Python’s data structures. In the final **challenge** tasks, be sure to write and use **functions** that employ these data structures to solve the problems.
