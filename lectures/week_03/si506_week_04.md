# SI 506 Week 04

## Topics

1. Iteration and control flow
   1. Nested lists
   2. Definite iteration: `for` loop
   3. The `if` statement
   4. Challenge 01
2. The accumulator pattern
   1. Challenge 02
   2. Challenge 03
   3. Accumulating counts
   4. Challenge 04
3. Looping with the `range` type
   1. `range` behaviors
   2. The `for` loop and `range`
   3. Employing `range` to replace list elements
   4. Chaining subscript operators
   5. Challenge 05
4. `if-else` conditions
   1. Challenge 06
   2. Challenge 07

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

This week's lecture data is drawn from the US Dept of Energy's
[Alternative Fuels Data Center](https://afdc.energy.gov/) information on model year 2023
[electric vehicles](https://afdc.energy.gov/vehicles/search/download.pdf?year=2023) (EVs).

:bulb: Each EV is represented by a nested list. In addition, the data elements ("headers") that
comprise each nested list are described in the first nested list.

:bulb: The abbreviation "mpge" in the string `fuel_economy_mpge` is short-hand for
_miles per gallon of gasoline-equivalent_.

```python
data = [
    [
        "make_model",
        "vehicle_type",
        "drivetrain",
        "fuel_economy_mpge",
        "all_elec_range_mi",
        "battery_capacity_kwh",
        "seat_count",
        "base_msrp",
    ],
    [
        "Audi e-tron GT/RS e-tron GT",
        "Sedan/Wagon",
        "AWD",
        "81-82",
        "232-238",
        "95",
        "5",
        "$104,900",
    ],
    ...
]
```

## 1.0 Iteration and control flow

This week we focus on _iteration_ (i.e., accessing sequence elements employing loops) and
_control flow_ (i.e., the order in which a program or script executes). You will learn how to
iterate or loop over a sequence (`list`, `range`, `str`, `tuple`) using a `for` and a `while` loop.
You will also learn how to write conditional statements in order to determine which computations
your code must perform. Conditional statements can be placed inside the body of a `for` loop in
order to act as data filters or terminate a looping operation if a particular condition has been
satisfied.

Conditional statements employ a variety of operators. As noted previously, Python operators are
organized into [groups](https://www.w3schools.com/python/python_operators.asp). We’ve touched on
arithmetic operators and assignment operators. Starting this week you will begin using other
operators when writing conditional statements, especially comparison, identity, and membership
operators. Use of logical operators such as `and`, `or`, and `not` will be discussed next week.

## 1.1 Nested lists

The Python _sequence_ is a container data type that holds objects that can be accessed individually
or in groups by their position. Both strings and lists are sequences. The `str` data type comprises
an ordered collection of _immutable_ characters, the `list` data type comprises an ordered
collection of _mutable_ elements, and the `tuple` data type comprises an ordered collection of
_immutable_ elements.

The lists and tuples that you've encountered thus far have consisted of strings and/or numbers.
In the example below, each element in the `ev_vehicles` list represents an electric vehicle (EV).
Each string contains a set of attributes (automaker, model, model year, range in mpg) that are
delineated by use of a comma and space as a separator.

```python
# EV attributes: make_model, vehicle_type, drivetrain, fuel_economy_mpge,
# all_elec_range_mi, battery_capacity_kwh, seat_count, base_msrp

ev_vehicles = [
    "Cadillac Lyric, SUV, RWD, 89, 312, 119, , $61,795",
    "Chevrolet Bolt EUV, Sedan/Wagon, FWD, 115, 247, 75, 5, $27,200",
    "Chevrolet Bolt EV, Sedan/Wagon, FWD, 120, 259, 75, 5, $25,600",
    "Ford F150 Lightning 4WD, Pickup, AWD, 66-70, 240-320, 165, 5, $55,974",
]
```

Accessing individual vehicle data in the list of strings requires splitting each string on the
comma and space (`", "`) in order to access the desired vehicle attribute(s) by position via
indexing:

```python
model = ev_vehicles[0].split(", ")[0]  # Cadillac Lyric
```

The above operation suggests that that vehicle data could be represented as a list of lists, with
each "inner" list element holding a distinct piece of information. Since lists (and tuples) can
reference more complex data types we should consider representinng each EV as a "nested" list rather
than a string.

```python
# EV attributes: make_model, vehicle_type, drivetrain, fuel_economy_mpge,
# all_elec_range_mi, battery_capacity_kwh, seat_count, base_msrp

ev_vehicles = [
    ["Cadillac Lyric", "SUV", "RWD", "89", "312", "119", "", "$61,795"],
    ["Chevrolet Bolt EUV", "Sedan/Wagon", "FWD", "115", "247", "75", "5", "$27,200"],
    ["Chevrolet Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["Ford F150 Lightning 4WD", "Pickup", "AWD", "66-70", "240-320", "165", "5", "$55,974"],
]
```

Accessing the first element's "model" element involves chaining the index positions.

```python
model = ev_vehicles[0][0]  # Cadillac Lyric
```

### 1.2 Definite iteration: the `for` loop

Indexing and slicing sequence elements by position is standard operating procedure for Python
programmers. However, if you need to interact with _all_ members of a sequence indexing and/or
slicing your way to success could prove tedious and inefficient. Python provides a ready solution
to this challenge in the guise of the `for` loop.

Writing a `for` loop simplifies sequence traversal. You can loop over the entirety (or a portion)
of a sequence confident that the loop will terminate automatically once the
the last character, element, or item in the sequence (or subset of the sequence) is reached.  This
process is known more generally as __definite iteration__.

The keywords `for` and `in` comprise the basic syntax of the `for` loop:

```python
for < element > in < sequence >:
    # indented block
    < statement A >
    < statement B >
    # ...
```

Note that the `for` loop statement is terminated by a trailing colon (`:`). The colon indicates the
start of the loop's code block. The statement(s) that comprise the loop's code block _must_ be
indented four (4) spaces. The statements are _local_ to the loop and are only executed when the
loop is run.

In the following example, each element in `ev_vehicles` is assigned the "loop" variable `vehicle`.
During each iteration of the loop the `vehicle` element is passed to the built-in `print()`
function. After the last `vehicle` element is printed the loop terminates.

```python
for vehicle in ev_vehicles:
    print(vehicle) # indented block
```

:exclamation: Failure to employ Python's indention rules can lead to unexpected computations and/or
trigger an `IndentionError`.

You can limit the number of loop iterations by targeting a subset of a sequence. In the following
example, slicing is employed to restrict the number of loop iterations to elements one and two in
`ev_vehicles`:

```python
for vehicle in ev_vehicles[1:3]:
    print(vehicle)  # indented block
```

### 1.3 The `if` statement

Looping just to loop is not all that useful. Data is compiled (usually) in the hope that later
statistical analysis will reveal otherwise hidden patterns in the data set. Conditional logic can be
embedded in a `for` loop block in order to interact with a sequence's elements in more meaningful
ways.

A Python conditional statement evaluates to either `True` or `False`. Conditional statements placed
inside a `for` loop block determine which computations, if any, are to be performed during each
iteration of the loop.  More generally, conditional statements help determine a computer
program's _control flow_ or the order in which individual statements are executed.

The keyword `if` comprises the basic syntax of a conditional statement:

```python
if < condition >:
    # indented block
    < statement C >
    < statement D >
    # ...
```

Like the `for` loop the `if` statement is terminated with a trailing colon (`:`). The colon
indicates the start of the conditional statement's code block. The statement(s) that comprise
the `if` statement's code block _must_ be indented four (4) spaces. The statements are _local_ to
the `if statement` and are _only_ executed if the statement condition returns `True`.

Below is a second example in which `ev_vehicles` elements are passed to the built-in `print()`
function. But in this case, the `if` statement filters on the "automaker" element and only calls
`print()` if the vehicle manufacturer is Ford.

```python
for vehicle in ev_vehicles:
    if vehicle[0].find("Ford") > -1:
        print(vehicle)
```

:bulb: `str.find()` returns `-1` if no match is obtained; otherwise the method call returns the
index of the first occurence of the passed in substring.

If, for example, you needed to identify and print all EVs in `ev_vehicles` produced by Chrevrolet
you could employ the [membership operator](https://www.w3schools.com/python/python_operators.asp)
`in` as is illustrated in the example below.

```python
for vehicle in ev_vehicles:
    if "chevrolet" in vehicle[0].lower():
        print(vehicle)
```

The opposite condition can also be evaluated. If you needed to identify and print all EVs in
`ev_vehicles` produced by automakers other than Chevrolet you could employ the `not in`
membership operator.

```python
for vehicle in ev_vehicles:
    if "chevrolet" not in vehicle[0].lower():
        print(vehicle)
```

:bulb: Use of `str.lower()`
renders the `if` statement _case-insentive_ ensuring that possible variations in the manufacturer
name (e.g., "Chevrolet", "chevrolet", "CHEVROLET"), will not result in skipping otherwise valid
matches. This is an example of "defensive" programming. When working with string data never assume
that the data is "clean" (i.e., uniform and consistent). Note that there will be occasions when you
will need to perform _case-sensitive_ string matching.

### 1.4 Challenge 01

__Task__: Print to the terminal screen the elements that represent Teslas in the list
`ev_vehicles`.

The list below represents a random selection of 2023 model year EVs sourced from the DOE
Alternative Fuels Data Center.

:bulb: Note that the first nested list represents "header" values.

```python
ev_vehicles = [
    ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    ["Tesla Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
    ...,
]
```

1. Implement a `for` loop and a conditional `if` statement to identify elements in `ev_vehicles`
   that represent Tesla EVs.

   :bulb: Employ slicing to exclude the first element in `ev_vehicles`.

2. If the vehicle is manufactured by Tesla, pass the variable that refers to the element to the
   built-in `print()` function.

:bulb: There are several different ways that you can write the `if` statement to achieve the
required filtering.

## 2.0 The accumulator pattern

One common programming “pattern” is to traverse a sequence (e.g., a `str`, `list`, or `tuple`),
_accumulating_ a value during each iteration of the loop and assigning it to another sequence
created and assigned to a variable _prior_ to implementing the `for` loop.

In the previous challenge instead of printing the Tesla vehicle elements to terminal screen we
could have instead "accumulated" each Tesla encountered by appending the value to an empty
list named `teslas`.

:bulb: Note that the first "headers" element in `ev_vehicles` is excluded from the loop below.

```python
teslas = []
for vehicle in ev_vehicles[1:]:
    if vehicle[0].lower().find("tesla") > -1:
        teslas.append(vehicle)
```

Another variant of the accumulator pattern is to initialize an accumulator value, assigning it a
default value that is then updated by a `for` loop whenever a certain loop condition is
satisfied.

In the example below, two accumulator values are utilized in order to find the electric vehicle
featuring the greatest range in miles. When looping over `ev_vehicles` the variable `max_range`
is assigned an updated value if a vehicle's range (converted from a string to an integer using the
built-in function `int()`) is greater than `max_range`. Likewise, the variable `ev_max_range`
is assigned a new value whenever the `if` the condition evaluates to `True`. When the loop
terminates, the nested vehicle list containing the max range value will have been assigned to
`ev_max_range`.

```python
ev_max_range = None
max_range = 0
for vehicle in ev_vehicles[1:]:
    vehicle_range = int(vehicle[4])  # cast str to int
    if vehicle_range > max_range:
        ev_max_range = vehicle[0]  # automaker model
        max_range = vehicle_range
```

:exclamation: The example above does not handle ties (i.e., multiple vehicles featuring the same
max range) You will learn how to handles ties later in the course.

### 2.1 Challenge 02

__Task__: Return a list of _unique_ EV vehicle types.

Utilize the accumulator pattern and the appropriate membership operator to populate a list of
_unique_ EV vehicle types (i.e., "Sedan/Wagon", "SUV", etc.).

1. Assign an empty list to the variable `ev_types`.

2. Loop over a slice of `elec_vehicles` that __excludes__ the first nested list element (the
   "headers").

3. Implement an `if` statement that checks whether or not the current EV "type" value is a member of
   `ev_types` employing the appropriate membership operator (e.g., `in` or `not in`).

4. If the type has _yet to be added_ to `ev_types`, add the value. If the type was added to the
   accumulator list during a previous loop iteration __do not__ add the value to the list in order
   to ensure the __uniqueness__ of the list elements.

5. Uncomment `print()` and check your work.

### 2.2 Challenge 03

__Task__: Identify the EV with the shortest battery range.

1. Assign `None` a variable named `ev_min_range`. This variable will eventually point to a string
   that represents the EV with the shortest range.

2. Assign a sensible "seed" value to a variable named `min_range`. This variable will eventually
   point to an integer that represents minimum battery range in miles.

3. Loop over the slice of `ev_vehicles` that __excludes__ the first nested list element (the
   "headers").

4. Inside the `for` loop, access the vehicle "range_mi" value and onvert it to an integer by passing
   it directly to the built-in function `int()`. Assign the return value to a variable named
   `vehicle_range`.

   :exclamation: Avoid assigning the value to a variable named `range`. Doing so "shadows" the
   `range()` type name and will trigger a runtime exception when `range()` is referenced later in
   the lecture code.

5. Implement an `if` statement that evaluates whether or not the "current" `vehicle_range` value
   __is less__ than the "previous" `min_range` value.

6. Inside the `if` block assign the EV model name to `ev_min_range` and the `vehicle_range` value
    to `min_range`.

7. Uncomment `print()` and check your work.

### 2.3 Accumulating counts

The built-in `len()` function provides the overall length or size of a sequence. But if you
want to return a count of a subset of a sequence in which slicing cannot be used, then consider
using a "counter" variable to hold a rolling count of the elements that satisfy a
given condition.

In the following example a count of vehicles manufactured by BMW is accumulated. A
default value of zero (`0`) is assigned to the `bmw_count` variable. The variable is utilized to
accumulate a count of the number of nested lists that represent EVs produced by BMW.

:bulb: Note use of the "assignment addition" operator `+=` to _increment_ the count. The expression
`bmw_count += 1` is the equivalent to `bmw_count = bmw_count + 1`, an example of Python
"syntatic sugar" that I encourage you to use.

```python
bmw_count = 0
for vehicle in ev_vehicles:
    if "bmw" in vehicle[0].lower():
        bmw_count += 1 # assignment addition equivalent to bmw_count = bmw_count + 1
```

:bulb You can also perform "assignment subtraction using the `-=` operator to _decrement_ a count.

### 2.4 Challenge 04

__Task__: Return a count of the number of EVs in `ev_vehicles` with a range
greater than or equal to 250 miles.

1. Assign zero (`0`) to a variable named `vehicle_count`.

2. Implement a `for` loop and a conditional `if` statement to identify vehicles with a range
   _greater than or equal to_ 250 miles.

   :exclamation: Exclude the first "headers" element in `ev_vehicles`.

   :bulb: Conditional statements often compare two values using the following comparison operators.
   The return value of such expressions is either `True` or
   `False`.

   | Operator | Description              |
   | :------- | :----------------------- |
   | `==`     | equal                    |
   | `!=`     | not equal                |
   | `>`      | greater than             |
   | `<`      | less than                |
   | `>=`     | greater than or equal to |
   | `<=`     | less than or equal to    |

3. If the conditional statement evaluates to `True` increment `vehicle_count` by one (`1`).

4. Uncomment the built-in function `print()` and check your work.

## 3.0 Looping with the `range` type

Although the Python official documentation includes `range()` in its table of
[built-in functions](https://docs.python.org/3/library/functions.html), the
[`range`](https://docs.python.org/3/library/stdtypes.html#typesseq-range) object is
actually an immutable sequence type like a `list` or a `tuple`.

The `range` object is employed to generate an _immutable_ sequence of numbers. The default behavior
starts the sequence at zero `0` and then increments by 1 up to but _excluding_ the specified stop
value passed to the object as an argument. Optional `start` and `step` arguments can be passed to
`range()` including negative step values that reverse the sequence.

```commandline
range([start,] stop[, step])
```

### 3.1 `range` behaviors

You can observe how the `range` object behaves by converting the sequence it generates to a list by
passing it to the built-in `list()` function.

```python
seq = range(10) # instantiate the range object with a stop argument of 10

seq = list(range(10)) # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

seq = list(range(5, 10)) # returns [5, 6, 7, 8, 9]

seq = list(range(5, 21, 5)) # returns [5, 10, 15, 20]

seq = list(range(20, 4, -5)) # returns [20, 15, 10, 5]
```

### 3.2 The `for` loop and `range`

You can use the `range` object to specify the maximum number of `for` loop iterations. In the
following looping example, the expression `range(5)` returns the numeric sequence `0, 1, 2, 3, 4`.
Consequently, the built-in function `print()` is called a total of five (5) times before the loop
terminates.

```python
for i in range(5):
    print("I want an EV!")
```

You can also pass the built-in function `len(< sequence >)` to `range` in a `for` loop in order to
limit the number of loop iterations to the length of the list. Doing so aligns the numeric sequence
returned by `range` (`0, 1, 2, ...`) to the index values of the list elements.

```python
automakers = [
    "Bayerische Motoren Werke AG",
    "Ford Motor Co.",
    "General Motors Co.",
    "Kandi Technologies Group",
    "Nissan Motor Co.",
    "Volkswagen AG",
    "Volvo Group",
    "Tesla, Inc."
    ]

for i in range(len(automakers)):
    print(f"{i} {automakers[i]}")
```

:exclamation: Note that the above `for` loop __does not__ loop over `automakers`; it loops over the
sequence of numbers generated by `range`. Inside the loop block each number (referenced by the
variable `i`) is utilized as an index to access each element in `automakers` by position.

### 3.3 Employing `range` to replace list elements

If you need to replace a list element with another value utilize a `for i in range():` loop to
accomplish the task. Employing a regular `for` loop to perform the assignment will not change the
underlying element, it only repoints the loop variable to the new value _leaving the underlying
element unchanged_:

```python
for automaker in automakers:
    automaker = automaker.upper() # assigns new string to loop variable only

# List elements are unchanged
# [
#     "Bayerische Motoren Werke AG",
#     "Ford Motor Co.",
#     "General Motors Co.",
#     ...
# ]
```

Looping over the numeric sequence generated by `range` permits one to reference each targeted list
element by its index. The assignment of a new value can then be performed successfully.

```python
for i in range(len(automakers)):
    automakers[i] = automakers[i].upper() # assigns new string to element
```

If you need to target select elements for modification you can pass `start` and `step` values to
`range` as in the following example:

```python
# Modify every third element commencing from index 0
for i in range(0, len(automakers), 3):
    automakers[i] = automakers[i].lower() # assigns new string element
```

### 3.4 Chaining subscript operators

Accessing nested list attributes by position is achieved using subscript operator chaining.
Obtaining the Tesla Model 3 AWD EV's range value from the `ev_vehicles` list is achieved by first
accessing the nested list by its index position (`-1`) and then accessing the vehicle's
range value by its index position (`4`) in a "chained" expression.

```python
# ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
# ["Tesla Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],

tesla_3_range = ev_vehicles[-1][4]
```

In the next example, subscript operator chaining relies on the loop variable `i` (an integer) to
access each nested electric vehicle list in `ev_vehicles`:

```python
tesla_s_range = 0
for i in range(len(ev_vehicles)):
    if ev_vehicles[i][0].lower() == "tesla model s":
        tesla_s_range = ev_vehicles[i][4]
```

:exclamation: In line with method chaining each chained expression employing the subscript operator
(`[]`) resolves to a value. Be mindful when calling a method on the value, you can trigger an
`AttributeError` if you lose track of the value's type and call a method not possessed by the type.

### 3.5 Challenge 05

__Task__: Use a `for` loop, `range`, the built-in function `len()`, and subscript operator chaining
to replace the vehicle type "SUV" with "Sports Utility Vehicle".

1. Utilize `range` to loop over a sequence of numbers keyed to the number of elements in
   `ev_vehicles`.

2. Inside the `for` loop, implement an `if` statement that evaluates whether or not a vehicle is
   categorized as an SUV (i.e., a Sports Utility Vehicle).

3. If the vehicle is an SUV, employ subscript operator chaining to replace the vehicle's "SUV"
   string with the string "Sports Utility Vehicle".

   Below is an example of a modified vehicle list:

   ```python
   ["BMW iX M60", "Sports Utility Vehicle", "AWD", "78", "288", "111", "5", "$108,900"]
   ```

4. Uncomment the built-in function `print()` and check your work.

## 4.0 `if-else` conditions

Execution of an `if` statement's indented code block occurs _only_ if the condition to be tested
evaluates to `True`. If `False` is returned and a need exists to execute other statements in
response an `else` statement can be added togetther with an indented code block.

```commandline
if < condition >:
    < statement A >
    # ...
else:
    < statement B >
    # ...
```

The `if-else` block below evaluates an EV's "type"; if the EV is classified as a "Sedan/Wagon" a
string representation of the vehicle is appended to the list `sedan_wagon`. Otherwise, string
representations of all other EV types encountered are appended to the list `suv_pickup`.

:bulb: the "headers" element is excluded from the loop.

```python
sedan_wagon = []
suv_pickup = []
for vehicle in ev_vehicles[1:]:
    string = f"{vehicle[0]} ({vehicle[1]})"
    if vehicle[1] == "Sedan/Wagon":
        sedan_wagon.append(string)
    else:
        suv_pickup.append(string)
```

A second example illustrates how to check if a value exists between a range of values. Assume that
the automotive industry considers an EV battery range between 225-325 mpge (inclusive) as a
"standard" range. Any EV battery ranges that fall on either side of the standard range are
considered outliers. You can determine the number of standard and outlier EV ranges in `ev_vehicles`
by implementing the following `if-else` statements:

```python
standard_ranges = []
outlier_ranges = []
for vehicle in ev_vehicles[1:]:
    string = f"{vehicle[0]} (range = {vehicle[4]} mi)"
    if 225 <= int(vehicle[4]) <= 325:
        standard_ranges.append(string)
    else:
        outlier_ranges.append(string)
```

:bulb: The conditional statement above includes the expression `225 <= int(vehicle[4]) <= 325`. The
expression evaluates whether or not a given EV battery range falls between __between__ 225 and 325
mpge (inclusive) with "inclusive" being interpreted as including the values 225 and 325 together
with all other values between the minimum and maximum values (or lower and upper bounds).

If the minimum and/or maximum values are considered _exclusive_ (i.e., outside the range of
values under consideration) use the less than or equal to (`<`) or greater than or equal to (`>`)
comparison operators in the expression.

### 4.1 Challenge 06

__Task__: Return counts of domestic and foreign designed EVs.

Assume that EVs are designed (though not necessarily manufactured) in the automaker's country of
origin. For this challenge you will employ the `us_automakers` list as a filter that permits you
to distinguish between US and foreign automakers.

```python
us_automakers = [
    "Cadillac",
    "Chevrolet",
    "Ford",
    "Lucid",
    "Polestar Automotive USA",
    "Rivian",
    "Tesla",
]
```

Each nested vehicle list in `ev_vehicles` has been restructured:

```python
ev_vehicles = [
    ["manufacturer", "model", "type", "range_mi", "base_msrp"],
    ["Tesla", "Model 3 RWD", "Sedan/Wagon", "272", "$46,990"],
    ["Porsche", "Taycan GTS Sport Turismo", "Sedan/Wagon", "233", "$86,700"],
    ...,
]
```

1. Assign zero (`0`) to two variables named `domestic_count` and `foreign_count` respectively.

2. Loop over the slice of `ev_vehicles` that __excludes__ the first nested list element (the
   "headers").

3. Implement `if-else` statements that increment the counts assigned to `domestic_count` and
   `foreign_count`.

   1. If in the `if` statement utilize the membership operator `in` to test whether or not an EV
      manufacturer is considered a US automaker (i.e., a member of `us_automakers`).

   2. If the membership check evaluates to `True` increment the `domestic_count` by one (`1`).

   3. Otherwise, increment the `foreign_count` by one (`1`).

4. Uncomment `print()` and check your work.

### 4.2 Challenge 07

__Task__: Assume a budget of $50,000.00 (USD) determines which electric vehicles are affordable
and which are considered unaffordable for the average consumer. Produce two lists of strings that
represent the two groups of vehicles.

1. Create two empty "accumulation" lists named `affordable` and `unaffordable`.

2. Utilize `range` to loop over a sequence of numbers keyed to the number of elements in
   `ev_vehicles`.

   :exclamation: Set the `range()` _start_ value to one (`1`) in order to avoid accessing the first
   "headers" element in the list.

3. Inside the loop block, convert the electric vehicle's "base_msrp" (manufacturer's suggested
   retail price) string value to an __integer__ (`int`) using subscript operator chaining to access
   the nested list element. Assign the integer value to a variable inside the `for` loop block.

   :exclamation: Recall that your code is looping over a sequence of numbers __not__ `ev_vehicles`.
   Utilize the loop variable `i` to access each nested vehicle list in `ev_vehicles`.

   :bulb: Utilize the built-in function `int()` to perform the conversion. Note that you need to
   pass to `int()` a version of the "bas_msrp" string that excludes both the currency symbol and any
   commas. Employ a handy `str` method to eliminate the characters in the new string that you
   produce.

4. Inside the loop block, create an f-string representation of the electric vehicle formatted as
   follows:

   ```python
   f"< manufacturer > < model > (Base MSRP = $< base_msrp >)"

   # Example: "Chevrolet Bolt EV (Base MSRP = $25,600)"
   ```

   Access the required vehicle elements embedded in the f-string using subscript operator chaining.
   Assign the formatted string literal (f-string) to a variable inside the loop block.

5. Implement `if-else` statements that populate the `affordable` and `unaffordable` lists with
   string representations of electric vehicles.

   If a vehicle's "base_msrp" is less than or equal to $50,000.00 (USD) add the string
   representation of the vehicle to the `affordable` list. Otherwise, add the string
   representation of the vehicle to the `unaffordable` list.

6. Uncomment the two `print()` functions and check your work.
