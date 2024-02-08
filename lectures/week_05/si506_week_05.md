# SI 506 Week 05

## Topics

1. Additional control flow statements
   1. `break` statement
   2. `continue` statement
2. Indefinite iteration: `while` loop
   1. Infinite loops
   2. `while` loop `else` condition
   3. `while` loop and conditional statements
   4. `while` loop and the `range` type
   5. Challenge 01
   6. Challenge 02
3. Built-in `input()` function
4. `if-elif-else` statements
   1. Challenge 03
5. Compound conditional statements
   1. Working with `None` or blank values
   2. Handling ties when counting
   3. Logical `and` operator
   4. Challenge 04
   5. Logical `or` operator
   6. Logical `not` operator
   7. Grouping related expressions
   8. Challenge 05

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

This week's lecture data was retrieved by accessing the US Department of Energy's
[National Renewable Energy Laboratory](https://www.nrel.gov/) (NREL)
[API](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/)
(Application Programming Interface). This involved utilizing the third-party Python
[Requests](https://requests.readthedocs.io/en/latest/) library to issue an HTTP GET request to
retrieve information about electric vehicle (EV) charging stations located in Ann Arbor and
Ypsilanti, Michigan.

Below is a description of the data retrieved for this week's lectures. Note that the data represents a
curated selection of information that can be sourced from the NREL's API.

| Column | Description |
|:-------|:------------|
| id                      | Unique identifer assigned to a station |
| station_name            | The name of the station |
| facility_type           | Facility type |
| access_code             | A description of who is allowed to access the station. |
| access_days_time        | Hours of operation |
| restricted_access       | For public stations, an indication of whether the station has restricted access, given as a boolean. |
| city                    | Municipality in which the station is located. |
| zip                     | The ZIP code (postal code) of the station's location. |
| street_address          | The street address of the station's location. |
| intersection_directions | Brief additional information about how to locate the station. |
| ev_network              | Network that maintains the station. |
| ev_connector_types      | Connector type(s) available at the station. |
| ev_dc_fast_num          | The number of DC Fast EVSE ports. |
| ev_level1_evse_num      | The number of Level 1 EVSE ports. |
| ev_level2_evse_num      | The number of Level 2 EVSE ports. |
| ev_other_evse           | The number and type of additional EVSE ports. |
| ev_pricing              | Pricing details. |
| date_last_confirmed     | The date the station's details were last confirmed. |

## 1.0 `break` and `continue` statements

You can interrupt control flow inside a loop using the `break` and `continue` statements.

### 1.1 `break` statement

The `break` statement is employed in a `for` loop to exit the loop and proceed to the next statement
in the code. Any statements _inside_ the loop that follow the `break` statement will be ignored. The
break statement is usually triggered by a specified condition. Using a `break` statement prevents
unnecessary looping and can result in performance gains if the sequence being looped over is large.

For example, if you need to confirm that the data set includes Ypsilanti EV station data, the
following loop would provide you with the answer:

```python
has_ypsi = False
for station in station_data[1:]:
    if station[6].lower() == 'ypsilanti':
        has_ypsi = True
        break # exit loop
```

:bulb: Consider leveraging the "headers" list to look up the city column's index value by replacing
the hard-coded subscript operator index value with the expression `headers.index('city'):`

```python
headers = station_data[0] # column headers

has_ypsi = False
for station in station_data[1:]:
    if station[headers.index('city')].lower() == 'ypsilanti':
        has_ypsi = True
        break # exit loop
```

### 1.2 `continue` statement

The `continue` statement is employed in a `for` loop to terminate the _current_ loop iteration and
proceed directly to the next iteration in the loop (if any), skipping any trailing statements.

In the example below, the goal is to return a list of electric vehicles that represent "outliers" in
terms of city driving battery range. If a vehicle's range is between 225 miles and 325 miles
(exclusive) the `continue` statement is executed and the trailing `list.append()` operation is
skipped. Only vehicles with a city range that falls on either side of the 225 - 325 mile range are
added to the `outliers` list.

:bulb: Use comparison operators arranged as `x < y < z` or `x <= y <= z` to test if a value
(typically a number but also a letter) is _between_ two values. The expression returns either
`True` or `False`.

```python
outliers = []
for vehicle in elec_vehicles[1:]:
    vehicle_range = int(vehicle[4]) # Do not name the var range (shadows the range() type)
    if 225 < vehicle_range < 325:
        continue # proceed to next iteration (skip)
    outliers.append(f"{vehicle[0]} {vehicle[1]} (range = {vehicle_range} mpge")
```

## 2.0 Indefinite iteration: the `while` loop

The `while` loop repeats a set of one or more statements _indefinitely_; that is, until a condition
is imposed that evaluates to `False` and terminates the loop.

```commandline
while < expression >:
    < statement A >
    < statement B >
```

In the example below, a counter `i` is initialized with a default value of zero (`0`). The `while`
loop, once initiated, will continue to iterate over the loop block _indefinitely_ until the
expression `i < 5` returns `False`. Note that the only way to terminate the looping operation is
to increment the counter value by `1` _inside the loop block.

```python
i = 0
while i < 5:
    print(i)
    i += 1 # increment (addition assignment operator)
```

If you wanted to know how many ChargePoint Network stations are in `station_data` you could
return a count by implementing the accumulator pattern using a `for` loop and "counter" variable:

```python
chargepoint_count = 0
for station in station_data[1:]:
    if station[headers.index('ev_network')].lower() == 'chargepoint network':
        chargepoint_count += 1
```

You could reimplement the task employing a `while` loop:

```python
chargepoint_count = 0
i = 1 # skip the header list
while i < len(station_data):
    if station_data[i][headers.index('ev_network')].lower() == 'chargepoint network':
        chargepoint_count += 1
    i += 1 # increment
```

:bulb: In the above example opting for _indefinite_ iteration (the `while` loop) adds unnecessary
complexity to the solution. The choice also risks triggering an infinite loop if the counter `i` is
not incremented correctly. In short, approach the `while` loop _with caution_.

### 2.1 Infinite loops

If a `while` loop is implemented incorrectly it will trigger an _infinite loop_, a runaway process
that, over time, will consume ever greater memory resources to the detriment of your both your
operatings system and hardware (you will hear the fans kick on as the laptop's internal
temperature rises). Eventually, your system will crash unless you kill the process.

Typically, a `while` loop is implemented when the number of required iterations is unknown. There
are other use cases, one of which we will explore below.

The following example is guaranteed to trigger an infinite loop since the `while` condition remains
`True` indefinitely:

```python
while True:
    print("infinite loop triggered") # Don't do this
```

You can tame a `while` loop condition initialized to `True` by adding a conditional statement that
includes a `break` statement in the loop code block.

```python
i = 0
while True:
    print('infinite loop triggered')
    if i == 5:
        print('infinite loop terminated\n')
        break # exit the loop
    i += 1 # increment (note indention)
```

:exclamation: if you trigger an infinite loop while running your module in VS Code click the
terminal pane's trash can icon in order to kill the session and end the runaway process.

### 2.2 `while` loop `else` condition

The `while` loop includes a built-in `else` condition that you can use to execute one or more
statements after the loop terminates.

```python
i = 0
while i < 5:
    print('I want an EV.')
    i += 1 # increment
else:
    print('Enough said. We believe you.')
```

### 2.3 `while` loop and conditional statements

You can employ conditional statements inside a `while` loop in order to determine the control flow
of each iteration. In the following example the modulus (`%`) operator is used to identify even and
odd numbers between 0 and 10.

:bulb: use the modulus operator to return the remainder after one number is divided by another. If
the remainder equals zero the number evaluated is an even number.

```python
i = 0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i += 1 # increment
```

You can also count in reverse ("countdown") by decrementing the counter `i` using the subtraction
assignment (`-=`) operator:

```python
i = 10
while i >= 0:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    i -= 1 # decrement
```

### 2.4 `while` loop and the `range` type

You can employ a `while` loop in conjunction with the `range` type to loop over a sequence of
numbers. In the example below the `while` loop iterates over the sequence `0, 2, 4, 6, 8` provided
by `range(0, 10, 2)`.

:exclamation: note that `i` is incremented by 2 not 1.

```python
i = 0
while i in range(0, 10, 2):
    print(f"{i} is an even number.")
    i += 2 # increment by 2
```

### 2.5 Challenge 01

__Task__: The "ev_connector_types" value is, in certain cases, a list masquerading as a string
(e.g., `'CHADEMO, J1772COMBO'`). Convert this value to a list for all stations in the `station_data`
list.

1. Uncomment the partially implemented `while` loop.

2. Pass arguments to the `range` type to return an instance of `range` that comprises a sequence of
   numbers that starts with (`1`) and ends with a number that is one less than the length of the
   `station_data` slice that excludes the "headers" list element.

   :bulb: Don't let the clause "one less than the length ..." mislead you when passing araguments to
   `range()`.

3. Inside the `while` loop call the appropriate string method to convert each station's
   "ev_connector_type" string value to a list:

   `'CHADEMO, J1772COMBO'` -> `['CHADEMO', 'J1772COMBO']`

   Assign the new list "back" to the "ev_connector_types" element.

   :bulb: Note how the nested list's "ev_connector_types" element is referenced using subscript
   operator chaining.

4. Inside the `while` loop block increment the variable `i` by one (`1`).

   :exclamation: In order to avoid triggering an infinite loop you _must_ increment the counter `i`
   inside the loop.

5. Uncomment `print()` and check your work.

### 2.6 Challenge 02

__Task__: Return the index value of the first nested list in `station_data` that represents a
station located in Ypsilanti, Michigan.

1. Uncomment the partially implemented `while` loop.

2. Pass arguments to the `range` type to to traverse a sequence of numbers starting
   with the number one (`1`). Sync the `stop` value to the length of the `station_data` list.

3. Inside the `while` loop write an `if` statement that tests two strings for __equality__. The
   comparison to be performed _must_ be __case insensitive__ and the values to compare are the
   current station's "city" value and the string "ypsilanti".

   :exclamation: Accessing the each `station_data` nested list's "city" value will require subscript
   operator chaining.

   :bulb: Employ the `headers` list to look up the "city" index rather than hard coding the index
   in the subscript operator.

4. If a match is obtained call the appropriate list method _inside_ the `if` statement block to
   return the __index__ of the nested list that represents the __first__ Ypsilanti station
   encountered in `station_data`. Assign the value to a variable name of your own choosing
   (e.g.,  `first_ypsi_station_idx`).

5. Inside the `if` statement block include a control flow statement that terminates the `while` loop
   whenever it is encountered.

6. Uncomment `print()` and check your work.

   ```python
    # First Ypsilanti station in list (return its index value)
    [
        '145371', 'Roundtree Place', None, 'public', '24 hours daily', None, 'Ypsilanti', '48197', '2539 Ellsworth Rd', None, 'Electrify America', 'CHADEMO, J1772COMBO', '6', None, None, None, None, '2022-09-07'
    ]
   ```

## 3.0 Built-in `input()` function

The built-in `input()` function accepts user-supplied strings from the command prompt. It is often
positioned inside a `while` loop in order to process user input. The pattern is illustrated in the
following example.

In the code below, the built-in function `input()` prompts the user for a street name. The
function call is placed inside a `while` loop in order to query the user continuously until a
a street name found in the `streets` list is provided.

The `if` statement performs a _case sensitive_ membership check. If a match is obtained the boolean
`True` is assigned to the variable `is_found`. If an exact match is not obtained (e.g., Ann Street
`!=` W Ann St), the `else` statement block provides for _case insensitive_ partial matching (e.g.,
"Ann" `in` "W Ann St). If a partial match is obtained, the boolean `True` is assigned to the
variable `is_found`.

The `break` statement is then employed to exit the `streets` loop.

Thereafter, if `is_found` resolves to `True` the built-in function `print()` is called and passed
the "SUCCESS" string. A second `break` statement is added to exit the `while` loop.  If `is_found`
remains `False` the built-in function `print()` is called and passed the "FAIL" string. The `while`
loop proceeds to the next iteration of the loop and the user is again prompted to provide a street
name.

:bulb: The variable `is_found` is key to the design of the example `while` loop. The conditional
logic inside the `while` loop requires a way to signal that a match has been obtained and that both
the inner `streets` loop and outer `while` loop can be exited. The `is_found` _truth value test_
(i.e., `if is_found:`) also eliminates the need to duplicate "SUCCESS" calls to the built-in
function `print()`. This is an illustration of the
[DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) in action.

```python
streets = (
    'Ann Arbor-Saline Rd',
    'Auto Mall Dr',
    'Boardwalk Dr',
    'Broadway St',
    ...
    'W Ann St',
    'W Liberty Rd',
    'W Washington',
    'W William St'
    )

while True:
    is_found = False
    entry = input('\nProvide street name: ')

    # Attempt to obtain an exact match; otherwise attempt to obtain a partial match
    if entry in streets:
        is_found = True # exact match obtained;
    else:
        for street in streets:
            if entry.lower() in street.lower():
                is_found = True
                break # partial match obtained, exit streets loop

    if is_found: # truth value test
        print(f"\nSUCCESS: One or more EV charging stations found on the provided street.")
        break # exit while loop

    print(f"\nFAIL: No EV charging stations found on provided street. Provide a different street name.")
```

## 4.0 `if-elif-else` conditions

Multiple conditions can be specified by including one or more `elif` conditions in between
an `if-else` block. The `if-elif-else` statement chain or ladder is executed from the top downwards.

```python
if < condition >:
    # < statement A >
    # ...
elif < condition >:
    < statement B >
    # ...
elif < condition >:
    < statement C >
    # ...
else:
    < statement D >
    # ...
```

The `else` statement is _optional_ but recommended, especially for new programmers, in order to
render explicit the conditional logic to be evaluated. You can also nest `if-elif-else` statement
blocks. We will explore nested conditional statements during a later lecture.

Note the use of three `elif` statements in the `while` loop below to check for specific
EV networks:

```python
# Simplify working with the data
headers = station_data[0]
stations = station_data[1:]

# Use in subscript notation below
ev_network_idx = headers.index('ev_network')

# Accumulate counts of the connector types
chargepoint_count = 0
elec_america_count = 0
ev_connect_count = 0
evgo_count = 0
greenlots_count = 0

for station in stations:
    if station[ev_network_idx].lower() == 'chargepoint network':
        chargepoint_count += 1
    elif station[ev_network_idx].lower() == 'electrify america':
        elec_america_count += 1
    elif station[ev_network_idx].lower() == 'ev connect':
        ev_connect_count += 1
    elif station[ev_network_idx].lower() == 'evgo network':
        evgo_count += 1
    elif station[ev_network_idx].lower() == 'greenlots':
        greenlots_count += 1
    else:
        continue # explicit but optional
```

### 4.1 Challenge 03

__Task__. Employ `if-elif-else` conditional statements to populate four "last_confirmed" annual
lists with station identifiers.

1. Uncomment the partially implemented `for` loop.

2. Inside the loop block employ subscript operator chaining to

   1. access the nested list element (a charging station) in `stations` whose index corresponds to
      `i`

   2. and access the station's "date_last_confirmed" value (i.e., the last element in the nested
      list).

   Assign the string to a variable named `last_confirmed`.

3. Implement `if-elif-else` conditional statements that check the year (`YYYY`) in which the
   station data was last confirmed. Use the accumulator lists to accumulate station identifiers
   ("id") based on the station's "date_last_confirmed" year value.

   :bulb: The `last_confirmed` date is a string formatted as follows: `YYYY-MM-DD` (e.g.,
   "2021-07-14").

   __Conditional statements__

   1. If a station's data was last confirmed in 2020, append its "id" value to the
      `last_confirmed_2020` list.

      :bulb: The "id" value is the first element in the nested charging station list.

   2. Utilize the `elif` statements to accumulate charging station ids for the years 2021 and 2022.

   3. Otherwise, if a station's data falls on either side of the years 2020-2022 append its "id"
      value to the `last_confirmed_other` list.

4. Uncomment the calls to `print()` and `pp.print()` and check your work.

   For example, after you run your code the `last_confirmed_2021` list _must_ contain the following
   ids:

   ```python
   ['42726', '44282', '44283', '44284', '44285', '44286', '102221', '184715', '184845', '184846', '198009']
   ```

## 5.0 Compound conditional statements (comparing values using logical operators)

Recall that the expression which comprises an `if` statement returns either `True` or `False`.

You can combine conditions and compare values in a single `if` statement using the logical
operators `and` (conjunction), `or` (disjunction) and `not` (negation), either singly or together
in various combinations, as occurs in Boolean algebra.

:exclamation: When crafting a compound `if` statement you _must_ specify each condition in its
entirety.

For example the following compound `if` statement triggers a runtime exception:

```commandline
>>> x = 5
>>> x > 2 and < 10
  File "<stdin>", line 1
    x > 2 and < 10
              ^
SyntaxError: invalid syntax
```

The compound `if` statement _must_ be written as follows:

```command line
>>> x = 5
>>> x > 2 and x < 10
True
```

Or better yet (in this case):

```commandline
>>> x = 5
>>> 2 < x < 10
True
```

For example, if you want to check whether or not a charging station was equipped with between `2`
and `4` (inclusive) EVSE units, you should consider carefully how you craft
your compound `if` statement lest you trigger a runtime exception.

### 5.1 Working with None or blank values

Note that some "columns" in the data set include `None` values. The presence of `None` or blank
(`''`) values is problematic. Their presence requires that we tread carefully when calling either
object methods (e.g., `str.split()`) or built-in functions (e.g., calling `int()` to cast a string
to integer) as either operation can trigger a runtime exception.

The code below provides a couple of approaches for dealing with `None` values encountered when
checking a station's Level 2 Electric vehicle supply equipment (EVSE).

A quick check confirms the presence of `None` values:

```python
level2_evse_idx = headers.index('ev_level2_evse_num') # lookup index value
ev_level2_evse_num_vals = []
for station in stations:
    if station[level2_evse_idx] not in ev_level2_evse_num_vals:
        ev_level2_evse_num_vals.append(station[level2_evse_idx])
```

Two approaches are available to check for the presence of `None`:

* Employ the identity operators `is` or `is not`.
* Truth value test (discussed in depth next week)

```python
station_evse = []

# INCORRECT SYNTAX
for station in stations:
    # if statement will trigger SyntaxError: invalid syntax
    if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

# CORRECT SYNTAX
for station in stations:
    if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

# PYTHONIC (INCLUDES TRUTH VALUE TEST)
station_evse.clear() # delete elements (avoid duplication)
for station in stations:
    if station[level2_evse_idx] and 2 <= int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")
```

### 5.2 Handling ties when counting

Below is another example of how to avoid triggering runtime exceptions when inadvertantly calling object methods on `None`.

Let's say you need to return station locations featuring the highest number of Level 2 EVSEs. You should assume that multiple locations could meet this requirement. In other words, you need to account for the possibility that ties exist in the data. In addition, stations that lack information on Level 2 EVSEs return a value of `None` so you must
adopt a defensive coding strategy to avoid triggering a runtime exception if you attempt (inadvertently) to operate on a `None` value.

The code satisfies both concerns. During each iteration of the loop the following actions occur:

* If `station[level2_evse_idx]` resolves to `None` the `continue` statement is invoked and the `for` loop proceeds immediately to next loop iteration.

* Otherwise, the `station[level2_evse_idx]` is converted to an integer
  and compared to the previous `evse_count` value.

* If `num` is greater than `evse_count` a new "leader" has been detected
  and the `evse_count` is assigned `num` and any previous stations appended to the `most_evse` list are removed by calling the `list.clear()` method. The new "leader" is then appended to the list.

* However if `num` is equal to the previous `evse_count` value a tie has been detected. In this case, the current station is appended to the `most_evse` list joining the previous leader(s).

```python
most_evse = []
evse_count = 0
for station in stations:
    if station[level2_evse_idx] is None:
        continue # proceed to next station
    num = int(station[level2_evse_idx])
    if num > evse_count:
        evse_count = num # new
        most_evse.clear() # clear previous leader(s)
        most_evse.append(station) # new leader
    elif num == evse_count:
        most_evse.append(station) # tie
    else:
        continue # explicit but optional
```

### 5.3 Logical `and` operator

The logical `and` operator combines two or more conditions in a single boolean expression. _All_
conditions comprising the expression _must_ evaluate to `True` for the expression to evaluates to
`True`; otherwise the expression evaluates to `False`.

```commandline
< condition > and < condition > [and ...]

>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
```

The U-M campus hosts a number of charging stations. The example below employs a `while` loop to
return a count of U-M EV charging stations. Note use of the `list.index()` method to look up the
index value associated with the "station_name" header value.

```python
name_idx = headers.index('station_name')
um_count = 0
i = 0
while i < len(stations):
    if stations[i][name_idx].startswith('U-M'):
        um_count += 1
    i += 1
```

If you needed to filter the U-M EV charging stations by a particular zip code (say, `48104`) you
could do so by writing a compound `if` statement that employs the logical `and` operator to join the
two conditions.

```python
zip_idx = headers.index('zip')
um_count_48104 = 0
i = 0
while i < len(stations):
    if stations[i][name_idx].startswith('U-M') and int(stations[i][zip_idx]) == 48104:
        um_count_48104 += 1
    i += 1
```

### 5.4 Challenge 04

__Task__. Employ a `for` loop to access a select subset of stations located on Wall Street.

1. Look up the index value of the `headers` element "street_address" by calling the appropriate list
   method. Assign the integer returned to the variable named `street_idx`.

2. Replace the `pass` statement in the loop block with a _compound_ `if` statement that filters on
   the following conditions:

   * U-M owned stations
   * "Wall St" locations

3. Add each nested charging station list that satisfies _both_ of the specified conditions to
   `um_stations_wall_st`.

4. Uncomment `print()` and `pp.pprint()` and check your work.

### 5.5 Logical `or` operator

The logical `or` operator combines two or more conditions in a single boolean expression. If _any_
condition comprising the expression evaluates to `True` the expression evaluates to `True`;
otherwise the expression evaluates to `False`.

```commandline
< condition > or < condition > [or ...]

>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
```

In the example below, we can accumulate stations owned by the Ann Arbor Downtown Development
Authority (A2DDA) by employing the logical `or` operator:

```python
a2dda_stations = []
for station in stations:
    name = station[name_idx]
    if name.startswith('A2DDA') or name.startswith('Ann Arbor Downtown Development Authority'):
        a2dda_stations.append(station[name_idx])
```

### 5.6 Logical `not` operator

The logical `not` operator reverses or negates a boolean expression. If the boolean expression
evaluates to `True` the inclusion of the logical `not` operator _reverses_ the value to `False`;
likewise if the boolean expression evaluates to `False` the inclusion of the logical `not` operator
_reverses_ the value to `True`.

:exclamation: note that the logical `not` operator reverses only the condition to which it is
paired. Reversing multiple conditions requires grouping the conditions with parentheses as
described below in the next section.

```commandline
not < condition >

>>> not True
False
>>> not True and True
False
>>> not True or True
True
>>> not True and False
False
>>> not True or False
False
>>> not False
True
>>> not False and True
True
>>> not False or True
True
>>> not False or False
True
```

Most of the stations in the `stations` list are part of the ChargePoint network. If you
needed to accumulate a count of stations that are either non-networked or a member of another
network you can employ the logical `not` operator to _reverse_ the booelan expression
returned by the expression contained in the following `if` statement.

```python
# Count EV stations that not part of the ChargePoint network
station_count = 0
for i in range(len(stations)):
    if not stations[i][ev_network_idx] == 'ChargePoint Network':
        station_count += 1
```

:bulb: One could argue that employing the comparison operator not equal (`!=`) instead of the
logical `not` operator provides a more readable expression:

```python
stations[i][ev_network_idx] != 'ChargePoint Network'
```

### 5.7 Grouping related expressions

You can employ parentheses `()` to group related conditions that comprise a boolean expression.
Pairing the logical `not` operator with a group will reverse the grouped conditions but not
conditions outside the group.

:exclamation: Logical operator precedences is `not`, then `and`, then `or`.

#### Examples

```commandline
< condition > and < condition > or < condition >
is equivalent to
(< condition > and < condition >) or < condition >

However

not < condition > and < condition > or < condition >
is equivalent to
not < condition > and (< condition > or < condition >)

>>> not False and False or False
False
>>> not False and (False or False)
False
```

If you needed to return a list of stations located in designated parking garages or parking lots
you could implement the following `while` loop:

```python
parking_facilities = []
i = 0
while i < len(stations):
    facility_type = stations[i][facility_type_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')):
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")
    i += 1
```

:bulb: Note the use of parentheses (`()`) surrounding the expressions comprising the `if` statement.
Their presence permits the `if` statement to be written across multiple lines in order to enhance
readability.

The compound `if` statement could be simplified by referencing the "facility_type" strings we wish
to target in a tuple. Instead of using a `while` loop we can instead loop over a sequence of numbers
supplied by the `range` type:

```python
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
for i in range(len(stations)):
    facility_type = stations[i][facility_type_idx]
    if facility_type is not None and facility_type.lower() in facility_types:
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")
```

If there was a need to restrict the results to stations open to the public the original `if`
statement can be amended by adding an additional condition using the logical `and` operator. This
time we will employ a standard `for` loop to perform the looping:

```python
parking_facilities = []
for station in stations:
    facility_type = station[facility_type_idx]
    access_code = station[access_code_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')
        and access_code.lower() == 'public'):
        parking_facilities.append(station)
```

:exclamation: Note that the compound statement groups the `or` conditions through the use of
parantheses (`()`) in order to ensure that the trailing `and` condition is evaluated correctly
given that the following conditions are not equivalent:

`(< expression > or < expression > or <expression >) and < expression > != < expression > or < expression > or <expression > and < expression >`

### 5.8 Challenge 05

__Task__. Create a list of all Ann Arbor Downtown Development Authority (A2DDA) stations located on
either Forest Ave or Maynard St.

1. Inside the loop block use the `name_idx` and `street_idx` index values to access the charging
   station's name and street values. Assign the values to the variables `name` and `street`.

2. Next, implement a compound conditional statement that enforces the following conditions:

   1. Station name is either "A2DDA" or "Ann Arbor Downtown Development Authority", and
   2. Station is located on either Forest Ave or Maynard St.

   <br />

   :bulb: Recall that both `name_idx` and `street_idx` index values are available and can be used
   to access each charging station's name and street values.

3. If the compound conditional statement evaluates to `True` the following formatted string will be
   appended to `a2dda_stations`:

   ```python
   f"{name} {station[street_idx]}"
   ```

4. Uncomment `print()` and check your work.
