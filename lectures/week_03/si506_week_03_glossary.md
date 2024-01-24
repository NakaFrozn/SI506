# SI 506 Week 03

## Python 3.x Glossary

## 1.0 Basic syntax and semantics

* __comment__. Explanatory text embedded in code with no impact on the runtime
  characteristics of the program or script. Single line comments are delinated by prefacing
  the line with a hash (`#`) character.

* __expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_sequence >)` is considered an expression.

* __immutable__. A characteristic of certain object types that renders them incapable of change.
  Strings and tuples are examples of an immutable type.

* __index__. Numeric position of an element or item contained in an ordered sequence. Python
  indexes are zero-based, i.e., the first element's positive index value is `0` not `1`.

* __iterable__. An object capable of returning its members one at a time. Strings, lists, tuples,
  and dictionaries are examples of an iterable.

* __mutable__. A characteristic of certain object types that render them modifiable. Lists and
  dictionaries are examples of a mutable type.

* __object__. A data [abstraction](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
  that possesses, at a minimum, an identity, type, and value. An object's attributes may also include
  defined behaviors (known as _methods_) that can be accessed by a user.

* __operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).

* __sequence__. An [iterable](https://docs.python.org/3/glossary.html#term-iterable) such as a
  `str`, `list`, `tuple`, or `dict` whose members (e.g., characters, elements, items) can be
  accessed individually or in groups by employing integer indices in the case of sequences or keys
  in the case of dictionaries.

* __statement__. An instruction that the Python interpreter can execute. For example, assigning a
  variable to a value such as `name = "arwhyte"` is considered a statement. A statement can be
  composed of one or more expressions (the reverse is not true).

* __subscript operator__. Square brackets (`[]`) appended to a sequence that enclose either an
  index value or a slicing expression. The resulting expression is used to access individual or
  groups of characters, elements, or items.

* __variable__. A name, label or pointer that refers to an object in memory.

* __value__. Data attached to an object. Data can range from a "primitive" type such as a
  number or boolean to more complex data types such as sequences, maps, date, and time, or even a
  the absence of a value as represented by `None`.

## 2.0 Data types

A data type (or type) is a data structure that contains a value or values. Each data type also
possess attributes that determine the operations that can be performed on it.

* __boolean__. A [truth value](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
  type ([`bool`](https://docs.python.org/3/library/functions.html#bool)) or expression that
  evaluates to `True` or `False`.

* __dictionary__. A _mutable_ [mapping](https://docs.python.org/3/glossary.html#term-mapping) type
  ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict)) wherein each referenced value is
  associated with or mapped to a defined key that is used to access the value. A dictionary is
  delineated by the use of curly braces (`{}`) and each `key: value` pair is separated by a comma
  (`,`) as in `{"institution": "University of Michigan", "fight_song": "The Victors"}`.

* __float__. A numeric type ([`float`](https://docs.python.org/3/library/functions.html#float))
  that references a floating point number.

* __integer__. A numeric type ([`int`](https://docs.python.org/3/library/functions.html#int))
  that references a whole number.

* __list__. A _mutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`list`](https://docs.python.org/3/library/stdtypes.html#list)) of object references
  (i.e., elements) that can be _mutated_ after creation. A list is delineated by the use of square
  braces (`[]`) as in `["arwhyte", "csev", "cteplovs"]`. List elements can be accessed either
  individually or in groups by employing integer indices.

* __string__. An _immutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`str`](https://docs.python.org/3/library/stdtypes.html#str)) of character references. Strings
  are delineated by the use of double (`""`) or single quotes (`''`) as in `"SI 506"`. Individual
  characters can be accessed either individually or in groups employing integer indices.

  :bulb: Note that the [Black](https://github.com/psf/black) code formatter
  [favors double quotes over single quotes](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#strings)
  as do SI 506 auto graders.

* __tuple__. A _immutable_ [sequence](https://docs.python.org/3/glossary.html#term-sequence) type
  ([`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)) of item references. Tuples are
  delineated by the use of parentheses (`()`) as in `("Ann Arbor", "MI")`. Tuple items can be
  accessed individually or in groups employing integer indices. Single item tuples _must_ include a
  trailing comma (`,`) as in `("Go Blue",)` or the expression will be treated as a string.

### 3.0 Functions

A defined block of statements that together perform a computation. Functions only execute
when they are explicitly called. A function can be defined with one or more _parameters_ that allow
it to accept _arguments_ from a caller in order to perform a computation. A function can also be
designed to return a computed value; otherwise it return `None` implictily. Python provides both
_built-in_ functions and the ability to create _user-defined_ functions. Functions are considered
"first-class" objects in the Python ecosystem.

* __built-in function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use in your code. The `print()` function is an
  example of a built-in function.

* __argument__. A value passed to a function or method.

* __caller__. The act of invoking or calling a function via an expression or statement.

* __method__. A function defined by and _bound to_ a particular object. Dot notation (`.`) is
  employed to call an object method. For example the `str` type is provisioned with a number of
  methods including `str.lower()`, `str.split()`, and `str.strip()`.

* __parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method can accept from a caller.

### 4.0 Operations

* __concatenation__. Joining one object value to another in order to create a new object. Combining
  two strings together (e.g., `greeting = "Hello " + "SI 506"`) to create a new string is an example
  of string concatenation.

* __formatted string literal (f-string)__. An [f-string](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)
  provides an economical syntax for constructing a string literal based on some combination of
  alphanumeric characters, object references (i.e., variables), spaces, and escape sequences. A
  formatted string literal is prefixed with `f` or `F` as in `f"email = {uniqname}@umich.edu"`.

* __slicing__. Accessing a subset of a sequence. A slice is created using the slice operator `[]`
  to define a stop index value, and optionally start and/or step indices, as in
  `some_sequence[1:10:2]` or by calling the built-in function
  [`slice()`](https://docs.python.org/3/library/functions.html#slice).

* __variable assignment__. Assigning a variable to an object (e.g. `uniqname = "arwhyte"`).
  A variable is nothing more than a name, label, or pointer to an object containing a value. It can
  be reassigned to another object at any time.
