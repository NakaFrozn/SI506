# SI 506: Functions

## Topics

1. The `main()` function
   1. Execution modes
   2. Why `main()`?
2. Function basics
   1. Defining and calling a function
   2. Specifying a return value
   3. Multiple parameters
   4. Positional arguments (order matters)
   5. Challenge 01
3. Keyword arguments and optional parameters
   1. Keyword arguments
   2. Optional parameters
   3. Skipping optional parameters
   4. Challenge 02
4. Passing a function call as an argument
5. Variable scope
6. Functions can call other functions
   1. Challenge 03
7. Truth value testing
8. Iterable packing and unpacking
   1. Triggering `ValueError` runtime exceptions
   2. Unpacking in a `for` loop
9. Additional Challenges
   1. Challenge 04
   2. Challenge 05
   3. Challenge 06

## 1.0 The main() function

The Python interpreter executes a program or script line by line starting from the top of the `*.py`
file. However, a code pattern exists that provides a more structured approach to defining an
"entry" or starting point for a program or script.

### 1.1 Execution modes

Python features _two_ file execution modes. Code in a file can be executed as a script from the
command line or the code can be _imported_ into another Python file in order to access its
definitions and statements.

If a Python file is executed from the command line the Python interpreter will run the file under
the special name "dunder" (i.e., double underscore) `__main__` rather than the program's actual
file name (e.g., `si506_week_XX.py`). We refer to such a file as a _script_ or a program.

Given this naming behavior we can choose the program's entry point and control the
program's execution flow by directing the Python interpreter to call a function named `main()`
_first_ in order to execute the statements defined in its code block.

```python
def main():
    # Execute statements
    # < statement A >
    # < statement B >
    # ...

if __name__ == "__main__":
    main() # call main function
```

### 1.2 Why `main()`?

Employing a `main()` function to manage your program's flow of execution separates the code
you write to manage a program's work flow from the code you write to perform specific tasks (e.g.,
functions). This encourages code modularization and, by relying on function calls to perform
specific tasks, helps to eliminate code duplication.

An important side benefit is that with the work flow code restricted to `main()` the other
definitions and statements comprising the file (e.g., functions, classes, constants) can be
imported as a module into another Python module without triggering the code located in `main()`.
This can occur because module code imported from one Python file into another Python file is known
by the Python interpreter by the module's actual file name and not by the name `__main__` as is the
case with scripts/programs run from the command line.

:bulb: the key takeaway from this section is that a Python script's _entry point_ can be
orchestrated to provide a controlled programmatic flow of execution.

We will cover modules, module imports, and execution modes in more detail _after_ the
midterm.

## 2.0 Function basics

Writing a function in order to perform a particular task is a form of code modularization designed
to simplify otherwise complex processes. Functions also encourage code re-use and adherance to the
_Don’t Repeat Yourself_ (DRY) principle of software development.

### 2.1 Defining and calling a function

A function is defined using the keyword `def` and given a name that ends with parentheses `()`.

