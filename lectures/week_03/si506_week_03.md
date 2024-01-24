# SI 506 Week 03

## Topics

1. Sequences: strings, lists, and tuples
   1. `str` basics
   2. `list` basics
   3. `tuple` basics
2. Creating a list from a string
   1. `str.split()`
   2. `str.splitlines()`
   3. Challenge 01 (the `assert` statement)
3. Indexing
   1. Accessing a character by position
   2. Accessing a list element by position
   3. Mutating a list element using indexing
   4. Challenge 02
4. Slicing
   1. Slicing start/end range
   2. Challenge 03
   3. Challenge 04
   4. Working with stride values
   5. Challenge 05
   6. Challenge 06
5. Other slicing operations
   1. Slice assignment
   2. `del` statement and slicing
   3. Built-in `slice()` function
6. Object methods and method chaining
   1. Select `str` methods
      1. `str.strip()`
      2. `str.find()`
      3. `str.index()`
      4. `str.join()`
   2. Challenge 07
   3. Select `list` methods
      1. `list.append()`
      2. `list.remove()`
      3. `list.extend()`
      4. `list.index()`
      5. `list.insert()`
      6. `list.sort()`
   4. Challenge 08
   5. Challenge 09
7. String formatting

## Reference

Bookmark the following
[w3schools](https://www.w3schools.com/python/default.asp) Python pages and/or have them open in a
set of browser tabs both during class and while working on this week's problem set:

* ["Python Built-in Functions"](https://www.w3schools.com/python/python_ref_functions.asp)
* ["Python Operators"](https://www.w3schools.com/python/python_operators.asp)
* ["Python List Methods"](https://www.w3schools.com/python/python_ref_list.asp)
* ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)
* ["Python Tuple Methods"](https://www.w3schools.com/python/python_ref_tuple.asp).

## Lecture data

It is quite natural to assume that the Python programming language is named after the family of
snakes known as _Pythonidae_ or python. But you would be wrong.
[Guido van Rossum](https://gvanrossum.github.io/), the creator of the Python programming language
named it after the absurdist English comedy sketch series
[_Monty Python's Flying Circus_](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)
(1969-1974) which starred the "Pythons" Graham Chapman, John Cleese, Eric Idle, Terry Jones,
Michael Palin and the animator Terry Gilliam.

This week's lecture features data derived from various Monty Python comedy sketches including the
Pythons' famous ["Spam" sketch](https://en.wikipedia.org/wiki/Spam_(Monty_Python)) (1970) including
the Spam dominated cafe
[menu](https://en.wikipedia.org/wiki/Spam_(Monty_Python)#/media/File:Monty_Python_Live_02-07-14_13_04_42_(14598710791).jpg).

During the Second World War and after Britain imposed rationing restrictions and, starting in 1941,
imported massive quantities of canned spam from the United States as a protein substitute for
imports of beef, pork, and poultry. The public, including my parents, grew to loathe it--which the
sketch plays upon in surrealist fashion.

:bulb: Have you ever wondered why unwanted email is referred to as "spam". Watch the
["Spam" sketch](https://vimeo.com/329001211) and you'll quickly understand why.

## 1.0 Sequences: strings, lists, and tuples

This week we discuss Python sequences, focusing on three sequence types: strings (type = `str`),
lists (type = `list`), and tuples (type = `tuple`).

### 1.1 `str` basics

A string (type: `str`) is an _ordered_ sequence of characters. Once created, the string is considered
_immutable_ and cannot be modified. The string is also an _iterable_, a type of object whose members
(in this case, characters), can be accessed.

String objects (an instance of the `str` class) are provisioned with _methods_ that permit
operations to be performed on the string. These behaviors are discussed in greater detail during
the next lecture.

```python
# A string
comedy_series = 'Monty Python'

# The object's unique identifier in memory
comedy_series_id = id(comedy_series)

# Return the object's type
comedy_series_type = type(comedy_series)

# Return the object's length
comedy_series_len = len(comedy_series)
```

You can confirm that a string is immutable by attempting to change one of its characters:

```python
# UNCOMMENT: Immutability check
# comedy_series[0] = 'm' # TypeError: 'str' object does not support item assignment
```

As you saw last week you can use the plus (`+`) operator to build a string. This is known as
string _concatenation_.

In the example below the variable `comedy_series` is (re)assigned to a new string object comprising
the value of `comedy_series` plus the hard-coded string `"'s Flying Circus"`. The output of `print()`
demonstrates that the new concatenated string is assigned a new identity that remains unchanged for
the life of the object.

```python
# String concatenation
comedy_series = comedy_series + "'s Flying Circus" # string concatenation (new object)
```

### 1.2 `list` basics

A list (type: `list`) represents an _ordered_ sequence of elements (e.g., strings, lists, and/or
other object types). The list is also an _iterable_, a type of object whose members (in this case,
elements), can be accessed. Unlike a string a Python list is mutable and capable of modification.
Elements can be added or removed from a list and, if the element is mutable, (e.g., a nested list)
can be modified. List elements are accessed by position using a zero-based index value.

List objects are also provisioned with methods that permit operations to be performed on the
list. These behaviors are discussed in greater detail in a later section.

```python
# A list
pythons = [
    'Graham Chapman',
    'John Cleese',
    'Terry Jones',
    'Eric Idle',
    'Michael Palin'
    ]

# The object's unique identifier in memory
pythons_id = id(pythons)

# Return the type
pythons_type = type(pythons)

# Return the length
pythons_len = len(pythons)
```

Unlike a string a list can be _mutated_ (i.e., modified) by adding, updating, substituting, and/or
removing elements. In the example below Terry Gilliam, the American animator (and later director),
was also a Python so let's add him to the list `pythons`. We can utilize a number of list methods
to accomplish the task. Each method call mutates the list _in-place_, returning `None` implicitly
to the caller. We will discuss list methods in greater detail at our next meeting.

```python
# In-place method call mutates the list
pythons.append('Terry Gilliam')
# pythons.insert(-1, 'Terry Gilliam')
# pythons.extend(['Terry Gilliam'])
```

You can also create a _new_ list by _concatenating_ two or more lists using the plus (`+`)
operator. In the example below a single element list containing the string 'Neil Innes' (considered
by many to be the seventh Python) is joined to the `pythons` list. This results in a new list which
is assigned to the existing variable `pythons`.

```python
# List concatenation
pythons = pythons + ['Neil Innes']
```

### 1.3 `tuple` basics

A Python tuple (type: `tuple`) is an _ordered_ sequence of items. Once created, the tuple is
considered _immutable_ and cannot be modified. The tuple is also an _iterable_, a type of object
whose members (in this case, items), can be accessed. Tuples provide an optimized data structure
for referencing groups of values that form "natural" associations that do not change over the life
of a program or script (e.g., 'Ann Arbor', 'Michigan', 'USA').

Tuples are typically defined by enclosing the items in parentheses `()` instead of square brackets
`[]` as is the case with lists.

```python
# A tuple
silly_walks = ('Monty Python', 'Sketch', 'The Ministry of Silly Walks', '15 September 1970')
```

A single item tuple __must__ include a trailing comma (`,`) or the Python interpreter
will consider the expression a string.

```python
python_theme_song = ('The Liberty Bell',) # Note trailing comma
```

:bulb: You can also create a _new_ list by _concatenating_ two or more tuples using the plus (`+`)
operator. In the example below the `python_theme_song` tuple is joined with two other tuples to form
a new tuple that names the unwitting composer of the Python's _Flying Circus_ theme song along with
its original publication date.

```python
python_theme_song = ('John Philip Sousa', 'Composer') + python_theme_song + (1893,) # Concatenation
```

:exclamation: Unlike a string a tuple can reference _mutable_ items like lists and dictionaries that
are capable of modification despite their inclusion in the tuple as is illustrated below:

```python
holy_grail = (
    'Monty Python and the Holy Grail',
    1975,
    [
        'Arthur, King of the Britons',
        'Sir Lancelot the Brave',
        'Sir Bedevere the Wise',
        'Sir Galahad the Pure'
        ]
    )
# holy_grail[1] = '3 April 1975' # Illegal
holy_grail[2].append('Patsy') # Mutates tuple list item with a new element
```

In a later lecture we will discuss how to compare two or more tuples using comparison operators
('=', '<', '>') in a conditional statement.

## 2.0 Creating a list from a string

String objects are provisioned with two methods that return a version of the
string converted to a list: `str.split()` and `str.splitlines()`.

### 2.1 `str.split()`

The `str.split()` method will return a list of string elements split on a
separator or delineator. Default behavior is to split the string whenever a
space is encountered.

The `str.split()` method defines two parameters:

* sep: the separator (or _delineator_) used to split the string (default = `' '`)
* max_splits: the maximum number of splits from left to right (default = `-1` (i.e., no limit))

```python
sketch_comedy = "Monty Python's Flying Circus"
words = sketch_comedy.split() # Returns ['Monty', "Python's", 'Flying', 'Circus']
```

Passing a separator value to `str.split()` will return a list of string elements split at the
specified separator:

```python
sketches = 'Dead Parrot Sketch, The Spanish Inquisition, The Argument Clinic'
sketches = sketches.split(', ') # Returns ['Dead Parrot Sketch', 'The Spanish Inquisition', 'The Argument Clinic']
```

### 2.2 `str.splitlines()`

The `str.splitlines()` method will return a list of string elements split on a line
boundary or break.

The `str.splitlines()` method defines a single parameter:

* keepends: each string element retains the trailing line break (`\n`) if `True` is specified

```python
excerpt = """Nobody expects the Spanish Inquisition.
Our chief weapon is surprise.
Surprise and fear. Fear and surprise.
Our two weapons are fear and surprise ...
and ruthless efficieny.
Our three weapons are fear and surprise and ruthless efficiency ...
and an almost fanatical devotion to the pope.
Uh! Four. No.
Amongst our weapons ....
Amongst our weaponry are such elements as fear, su -- I'll come in again.
"""

lines = excerpt.splitlines() # Returns list of string elements split on each line break
```

### 2.3 Challenge 01

__Task__: Combine two strings and then split the string and return a list of sentence elements.

:bulb: A string can span multiple lines by employing a trailing backslash (`\`) after each
line or by surrounding the multiple lines by a parentheses (`()`).

Below is a short excerpt from a longer exchange between Arthur, King of the Britons, and a peasant
named Dennis that occurs early on in the 1975 film `Monty Python and the Holy Grail`.

```python
arthur = (
    "The Lady of the Lake, "
    "her arm clad in the purest shimmering samite, "
    "held aloft Excalibur from the bosom of the water "
    "signifying by Divine Providence that "
    "I, Arthur, was to carry Excalibur. "
    "That is why I am your king."
)

dennis = (
    "Listen, strange women lying in ponds distributing swords "
    "is no basis for a system of government. "
    "Supreme executive power derives from a mandate from the masses, "
    "not from some farcical aquatic ceremony."
)
```

1. Combine the `arthur` and `dennis` strings. Assign the new string to a variable named `excalibur`.

   :exclamation: You _must_ maintain proper spacing when joining the strings (i.e., one space
   between sentences).

2. Split the string into a list of __sentence__ elements and assign the new list to a variable named
   `excalibur`.

3. Uncomment both the `print()` call and the `assert` statement and run your code.

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

## 3.0 Indexing

You can access individual members of a sequence by their position or index value. Python's index
notation is __zero-based__. Individual characters in a string or individual elements in a list can
be accessed using the subscript operator (`[]`) and an index value.

:bulb: _slice notation_ employs two brackets `[< index | slice >]`
enclosing either a positive or negative index value (eg., `some_sequence[0]`) or a slicing
expression `some_sequence[:5]`.

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |
|   0    |   1    |   2    |   3    |   4    |   5    |   6    |   7    |   8    |   9    |   10   |   11   |
|   M    |   o    |   n    |   t    |   y    | &nbsp; |   P    |   y    |   t   |    h    |    o   |    n   |
|   -12  |   -11  |  -10   |   -9   |   -8   |   -7   |   -6   |   -5   |    -4  |   -3   |   -2   |   -1   |

### 3.1 Accessing a character by position

```python
name = 'Monty Python'
letter = name[0] # first letter (zero-based index)

letter = name[4]

letter = name[-1]
```

:bulb: `name[0]` is considered an expression since it resolves to a value (e.g., "M").

### 3.2 Accessing a list element by position

In the example below, the second item in the Bromley cafe menu (`'Egg, sausage and bacon'`) is
accessed using a positive index value while the second to the last item in the menu
(`'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam'`) is accessed using
a negative index value.

```python
menu = [
    'Egg and bacon',
    'Egg, sausage and bacon',
    'Egg and Spam',
    'Egg, bacon and Spam',
    'Egg, bacon, sausage and Spam',
    'Spam, bacon, sausage and Spam',
    'Spam, egg, Spam, Spam, bacon and Spam',
    'Spam, Spam, Spam, egg and Spam',
    'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam',
    'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam'
    ]

menu_item = menu[1] # second element (zero-based index)

menu_item = menu[-2]
```

### 3.3 Mutating a list element using indexing

You can assign a new value to a list element by referencing its index position.

```python
menu[3] = 'Scrambled eggs, bacon and Spam'
```

:exclamation: If an index value references a non-existent position in a sequence an `IndexError`
will be raised.

```python
# UNCOMMENT
# menu_item = menu[10] # IndexError: list index out of range
```

### 3.4 Challenge 02

__Task__: Return the first `menu` item that includes more than one helping of Spam.

1. Employ indexing to return the first `menu` item that includes multiple helpings of Spam. Assign 
   the slice to a variable named `order`.

2. Uncomment both the `print()` call and the `assert` statement and run your code.

## 4.0 Slicing

You can access a `list` element, `tuple` item, or `str` character by position using an index
operator. You can also access a subset or _slice_ of elements, items, or characters using Python's
slicing notation.

A slicing operation starts at index position zero (`0`) and returns all members of a sequence up
to but excluding the member located at the specified `end` position. An optional `start` position
can be specified in order to start the slice at an index other than zero (`0`). Negative values
can be employed to commence the slice from the end as opposed to the beginning of the sequence.

An optional `stride` number can also be specified in order to skip members or reverse the slice.
A positive `stride` value will return every *n*th member in the slice range;
inclusion of a negative `stride` value will return every *n*th member in the slice range in
_reverse_ order. The default `stride` value equals `1`.

```python
some_sequence[< start (optional) >: < end >: < stride (optional) >]
```

The slicing syntax simplifies referencing and/or extracting a subset of a given sequence.
List slicing can result in list traversal performance gains since slicing obviates the need to loop
over an entire list in order to operate on a targeted subset of elements. We will explore
this aspect of slicing when we explore list iteration in more detail starting next week.

```python
cast = [
    'Terry Jones, Waitress',
    'Eric Idle, Mr Bun',
    'Graham Chapman, Mrs Bun',
    'John Cleese, The Hungarian',
    'Michael Palin, Historian',
    'Extra, Viking 01',
    'Extra, Viking 02',
    'Extra, Viking 03',
    'Extra, Viking 04',
    'Extra, Viking 05',
    'Extra, Viking 06',
    'Extra, Police Constable'
]
```

### 4.1 Slicing start/end range

:bulb: In the slicing example below the start value `1` is considered _inclusive_ while the end
value `3` is considered _exclusive_ (i.e., the element is excluded from the slice).

```python
# Return Mr and Mrs Bun.
cast_members = cast[1:3] # Returns ['Eric Idle, Mr Bun', 'Graham Chapman, Mrs Bun']
```

Negative slicing can also be employed to return the Mr and Mrs Bun:

```python
# Return Mr and Mrs Bun.
cast_members = cast[-11:-9]
```

If you were asked to return a `cast` slice containing _only_ the named cast members the following
slicing expression would get the job done:

```python
# Return named cast members.
named_cast_members = cast[:5] # or cast[0:5]
```

On the other hand, if you were asked to return a `cast` slice containing _only_ the unnamed cast
members (the extras) consider employing negative slicing:

```python
# Return cast extras (i.e., Vikings 01-06, Police Constable) using negative slicing.
cast_members = cast[-7:] # warn: not the same as cast[-7:-1]
```

### 4.2 Challenge 03

__Task__: Retrieve a subset of the `cast` list using positive slicing.

1. Employ slicing to access the elements in `cast` that represent John Cleese and Michael Palin
   using _postive_ index values. Assign the return value (a new list) to the variable
   `cleese_palin`.

2. Uncomment both the `print()` call and the `assert` statement and run your code.

### 4.3 Challenge 04

__Task__: Retrieve a subset of the `cast` list using negative slicing.

1. Employ slicing to access the Viking elements in `cast` using _negative_ index values. Assign the
   return value (a new list) to the variable `vikings`.

2. Uncomment both the `print()` call and the `assert` statement and run your code.

### 4.4 Working with stride values

An optional `stride` value can be specified to _increase_ the number of slicing steps in order to
_skip_ one or more elements, items, or characters in a sequence. Providing a negative stride value
_reverses_ the operation.

Utilize the Spam sketch `cast` list to practice slicing with `stride` values.

```python
cast = [
    'Terry Jones, Waitress',
    'Eric Idle, Mr Bun',
    'Graham Chapman, Mrs Bun',
    'John Cleese, The Hungarian',
    'Michael Palin, Historian',
    'Extra, Viking 01',
    'Extra, Viking 02',
    'Extra, Viking 03',
    'Extra, Viking 04',
    'Extra, Viking 05',
    'Extra, Viking 06',
    'Extra, Police Constable'
]
```

For example, the optional stride value can be employed to access _Spam_ sketch `cast` members who
are now deceased:

* Terry Jones (1942-2020)
* Graham Chapman (1941-1989)

```python
cast_members = cast[:3:2]
```

You can employ a _negative_ stride value to return a version of the list with the order of the
elements _reversed_:

```python
cast_members = cast[::-1]
```

You can also employ a stride value to return a version of the list containing _every other_ element:

```python
cast_members = cast[::2]
```

### 4.5 Challenge 05

__Task__: Return every other cast member in reverse order.

1. Employing slicing with a `stride` value to return _every other_ cast member of the `cast` list in
   reverse order.

2. Assign the new list to the variable `cast_members`.

3. Uncomment the `print()` call, the `pprint()` call, and the `assert` statement and run your code.

### 4.6 Challenge 06

__Task__: Return every other Viking.

1. Employing slicing with a `stride` value to return _every other_ Viking cast member of the `cast`
   list.

2. Assign the new list to the variable `cast_members`.

3. Uncomment the `print()` call, the `pprint()` call, and the `assert` statement and run your code.

## 5.0 Other slicing operations

### 5.1 Slice assignment

Recall that you can assign a new value to a list element by referencing its index position.

```python
cast[4] = 'Michael Palin, The Historian' # Adds the definite article "The"
```

You can also replace a subset of a list with another list or subset of a list using slice
assignment.

```python
mounties = [
    'Extra, Canadian Mountie 01',
    'Extra, Canadian Mountie 02',
    'Extra, Canadian Mountie 03',
    'Extra, Canadian Mountie 04',
    'Extra, Canadian Mountie 05',
    'Extra, Canadian Mountie 06'
]
```

```python
# Replace part of a list (length unchanged).
cast[5:11] = mounties[0:] # replace Vikings with Mounties
```

```python
# Replace part of a list (length changes).
cast[5:11] = mounties[1:5] # replace Vikings with Mounties 02-04
```

### 5.2 `del` statement and slicing

You can employ slicing and the `del` statement to remove subsets of a sequence.

```python
# Delete the Mounties (retain the Police Constable)
del cast[-5:-1]
# del cast[5:9] # alternative
```

### 5.3 Built-in `slice()` function

You can also use the built-in `slice()` function to return a slice object and apply it to a
sequence. `slice()` accepts three arguments: an optional integer `start` value
(default = 0), a required integer `end` value that specifies the position in which to end the
slicing operation, and an optional `step` or stride value that specifies the slicing step
(default = 1).

```python
# slice([start, ]end[, step]) object
s = slice(1, 4, 2)
cast_members = cast[s] # Returns Idle and Cleese
```

## 6.0 Object methods and method chaining

When you create a string, list, or tuple you create an object that is based on a `class`, a type
that can both hold data and perform actions. Think of a `class` as a template, blueprint, or model
for creating objects. Each string or list that you create and assign to a variable represents an
_instance_ of the class upon which it is based (i.e., the class types `str`, `list`, and `tuple`).
Such objects possess individual characteristics (data) and common behaviors (methods).

Object methods, if defined, are _called_ using dot (`.`) notation. If a method "signature" includes
one or more _parameters_, these can be passed to the method as comma-separated _arguments_ that are
included inside the method name's parentheses.

:exclamation: If a method definition does not specify an _explicit_ return value, `None` (type:
`NoneType`) will be returned implicitly to the caller.

```python
menu_item = 'Spam, egg, Spam, Spam, bacon and Spam'

# str.lower() -- no argument method
menu_item_lower = menu_item.lower()

# str.count(value, start=0, end=len(str) - 1) -- start and end are optional
spam_count = menu_item.count('Spam')

# str.split(sep=' ', maxsplit=-1) -- sep and maxsplit are optional
items = menu_item.split(', ') # returns list

# list.remove(element) -- in-place operation; removes 1st occurence; returns None
items.remove('egg')

# WARN: Do not do this: items variable no longer points to a list object
items = items.remove('bacon and Spam') # None is returned
```

Method calls can also be "chained". Each method call returns a value (object) to which the next
method call is bound. Order matters. Note that calling a method not defined for an object will raise
an `AttributeError`.

```python
menu_item = 'Egg, bacon, sausage and Spam'

# Good. Replace, convert to lower case, and split.
items = menu_item.replace(' and', ',').lower().split(', ')

# Bad. The trailing list.append() returns None (oops!)
items = menu_item.replace(' and', ',').lower().split(', ').append('pancakes')

# Ugly. Premature split. Calling lower on a list object raises a runtime error
# AttributeError: 'list' object has no attribute 'lower'
items = menu_item.replace(' and', ',').split(', ').lower()
```

### 6.1 Select `str` methods

String objects (type `str`) include "built-in" behaviors that are defined as _methods_. Calling a
string method may require that one or more arguments (values) be passed to it in
order to perform the requested computation. Depending on the method definition, the operation may
result in a computed value being returned to the caller; otherwise `None` is returned (implicitly).

Earlier discussions introduced the following string methods:

* `str.count()`
* `str.lower()`/`str.upper()`
* `str.replace()`
* `str.split()`/`str.splitlines()`
* `str.startswith()`/`str.endswith()`

Below is another group of string methods that you should get to know.

### 6.1.1 `str.strip()`

Returns a "trimmed" version of the string, removing leading and trailing spaces as well as newline
escape sequences (`\n`).

```python
monty_python = " Monty Python's Flying Circus \n"
monty_python = monty_python.strip()
```

:bulb: To remove spaces from either the beginning or the end of the string use `str.lstrip()`
or `str.rstrip()`.

### 6.1.2 `str.find()`

Finds the _first_ occurence of the specified value and returns its index value. If the value is not
located -1 is returned.

```python
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('Spam')

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('ham')
```

:bulb: `str.rfind()` attempts to locate the _last_ occurence of the specified value. If the value
is not located -1 is returned.

### 6.1.3 `str.index()`

Finds the _first_ occurence of the specified value and returns its index value. If the value is not
located a `IndexError` is raised.

```python
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.index('egg and Spam')

# TODO UNCOMMENT and raise runtime exception
# position = menu_item.index('ham') # IndexError
```

### 6.1.4 `str.join()`

Returns a new string by joining each element in the passed in _iterable_ to the specified string.

```python
items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ' '.join(items) # build a string by joining each element to an empty string

menu_item = ', '.join(items) # build a string by joining each element to a comma
```

### 6.2 Challenge 07

__Task__: The Python's cafe in Bromley is under new management. Revise the cafe `menu` employing
various string methods.

:bulb: Break the problem into subproblems solving each subproblem in turn by calling a `str` method.
Uncomment the `print()` function and run your file after every change, printing `menu_v2` to the
terminal screen in order to check your work.

1. Implement the following changes to the multiline string named `menu`. Use __method chaining__ to
   accomplish the task.

   :exclamation: The requirements are __unordered__ and may not represent the correct order of
   operations to perform.

   * Replace every instance of the substring `sausage` with the string `toast`.

   * Substitute every __third (3rd) helping__ of `Spam` listed in a menu item
     with the value assigned to the variable `healthy_choice`.

     Example substring substitution:

     `'Spam, Spam, Spam, egg and Spam' -> 'Spam, Spam, Oatmeal, egg and Spam'`

   * Split the multiline string into a list and assign the new menu to the variable named `menu_v2`.

   * Convert the menu to lower case.

2. Uncomment the `print()` call, the `pprint()` call, and the `assert` statement and run your code.

### 6.3 Select `list` methods

As with strings, List objects (type: `list`) also include "built-in" behaviors that are defined as
_methods_. Calling a `list` method may require that one or more arguments (values) be passed to
it in order to perform the requested computation. Depending on the method definition, the operation
may result in a computed value being returned to the caller; otherwise `None` is returned.

Below is a select list of `list` methods.

### 6.3.1 `list.append()`

Appends element to the end of a list. The operation mutates the list _in-place_, returning `None`
implicitly to the caller.

```python
menu_v2.append('red beans and rice') # modify in-place (no variable assignment)
```

:exclamation: Do not assign the return value of `list.append(< element >)` to the current list
variable. Doing so will assign `None` to the variable.

### 6.3.2 `list.remove()`

Remove element from list. The operation mutates the list _in-place_, returning `None`
implicitly to the caller.

```python
item = menu_v2[-2] # Lobster Thermidor
menu_v2.remove(item)
```

### 6.3.3 `list.extend()`

Extend list with another list. The operation mutates the list _in-place_, returning `None`
implicitly to the caller.

```python
healthy_items = ['cereal, yogurt, and spam', 'oatmeal, fruit plate, and spam']
menu_v2.extend(healthy_items)
```

### 6.3.4 `list.index()`

Return index position by value.

```python
index = menu_v2.index('egg, bacon, and spam')
```

### 6.3.5 `list.insert()`

Insert element at specified index position. The operation mutates the list _in-place_, returning
`None` implicitly to the caller.

```python
menu_v2.insert(1, 'belgian waffle, strawberries, and spam')
```

### 6.3.6 `list.sort()`

Sort the list. The operation mutates the list _in-place_, returning `None` implicitly to the caller.

:bulb: You can pass the optional arguments `reverse=True|False` (pipe = 'or') as well as
`key=some_function` in order to further specify the sorting criteria (out of scope for the moment).

```python
menu_v2.sort() # default alpha sort
```

### 6.4 Challenge 08

__Task__: Create yet another version of the Bromley cafe menu.

1. Use slicing to create a new list by reversing the order of `menu_v2`. Assign the new list to a
   variable named `menu_v3`. Uncomment `print()` and check your work.

   :exclamation: the list method `list.reverse()` reverses the order of a list's elements
   "in-place"; in other words it mutates an _existing_ list rather than returning a new list to the
   caller.

2. Use the appropriate list method to eliminate the `menu_v3` item 'egg and spam'. Uncomment
   `print()` and check your work.

3. Use the appropriate list method to add 'blueberry pancakes' to `menu_v3` in the sixth (6th)
   position.

4. Uncomment the `print()` call, the `pprint()` call, and the `assert` statement and run your code.

### 6.5 Challenge 09

__Task__: Return a slice of the new Bromley cafe menu.

1. Use the appropriate list method to return the index value of the menu item
   __"egg, toast and bacon"__. Assign the return value to a variable named `idx`. Uncomment
   `print()` and check your work.

2. Use the appropriate built-in function to return the length of `menu_v3`. Assign the return value
   to a variable named `length`.

3. Uncomment `print()` and check your work.

4. Utilize the `idx` and the `length` values in a slicing expression that returns a subset of
   `menu_v3` that contains _only_ those menu items that list "egg" _first_. Assign the new list to
   the variable named `egg_first_dishes`. Uncomment `print()` and check your work.

   :bulb: You can calculate a slice's `start`, `end`, and/or `stride` value by embedding an
   arithmetic expression inside the slice notation's subscript operator `[]`.

   ```python
   menu_v3[< start >:< end arithmetic >]
   ```

   The new list that you must produce:

   ```python
   egg_first_dishes = [
     'egg, toast and bacon',
     'egg, bacon, toast and spam',
     'egg, bacon and spam',
     'egg and bacon'
     ]
   ```

5. Uncomment the `print()` call, the `pprint()` call, and the `assert` statement and run your code.

## 7.0 String formatting

There are three ways to format one or more values as a string. We recommend that you utilize the
newest approach: the _formatted string literal_ (f-string). That said, you will encounter the other
string formatting routines when reading older code or tutorials so its important to understand how
to implement the other approaches.

### 7.1 Formatted string literal (f-string)

The f-string syntax `f"some_string {some variable}"` is less verbose and easier to construct than
earlier string formatting approaches. Employ curly braces to denote embedded variables in the
expression.

```python
special_item = 'egg, bacon, spam and sausage'
question = f"Why can't she have {special_item}?" # embedded variable
```

:bulb: Recall that `\n` represents an escape sequence, specifically an ASCII linefeed (LF). Think of
`\n` as "new line". Passing `\n` in a string will insert a new line at the position of the escape
sequence.

### 7.2 `str.format()`

Formats the specified value(s) and inserts them inside the string's using curly braces `{}` as a
placeholder.

```python
question = "Could I have {}, {}, {} and {}, without the spam?".format('egg', 'bacon', 'spam', 'sausage')
```

:bulb: The placeholders can be identified using empty placeholders `{}`, numbered indexes `{0}`, or
named indexes `{egg}`.

### 7.3 C-style or simple positional formatting

The oldest of the three string formatting approaches. Uses the `%` character as a placeholder.

Placeholders (select list):

* `%c` = single character placeholder
* `%d` = decimal placeholder
* `%i` = integer placeholder
* `%s` = string placeholder

```python
question = "No, it wouldn't be %s, %s, %s and %s, would it?" % (egg, bacon, spam, sausage)
```

For a summary of ye olde C-style / simple positional formatting see Frank Hofman,
["Python String Interpolation with the Percent (%) Operator"](https://stackabuse.com/python-string-interpolation-with-the-percent-operator/) (Stack Abuse, nd).
