# SI 506: Files

## Topics

1. Docstrings
2. File system paths
   1. Abolute path
   2. Relative path
   3. Path portability
   4. The `pathlib` module
   5. The `os` module (ye olde way)
3. Opening a file
   1. The `with` statement and the built-in `open()` function
   2. File opening modes
   3. Read methods: `read()`, `readline()`, `readlines()`
   4. `read_file()` function
   5. Write methods: `write()`, `writelines()`
   6. `write_file()` function
   7. Challenge 01
4. Working with CSV files
   1. The `csv` module
   2. `read_csv()` function
   3. `write_csv()` function
   4. Challenge 02
5. Error handling with `try` and `except` statements
   1. Challenge 03
6. Additional challenges
   1. Challenge 04
   2. Challenge 05
   3. Challenge 06
   4. Challenge 07 (Bonus)

## Lecture data

* __data-resnick-citations.csv__. A comma-separated values (CSV) delimited text file containing
  biblometric data (e.g., citation report) of Professor Paul Resnick's articles, book chapters,
  and conference papers. Data sourced from the
  [Web of Science](https://search.lib.umich.edu/databases/record/10165?query=web+of+science)
  database and exported into [Endnote](https://endnote.com/).

  Beyond illustrating this week's topic on reading from/writing to files, the data set also helps
  illustrate UMSI scholarly output, scholarly connections within UMSI (e.g., UMSI co-authors) as
  well as scholarly “influence" (citation counts).

  The first element constitutes the list "headers".

   ```python
   [
       [
            "Title", "Authors", "Book Editors", "Source Title", "Publication Date",
            "Publication Year", "Volume", "Issue", "Part Number", "Supplement", "Special Issue",
            "Beginning Page", "Ending Page", "Article Number", "DOI", "Conference Title",
            "Conference Date", "Total Citations", "Average per Year", "1995", "1996", "1997",
            "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008",
            "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
            "2020"
        ],
        ...
   ]
   ```

* __data-umsi-faculty.csv__. List of UMSI faculty (last name, first name).

  The first element constitutes the list "headers".

   ```python
   [
       ["Last Name", "First Name"],
       ...
   ]
   ```

## 1.0 Docstrings

The Python documentation string or [docstring](https://www.python.org/dev/peps/pep-0257/) is a
string literal that is positioned as the first statement in a function. The docstring provides a
short summary of the function's expected behavior, including details regarding defined parameters
(required and optional) and the return value, if any. The Python interpreter assigns the string to
the special "dunder" (i.e., double underscore) `__doc__` object attribute and is available via
introspection. Docstrings can also be assigned to modules, classes, and class methods.

There are two forms of docstrings: single line and multi-line statements. Single line Docstrings are
reserved for describing obvious behaviors. For example, the built-in `len()` function is described
with a single line docstring:

```commandline
>>> len.__doc__
'Return the number of items in a container.'
```

The docstrings in functions and other objects that you may encounter in this
course resemble a specially formatted multiline string bounded by triple quotation marks
(`"""`).

The docstring format we use is as follows:

```python
"""Short description outlining the purpose and expected behavior of the function. Between one
and five sentences should suffice to describe the function in all its glory.

Parameters:
    < name > (< type >): Terse description of the parameter.
    . . . [Repeat for each parameter, required and optional]

Returns:
    < type >: Terse description of the return value. If no value is explicitly returned specify
              `None` as the type.
"""
```

The teaching team will make increasing use of docstrings in both lectures, labs, problem sets and
lab exercises, the midterm, and the last assignment in order to describe a function's purpose,
define parameters and indicate an explicit return value, if any.

## 2.0 File system paths

Content stored in a hierarchical file system can be identified and accessed via a _path_. A path
points to a specific location in a hierarchical file system. File paths are either _absolute_ or
_relative.

### 2.1 Absolute path

An _absolute path_ includes the root element (i.e., `/`, `C:`) and the directory list (delimited
by either a forward `/` (macOS/*nix or a backwords slash `\` (Windows)) required to reach
the target directory or file.

```python
# macOS/*nix
path = "/Users/arwhyte/Documents/umich/courses/SI506/lectures/week_07/si506_week_07.py"

# Windows (Git Bash)
path = "/c/Users/arwhyte/Documents/umich/courses/SI506/lectures/week_07/si506_week_07.py"

# Windows (Command Prompt)
path = "C:\Users\arwhyte\Documents\umich\courses\SI506\lectures\week_07\si506_week_07.py"
```

### 2.2 Relative path

A _relative path_ is defined in relation to the current working directory (cwd). Given the
absolute paths above the relative path `lectures/week_07` or `./lectures/week_07` implies
that the current working directory is either `/Users/arwhyte/Documents/umich/courses/SI506/lectures`
(macOS/*nix) or `/c/Users/arwhyte/Documents/umich/courses/SI506/lectures/` (Windows Git Bash).

### 2.3 Path portability

One drawback to using _hard-coded_ absolute paths is that such paths are __not portable__ between
operating systems and file systems. With rare exceptions, the absolute paths listed above
would trigger a runtime `FileNotFoundError` exception if included in a Python `*.py` file shared
with you.

:exclamation: Avoid submitting assignments to Gradescope that include _hard-coded_ absolute paths.
An absolute path included in your `*.py` file that is appropriate for your local file system is
_guaranteed_ to trigger a runtime `FileNotFoundError` exception when encountered by Gradescope. In
other words, your machine's macOS or Windows file system absolute paths do not match the absolute
paths required for Gradescope's Linux environment (or a classmate's laptop file system). In other
words, absolute paths are rarely if ever portable between file systems.

### 2.4 The `pathlib` module

The Python standard library includes modules to deal with these challenges. The `pathlib` module
provides an object-oriented approach to creating and managing paths. The `pathlib` module included
in your Python 3.x download is designed to work with your operating system (OS) so no special
configuration is required for it to recognize and work with OS-specific file system paths.

:exclamation: In order to use the `pathlib` module you must _import_ it into your program. This is
done by adding an `import` statement to your code located at the top of your `*.py` file. Once
imported you can instantiate (i.e., create) an instance of the `Path` class and then access its
methods and other attributes. In the example below a `Path` instance's `cwd()` method is called to
return the current working directory path.

```python
from pathlib import Path


cwd = Path.cwd() # method call
```

You can call the `Path` instance's `resolve()` and `absolute()` methods to construct an absolute
path to this `*.py` file's parent directory:

:bulb: the "dunder" (double underscore) `__file__` attribute is assigned to the module that is
currently being imported (e.g.,  `si506_week_07.py` file).

```python
parent_path = Path(__file__).resolve().parent
# OR
parent_path = Path().absolute()
# OR
parent_path = Path().resolve()
```

As hinted above, you can leverage the "dunder" `__file__` attribute when instantiating `Path()` to
retrieve the absolute path of a target file such as `si506_week_07.py`:

```python
abs_path = Path(__file__).absolute()
# OR
abs_path = Path(__file__).resolve()
# OR
abs_path = Path("si506_week_07.py").resolve()
```

You can construct paths by calling the `joinpath()` method:

```python
parent_path = Path(__file__).resolve().parent # parent directory
faculty_path = parent_path.joinpath("data-umsi-faculty.csv")
resnick_path = parent_path.joinpath("data-resnick-citations.csv")
```

And you can retrieve segments from a path:

```python
print("\n3.4 Path parts",
   f"\nname = {resnick_path.name}",
   f"\nstem = {resnick_path.stem}",
   f"\nsuffix = {resnick_path.suffix}",
   f"\nparent dir = {resnick_path.parent}",
   f"\nparent.parent dir = {resnick_path.parent.parent}"
   )
```

There is much more to `pathlib` than returning absolute paths. For more information on using
the module see this week's recommended readings.

### 2.5 The `os.path` module

In addition to the (more modern) `pathlib` module, the standard library's `os.path` module also
includes a number of useful functions for constructing pathnames out of strings. Like `pathlib.path`
you get the `os.path` module designed for the operating system Python 3.x is expected to run on
(e.g., macOS, Windows 10).

:bulb: You will likely encounter `os.path` in the wild despite being superceded by the newer
`pathlib.Path` module. `os.path` provides string representations of filesystem paths while
`pathlib.Path` provides a dedicated path object for representing and manipulating filesystem paths.

```python
import os


# Current working directory
os_cwd = os.getcwd()

# Absolute path to directory in which *.py is located.
os_parent_path = os.path.dirname(os.path.abspath(__file__))

# Construct macOS and Windows friendly paths
os_faculty_path = os.path.join(os_parent_path, "umsi-faculty.csv")
os_resnick_path = os.path.join(os_parent_path, "resnick-citations.csv")
```

## 3.0 Opening files

This week you will learn how to create, read, and modify files stored in your machine's file system.
Data previously accessed via an in-file list will instead be stored in files that you will access
programmatically.

:exclamation: If you encounter a `FileNotFoundError` when attempting to open a file when running
your code in VS Code make sure that the terminal setting “Execute in File Dir” is enabled (i.e.,
checked). Review the relevant macOS or Windows "Installing Visual Studio Code"
[guide](https://si506.org/guides/) for setup instructions.

### 3.1 The `with` statement and the built-in `open()` function

The `with` statement ([PEP 343](https://www.python.org/dev/peps/pep-0343/)) is a control-flow
structure that helps manage resources more efficiently. This is particularly helpful when reading
from and writing to files. The `with` statement provides a _Context Manager_ that ensures that
"clean up" tasks such as closing an open file object occur (even if an error is encountered) without
the need to call a file object's `close()` method explicitly.

:bulb: Leveraging the `with` statement when reading from/writing to a file is
considered a best practice because the Context Manager it provides frees up system resources and
ensures that any file changes not yet accessible due to buffering are made available.

```python
filepath = "./data-umsi-faculty.txt" # relative path
# filepath = "data-umsi-faculty.txt" # alternative

with open(filepath) as file_obj: # open
    data = file_obj.read() # returns a single string, file object closed automatically
```

```python
filepath = Path("data-umsi-faculty.txt").resolve() # absolute path (portable)

with open(filepath) as file_obj: # open
    data = file_obj.read() # returns a single string, file object closed automatically
```

:bulb: you can pass a `size` argument (type `int`) to the `read()` method if you need to limit the
number of bytes to return.

:exclamation: Examples abound of file read/write operations that do not employ the
`with` statement. _Do not_ adopt this out-dated approach. While you can call the built-in `open()`
function directly to access a file and return a file object (also known as
a file handle) resist the temptation to do so. Doing so requires that you close
the file handle explicitly (which is easy to forget). For long running programs, a file objects
left open can drain resources.

```python
# Do not do this (requires calling the file object's close() method)
file_obj = open(filepath) # open
data = file_obj.read() # returns a single string
file_obj.close() # close (REQUIRED)
```

### 3.2 File opening modes

You can specify the _mode_ by which the built-in `open()` function opens a file. For SI 506 only the
"read" (`r`) and "write" (`w`) modes will be employed for opening text, CSV, and JSON files. That
said you should familiarize yourself with the other available modes, noting too that Python can
work with binary content such as images and PDF files.

| Character | Mode | SI 506 (in scope) |
|:----------|:-----|:-----------------:|
| __'r'__ | open for reading (default); equivalent to `rt` | __Yes__ |
| __'w'__ | open for writing, truncating the file first  | __Yes__ |
| 'a' | open for writing, appending to the end of the file if it exists |  No |
| 'x' | open for exclusive creation, failing if the file already exists | No |
| 'b' | binary mode (e.g., image, PDF), contents returned as bytes objects; `rb` = read binary; `wb` = write binary | No |
| 't' | text mode (default) | No |
| '+' | open for updating (reading and writing) | No |

```python
with open(filepath, "r") as file_obj: # open in read mode
    data = file_obj.read()

print(f"\n3.3 Data type = {type(data)}")

# Write out files with names converted to upper case
with open("./stu-umsi-faculty-v1.txt", "w") as file_obj: # open in write mode
    file_obj.write(data.upper()) # writes string to file
```

### 3.3 Read methods: `read()`, `readline()`, `readlines()`

The example above introduced the `read()` method, which, by default, reads the file object in its
entirety and returns as a single string. In contrast, the `readline()` method reads a single line
of text. You can call `readline()` n-times in order to return successive lines of text. You can
also pass a `size` argument of type `int` to the `readline()` method in order to limit the
number of characters to be returned.

```python
with open(filepath, "r") as file_obj: # open in read mode
    data = file_obj.readline()
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
```

A more useful file object method is `readlines()`. The `readlines()` method returns a list of
strings corresponding to each line in the file object.

:exclamation: Note that each string returned includes a trailing _newline_ escape sequence `\n`.

```python
with open(filepath, "r") as file_obj: # open in read mode
    data = file_obj.readlines() # returns list; elements include trailing '\n'
```

:exclamation: You are limited to calling a file object's `read()` method or `readlines()` method
_once_ after opening a connection to a file.

```python
with open(filepath, "r") as file_obj: # open in read mode
    data = file_obj.read()
    data_lines = file_obj.readlines() # WARN: does not execute
```

### 3.4 `read_file()` function

Given that opening a file is a common operation let's define a function to perform the task.

Given a valid `filepath`, the function `read_file` below opens a file, returns a file object, and
retrieves the content as a list before returning it to the caller. The function defines three
parameters:

* `filepath` (`str`): path to the file
* `encoding` (`str`): specifies the encoding used to _decode_ (i.e., read) the file. Default =
  `utf-8`.
* `strip` (`bool`): specifies whether or not individual lines in the file object are
  returned "as is" or are stripped of leading/trailing whitespace as well as the newline escape
  sequence `\n` removed. Default = `True`.

```python
def read_file(filepath, encoding="utf-8", strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file.
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """
    with open(filepath, "r", encoding=encoding) as file_obj:
        if strip:
            data = []
            for line in file_obj:
                data.append(line.strip())  # strip leading/trailing whitespace including '\n'
            return data
        else:
            return file_obj.readlines()  # list
```

### 3.5 Write methods: `write()`, `writelines()`

To write data to a file call the built-in `open()` function in "write" (`w`) mode. The file object
that is returned includes both a `write()` method and a `writelines()` method. Call the `write()`
method when working with a string.

```python
with open(filepath, "r") as file_obj: # open in read mode
        data = file_obj.read() # returns a single multiline string

# Write out files with names converted to upper case
with open("./stu-umsi-faculty-v2.txt", "w") as file_obj: # open in write mode
    file_obj.write(data.lower())
```

Call the `writelines()` method when working with a sequence. In the example below the data is
retrieved from the file, then each name is reversed (last name, first name -> first name last
name), and the results written to a text file.

:exclamation: Note that the `write()` method does not add a newline escape sequence to the string
passed to it.

```python
with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a list

# Reverse names: last, first -> first, last
for i in range(len(data)):
    name = data[i].strip().split(", ")  # strip \n
    data[i] = f"{name[1]} {name[0]}\n"  # restore \n

with open("./stu-umsi-faculty-v3.txt", "w") as file_obj:  # open in write mode
    file_obj.writelines(data)
```

An alternative to the above approach is to loop over `data` inside the `with open()` block, split
each faculty member string, and then reverse the name elements in an f-string that is passed
directly to the file object's `write()` method. This avoids mutating the `data` list.

```python
with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a single multiline string

with open("./stu-umsi-faculty-v4.txt", "w") as file_obj:  # open in write mode
    for row in data:
        name = row.strip().split(", ")
        # file_obj.write(f"{name[1]} {name[0]}") # WARN: lose trailing `n`
        file_obj.write(f"{name[1]} {name[0]}\n")  # restore `\n`
```

### 3.6 `write_file()` function

Given that writing content to a file is a common task that could occur multiple times in a program,
we should migrate the write operation to a function.

Given a valid `filepath`, the `write_file` function below writes the passed in `data` to the target
file. The function defines four parameters:

* `filepath` (`str`): path to target file (if file does not exist it will be created)
* `data` (`list` | `tuple`): sequence to be written to the target file
* `encoding` (`str`): encoding used to _encode_ (i.e., write) the file. Default =
  `utf-8`.
* `newline` (`bool`): specifies whether the newline escape sequence (`\n`) should be appended to
  each string element in the passed in `data` list. Default = `True`.

```python
def write_file(filepath, data, encoding="utf-8", newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence of strings comprising the content to be written to the
                             target file
        encoding (str): name of encoding used to encode the file.
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """
    with open(filepath, "w", encoding=encoding) as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n")  # add newline
        else:
            file_obj.writelines(data)  # write sequence to file
```

### 3.7 Challenge 01

__Task__. Read a text file containing the names of UMSI faculty. Append each surname to a list
and then write the list in _reverse_ order to a text file.

1. Call the function `read_file()` and pass it the argument `filepath`. Assign the return value to
   the variable named `data`.

2. Loop over `data`. For each "row" encountered, perform the following tasks:

   1. Split the faculty member string into a list by employing the appropriate delimiter.

   2. Access the faculty member's "surname" element.

   3. Append the "surname" element to the list named `surnames`.

      :bulb: The above tasks can be written as a one-line expression.

3. After implementing the loop, uncomment the `write_file()` function call and __replace__ the
   second argument with an expression that reverses the order of the `surnames` list.

4. Next, uncomment the code that reads `./stu-umsi-faculty-v5.txt` and assigns the surnames
   retrieved to the variable `data_v5`.

5. Uncomment the following `assert` statement:

   ```python
   assert data_v5[::-1] == surnames  # Reverse to match
   ```

6. Run your code. If your code triggers an `AssertionError` then recheck your work.

   :bulb: You will encounter `assert` statements in this week's problem set. Assert statements
   allow you to test or _assert_ that a condition is `True`.

   ```commandline
   assert < expression >
   ```

   In the example above two lists were checked for equality. If the `assert` statement evaluates to
   `False` an `AssertionError` is raised and the Python interpreter terminates code execution.

   :exclamation: Consider `assert` statements a convenience intended for pre-production testing and
   debugging only. Do not rely on `assert` statements to enforce security checks, validate data, or
   determine the flow of execution since `assert` statements are disabled when code is executed in
   optimized mode. For more on `assert` statements see Leodanis Pozo Ramos,
   ["Python's assert: Debug and Test Your Code Like a Pro"](https://realpython.com/python-assert-statement/)
   (Real Python, Feb 2022).

## 4.0 Working with CSV files

A comma-separated values (CSV) file is a common data interchange format used to represent
tabular data. It is a delimited text file that utilizes a comma (`,`) typically to separate individual
values. Other delimiters include pipes (`|`) or tabs, though use of the latter is usually referred
to as a tab-delimited values (TSV) file.

Keep in mind the following when working with or creating CSV files:

1. If a value in a CSV file includes a delimiter (e.g., a comma), the value is usually surrounded by
   double quotation marks (`""`).

2. The first row in a CSV file is often a designated "header" row that contains a list of the column
   names (or headers) that describe the following data. This is recommended practice that helps to
   make the CSV file self-documenting. But you need to exclude the row when working with the actual
   data.

3. Occasionally the first character in a CSV file is a
   [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark) (BOM). You can filter it out by
   changing the built-in `open()` function's optional encoding value to `utf-8-sig`.

   ```python
   with open("path_to_a_csv_file.csv", encoding="utf-8-sig") as fileobj:
       # Retrieve data
   ```

4. You can save Excel spreadsheets and export Google sheets as CSV files.

5. The VS Code marketplace features an extension called
   [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) that
   you can install in order to make viewing a CSV file a more pleasant experience.

### 4.1 The `csv` module

The Python Standard library includes a [`csv` module](https://docs.python.org/3/library/csv.html)
that simplifies working with CSV files. In order to use the `csv` module you _must_ import it into
your program. This is done by adding an `import` statement to your code located at the top of your
file.

```python
import csv
```

The `csv` module defines a number of classes, functions and constants. This week we focus on two
functions:

* `csv.reader()`. Returns a reader object that can iterate over the contents of a CSV file
* `csv.writer()`. Returns a writer object that can convert data into delimited strings that are
  stored in a CSV file

Since reading from and writing to CSV files is a common task that is often repeated in a Python
program the teaching team has implemented two functions that you can use whenever you need to work
with a CSV file.

### 4.2 `read_csv()` function

The `read_csv()` function leverages the `csv` module's `reader` object to retrieve data from a CSV
file. The function defines four parameters:

* `filepath` (`str`): location of the CSV file to be read.
* `encoding` (`str`): encoding used to _decode_ (i.e., read) the file. Default = `utf-8`.
* `newline` (`str`): replacement value for newline `"\n"` or `"\r\n"` (Windows) character
  sequences. Default = `""` (blank).
* `delimiter` (`str`): delimiter that separates each row value. Default = `","`.

The function employs the `with` statement and the built-in `open()` function to open the file and
return a file object. A `reader` object is then created by calling the `csv.reader()` function and
passing it the `file_obj` and `delimiter` as arguments. The reader object is an _iterable_
(e.g., has members that can be accessed) and you can loop over it in order to access each "row"
element. Doing so allows each `row` in the `reader` to be appended to the `data` list. Once the
`for` loop finishes its work, the `data` list is returned to the caller.

```python
def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass "utf-8-sig" as the < encoding > argument.

    WARN: If newline="" is not specified, newlines "\n" or "\r\n" embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline "\n"
                       or "\r\n" (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """
    with open(filepath, "r", encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data
```

### 4.3 `csv.writer()` function

The `write_csv()` function leverages the `csv` module"s `write` object to convert data into
delimited strings that are written to a CSV file. The function defines five parameters:

* `filepath` (`str`): path to target file (if file does not exist it will be created)
* `data` (`list` | `tuple`): sequence to be written to the target file
* `headers` (`list` | `tuple`): optional header row list or tuple
* `encoding` (`str`): encoding used to _encode_ (i.e., write) the file. Default = `utf-8`.
* `newline` (`str`): replacement value for newline `"\n"` or `"\r\n"` (Windows) character
  sequences. Default = `""` (blank).

Similar to `read_csv()` the function employs a `with` statement and the built-in `open()` function
to open the file and return a file object. A `writer` object is then created by calling the
`csv.writer()` function and passing it the `file_obj` as an argument.

The delimiter value `headers` is truth-tested.  If the conditional statement is _truthy_ a headers
row is written by calling the `writer.writerow()`. Then each row in `data` is written to the file.
If no headers are provided by the caller the `headers` default value is considered `falsy` and the
`data` list is passed directly to the `writer.writerows()` method.

:exclamation: The `write_data` function requires that data passed to it is either a `list` or a
`tuple`. If working with strings, each string _must_ be placed in a `list` otherwise the
`csv_writer` will parse the string as a sequence, treating each character as a seperate data element
and separating each with a comma when written to the CSV file.

```python
def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline="" is not specified, newlines "\n" or "\r\n" embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    "\r\n" an extra "\r" will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline "\n"
                       or "\r\n" (Windows) character sequences

    Returns:
        None
    """
    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)
```

Utilize the `read_csv()` and `write_csv()` functions to read CSV files, manipulate and/or
analyze the data returned, and write the results of our work to one or more "target" CSV files.

### 4.4 Challenge 02

__Task__. Utilize the function `read_csv()` to read a CSV file. Apply a filtering condition to
identify publications coauthored by Professor Paul Resnick that feature the word "recommender" in
the title. Then call the function `write_csv()` to write the filtered data to a new CSV file.

:bulb: Paul is considered a pioneer in the development of such systems.

1. In `main()` call the function `read_csv()` and pass it the argument `filepath`. Assign the return
   value to a variable named `publications`.

2. Uncomment the accumulator list `recommender_publications`.

3. Uncomment the `for` loop. Inside the loop block replace the `pass` statement with an `if`
   statement that evaluates whether or not the current publication's "Title" element contains the
   substring "recommender". Perform a _case insensitive_ string comparison.

   :bulb: Leverage the `headers` list to look up the "Title" element's index.

4. If the conditional statement evaluates to `True` add the current publication (a `list`) to
   `recommender_publications`.

5. After the loop terminates call the function `write_csv()` and pass `filepath` (new CSV),
   `recommender_publications`, and `headers` as arguments.

6. Run your code and check the file output.

## 5.0 Error handling with `try` and `except` statements

The Resnick publication/citation data contains a variety of numbers masquerading as strings.
However, given the number of list elements, looping over the data and attempting to determine which
elements to convert to type `int` appears problematic.

Python's `try` and `except` statements can help reduce the complexity of the challenge. The idea
behind the statements is to _try_ and perform an operation inside the `try` statement block and if
the action triggers a runtime exception allow the accompanying `except` statement to _catch_ the
exception before it terminates execution and perform one or more operations in response.

The strategy is to handle errors _after_ they are encountered rather than before, an approach
known by the acronym __EAFP__ (i.e., easier to ask forgiveness than permission).

The function `convert_to_int` illustrates how to leverage `try` and `except` statements to keep a
program/script running despite encountering a runtime exception (in this case a `ValueError`) if
a value is passed to the function that cannot be converted to an integer by the built-in `int()`
function.

```python
def convert_to_int(value):
    """Attempts to convert a string, number or boolean value to an int. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        int: if value successfully converted else returns value unchanged
    """

    try:
        return int(value)
    except ValueError:
        return value
```

When a `value` is passed to `convert_to_int` the Python interpreter will attempt to execute the
`try` clause. Should the `try` block result in an exception, the interpreter will proceed
directly to the `except` clause and execute its statement block, thus avoiding the termination of
the program's execution due to an exception (such as a `ValueError`).

An `except` clause may specify a specific exception type or multiple exceptions expressed as a
parenthesized tuple:

```python
except ValueError:
   ...
```

```python
except (AttributeError, TypeError, ValueError):
      ...
```

Also a `try` statement may be accompanied by more than one `except` clause in order to specify
different handlers for different exceptions. An `else` clause can be added after the `except`
statement(s) in order to include code that _must_ be executed if the `try` statement block does
not raise an exception.

:exclamation: If an exception occurs that does not match the specified exception(s) named in the
`except` clause an _unhandled_ exception is triggered and code execution will cease as a result.

### 5.1 Challenge 03

__Task__. Leverage the function `convert_to_int()` to convert list elements masquerading as strings
to integers.

:bulb: In order to accomplish the task you will need to call the function `convert_to_int` from
inside a nested loop (a future topic) or pair the function with another function that allows us to
traverse each publication's elements. The function `clean_data` is designed to handles that task.

1. Implement the function `clean_data()` (replace the `pass` statement).

   :exclamation: Review the function's docstring to better understand the task it is to perform, the
   parameter it defines, and the return value it computes.

2. In the function block implement a `for i in range()` loop. Instantiate the `range` object with a
   stop value equal to the length of the passed in `publication` list. Loop over the numeric
   sequence provided by `range` and use `i` to access each `publication` element. Pass each element
   to the function `convert_to_int()`. Assign the return value (back) to the _current_ `publication`
   element.

3. After the loop terminates `return` the mutated `publication` list to the caller.

4. After implementing the function return to `main()`.

5. Uncomment the `idx` variable assignment.

6. Uncomment the `for` loop. Inside the loop block, replace the `pass` statement by calling the
   function `clean_data()` and passing the current element (a nested "publication" list) as the
   argument. Assign the return value (back) to the current nested list element.

7. Uncomment `print()` and check your work.

   If all goes well each mutated publication element will resemble the following list:

   ```python
   ["Recommender systems", "Resnick, Paul; Varian, HR", "", "COMMUNICATIONS OF THE ACM", "MAR 1997",
   1997, 40, 3, "", "", "", 56, 58, "", "10.1145/245108.245121", "", "", 1552, "64.67", 0, 0, 3, 4,
   16, 24, 19, 24, 34, 49, 52, 38, 73, 79, 91, 82, 80, 83, 87, 107, 126, 132, 112, 113, 91, 33]
   ```

## 6.0 Additional Challenges

Below are additional challenges that focus on implementing functions and reading from and writing to
CSV files.

### 6.1 Challenge 04

__Task__. Implement a function that permits retrieval of any publication element
using the CSV "headers" row as an index lookup mechanism.

1. Implement the function `convert_to_float()`. Review the function's docstring to better understand
   the task it is to perform, the parameter it defines, and the return value it computes.

   :bulb: Adopt the same value handling pattern as `convert_to_int()`.

2. Implement the function `get_attribute`. Review the function's docstring to better understand the
   task it is to perform, the parameters it defines, and the return value it computes.

   :bulb: The function can be implemented with one line of code.

   Once implemented, you can employ the function to return any single publication attribute
   (e.g., Title, Publication Year, Total Citations) by leveraging the CSV's "headers" row of column
   names to look up the element's index value.

3. After implementing `get_attribute()` return to the `main` function. Loop over the `publications`
   list.

4. Uncomment the `idx` variable assignment.

5. Uncomment the `for` loop. Inside the loop block do the following:

   1. Each publication's "Average per Year" value is a string that can be converted to a float. Call
      the function `get_attribute()` passing it the arguments it requires to return the current
      publication's "Average per Year" value. Assign the return value to a variable (name your
      choice).

   2. Next, call the function `convert_to_float()` and pass to it the value to be converted. Assign
      the return value to the current publication's "Average per Year" __element__ using the
      provided `idx` value. (i.e., mutate the element).

6. Uncomment `print()` and check your work.

### 6.2 Challenge 05

__Task__: Return a list of UMSI-coauthored publications. Write the results to a file.

1. In the `has_umsi_faculty_author()` function block add a compound conditional `if` statement that
   implements the following two conditions:

   1. The local `name` value __must not equal__ either the passed in or default `ignore` value
      (default = "Resnick, Paul").
   2. The local `name` value matches a string element in the `coauthors` list.

   If a match is obtained `return` the boolean value `True`. Otherwise, the function returns
   `False`.

   :exclamation: Both conditions _must_ evaluate to `True` for the entire conditional statement to
   evaluate to `True`. For example, the following `coauthors` string contains three UMSI coauthors:

   ```python
   "Resnick, Paul; Adar, Eytan; Lampe, Cliff"
   ```

   The conditional statement that you write inside the `umsi_faculty` loop block _must_ ignore Paul
   but match on "Adar, Eytan".

2. After fixing `has_umsi_faculty_author` return to `main()`.

3. Uncomment the `umsi_faculty` variable assignment.

4. Uncomment the `for` loop. Inside the loop block do the following:

   1. Call the call the function `get_attribute()` and pass it the three arguments it requires to
      retrieve the current publication's "Authors" value (a `str`).

   2. Split the "Authors" string (delimiter = "; ") and assign the new list to a variable named
      `authors`.

   3. Insert an `if` statement that evaluates the return value's "truthiness" when
      `has_umsi_faculty_author()` is called. Pass `umsi_faculty` (minus the header row) and
      `authors` as arguments to the function.

   4. If the conditional statement evaluates to `True` the current publication is appended to
      `umsi_coauthored_publications`.

5. Call the function `write_csv` and write the updated `umsi_coauthored_publications` list to the
   file `stu-resnick-citations-umsi_coauthored.csv` employing `headers` as the headers argument.

### 6.3 Challenge 06

__Task__: Return the publication(s) with the highest citation count (ties _must_ be accommodated).
Write the results to a file.

1. In `main()` assign sensible start values to the variables `max_citations` (`list`) and
   `max_count` (`int`).

2. Loop over the `publications` list (exclude the "headers" element) and do the following:

   1. Call the function `get_attribute()` to retrieve the current publication's "Total Citations"
      count and assign the return value to a variable of your own choosing.

   2. Implement conditional statements that compares the current publication's "Total Citations"
      count to the previously recorded `max_count`.

      __Requirements__

      1. If the current "Total Citations" count is greater than the previous count, _remove_ all
      publications added previously to `max_citations` and then append the current publication to
      the list (the new leader). Update `max_count`.

      2. If the current count is equal to the previous `max_count` append the publication to
      `max_citations`.

      3. Otherwise, proceed to the next iteration of the loop.

3. After exiting the loop call the function `write_csv` and write the updated `max_citations` list
   to a file named `stu-resnick-citations-max_citations.csv` passing the `headers` list as the
   `headers` argument.

### 6.4 Challenge 07 (Bonus)

__Task__: The data set includes columns that provide an annual count of the number of citations
garnered by each publication for the period 1995-2020. However, the total citation count per year
is not provided and must be calculated. Implement a function that computes the total citation count
across all publications for a given year.

1. Uncomment the `idx` variable assignment (a hint to get you started).

2. Return a slice of `headers` that includes all "year" elements (1995-2000). Use `idx` as the
   slicing start value. Assign the list to a variable named `years`.

   :bulb: Look up the index value for the `headers` element `1995` and use it as the start value in
   your slicing notation.

3. Implement the function `get_citation_count_by_year`. Review the function's docstring to better
   understand the task it is to perform, the parameters it defines, and the return value it
   computes.

4. After implementing `get_citation_count_by_year` return to the `main` function. Loop over the
   `years` list and in the loop block call the function `get_citation_count_by_year` passing to it
   the `publications` list, `headers`, and the current year value as arguments. Assign the return
   value to a local variable of your own choosing (e.g., `count`).

5. Append the annual citation count to the accumulator list `annual_counts` in the form of a
   two-item tuple comprising the year and total citations count for the year.

   ```python
   [
       (< year x >, < total citations >),
       (< year y >, < total citations >),
       . . .
   ]
   ```

6. After exiting the loop call the function `write_csv` and write the `annual_counts` list to the
   file `stu-resnick-citations-annual_counts.csv`. Since each nested tuple comprises two items pass
   `["year", "citations"]` as the headers argument.