:bulb: Per [PEP 8](https://pep8.org/#function-names):

> Function names should be lowercase, with words separated by underscores as necessary to improve
> readability.

In addition consider names employing a `< verb >_< noun >` format, such as `convert_to_int`,
`read_csv`, or `get_resource`.

A function may be defined with one or more _parameters_. This allows the function to accept input
for processing. The function declaration line is terminated by a colon (`:`).

A function includes an indented code block. Code intended for execution _must_ be placed inside the
block. A function's code block is executed if, and only if, the function is called explicitly;
otherwise, the code block is ignored by the Python Interpreter.

In the example below the function named `print_slogan` is defined with a single _parameter_ named
`cereal`. This allows the function to accept input for processing. If the function `print_slogan()`
is called and supplied with a list representation of a cereal (known as an _argument_) that features
a well-understood structure&mdash;the third element references the slogan&mdash;the function will
pass the cereal's slogan on to the built-in function `print()` to stream the value to the terminal.

```python
cereals = [
    ['manufacturer', 'brand', 'slogan', 'serving_size_gm', 'sugar_gm'],
    ['Post Consumer Brands', 'Honey Bunches of Oats', "Taste the joy in every spoonful.", 30, 6],
    ['General Mills', 'Cocoa Puffs', "I'm cuckoo for Cocoa Puffs!", 36, 13.4],
    ['Kellogg Company', 'Frosted Flakes', "They're Gr-r-reat!", 41, 14.5],
    ['General Mills', 'Honey Nut Cheerios', 'Have a Change of Heart', 28, 9],
    ['Post Consumer Brands', 'Grape-nuts', 'Ever eat a pine tree? Many parts are edible.', 29, 4.4],
    ['Kellogg Company', 'Raisin Bran', 'Two scoops of raisins in every box.', 59, 18],
    ['General Mills', 'Cheerios', 'Go with the Goodness of Cheerios.', 28, 1.3],
    ['Kellogg Company', 'Fruit Loops', 'Follow my nose. It always knows.', 39, 12],
    ['Post Consumer Brands', 'Shredded Wheat', 'Bet you can’t eat three.' , 49, 0.4],
    ['General Mills', 'Lucky Charms', "They're magically delicious.", 36, 13],
    ['Quaker Oats Company', "Cap'n Crunch", "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.", 27, 12],
    ['Post Consumer Brands', 'Fruity Pebbles', "They're Yabba-Dabba-Delicious!", 27, 9.3],
    ['Kellogg Company', 'Corn Flakes', "Wake up, up, up to Kellogg's Cornflakes!", 29, 10],
    ['Kellogg Company', 'Apple Jacks', "We eat what we like.", 28, 8],
    ['General Mills', 'Wheaties', "The Breakfast of Champions", 27, 4.1]
    ]


def print_slogan(cereal):
    print(cereal[2])


frosted_flakes = cereals[3]
print_slogan(frosted_flakes) # Call function and pass argument
```

:exclamation: A function call is an _expression_ (i.e., the call resolves to a value).

### 2.2 Specifying a return value

A function may include a `return` statement that signals the end of any computations performed
and "returns" a value to the caller.

:exclamation: Functions that do not specify a `return` statement return `None` to the caller.

In the example below the function named `get_slogan` is defined with a single parameter named
`cereal`. The function accepts input and returns a string that represents the cereal's slogan.

```python
def get_slogan(cereal):
    return cereal[2]

raisin_bran = cereals[6]
slogan = get_slogan(raisin_bran)
```

### 2.3 Multiple parameters

A function definition can specify multiple parameters. The caller _must_ pass to the function the
required number of _arguments_ or a runtime error will occur.

In the example below, the function `format_slogan` is called with the required arguments passed
_by position_. The function's return value is then assigned to a variable.

```python
def format_slogan(name, slogan):
    return f"{name}: {slogan}"


wheaties_slogan = format_slogan(cereals[-1][1], cereals[-1][2])
```

### 2.4 Positional arguments (order matters)

If positional arguments are passed to a function, the caller must pass them in the correct order to
ensure that the function can process the values as expected.

In the example below, the function `format_slogan` is called but the arguments are passed to it in
the wrong order. The resulting computation returns an unexpected and incorrect value.

```python
apple_jacks_slogan = format_slogan(cereals[-2][2], cereals[-2][1]) # Oops! string reversed
```

### 2.5 Challenge 01

__Task__. Fix a partially implemented function that returns a list of cereal brands associated with
a given manufacturer.

1. Implement the accumulator pattern _inside_ the function block to accomplish the following
   sub-tasks:

   1. Iterate over the passed in `cereal_brands` list.

   2. Write an `if` statement that filters on the passed in `company` argument. If the cereal being
      evaluated (a `list`) is produced by the `company`, append the cereal's name to the `brands`
      list.

      :exclamation: The `if` statement that you write _must_ allow the caller to pass in a string
      that __matches part or all__ of a company name (i.e., "Kellogg" or "kellogg" matches "Kellogg
      Company"); in other words implement a _case insensitive_ "near match" string comparison.

2. After implementing `get_cereals_by_company` call the function and retrieve all cereal brands in
   `cereals` produced by Post Consumer Brands. Assign the function's return value to the variable
   named `post_cereals`.

3. Call the function __a second time__ and retrieve all cereal brands in `cereals` produced by the
   Kellogg Company. Assign the function's return value to the variable named `kellogg_cereals`.

4. Uncomment the two calls to `print()` and check your work.

## 3.0 Keyword arguments and optional parameters

### 3.1 Keyword arguments

The caller of a function can pass _keyword arguments_ specifying both a key and value in the form
`key=value`. The argument is denoted by its keyword rather than by its position in the argument
list.

Keyword arguments free you from having to worry about correctly ordering your arguments in the
function call. Each keyword argument specified clarify the "name" of each value in the function call
by binding the value directly to the key.

:exclamation: Note that by convention keyword arguments do not include spaces on either side of the
assignment operator.

The following example illustrates passing keyword arguments in _reverse_ order to that specified by
the function definition:

```python
general_mills_cereals = get_cereals_by_company(company='general mills', cereal_brands=cereals)
```

:exclamation: By convention keyword arguments _do not_ include spaces on either side of the
assignment operator. The auto grader will check your keyword argument styling so style your keyword
arguments per [PEP 08](https://pep8.org/#other-recommendations):

```python
# Do this
some_var = some_func(arg_01=val_01, arg_02=val_02)

# Not this
some_var = some_func(arg_01 = val_01, arg_02 = val_02)
```

### 3.2 Optional parameters

As noted above, a function definition can specify one or more parameter values. Each parameter can
specify a default value. In such cases, the caller is _not required_ to pass in a corresponding
argument unless a need exists to override the default value.

In the example below, the function `calculate_sugar_content` defines a parameter named `precision`
that determines the number of decimal places to round the return value. A default value of two (`2`)
is specified. The function can be called in one of two ways:

1. Pass one argument: the required cereal brand (a `list`). The function will then compute a value
   and round it the second decimal place (the default `precision` value).

2. Pass two arguments: the required cereal brand (a `list`) and an integer that overrides the
   default `precision` value.

:exclamation: Optional parameters _must_ be listed _after_ required parameters in order to allow
required arguments to be passed solely by position.

```python
def calculate_sugar_content(cereal_brand, precision=2):
    return round(cereal_brand[-1] / cereal_brand[-2], precision)
```

To simplify accessing individual cereal brands from the `cereals` list so that we can pass the
cereal to `calculate_sugar_content` as an argument, let's write a "helper" function named
`get_cereal`. This function will retrieve a list representation of a cereal brand by its name.

```python
def get_cereal(cereal_brands, cereal_name):
    for cereal in cereal_brands:
        if cereal_name.lower() in cereal[1].lower():
            return cereal # match, exit loop immediately
```

:bulb: Note the placement of the `return` statement _inside_ the `if` statement block. If the
condition resolves to `True` the matching cereal (a `list`) is returned immediately to the caller,
the loop is terminated, and the function is exited. If no match is obtained the function returns
`None` (implicitly) to the caller. This is an efficient design as it eliminates unnecessary looping.

The caller can now easily retrieve a cereal from the `cereals` list, calculate its sugar content,
and round the value to be returned to any number of decimal places.

```python
# Retrieve cereal
cocoa_puffs = get_cereal(cereals[1:], 'Cocoa Puffs')

# Accept precision default value
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs)

# Override precision default value
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs, 3) # override
```

### 3.3 Skipping optional parameters

If a function definition includes _multiple_ optional parameters, keyword arguments
_must_ be employed whenever a preceeding optional argument is skipped when calling the function.

In the example below the function returns either a percentage value formatted as string or float
value. If the caller passes to the function an optional `precision` value (say `3`), a keyword
argument must be passed to ensure the correct parameter binding if the optional `format_pct` value
is not specified explicitly by the caller.

```python
def calculate_sugar_content_v2(cereal_brand, precision=2, format_pct=False):
    if format_pct:
        return f"{cereal_brand[-1] / cereal_brand[-2] * 100:.{precision}f}%" # trailing % sign
    else:
        return round(cereal_brand[-1] / cereal_brand[-2], precision)

raisin_bran = get_cereal(cereals[1:], 'raisin bran')

# 3 binds to wrong parameter; returns string
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, 3)

print(f"\n2.3.1 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Keyword argument binds 3 correctly, returns float
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, precision=3)

print(f"\n2.3.2 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Returns formatted string
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, format_pct=True, precision=3)
```

### 3.4 Challenge 02

__Task__: Implement a general purpose function that utilizes "headers" elements to look up and
retrieve any attribute of a nested cereal list element.

1. Implement the function named `get_cereal_attribute`. The function defines three parameters:

   1. cereal (`list`): list representation of a cereal brand

   2. headers (`list`): list representing data column "header" elements (e.g., "serving_size_gm")

   3. header (`str`): header value that acts as a filter

   Replace the placeholder `pass` statement in the function block with your code.

   The function utilizes the cereal `headers` and the `header` column name to look up a cereal
   attribute (i.e., element) by its index position and return the value to the caller.

   :bulb: The function block requires only a single line of code.

2. After implementing the function `get_cereal_attribute()` call the function `get_cereal()` and
   pass to it the arguments required to return the nested list in `cereals` that represents
   Kellogg's __"Corn Flakes"__. Assign the return value (a `list`) to the variable `corn_flakes`.

3. Next, call `get_cereal_attribute()` and pass it the arguments that it requires to retrieve the
   `corn_flakes` serving size value in grams. Assign the return value to the variable named
   `corn_flakes_serving_size_gm`.

   :exclamation: Pass the following string to `get_cereal_attribute()` as the third argument:
   "serving_size_gm".

4. Uncomment `print()` and check your work.

## 4.0 Passing a function call as an argument

You can "nest" a function call among the arguments that you pass to a function. Strictly speaking,
you are passing the _return value_ of the function as an argument to the function rather than the
function itself.

:bulb: A Python function is considered a "first-class" object. A function can be stored in a data
structure such as a list, tuple or a dictionary. A function can also be passed by name as an
argument to another function. A function designed to accept a function as an argument is considered
a _higher-order_ function. We will discuss higher-order functions in a future lecture.

Let's create a third version of the function that calculates a cereal's sugar content. Instead of
passing a cereal list to the function in order to access its serving size and sugar content values,
the required numeric values will be passed directly to the function as its first and second
arguments:

```python
def calculate_sugar_content_v3(serving_size_gm, sugar_gm, precision=2, format_pct=False):
    if format_pct:
        return f"{sugar_gm / serving_size_gm * 100:.{precision}f}%"
    else:
        return round(sugar_gm / serving_size_gm, precision)
```

Calculating a cereal's sugar content per given serving size can now be obtained by the following
function calls:

```python
cereal = get_cereal(cereals[1:], 'Grape-nuts')
serve_size_gm = get_cereal_attribute(cereal, headers, 'serving_size_gm')
sugar_gm = get_cereal_attribute(cereal, headers, 'sugar_gm')
sugar_content = calculate_sugar_content_v3(serve_size_gm, sugar_gm, precision=3, format_pct=True)
```

Alternatively, function calls can be nested in other function calls:

```python
cereal = get_cereal(cereals[1:], 'Grape-nuts')
sugar_content = calculate_sugar_content_v3(
    get_cereal_attribute(cereal, headers, 'serving_size_gm'),
    get_cereal_attribute(cereal, headers, 'sugar_gm'),
    precision=3,
    format_pct=True
)
```

or

```python
sugar_content = calculate_sugar_content_v3(
    get_cereal_attribute(get_cereal(cereals[1:], 'Grape-nuts'), headers, 'serving_size_gm'),
    get_cereal_attribute(get_cereal(cereals[1:], 'Grape-nuts'), headers, 'sugar_gm'),
    precision=3,
    format_pct=True
)
```

## 5.0 Variable scope

Now that you have begun to write functions it's time to discuss Python's rules for resolving name
references (i.e., variables). Accessing a variable and the object to which it is assigned depends in
large part on _where_ the variable is defined in your program. An object's duration or lifetime also
depends in part on _where_ in your program it is assigned. A variable's _scope_ is limited to those
parts of a program in which the variable is visible and can be accessed.

A variable defined _inside_ a function is considered _local_ to that function. In other words, a
local variable can only be accessed from inside the function's code block. On the other hand, a
variable defined outside a function in the main part of a program file or module possesses top level
or _global_ scope. Such a variable is visible throughout the program from the point in which it was
first defined. Treat _global_ variables carefully. Referencing _global_ variables inside functions
can have unintended effects.

Python keywords and built-in functions possess a special _built-in_ scope and are also
available whenever you execute a script or run your program.

The variable `cereals` possesses global scope. On the other hand, the variable
`brands` is _local_ to the function named `get_cereals_by_company()` and is only available within
the function block.

```python
def get_cereals_by_company(cereal_brands, company):
    brands = [] # local scope only
    for cereal in cereal_brands:
        if cereal[0].lower().startswith(company.lower()):
            brands.append(cereal[1])
    return brands
```

You can test this by attempting to access the variable `brands` from outside the function. For
example, if you attempt to pass `brands` to the built-in `print()` function outside the function
block you will trigger a `NameError` runtime exception:

```commandline
NameError: name 'brands' is not defined
```

## 6.0 Functions can call other functions

Ideally, a function should perform a single computational task, delegating all related tasks to
other functions to perform.

For example, say you were asked to identify cereals that contain corn syrup.

```python
cereal_ingredients = [
    ['manufacturer', 'brand', 'ingredients'],
    ['Kellogg Company', 'Frosted Flakes', ('Milled Corn', 'Sugar', 'Malt Flavoring', 'High Fructose Corn Syrup', 'Salt')],
    ['Kellogg Company', 'Raisin Bran', ('Whole Grain Wheat', 'Raisins', 'Wheat Bran', 'Sugar', 'High Fructose Corn Syrup')],
    ['General Mills', 'Cheerios', ('Whole Grain Oats', 'Modified Corn Starch', 'Sugar', 'Salt')],
    ['General Mills', 'Cocoa Puffs', ('Whole Grain Corn', 'Sugar', 'Corn Syrup', 'Cornmeal', 'Canola and or Rice Bran Oil')],
    ['General Mills', 'Lucky Charms', ('Oats', 'Marshmallows', 'Sugar', 'Corn Syrup', 'Corn Starch')],
    ['Post Consumer Brands', 'Shredded Wheat (original spoon size)', ('Whole Grain Wheat',)],
    ['Post Consumer Brands', 'Grape-nuts', ('Whole Grain Wheat', 'Flour', 'Malted Barley Flour', 'Salt', 'Dried Yeast')]
    ]
```

A data structure review suggests that the problem needs to be broken down into several subproblems.
This process is known as _decomposition_.

1. Loop over the "cereals" slice in `cereal_ingredients` (i.e., exclude the "headers" nested list).
   Each element encountered is a nested list that represents a cereal.
2. During each loop iteration access the current cereal's "ingredients" `tuple` element.
3. Loop over the tuple of ingredients and filter on "corn syrup".
4. If an ingredient _contains_ the substring "corn syrup", append the cereal to an accumulator list.

Decomposing the problem into subproblems suggests that two loops are required to access each
cereal's ingredients. You could get at the data by implementing a nested loop (a future topic), or a
`for` loop and a function, or two functions. The latter approach is preferred because each function
can perform a specific task that is then available for "reuse" elsewhere in your program.

In the solution below the two functions are named `has_ingredient` and `get_cereals_by_ingredient`.
The functions perform the following operations:

* `has_ingredients`: Indentifies whether or not an ingredient is a member of a cereal's tuple of
  ingredients. Performs a case insensitive string comparison that __matches part or all__ of a an
  ingredient name. If a match is obtained returns `True`; otherwise returns `False`.

* `get_cereals_by_ingredient`: Loops over the list of cereals provided by the caller. Delegates to
  the function `has_ingredient` the task of identifying whether or not a cereal possesses a specified
  ingredient. If an ingredient match is obtained, adds the cereal list to an local accumulator list.

* After the loop terminates, the accumulator list is returned to the caller.

:bulb: Since `has_ingredient` returns either `True` or `False` the function call (an expression) can
be embedded in an `if` statement.

```python
def has_ingredient(ingredients, ingredient):
    for item in ingredients:
        if ingredient.lower() in item.lower():
            return True # exit function; terminates loop
    return False


def get_cereals_by_ingredient(cereals, ingredient):
    results = []
    for cereal in cereals:
        if has_ingredient(cereal[-1], ingredient):
            results.append(cereal)
    return results


corn_syrup = get_cereals_by_ingredient(cereal_ingredients[1:], 'corn syrup')
```

### 6.1 Challenge 03

__Task__: Retrieve cereal(s) with the lowest sugar content. Possible ties _must_ be accommodated.

1. Assign a sensible start value to the variable `min_sugar_gm` that will allow you to assign
   progressively smaller values as you loop over the `cereals` list.

2. Inside the loop block call the function `get_cereal_attribute()` and pass it the appropriate
   arguments in order to assign the current cereal's "brand", "serving_size_gm", and "sugar_gm"
   values to the variables `cereal_brand`, `serving_size_gm`, and `sugar_gm`.

3. Inside the loop block call the function `calculate_sugar_content_v3()` and pass it the arguments
   it needs to compute the sugar content of the current `cereal`. Assign the return value to the
   variable `sugar_content`.

4. Insert the missing variable and appropriate comparison operator into the partially implemented
   `if` statement.

5. Inside the `if` block assign the appropriate value to `min_sugar_gm`.

   :bulb: Given that a new low sugar cereal has been detected calling `min_sugar_content.clear()`
   removes all previous cereal names added to the accumulator list.

6. The possibility exists that the current cereal's `sugar_content` is equal to the previous low
   value. Insert the appropriate comparison operator into the `elif` statement that reflects this
   possibility.

7. Uncomment the `min_sugar_cereals` variable assignment (includes the function call).

8. Uncomment `print()` and check your work.

## 7.0 Truth value testing

In Python every object can be tested for its
[_truth value_](https://docs.python.org/3/library/stdtypes.html#truth-value-testing). You can check
an object's truth value in an `if` or `while` statement or as an operand (i.e., the value the
operator operates on) in an `and`, `or` `not` Boolean operation. A value that evaluates to `True`
is considered _truthy_ while a value that evaluates to `False` is considered _falsy_.

For SI 506 the following values are considered "truthy" or "falsy":

| Type                                       | Value     | Truth value |
|:-------------------------------------------|:----------|:------------|
| Nonetype                                   | `None`    | falsy       |
| numeric (`int`, `float`)                   | non-zero  | truthy      |
| numeric (`int`, `float`)                   | 0, 0.0    | falsy       |
| boolean                                    | `True`    | truthy      |
| boolean                                    | `False`   | falsy       |
| sequence (`list`, `range`, `tuple`, `str`) | non-empty | truthy      |
| sequence (`list`, `range`, `tuple`, `str`) | empty     | falsy       |
| associative array (`dict`)                 | non-empty | truthy      |
| associative array  (`dict`)                | empty     | falsy       |

The following example demonstrates testing a list's truth value utilizing the built-in function
`bool()` which accepts an object and returns either `True` or `False` per the standard truth value
testing rules:

```python
def get_truth_value(val):
    return bool(val) # check's the object's truth value

fruity_pebbles = None
truth_value = get_truth_value(fruity_pebbles) # falsy

fruity_pebbles = []
truth_value = get_truth_value(fruity_pebbles) # falsy

fruity_pebbles = ['Post Consumer Brands', 'Fruity Pebbles', 27, 9.3]

truth_value = get_truth_value(fruity_pebbles) # truthy
```

You can employ an `if` or `elif` statement to check an object's truth value. In the example below
the function named `has_cereal` is provisioned with two parameters: `cereals` (`list`) and
`cereal_brand` (`str`). The function tests the truth value of the expression
`get_cereal(cereals, cereal_brand)`. The function call returns either a string (a cereal brand) or
`None`. However, when called from within an `if` statement the expression evaluates to either `True`
(a string is returned) or `False` (`None` is returned). If the conditional statement evaluates to
`True` the function returns the boolean `True`; otherwise it returns `False`.

```python
def has_cereal(cereals, cereal_brand):
   if get_cereal(cereals, cereal_brand):
      return True
   else:
      return False


has_golden_grahams = has_cereal(cereals, 'Golden Grahams') # Returns False
```

The function can also be implemented without an `else` statement:

```python
def has_cereal(cereals, cereal_brand):
    if get_cereal(cereals, cereal_brand):
        return True
    return False # Required otherwise None is returned
```

## 8.0 Iterable packing and unpacking

Both lists and tuples can be "packed" and "unpacked".

_Packing_ a list or tuple involves assigning multiple list elements or tuple items to a single object.

```python
# Packing
shredded_wheat = ['Post Consumer Brands', 'Shredded Wheat', 'Bet you can’t eat three.', 49, 0.4]

# Equivalent
shredded_wheat = get_cereal(cereals[1:], 'shredded wheat')
```

_Unpacking_ or multple assignment involves accessing multiple list elements or tuple items and
assigning the values to an equal number of comma-separated variables positioned on a single line.

```python
# Unpacking
manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm = shredded_wheat
```

### 8.1 Triggering `ValueError` runtime exceptions

Multiple assignment requires that list elements or tuple items are mapped (e.g., assigned) to an
_equal_ number of variables. Mismatches on either side of the assignment operator (`=`)  will raise
a `ValueError` runtime exception.

```python
# Triggers ValueError: too many values to unpack (expected 4)
manufacturer, cereal_brand, slogan, sugar_gm = shredded_wheat

# Triggers ValueError: not enough values to unpack (expected 6, got 5)
manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm, rating = shredded_wheat
```

:exclamation: Also make sure that the comma-separated variables employed in the unpacking operation
are ordered correctly; otherwise unanticipated variable assigments will occur.

```python
# Variables ordered incorrectly
slogan, cereal_brand, manufacturer, sugar_gm, serving_size_gm = shredded_wheat
```

### 8.2 Unpacking in a loop

Recall that every iteration of a `for` loop involves the _implicit_ assignment of a loop variable to
an element or item between the `for` and `in` keywords. You are not limited to a single implicit
loop variable assignment as is demonstrated in the second `for` loop below:

```python
# Conventional unpacking (first four cereals)
for cereal in cereals[1:5]:
    manufacturer, brand, slogan, serving_size_gm, sugar_gm = cereal
    print(
        f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSlogan: {slogan}",
        f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}"
    )

# Unpack into loop variables (last four cereals)
for manufacturer, brand, slogan, serving_size_gm, sugar_gm in cereals[-4:]:
    print(
        f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSlogan: {slogan}",
        f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}"
    )
```

## 9.0 Additional Challenges

Five star product ratings systems are ubiquitious on the Web but are now regarded as highly
problematic measures of customer satisfaction. One would expect the ratings to tend towards a
normal distribution as the number of ratings increase (obeying the Law of Large Numbers). Instead,
the ratings tend to exhibit an asymmetric bimodal distribution (the infamous J-curve) with respect
to the distribution of responses with the curve heavily skewed in the direction of highly favorable
ratings. Self-selection bias provides a partial explanation for this phenomenon (i.e., only people
who love or hate a product opt to rate it--which suggests that a simpler thumbs up/down scale would
better capture such sentiments).

Anyways, let's explore cereal ratings data sourced from Walmart.

```python
cereal_ratings_data = [
    ['manufacturer', 'brand', 'five_stars', 'four_stars', 'three_stars', 'two_stars', 'one_star'],
    ['Kellogg Company', 'Apple Jacks', 185, 21, 10, 4, 2],
    ...,
    ['General Mills', 'Wheaties', 215, 18, 5, 2, 12]
    ]
```

### 9.1 Challenge 04

__Task__. Implement a function that returns the ratings for a given cereal.

1. Implement a function named `get_ratings` that defines a single parameter:

   * `cereal` (list): represents a cereal brand and its 1 to 5 star ratings.

   __Requirements__

   1. The function _must_ return a list of the cereal's 1 to 5 star rating elements (e.g.,
      `[185, 21, 10, 4, 2]`).

      :bulb: this function can be implemented with one line of code.

2. After implementing `get_ratings`, call the function `get_cereal` and pass the following
   arguments to it in __reverse__ order using __keyword arguments__:

   1. the `cereal_ratings` list
   2. the string "raisin bran"

   Assign the return value to a variable named `raisin_bran`.

3. Next, call `get_ratings` and pass `raisin_bran` to it as the argument. Assign the return value
   to a variable named `raisin_bran_ratings`.

4. Uncomment the `brand` assignment and `print()` and check your work.

### 9.2 Challenge 05

__Task__. Loop over the `cereal_ratings` list and accumulate values to a new list named
`ratings_groups` that summarize each cereal's ratings as "favorable", "neutral", and "unfavorable".

1. The empty `rating_groups` list will serve as an accumulator.

2. Loop over the `cereal_ratings` list. For each cereal encountered call the function `get_ratings`
   and pass the cereal list to it as the argument.

3. _Unpack_ the return value (a `list`) into five local variables named: `five`, `four`, `three`,
   `two`, and `one`.

4. Access the rating counts and assign the values to the following local variables per the specified
   groupings:

   1. `favorable` = sum of the 5 star and 4 star rating counts
   2. `neutral` = 3 star rating count
   3. `unfavorable` = sum of the 2 star and 1 star rating counts

5. Construct an f-string using the function's local variables formatted as follows:

   ```python
   f"<cereal name> ratings: favorable=< favorable count >, neutral=< neutral count >, unfavorable=< unfavorable count >"
   ```

6. Append the string to the list `rating_groups`.

7. Uncomment `print()` and `pp.print()` and check your work.

### 9.3 Challenge 06

__Task__. Implement functions that aid in computing a favorability rating (percent value) for a given
cereal.

1. Replace the `pass` statement in the function `count_ratings` to ensure that the function
   increments the `count` value correctly.

2. Implement a function named `calculate_favorable_rating_pct` that defines a single parameter:

   * `cereal` (list): represents a cereal brand and its 1 to 5 star ratings.

   __Requirements__

   1. The function _must_ calculate a cereal's favorability rating based on the following equation:

      ```python
      (<5 star rating count> + <4 star rating count>) / < total ratings count> * 100
      ```

   2. The function _must_ delegate to `get_ratings` the task of retrieving a cereal's ratings.

   3. The function _must_ delegate to `count_ratings` the task of providing a total count of all
      ratings provided for a given cereal.

   4. After calculating the passed in cereal's favorability rating, return the percentage value to the
      caller.

3. :bulb: After implementing `calculate_favorable_rating_pct` the function `get_cereal` is called to
   retrieve the nested list that represents the Honey Nut Cheerios brand. The list is assigned to
   the variable named `honey_nut_cheerios`.

4. Call the function `calculate_favorable_rating_pct` and pass `honey_nut_cheerios` to it as the
   argument. Assign the return value to the variable `cheerios_fav_pct`.

5. Uncomment the `brand` assignment and `print()` and check your work.
