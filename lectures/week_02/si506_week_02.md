# SI 506 Week 02

## Topics

1. Comments (single line, block)
2. Values and types
   1. Numeric: integer, float (decimal)
   2. Sequences: strings, lists, tuples, set
   3. Dictionary (associate array)
   4. Boolean
   5. Nonetype
3. Variables
   1. Variable assignment
   2. Variable naming rules and conventions
   3. Challenge 01
4. Built-in functions `print()`, `type()`, `len()`
   1. `print()`: print passed in argument to the screen
   2. `type()`: determine object's data type
   3. `len()`: check length of a sequence (i.e., number of elements)
   4. Challenge 02
5. Basic arithmetic (add, subtract, multiply, divide)
   1. Arithmetic operators
   2. Challenge 03
6. Statements and expressions
   1. Challenge 04
   2. Challenge 05
7. Object behaviors (a gentle intro)
   1. `str.lower()`, `str.upper()`
   2. `str.startswith()`, `str.endswith()`
   3. `str.count()`
   4. `str.replace()`
   5. Challenge 06
   6. Challenge 07
8. String formatting: formatted string literal
   1. Challenge 08

## Reference

Bookmark the following
[w3schools](https://www.w3schools.com/python/default.asp) Python pages and/or have them open in a
set of browser tabs both during class and while working on this week's problem set:

* ["Python Built-in Functions"](https://www.w3schools.com/python/python_ref_functions.asp)
* ["Python Operators"](https://www.w3schools.com/python/python_operators.asp)
* ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)

## Lecture data

The American Library Association's Office for Intellectual Freedom (OIF) maintains a list of the
["Top 13 Most Challenged Books of 2022"](https://www.ala.org/advocacy/bbooks/frequentlychallengedbooks/top10?gclid=Cj0KCQjwusunBhCYARIsAFBsUP-k5zOE844CAvg-2xeu0moS-nvQVVwJvVDVdFrRDZWH3RBEJpuuZoUaAicbEALw_wcB)
in order to highlight censorship in US libraries and schools (2023 figures have yet to be released).
The ALA recorded 1,269 attempts to ban or restrict library resources during 2022. The resources
targeted included 2,571 unique titles. These numbers exceed the 2021 totals (729 censorship
challenges, 1,597 titles), the highest number of annual challenges reported by the ALA in a single
year since it began tracking challenges twenty years ago. The ALA reports that the majority of
challenges involved works by or about Black or LBGTQIA+ persons. This week's lectures features
challenged works drawn from the ALA "Most Challenged" list.

Other sources consulted include:

* [ALA](https://www.ala.org/). ["Unite Against Book Bans"](https://uniteagainstbookbans.org/).
* [pen.org](https://pen.org/). ["Banned in the USA: The Growing Movement to Censor Books in Schools"](https://pen.org/report/banned-usa-growing-movement-to-censor-books-in-schools/).

## 1.0 Comments

Explanatory text known as "comments" can be embedded in code with no impact on the runtime
characteristics of the program or script. In Python single line comments are delinated by prefacing
the line with a hash (`#`) character.

```python
# A single line comment
```

Successive lines of comments are considered a "block" comment.

```python
# A single line comment
# Yet another single line comment
# And yet another single line comment
```

You can also comment code rendering it inert and incapable of being interpreted (i.e., executed) at
runtime.

```python
# x = 5
# y = 2
# sum = x + y
```

You can also place a comment "inline" at the end of a line of code:

```python
url = "https://uniteagainstbookbans.org/"  # ALA initiative
```

:bulb: Later in the course you will be introduced to documentation strings or "docstrings" which are
used to document classes, functions, and methods.

## 2.0 Values and types

>"Everything is an Object"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jake VanderPlas, _A Whirlwind Tour of Python_ (O'Reilly Media, Inc., 2016)

> "Objects are Python's abstraction for data. All data in a Python program is represented by objects
> or by relations between objects."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python Software Foundation, ["The Python Language Reference"](https://docs.python.org/3/reference/datamodel.html)

![Python objects](python_objects.png)

Python is an object-oriented programming language. This means that the Python data model represents
strings, integers, floating point numbers, containers (e.g., `list`, `tuple`, `set`), mappings
(`dict`), functions, class instances, modules and other types as __objects__.

The basic characteristics of a Python object can be summarized as follows:

1. Every object possesses an _identity_ (memory address), _type_, and _value_.
2. An object’s _type_ determines its behavior as well as defines the possible values it may contain.
3. The value of some objects can be modified. An object's _mutability_ (e.g., _mutable_ = capable of
   modification; _immutable_ = incapable of modification) is determined by its _type_.
4. Objects are never explicitly destroyed; memory management and "garbage-collection" is typically
   ceded to the Python interpreter without the need for manual intervention.

### 2.1 Numeric: integer, float (decimal), complex

```python
# Integer
781

# Float
.781

# Complex
4 + 3j  # combines a real and imaginary number
```

### 2.2 Sequences: strings, lists, tuples, set

```python
# String (ordered, immutable)
"I am a sequence of characters" # string

# List (ordered, mutable)
["arwhyte", "brooksch", "collemc", "csev", "cteplovs"] # list with five elements

# Tuple (ordered, immutable)
(504, 506, 507)
(arwhyte,)  # single item tuple (note trailing comma)

# Set (unordered, mutable, but each element must be immutable as well as unique)
{27, 24, False, 7.5, True, "text"}
```

A "multiline" string (actually a string constant) can be expressed by the surrounding the string
with either triple quotation marks (`"""`) or triple apostrophes (`'''`).

:bulb: The Black formatter favors use of quotation marks over apostrophes.

The following example reproduces the first two sentences of Toni Morrison's foreward to the 2007
Vintage International edition of the _The Bluest Eye_, first published in 1970.

```python
"""There can't be anyone, I am sure, who doesn't know what it
feels liked to be disliked, even rejected, momentarily or for sus-
tained periods of time. Perhaps the feeling is merely indiffer-
ence, mild annoyance, but it may also be hurt. It may even be
that some of us know what it is like to be actually hated&mdash;
hated for things we have no control over and cannot change. . . .
"""
```

The same string can also be expressed across multiple lines by surrounding it with parentheses `()`
and employing the escape sequence (`\n`) to denote each line break.

:bulb: The `\n` characters represents an escape sequence, specifically an ASCII linefeed (LF).
Think of `\n` as "newline". Passing `\n` in a string will insert a new line at the position of the
escape sequence.

```python
(
    "There can't be anyone, I am sure, who doesn't know what it\n"
    "feels liked to be disliked, even rejected, momentarily or for sus-\n"
    "tained periods of time. Perhaps the feeling is merely indiffer-\n"
    "ence, mild annoyance, but it may also be hurt. It may even be\n"
    "that some of us know what it is like to be actually hated--\n"
    "hated for things we have no control over and cannot change. . . ."
)
```

### 2.3 Dictionary (associative array)

A dictionary is composed of key-value pairs. Insertion order is maintained.

```python
{
   "year": 2022,
   "censorship_attempts": 1269,
   "books_targeted": 2571,
   "source": "https://ala.org/"
}
```

### 2.4 Boolean

```python
True
False
```

### 2.5 Nonetype

`None` is an object of type `<class 'NoneType'>` and represents `null` or the absence of a concrete
value.

:exclamation: Note that `None` does not equal 0.

```python
None
```

## 3.0 Variables

A Python _variable_ is a name or label that refers to an object in memory. Jake VanderPlus describes
the concept in _A Whirlwind Tour of Python_:

>“. . . variables are simply pointers [to objects], and the variable names themselves have no attached type information.”

Or as Naomi Cedar writes in _The Quick Python Book_, Third Edition (Manning Publications, 2018):

>"The name variable is somewhat misleading . . .; name or label would be more accurate.”

### 3.1 Variable assignment

Employ the assignment (`=`) operator to _assign_ a variable to a value or _bind_ the name (i.e.,
the pointer or label) to the object (e.g., `variable_name = < object >`).

```python
organization = "American Library Association"
year_founded = 1876
strategic_directions = [
    "Advocacy",
    "Information Policy",
    "Professional & Leadership Development.",
    "Equity, Diversity & Inclusion"
    ]

tweet = """Standing up for the right to read can feel daunting. But without
your voice, there may be no one standing between book bans
and your community.

Make a plan and make your voice heard - attend a library or
school board meeting:
https://uniteagainstbookbans.org/attend-library-school-board-meetings/
#UniteAgainstBookBans
"""  # @UABookBans Aug 28, 2023
```

### 3.2 Variable naming rules and conventions

Default convention: lowercase word(s) or recognizable abbreviation (e.g., num, val, var);
separate words with an underscore.

:exclamation: Readability and comprehensibility matters. See the Python Community's
[Style Guide for Python Code (PEP 8](https://pep8.org/) (reformatted by Kenneth Reitz).

#### 3.2.1 Good

```python
# Choose lowercase
title = "Beloved"

# Separate words with underscore (_)
banned_author = "Toni Morrison"

# Use plural form to indicate a set or sequence
banned_titles = ["The Bluest Eye", "Beloved", "Song of Solomon"]

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 1269

# "is_", "has_" prefix: Boolean True/False
is_banned = False
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = "https://www.ala.org/"

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y  # arithmetic expression

# For loop incorporating a counter < i > value
i = 1 # counter
for title in banned_titles:
    print(f"{i}. {title}")
    i += 1 # addition assignment (increment)
```

#### 3.2.2 Bad (But Legal)

```python
# Opaque
b = "Beloved"
sos = "Song of Solomon"

# Reserve CamelCase for class names, e.g. GraphicMemoir().
GraphicMemoir = "Gender Queer"  # restyle variable as graphic_memoir

# Not a fan of trailing data type suffixes (_list)
banned_authors_list = ["Maia Kobabe", "George M. Johnson", "Mike Curato"] # prefer course_codes (plural)
```

:exclamation: Avoid prefixing or suffixing variable names with single (`_`) or double underscores (`__`)
&mdash; known in the Python community as a "dunder" &mdash; until you gain experience as a Python
programmer.

Variable names prefixed with a single underscore like `_course_code` are, by convention, considered
private member variables in a class. Variable names prefixed with a double underscore like
`__course_code__`, get renamed at runtime by the Python interpreter in a process known as "name
mangling".

:bulb: These and other naming conventions that employ leading and/or trailing underscores are
_out of scope_ for SI 506. That said, if you want to learn more on the subject see D. Bader,
["The Meaning of Underscores in Python"](https://dbader.org/blog/meaning-of-underscores-in-python)
(dbader.org, nd).

#### 3.2.3 Ugly (Illegal)

The Python Interpreter will raise a `SyntaxError` at runtime whenever it encounters the following
illegal names:

:exclamation: Python [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
are reserved and cannot be used as variable names.

```python
# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)
class = "SI 506"

# Illegal: variable name commences with a numeric value.
506_lab = "SI 506"

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)
$number = 506

# Illegal: variable name includes a dash (`-`).
course-list = ["SI 506", "SI 507", "SI 618"]

# Illegal: variable name includes whitespace.
course name = "SI 506" # illegal; uncomment to test
```

:exclamation: Also avoid use of
[built-in function](https://docs.python.org/3/library/functions.html) names as variable names.
Name clashes may occur in your code. If you do opt to use or "shadow" such names add a trailing
underscore character to the name (`_`) per the
[PEP 08](https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments) recommendation or
opt for a different name (`len_` or `length` for `len`).

```python
# Shadowing; risk name clash with built-in functions
id = 506
str = "Go Blue"
min = 0
max = 27
len = 6

# Alternative names
id_ = 506

str_ = "Go Blue"
val = "Go Blue"

min_ = 0
min_val = 0

max_ = 27
max_val = 27

len_ = 6
length = 6
```

### 3.3 Challenge 01

__Task__: Create a list of strings that represent the top four (`4`) books targeted for banning in
the US in 2022.

1. Employ a _list literal_ to create a list containing the following strings:

   * Gender Queer: A Memoir
   * All Boys Aren’t Blue
   * The Bluest Eye
   * Flamer

   :bulb: A list literal is defined by enclosing comma-separated values between square brackets
   (`[]`).

   :exclamation: One book title includes an apostrophe (`'`). Employ double quotes (`"`) to denote
   the string.

2. Assign the list to a variable named `titles`.

3. After creating the list _uncomment_ the accompanying built-in function `print()` (i.e., remove
   the leading `#`) and then click the run button to execute your code.

## 4.0 Built-in Functions (`print()`, `type()`, `len()`)

The Python standard library includes a number of
[built-in functions](https://docs.python.org/3/library/functions.html) that are always available for
you to call.

:bulb: A function is a defined block of code that performs (ideally) a single task. Functions only
run when they are explicitly called. A function can be defined with one or more _parameters_ that
allow it to accept _arguments_ from the caller in order to perform a computation. A function can
also be designed to return a computed value. Functions are considered "first-class" objects in the
Python ecosystem. You will soon write your own functions; for now we introduce a select number of
built-in functions for you to use.

### 4.1 `print()`: print passed in argument to the screen

```python
# Passing a hard-coded string.
print("\n4.1.1 Libraries rock!") # \n = newline escape character

# Passing a variable name which points to a string.
print(f"\n4.1.2 organization = {organization}") # formatted string literal
```

### 4.2 `type()`: determine object's data type

```python
data_type = type(year_founded)
print(f"\n4.2.1 year_founded type = {data_type}") # returns <class 'int'>

data_type = type(tweet)
print(f"\n4.2.2 tweet type = {data_type}") # returns <class 'str'>

data_type = type(strategic_directions)
print(f"\n4.2.3 strategic_directions type = {data_type}") # returns <class 'list'>
```

### 4.3 `len()`: check length of a sequence (i.e., number of elements)

```python
# Count characters in string (including whitespace).
char_count = len(tweet)
print(f"\n4.3.1 tweet length = {char_count}")

# Count number of elements in list.
element_count = len(strategic_directions)
print(f"\n4.3.2 strategic_directions length = {element_count}")
```

### 4.4 Challenge 02

__Task__: Utilize the `titles` list to explore the built-in functions `len()`, `type()`, and
`print()`.

1. Call the built-in function `type()` passing `titles` as the argument. Assign the return
   value to a variable named `data_type`. Print `data_type` to the terminal screen.

2. Return the length of the `titles` list and then immediately print the value to the terminal
   screen. Perform the two tasks by writing only a _single line of code_.

## 5.0 Basic Arithmetic (addition, subtraction, multiplication, division operators)

Python supports math operations. The order of operations is expressed conveniently by the acronym
__PEMDAS__: Parentheses, Exponentation, Multiplication \| Division (same precedence), Addition \|
Subtraction.

1. Parentheses have the highest precedence and can be used to force an expression to evaluate in the
   order you want. Since expressions in parentheses are evaluated first, `2 * (3-1)` is 4, and
   `(1+1)**(5-2)` is 8. You can also use parentheses to make an expression easier to read, as in
   `(minute * 100) / 60`, even though it doesn’t change the result.

2. Exponentiation has the next highest precedence, so `2 ** 1 + 1` is 3 and not 4, and `3 * 1 ** 3`
   is 3 and not 27.

3. Multiplication and both division operators have the same precedence, which is higher than
   addition and subtraction, which also have the same precedence. So `2*3-1` yields 5 rather than 4,
   and `5-2*2` is 1, not 6.

4. Operators with the same precedence (except for **) are evaluated from left-to-right. In algebra
   we say they are left-associative. So in the expression `6-3+2`, the subtraction happens first,
   yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right
   to left, the result would have been `6-(3+2)`, which is 1.

### 5.1 Arithmetic operators

| Operator | Name | Description |
| :------- | :--- | :---------- |
| + | Addition | |
| - | Subtraction | |
| * | Multiplication | |
| / | (Floating Point) Division | Returns a floating-point value (a `float`) that contains a fractional component (`5 / 2` returns `2.5`).|
| // | Floor Division | Returns an integer (i.e., a whole number) ignoring any fractional component (`5 // 2` returns `2`). |
| % | Modulus | Returns the remainder of a division operation (e.g., `5 % 2` returns `1`).  |
| ** | Exponentiation | Returns the product of a number (the base) multiplied `n` times specified exponent (`2.5 ** 2` returns `6.25`). |

### 5.2 Challenge 03

__Task__. Perform various SI 506-inspired arithmetic operations starting off with the values
assigned to the following variables:

```python
# SI 506
lecturer_count = 1
gsi_count = 3
ia_count = 3
student_count = 111
seat_count = 162
```

1. Return a count of all members of the teaching team employing the appropriate variables. Assign
   the value returned to a variable named `team_count`. Then uncomment `print()` and run your code.

2. Given the current `student_count`, return the number of available seats in the classroom. Assign
   the value returned to a variable named `open_seats`. Then uncomment `print()` and run your code.

3. Return the maximum permitted enrollment for SI 506. You can approximate the max enrollment by
   multiplying the number of GSIs by forty (`40`). Assign the return value to a variable named
   `max_enrollment`. Then uncomment `print()` and run your code.

4. Calculate the ratio of students to GSI using _floor_ division. Assign the
   return value to a variable named `students_per_gsi`. Then uncomment `print()` and run your code.

5. Calculate SI 506's current enrollment expressed as _a percentage_ of the max enrollment using
   _floating-point_ division. Assign the return value to a variable named `max_enrolled_pct`. Then
   uncomment `print()` and run your code.

## 6.0 Statements and expressions

A Python _statement_ is an instruction that performs some action. For example, a variable assignment
is considered a statement. Actions that evaluate one or more conditions (`if-else-if`) or involve
iteration over a sequence or a dictionary (`for`, `while`) are also considered statements.

A Python _expression_ is a combination of values, pointers (i.e., variables), operators, and/or
function or method calls that return a value.

:bulb: A statement can include one or more expressions (the reverse is not true).

```python
office = "ALA Office for Intellectual Freedom"  # statement

challenges = 377 + 156 + 729 + 1269  # arithmetical expression within a statement

print(challenges)  # expression (function call)
```

### 6.1 Challenge 04

__Task__. Assign string values to specified variables. Confirm variable assignments by passing
variables to the built-in `print()` function.

Maia Kobabe's graphic memoir _Gender Queer: A Memoir_ (2019) leads the 2022 list of most challenged
books according to the ALA.

1. Assign the string "Gender Queer: A Memoir" to a variable named `banned_title`.

2. Assign the string "Maia Kobabe" to a variable named `banned_author`.

3. Assign the string "(Lion Forge Comics, 2019)" to a variable named `banned_publisher`.

4. Call the built-in `print()` function and pass the three variables to it as arguments in the
   following order:

   1. `banned_author`
   2. `banned_title`
   3. `banned_publisher`

   Separate each argument by a comma and a space (`, `) inside the function's trailing parentheses
   (`print(< var_01 >, < var_02 >, < var_03 >)`).

   :bulb: The built-in `print()` function can accept multiple arguments. See Bartosz Zaczyński,
   ["Your Guide to the Python print() Function"](https://realpython.com/python-print/) (Real Python,
   Aug 2019) for an extended discussion of `print()` capabilities.

5. The terminal output _must_ match the following string:

   ```commandline
   Maia Kobabe Gender Queer: A Memoir (Lion Forge Comics, 2019)
   ```

### 6.3 Challenge 05

__Task__. Use string concatenation to return a _new_ string assembled from the three "banned"
variables.

:bulb: You can use the plus (`+`) operator to construct a new string by joining two or more strings.
This is known as string _concatenation_.

1. Concatenate the "banned" strings by creating an expression that positions the plus (`+`) operator
   _between_ each of the three variables.

   :exclamation: Employ the same variable order as the previous challenge.

2. Add a string comprising a comma _and_ a space between `banned_author` and `banned_title`. This
   will require the insertion of another plus (`+`) operator in the expression.

3. Add a string comprising a space between `banned_title` and `banned_publisher`.
   This will require the insertion of yet another plus (`+`) operator in the expression.

4. Append a trailing period (`.`) to the end of the concatenated string you are constructing.

5. Assign the expression (a new string) to a variable named `banned_book`.

6. Call the built-in `print()` function (an expression) and pass to it `banned_book` as the
   argument. The terminal output _must_ match the following string:

   ```commandline
   Maia Kobabe, Gender Queer: A Memoir (Lion Forge Comics, 2019).
   ```

## 7.0 Object behaviors (a gentle intro)

The string (`str`) type or object can be said to exhibit behaviors that are expressed in the form of
_methods_ that you can call. For example, you can employ _dot notation_ to call `str` type's
`upper()` method in order to return a version of the string converted to all upper case characters:

```python
event = "banned books week (1-7 October 2023)"
event_upper_case = event.upper()
```

Over the course of the semester you will learn to use a number of `str` methods. For a complete
listing see w3schools'
["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp).

:bulb: Other data types such as lists, tuples, and dictionaries also include methods that you can
call. We will explore those types and their methods in the coming weeks.

Below are a few examples of `str` methods that you can call.

### 7.1 `str.lower()`, `str.upper()`

Return a version of the string in which its characters have been converted to either upper case or
lower case.

```python
title = "Beyond Magenta"
lower_case = title.lower()  # Returns beyond magenta
upper_case = title.upper()  # Returns BEYOND MAGENTA
```

### 7.2 `str.startswith()`, `str.endswith()`

Calling `str.startswith()` returns `True` if the string commences with the specified value. Calling
`str.endswith()` returns `True` if the string ends with the specified value. In either case, if the
condition is not satisfied the method returns `False`.

```python
title = "Out of Darkness"
starts_with_O = title.startswith("O") # Returns True
ends_with_S = title.endswith("S") # Returns False
```

### 7.3 `str.count()`

Return the number of times a specified value occurs in a string.

New York Times, The Learning Network,
["What Students Are Saying About Banning Books From School Libraries"](https://www.nytimes.com/2022/02/18/learning/students-book-bans.html) (New York Times, 18 Feb 2022)

```python
source = 'The Learning Network, "What Students Are Saying About Banning Books From School Libraries" (New York Times, 18 Feb 2022).'
char_a_count = source.count("a") # Returns 6
char_ban_count = source.count("Ban") # Returns 1
```

### 7.4 `str.replace()`

Returns a new string by replacing the specified substring with a new value.

```python
ala_statement = "The American Library Association condemns censorship and works to ensure free access to information."
ala_statement = ala_statement.replace("American Library Association", "ALA") # Returns The ALA condemns ....
```

### 7.5 Challenge 06

__Task__. Fix a typo in a challenged book title using the appropriate string method that can return
a corrected version of the string.

Angie Thomas's debut novel _The Hate U Give_ (2017) has been targeted for removal from library
collections nearly every year since its publication five years ago.

1. The string value named `title` contains a typographical error in the book's title. Select
   the appropriate `str` method introduced above that can be used to return a corrected version of
   the string.

2. Assign the return value to the (existing) variable `title`.

   :bulb: Note the object identifier values returned by calling the built-in `id()` function in the
   accompany `print()` output. The id change demonstrates that the `title` variable has
   been reassigned to a new string object.

### 7.6 Challenge 07

__Task__. Employ the appropriate string method that returns a count of the number of times a
specified character occurs in the string object.

In 2020 the historian Ibram X. Kendi published _Stamped: Racism, Antiracism, and You_, a young adult
"remix" of his monograph
_Stamped from the Beginning: The Definitive History of Racist Ideas in America_ (2016). The book
quickly emerged as one of the most challenged books of 2020, ranking second on the ALA's annual
list.

1. Select
   the appropriate `str` method introduced above that returns an integer value representing the
   number of times the character `i` occurs in the string `stamped`.

2. Assign the return value to the variable named `i_count`.

3. Uncomment the accompanying `print()` expression, run your code, and review its output.

## 8.0 String formatting: formatted string literal

The lectures, lab exercises, and problem sets will often include a number of pre-positioned
`print()` functions (an expression) in which a _formatted string literal_ (a.k.a f-string) is
passed in as an argument.

The f-string syntax `f"some_string {some_variable}"` is less verbose and easier to construct than
earlier string formatting approaches. You will learn how to write f-strings as well as format
strings using the older approaches in the very near future.

```python
author = "Toni Morrison"

print(f"\n8.0 author = {author}") # note use of curly braces
```

:bulb: Inclusion of the leading newline escape sequence (`\n`) in the f-string is for terminal
output display purposes only. It is not required but provides a line break between the preceding
output and the output that follows.

### 8.1 Challenge 08

__Task__. Pass a formatted string literal (f-string) to the built-in `print()` function.

Nobel Prize winner Toni Morrison's first novel _The Bluest Eye_ (1970) has appeared on the ALA's
[Top 10 Most Challenged Books list](https://www.ala.org/advocacy/bbooks/frequentlychallengedbooks/top10)
five times since 2006.

```python
bluest_eye = "Toni Morrison, The Bluest Eye (Holt, Rinehart and Winston, 1970)."
```

1. Call the built-in `print()` function and pass it an f-string that produces the following
   terminal output:

   ```commandline
   < newline >
   9.0 bluest_eye length = 65
   ```

2. Format the f-string as follows:

   ```python
   f"< newline >9.0 bluest_eye length = < expression >"
   ```

   __Requirements__

   1. The f-string _must_ commence with a newline escape sequence.

   2. The f-string _must_ include a call to the built-in function `len()` (the `< expression >`).
      Pass `bluest_eye` to `len()` as the argument.

      :bulb: The return value of `len()` (an integer) is the length of `bluest_eye`, which
      corresponds to the number of characters (including spaces) in the string.

3. Call the built-in function `print()` and pass the f-string expression to it as the argument.

   :exclamation: Do not assign the f-string to a variable. Pass it directly to `print()`. In other
   words, construct the f-string inside the function's parentheses (`(...)`).

4. Run your code. Compare your output with the expected output.
