Below is a **50-exercise** collection centered on **Python Input & Output**, organized into **Medium**, **Hard**, and **Challenge** tiers. Each exercise follows the requested format:

1. **Number of exercise : Name of exercise**  
2. **What you must do**  
3. **Functions/Modules You Can Use**  
4. **Different Ways to Solve (Conceptual)**  
5. **Next Exercise**  

All examples reference *possible* functions or modules, but **no code** is provided.

---

## **Medium Exercises (1–15)**

---

### 1: Formatted Greeting
**What You Must Do**  
Prompt the user for their first and last name, then print a greeting (e.g., “Hello, Jane Doe!”). Focus on using string formatting features.

**Functions/Modules You Can Use**  
- `input()`
- `print()`
- f-strings, `str.format()`, or older `%` formatting

**Different Ways to Solve (Conceptual)**  
1. Construct a formatted string using f-strings or `str.format()` to place first and last name in one sentence.  
2. Use `%` formatting to show how it was done historically.

**Next Exercise**  
[2: Right-Justified Numbers](#2-right-justified-numbers)

---

### 2: Right-Justified Numbers
**What You Must Do**  
Print numbers from 1 to 10, each right-justified to a width of 3 characters, so they align nicely in one column.

**Functions/Modules You Can Use**  
- `range()`
- `print()`
- `str.rjust()`, or format specifiers (f-strings / `str.format()`)

**Different Ways to Solve (Conceptual)**  
1. Loop from 1 to 10, convert each number to string, and use `rjust()` with a width of 3.  
2. Use format mini-language with something like `">3"` or a similar approach in f-strings.

**Next Exercise**  
[3: Reading a Single File](#3-reading-a-single-file)

---

### 3: Reading a Single File
**What You Must Do**  
Create or use a small text file (`story.txt`). Open and read all its lines, then print them while stripping the trailing newline.

**Functions/Modules You Can Use**  
- `open()`
- `with` statement (context manager)
- `str.strip()`

**Different Ways to Solve (Conceptual)**  
1. Use `with open(...) as f:` and `readlines()` then iterate over each line.  
2. Use `for line in f:` and strip newlines while printing.

**Next Exercise**  
[4: Counting Lines](#4-counting-lines)

---

### 4: Counting Lines
**What You Must Do**  
Prompt the user for a filename. Read through the file line-by-line, and count how many lines it contains. Print the result.

**Functions/Modules You Can Use**  
- `input()`
- `open()`, file iteration
- A loop or list comprehension for counting

**Different Ways to Solve (Conceptual)**  
1. Increment a counter in a `for` loop.  
2. Convert the file’s lines to a list and use `len()`.

**Next Exercise**  
[5: Writing User Input to File](#5-writing-user-input-to-file)

---

### 5: Writing User Input to File
**What You Must Do**  
Ask the user for some text input, then write exactly what they typed into a new file (`output.txt`). Print a confirmation message.

**Functions/Modules You Can Use**  
- `input()`
- `open(..., "w")`
- `print()`

**Different Ways to Solve (Conceptual)**  
1. Use a single `with open(..., "w"):` block and `write(...)`.  
2. Append additional text, or handle newline yourself if you want more advanced behavior.

**Next Exercise**  
[6: Simple Table Printing](#6-simple-table-printing)

---

### 6: Simple Table Printing
**What You Must Do**  
Given a dictionary (e.g., `{ "Alice": 24, "Bob": 19, "Charlie": 30 }`), print each name and age in a nicely aligned table.

**Functions/Modules You Can Use**  
- Dictionary iteration
- f-strings or `str.format()`
- Right or left alignment

**Different Ways to Solve (Conceptual)**  
1. Determine suitable column widths and align each value accordingly.  
2. Use format mini-language (e.g., `"{:<10}{:>5}"`) or a custom approach with `ljust()`/`rjust()`.

**Next Exercise**  
[7: Reading and Summing Numbers](#7-reading-and-summing-numbers)

---

### 7: Reading and Summing Numbers
**What You Must Do**  
Ask the user for a filename. The file contains one integer per line. Read them, sum them, and print the total.

**Functions/Modules You Can Use**  
- `input()`
- `open()`
- `int()`
- Summation with loops or built-in functions

**Different Ways to Solve (Conceptual)**  
1. Accumulate the sum in a loop.  
2. Use a list comprehension plus `sum()`.

**Next Exercise**  
[8: Appending to a Log File](#8-appending-to-a-log-file)

---

### 8: Appending to a Log File
**What You Must Do**  
Create or open `log.txt` in append mode. Let the user type a message, and write it to the file with a timestamp. Print confirmation.

**Functions/Modules You Can Use**  
- `input()`
- `open(..., "a")`
- Possibly `datetime` for timestamps

**Different Ways to Solve (Conceptual)**  
1. Append the text with a simple custom timestamp string.  
2. Use Python’s date/time utilities for a more precise format.

**Next Exercise**  
[9: Reading Partial File Content](#9-reading-partial-file-content)

---

### 9: Reading Partial File Content
**What You Must Do**  
Have a file with at least 100 characters. Open the file, read the first 50 characters, print them, then read the next 50, print them, etc.

**Functions/Modules You Can Use**  
- `open()`
- `read(size)`
- Possibly loops or repeated calls to `read()`

**Different Ways to Solve (Conceptual)**  
1. Repeatedly call `read(50)` until the file is exhausted.  
2. Use a while loop, checking if the returned data is empty.

**Next Exercise**  
[10: Manual String Formatting vs. f-Strings](#10-manual-string-formatting-vs-f-strings)

---

### 10: Manual String Formatting vs. f-Strings
**What You Must Do**  
Create a dictionary (`product -> quantity`) and print each key-value pair in two different ways: (1) manual concatenation plus `rjust()`/`ljust()`, (2) using f-strings or `str.format()`.

**Functions/Modules You Can Use**  
- Dictionary iteration
- `str.ljust()`, `str.rjust()`
- f-strings or `str.format()`

**Different Ways to Solve (Conceptual)**  
1. Construct strings with `+` and spacing or `rjust()/ljust()`.  
2. Use f-strings with alignment specifiers.

**Next Exercise**  
[11: Check If File Exists Then Write](#11-check-if-file-exists-then-write)

---

### 11: Check If File Exists Then Write
**What You Must Do**  
Prompt user for a filename, check if it exists. If it does, ask whether to overwrite or append. If not, create and write “File created!”.

**Functions/Modules You Can Use**  
- `input()`
- `os.path` or a `try/except` approach
- `open()` in various modes

**Different Ways to Solve (Conceptual)**  
1. Use `try: open(...) except FileNotFoundError:` to detect existence.  
2. Use `import os`, then `os.path.exists(filename)` to check.

**Next Exercise**  
[12: Interactive Palindrome Checker (Console Input)](#12-interactive-palindrome-checker-console-input)

---

### 12: Interactive Palindrome Checker (Console Input)
**What You Must Do**  
Continuously prompt the user for a word (until “quit”). Check if it’s a palindrome, and print an appropriate message.

**Functions/Modules You Can Use**  
- `input()`
- String slicing
- Loops and `break`

**Different Ways to Solve (Conceptual)**  
1. Compare string to its reversed version.  
2. Use a function that checks palindrome character by character.

**Next Exercise**  
[13: zfill Practice](#13-zfill-practice)

---

### 13: zfill Practice
**What You Must Do**  
Ask the user for a number as a string (e.g., “58”) and apply `.zfill(6)` to pad it to a width of 6 with leading zeros. Print it.

**Functions/Modules You Can Use**  
- `input()`
- `str.zfill()`

**Different Ways to Solve (Conceptual)**  
1. Directly apply `zfill(6)` on the user input.  
2. Demonstrate how it handles negative numbers or decimal strings if you want extra exploration.

**Next Exercise**  
[14: Load JSON from a String](#14-load-json-from-a-string)

---

### 14: Load JSON from a String
**What You Must Do**  
Have a valid JSON string (like `{"username": "alice", "active": true, "score": 42}`). Load it into a Python dictionary with `json.loads()` and print the result in a neat way.

**Functions/Modules You Can Use**  
- `import json`
- `json.loads()`
- `print()`

**Different Ways to Solve (Conceptual)**  
1. Print the raw dictionary.  
2. Loop through dictionary items and format output.

**Next Exercise**  
[15: Print with Old % Formatting](#15-print-with-old--formatting)

---

### 15: Print with Old % Formatting
**What You Must Do**  
Prompt the user for a floating-point number, then print it in a sentence using `%` string formatting, rounded to 2 decimals.

**Functions/Modules You Can Use**  
- `input()`
- `float()`
- `%` formatting (e.g., `%5.2f`)

**Different Ways to Solve (Conceptual)**  
1. Use `%` with a format like `%.2f`.  
2. Let the user type the entire expression, but that might defeat the purpose of demonstrating `%`.

**Next Exercise**  
[16: Advanced F-String Formatting](#16-advanced-f-string-formatting)

---

## **Hard Exercises (16–35)**

---

### 16: Advanced F-String Formatting
**What You Must Do**  
Given variables like `product = "Laptop"`, `price = 899.99`, `quantity = 7`, print them in one line with specified widths and justifications (e.g., left-justify the product, right-justify the price, zero-pad the quantity).

**Functions/Modules You Can Use**  
- f-strings with format specifiers
- `str.zfill()`
- Possibly `"{:10}"`, `"{:>8.2f}"` if using `str.format()`

**Different Ways to Solve (Conceptual)**  
1. Use f-strings with something like `f"{product:<10}"`, `f"{price:>8.2f}"`, `f"{quantity:04}"`.  
2. Combine old `%` formatting or `str.format()` with alignment codes.

**Next Exercise**  
[17: Reading Large Files in Chunks](#17-reading-large-files-in-chunks)

---

### 17: Reading Large Files in Chunks
**What You Must Do**  
Use a large text file. Read it in chunks of 1024 bytes, printing a progress message each time a chunk is processed.

**Functions/Modules You Can Use**  
- `open(..., "rb")` or `open(..., "r")`
- `read(size)`
- Possibly a while loop

**Different Ways to Solve (Conceptual)**  
1. Use a loop that reads 1024 bytes until an empty result.  
2. Track chunk count and multiply by 1024 for approximate position.

**Next Exercise**  
[18: Converting a Text File to JSON](#18-converting-a-text-file-to-json)

---

### 18: Converting a Text File to JSON
**What You Must Do**  
Given a text file with lines like `Alice,24`, `Bob,19`, `Charlie,30`, parse each line into a dictionary `{ "name": ..., "age": ... }`, then store all dictionaries in a JSON array in a new file.

**Functions/Modules You Can Use**  
- `open()`
- `json.dump()`
- String splitting

**Different Ways to Solve (Conceptual)**  
1. Read line by line, split on comma, build a list of dictionaries.  
2. Use `map()` or a comprehension to parse lines before dumping to JSON.

**Next Exercise**  
[19: Seeking and Overwriting](#19-seeking-and-overwriting)

---

### 19: Seeking and Overwriting
**What You Must Do**  
Open a file in binary mode, write 20 bytes, then use `seek()` to move to the 10th byte and overwrite the next 5 bytes with something else.

**Functions/Modules You Can Use**  
- `open(..., "rb+")` or `open(..., "wb+")`
- `seek()`
- `write()`

**Different Ways to Solve (Conceptual)**  
1. Write a string or bytes, then `seek(10, 0)` and overwrite.  
2. Print or read after to confirm changes.

**Next Exercise**  
[20: Formatted Table of Factorials](#20-formatted-table-of-factorials)

---

### 20: Formatted Table of Factorials
**What You Must Do**  
For numbers 1 to 10, print each number and its factorial in two columns. The first column is 2 characters wide, the second is 10 characters wide.

**Functions/Modules You Can Use**  
- `math.factorial()` or a custom factorial
- f-strings or `str.format()`

**Different Ways to Solve (Conceptual)**  
1. Use a loop from 1 to 10 and format each row.  
2. Possibly create a list of tuples, then print them in a second step.

**Next Exercise**  
[21: Counting Word Frequency in a File](#21-counting-word-frequency-in-a-file)

---

### 21: Counting Word Frequency in a File
**What You Must Do**  
Read a file into a string, split into words, count occurrences of each word, then print the top 5 most common words with their counts.

**Functions/Modules You Can Use**  
- `open()`
- `split()` or `re.split()` for advanced splitting
- A dictionary or `collections.Counter`

**Different Ways to Solve (Conceptual)**  
1. Use a normal dictionary to count.  
2. Use `collections.Counter` and `most_common(5)`.

**Next Exercise**  
[22: Generating a 'CSV' File](#22-generating-a-csv-file)

---

### 22: Generating a 'CSV' File
**What You Must Do**  
Ask the user for 3 student names and their scores. Write them into `grades.csv` in a CSV-like format. Confirm by reading and printing it.

**Functions/Modules You Can Use**  
- `input()`
- `open(..., "w")`
- Possibly the `csv` module

**Different Ways to Solve (Conceptual)**  
1. Manually write lines in the format `"name,score"`.  
2. Use Python’s built-in `csv.writer` for more complex scenarios.

**Next Exercise**  
[23: Loading and Updating JSON](#23-loading-and-updating-json)

---

### 23: Loading and Updating JSON
**What You Must Do**  
Have a JSON file listing tasks (title + boolean “completed”). Load it, prompt user for a task title, mark it completed, save the file again.

**Functions/Modules You Can Use**  
- `json.load()` / `json.dump()`
- Loops to find the matching dictionary
- `input()`

**Different Ways to Solve (Conceptual)**  
1. Convert the JSON list to a Python list, iterate, update the matching item, dump back.  
2. Implement a function for updating tasks to keep the code clean.

**Next Exercise**  
[24: Multiple File Reading](#24-multiple-file-reading)

---

### 24: Multiple File Reading
**What You Must Do**  
Ask for multiple filenames in one line (comma-separated). For each, open and read it. Print the length (in characters) of each file. Warn if a file doesn’t exist but continue.

**Functions/Modules You Can Use**  
- `input()`
- `split(',')`
- `open()` in a `try/except`

**Different Ways to Solve (Conceptual)**  
1. Use a loop, strip spaces, attempt to open each file, read and measure length.  
2. If file not found, log an error message and move on.

**Next Exercise**  
[25: Lexical Order of Lines](#25-lexical-order-of-lines)

---

### 25: Lexical Order of Lines
**What You Must Do**  
Read lines from `lines.txt`, sort them lexicographically, write them to `sorted_lines.txt`, and print the first 5 sorted lines in the console.

**Functions/Modules You Can Use**  
- `open()`
- `sorted()` on a list of strings
- Slicing for the first 5 elements

**Different Ways to Solve (Conceptual)**  
1. Read and store lines in a list, then sort.  
2. Use an in-memory approach or a more complex external sort for huge files.

**Next Exercise**  
[26: Selective Data Extraction](#26-selective-data-extraction)

---

### 26: Selective Data Extraction
**What You Must Do**  
Given lines of varying formats (comments starting with `#`, key-value lines with `=`, lines inside `[Section]` blocks, etc.), parse them differently. Store key-value pairs in a dictionary and other lines in a separate list.

**Functions/Modules You Can Use**  
- `open()`
- `startswith()`
- String splitting on `=`

**Different Ways to Solve (Conceptual)**  
1. Use conditionals to detect `#`, `=`, or `[Section]`.  
2. Build multiple data structures (a dictionary, a list, maybe a list of sections).

**Next Exercise**  
[27: Apply a Function to File Lines](#27-apply-a-function-to-file-lines)

---

### 27: Apply a Function to File Lines
**What You Must Do**  
Write a function (e.g., `process_line(line)`) that modifies text (like reversing or toggling case). Open a file, apply the function to each line, then print or store the results.

**Functions/Modules You Can Use**  
- `open()`
- A custom `process_line(line)`
- Possibly `str.upper()`, `str.lower()`, etc.

**Different Ways to Solve (Conceptual)**  
1. Call `process_line(line)` in a loop while reading the file.  
2. Store all processed lines in a list before printing them at once.

**Next Exercise**  
[28: Write a Custom Logger](#28-write-a-custom-logger)

---

### 28: Write a Custom Logger
**What You Must Do**  
Create a function `log_event(message, level="INFO")` that appends to `app.log` in a format like `[2025-04-16 12:00][INFO] Some message`.

**Functions/Modules You Can Use**  
- `open(..., "a")`
- Possibly `datetime` for timestamps
- A function definition for logging

**Different Ways to Solve (Conceptual)**  
1. Use simple string concatenation for formatting.  
2. Use advanced time formatting if desired.

**Next Exercise**  
[29: User Input, Validate, Write](#29-user-input-validate-write)

---

### 29: User Input, Validate, Write
**What You Must Do**  
Prompt the user for an email address. Keep asking until they provide a string with “@”. Write valid emails to `emails.txt`, then print how many emails total are in that file.

**Functions/Modules You Can Use**  
- `input()`
- `while` loops
- `open()`

**Different Ways to Solve (Conceptual)**  
1. Validate with a simple `if "@" in user_input`.  
2. Read `emails.txt` again to count lines after writing.

**Next Exercise**  
[30: Progress Bar Simulation](#30-progress-bar-simulation)

---

### 30: Progress Bar Simulation
**What You Must Do**  
Simulate a progress bar from 1 to 100, updating a single console line (e.g., `[####       ] 40%`). Use a short delay each iteration.

**Functions/Modules You Can Use**  
- Loops
- Possibly `time.sleep()`
- Printing with `\r` or `sys.stdout.flush()`

**Different Ways to Solve (Conceptual)**  
1. Print each percentage with carriage return to overwrite the line.  
2. Build a string representing how many `#` vs. spaces.

**Next Exercise**  
[31: Formatted Directory Listing (Requires OS Knowledge)](#31-formatted-directory-listing-requires-os-knowledge)

---

### 31: Formatted Directory Listing (Requires OS Knowledge)
**What You Must Do**  
Use `os.listdir()` to list files in the current directory. Print each filename left-aligned and the file size right-aligned.

**Functions/Modules You Can Use**  
- `import os`
- `os.listdir()`
- Possibly `os.path.getsize()`
- Format strings

**Different Ways to Solve (Conceptual)**  
1. Gather filenames, get sizes, store in a list of tuples, then print.  
2. Format each line so the name is in a certain width, size in another.

**Next Exercise**  
[32: Custom JSON Encoder/Decoder](#32-custom-json-encoderdecoder)

---

### 32: Custom JSON Encoder/Decoder
**What You Must Do**  
Create a class `Person(name, age)`. Write logic to encode a `Person` into JSON and decode it back to a `Person` instance. Demonstrate reading/writing a few Person objects to a file.

**Functions/Modules You Can Use**  
- `json.dump()` / `json.load()`
- Custom JSON encoder/decoder classes or hooks

**Different Ways to Solve (Conceptual)**  
1. Use `default=` param for custom encoding and `object_hook` for decoding.  
2. Manually convert `Person` objects to dictionaries, then decode them.

**Next Exercise**  
[33: Chunked Transfer to Another File](#33-chunked-transfer-to-another-file)

---

### 33: Chunked Transfer to Another File
**What You Must Do**  
Open an existing file in binary mode, read it in 1 KB chunks, and write each chunk to a new file. Compare sizes at the end.

**Functions/Modules You Can Use**  
- `open(..., "rb")`
- `read(1024)`
- A loop until empty chunk

**Different Ways to Solve (Conceptual)**  
1. While loop reading 1024 bytes, writing to the new file.  
2. Check final size using `os.path.getsize()` to confirm correctness.

**Next Exercise**  
[34: Generate a Table with the Old % Formatting](#34-generate-a-table-with-the-old--formatting)

---

### 34: Generate a Table with the Old % Formatting
**What You Must Do**  
Display a multiplication table (1 to 9) using the old `%` string formatting. Align columns neatly.

**Functions/Modules You Can Use**  
- `%` formatting
- Loops (nested loops for multiplication table)

**Different Ways to Solve (Conceptual)**  
1. Loop over rows and columns, building each row as a string.  
2. Format each multiplication result with something like `"%2d"` for neat alignment.

**Next Exercise**  
[35: Multi-File JSON Consolidation](#35-multi-file-json-consolidation)

---

### 35: Multi-File JSON Consolidation
**What You Must Do**  
Imagine multiple JSON files in a directory, each containing a list of dictionaries. Load each file, concatenate all lists, then write to `combined.json`. Print total items.

**Functions/Modules You Can Use**  
- `import os`
- `json.load()` / `json.dump()`
- List concatenation

**Different Ways to Solve (Conceptual)**  
1. Gather filenames with `os.listdir()`, open each, extend a master list, then dump it.  
2. Use a function that merges all lists dynamically as you read them.

**Next Exercise**  
[36: Custom CSV to JSON Parser with Error Handling](#36-custom-csv-to-json-parser-with-error-handling)

---

## **Challenge Exercises (36–50)**

---

### 36: Custom CSV to JSON Parser with Error Handling
**What You Must Do**  
Parse a CSV file (e.g., `name,age,city`) line by line, attempt to convert `age` to an integer. If not possible, log an error to `parser_errors.log`. Collect valid rows into a JSON array.

**Functions/Modules You Can Use**  
- `open()`
- `json.dump()`
- A simple or advanced CSV parse (`split(',')` or `csv.reader`)

**Different Ways to Solve (Conceptual)**  
1. Read each line, split by comma, use `int()` for age, handle exceptions.  
2. Keep track of invalid lines separately, log them.

**Next Exercise**  
[37: Two-Level File Reader (Packages + Modules)](#37-two-level-file-reader-packages--modules)

---

### 37: Two-Level File Reader (Packages + Modules)
**What You Must Do**  
Ask the user for a directory, then recursively go through sub-directories, opening each `.txt` or `.py` file, counting total lines. Print the total line count.

**Functions/Modules You Can Use**  
- `import os`
- `os.walk()` or manual recursion
- Counting lines by reading

**Different Ways to Solve (Conceptual)**  
1. Use `os.walk()` for simpler recursion.  
2. Manually traverse directories with `os.listdir()` and detect sub-folders.

**Next Exercise**  
[38: Interactive CLI: Save/Load State](#38-interactive-cli-saveload-state)

---

### 38: Interactive CLI: Save/Load State
**What You Must Do**  
Write a mini command-line interface that maintains a list of tasks in memory. Commands: `add <task>`, `list`, `save`, `load`, `quit`. Use JSON to persist tasks.

**Functions/Modules You Can Use**  
- `input()` in a loop
- `json.load()`, `json.dump()`
- Possibly a dictionary or list to store tasks

**Different Ways to Solve (Conceptual)**  
1. Use an infinite while loop reading commands, then parse them.  
2. Keep the code modular by separating each command’s logic.

**Next Exercise**  
[39: Head/Tail Command Implementation](#39-headtail-command-implementation)

---

### 39: Head/Tail Command Implementation
**What You Must Do**  
Recreate simplified versions of UNIX `head` and `tail`. For `head <file> <N>`, print the first N lines; for `tail <file> <N>`, print the last N lines.

**Functions/Modules You Can Use**  
- `open()`
- Possibly reading all lines or using a buffer
- `collections.deque` might help for tail

**Different Ways to Solve (Conceptual)**  
1. Read file fully, slice the first/last N lines.  
2. For very large files, read efficiently line by line for tail.

**Next Exercise**  
[40: F-String Debugging for Complex Expressions](#40-f-string-debugging-for-complex-expressions)

---

### 40: F-String Debugging for Complex Expressions
**What You Must Do**  
Write code that includes a few complex expressions (like dictionary lookups or arithmetic). Print them using f-strings with the `= ` debug feature. Show the expression and its result.

**Functions/Modules You Can Use**  
- f-strings with `=`
- Possibly a dictionary or calculations

**Different Ways to Solve (Conceptual)**  
1. Use an example like `f"{my_dict['key']+x = }"`.  
2. Provide multiple debug expressions in the same line.

**Next Exercise**  
[41: Automatic Column Widths](#41-automatic-column-widths)

---

### 41: Automatic Column Widths
**What You Must Do**  
Read a CSV file with unknown columns. Determine the maximum width of each column, then print rows in a neat, aligned format.

**Functions/Modules You Can Use**  
- `open()`
- `split(',')`
- Possibly the `csv` module
- `max()` logic for widths

**Different Ways to Solve (Conceptual)**  
1. First pass: read all lines, parse columns, track max length for each column index.  
2. Second pass or stored data: print each row with the correct spacing.

**Next Exercise**  
[42: Encrypted File Write](#42-encrypted-file-write)

---

### 42: Encrypted File Write
**What You Must Do**  
Prompt the user for a message, apply a simple Caesar cipher (shift each character’s ASCII by 3), write to `secret.txt`. Then read and decrypt to confirm original.

**Functions/Modules You Can Use**  
- `open()`
- Basic string manipulation (chr(), ord())
- Possibly a separate decrypt function

**Different Ways to Solve (Conceptual)**  
1. Iterate over each character, shift by 3, handle wrap-around if letters only.  
2. Shift all bytes if you consider binary data.

**Next Exercise**  
[43: Binary File Comparison](#43-binary-file-comparison)

---

### 43: Binary File Comparison
**What You Must Do**  
Write a function to compare two binary files, returning True if they are identical byte-for-byte, otherwise False. Test with several files.

**Functions/Modules You Can Use**  
- `open(..., "rb")`
- `read()` in chunks or all at once
- Possibly a loop comparing chunks

**Different Ways to Solve (Conceptual)**  
1. Compare them chunk by chunk.  
2. Compare their sizes first, then compare content.

**Next Exercise**  
[44: Merging Sorted Files](#44-merging-sorted-files)

---

### 44: Merging Sorted Files
**What You Must Do**  
Assume two text files each contain sorted integers (one per line). Merge them into a new file that remains sorted (like mergesort’s merge step).

**Functions/Modules You Can Use**  
- `open()`
- `readlines()` or a streaming approach
- Possibly a “two-pointer” technique

**Different Ways to Solve (Conceptual)**  
1. Read both lists fully, combine, then sort.  
2. Do a true merge step, reading line by line from each file.

**Next Exercise**  
[45: Summaries of Log Files](#45-summaries-of-log-files)

---

### 45: Summaries of Log Files
**What You Must Do**  
Given a log file with lines like `[2025-04-16 10:00][INFO] Startup`, parse the timestamp, level, and message. Print how many INFO, DEBUG, ERROR lines. Write a filtered file containing only lines above a chosen severity.

**Functions/Modules You Can Use**  
- `open()`
- String slicing or splitting
- Possibly a dictionary to count levels

**Different Ways to Solve (Conceptual)**  
1. Use brackets `[]` to split or find indexes.  
2. Map each level to a numeric severity, then filter.

**Next Exercise**  
[46: Large JSON Editor](#46-large-json-editor)

---

### 46: Large JSON Editor
**What You Must Do**  
Handle a massive JSON file with an array of objects. Carefully load and update each object’s `"active"` field (set to true if missing), save to a new file.

**Functions/Modules You Can Use**  
- `json.load()` but be mindful of memory
- Possibly incremental or streaming approaches
- Logic to add `"active": true` if missing

**Different Ways to Solve (Conceptual)**  
1. If memory allows, load entire JSON, loop, modify, dump.  
2. For extremely large files, consider streaming solutions with libraries that parse JSON in chunks.

**Next Exercise**  
[47: Recursive 'Tree' Print of Directories](#47-recursive-tree-print-of-directories)

---

### 47: Recursive 'Tree' Print of Directories
**What You Must Do**  
Implement a “tree” command: print directory and file names with indentation that reflects sub-directory structure.

**Functions/Modules You Can Use**  
- `os.listdir()`, `os.path.isdir()`
- Recursion
- Possibly a parameter to track depth

**Different Ways to Solve (Conceptual)**  
1. Recursively call a function that prints directories at each level.  
2. Use `os.walk()` and compute indentation based on depth.

**Next Exercise**  
[48: Simulated Database Write](#48-simulated-database-write)

---

### 48: Simulated Database Write
**What You Must Do**  
Keep a dictionary in memory (like `id -> record`). Each time the user adds or modifies a record, write the whole dictionary to a JSON file. Provide an “undo” by reading a previous commit.

**Functions/Modules You Can Use**  
- `json.dump()`
- Possibly multiple versions of the file or timestamped backups
- Basic data structure manipulation

**Different Ways to Solve (Conceptual)**  
1. Every modification triggers a “commit” by writing the entire dictionary.  
2. Keep multiple commits to allow stepping backwards.

**Next Exercise**  
[49: Custom Configuration Format](#49-custom-configuration-format)

---

### 49: Custom Configuration Format
**What You Must Do**  
Invent a mini-format like:
```
[Settings]
language=EN
fullscreen=true

[User]
name=John Doe
```
Parse it so you end up with a nested dictionary, e.g. `{ "Settings": { "language": "EN", "fullscreen": "true" }, "User": {"name": "John Doe"} }`.

**Functions/Modules You Can Use**  
- `open()`
- Checking lines for `[Section]` or `=`
- Conditionals

**Different Ways to Solve (Conceptual)**  
1. Keep track of the current section in a variable as you read.  
2. Build sub-dictionaries inside a main dictionary keyed by section name.

**Next Exercise**  
[50: Multi-Mode File Operation (Argparse Simulation)](#50-multi-mode-file-operation-argparse-simulation)

---

### 50: Multi-Mode File Operation (Argparse Simulation)
**What You Must Do**  
Write a script that takes a mode (`--read`, `--write`, or `--append`) and a filename:
- `--read`: Print the file contents.
- `--write`: Overwrite the file with user input.
- `--append`: Append user input to the file.

**Functions/Modules You Can Use**  
- `input()` or `sys.argv`
- `open()` in read, write, append modes
- Possibly string formatting for success messages

**Different Ways to Solve (Conceptual)**  
1. Use a function for each mode.  
2. Simulate `argparse` by parsing command-line arguments manually.

**Next Exercise**  
N/A (this is the last exercise)

---

### End of Exercises

This completes the list of **50 Input/Output Exercises** with the requested format. You can now copy these into a Markdown file, expand on each task, and practice implementing solutions without relying on pre-written code snippets. Good luck!