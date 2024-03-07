# SI 506 Problem Set 06

## Exploring player and team shooting performance during the 2023 FIFA Women's World Cup

## 1.0 Overview

This problem set involves writing a small program/script that explores player and team shooting
performance during the 2023 FIFA Women's World Cup ⚽ hosted by Australia 🇦🇺 and New Zealand 🇳🇿.
Thirty-two (`32`) teams competed in the tournament with Spain 🇪🇸 emerging as the champion.

## 2.0 Data

The data was sourced from [FBREF](https://fbref.com/en/). Before commencing the challenges, review
the data file. Note how the data is structured. Examine the
"headers" row.

:exclamation: Place the data file in the same directory as the README and template `*.py` file.

| File | Source | Description |
| :--- | :----- | :---------- |
| `data-2023-fifa_wwc-players.csv` | [FBREF](https://fbref.com/en/comps/106/shooting/Womens-World-Cup-Stats) | Player Shooting 2023 FIFA Women's World Cup. |

## 3.0 Black Formatter

Format your code submissions using VS Code's Black Formatter extension. Change Black's
`line-length` setting from 88 to 100 characters and add the `experimental-string-processing`
setting. See VS Code [install guides](https://si506.org/guides/) for instructions if you have
yet to install the extension and update the settings.

## 4.0 Challenges

The problem set comprises nine (`9`) challenges. Your assignment
is to implement a small program/script that surfaces a number of insights regarding player and team
shooting performance during the 2023 Women's World Cup. The program features a number of functions
including a `main()` function that serves as the entry point to the program and orchestrator of the
program's work flow.

:exclamation: Team 506 recommends strongly that you complete each challenge in the order
specified in this README document.

### 4.1 Challenge 01 (10 points)

__Task__: Access data in a CSV file. Drop "columns" not required for this analysis. Access the
mutated "headers" element and mutated "players" elements and assign a variable to each.

1. In the `main()` function, instantiate an instance of `Path` by passing to it a string that
   represents the name of the data file (e.g., `"< file_name >.< file extension >"`). As you
   instantiate the `Path` object, call its `absolute()` _or_ `resolve()` method to render the path
   absolute. Assign a variable named `filepath` to the `Path` object.

2. Call the function `read_csv()` and pass it required argument `filepath`. Assign a variable
   named `data` to the return value.

3. Iterate over the `data` list and mutate each nested list by accessing a subset of the nested
   list's elements and assigning it "back" to the nested list. The subset of elements represents
   the "columns" required for this analysis.

   __Requirements__

   1. Employing a `for` loop and the loop variable `i` iterate over a sequence of integers provided
      by the `range` type. When instantiating (i.e., creating) the `range()` instance pass it the
      `data` list length as the __stop__ argument.

   2. Inside the loop block, mutate each nested list in `data` by "dropping" nested list elements
      not required for this analysis of player and team shooting performance. Retain only the first
      __ten (10) elements__ of each nested list. Create an expression that uses the subscript
      operator `[]` and a positive __slicing expression__ to access the target elements in the
      nested list. Assign the subset of elements "back" to the nested list (this requires subscript
      operator chaining).

      :bulb: Recall that you are iterating over a sequence of integers. Create a "chained"
      expression that accesses each nested list in `data` and then the subset of nested list's
      elements to retain. Assign the resulting new list "back" to the nested element as specified
      above.

   3. The loop block that you implement is limited to a __single line of code__.

4. After implementing the loop block uncomment the relevant `print()` calls and `assert` statements.
   Run your code. Confirm that the loop operation is mutating the nested lists in `data` correctly.

5. Assign a variable named `headers` to the "headers" element in `data`. Employ __slicing__ to
   access a subset of `data` that represents the "player" elements. Assign a variable
   named `players` to the slice.

### 4.2 Challenge 02 (25 points)

__Task__: Implement the functions named `format_player_position()` and `clean_squad()`.

1. Implement `format_player_position()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Requirements__

   1. Inside the function block call the appropriate `str` method that returns a new version of the
      passed in `position` string in which all commas (",") have been converted to pipes ("|").

   2. Return the new version of the string directly to the caller _without_ first assigning it to a
      local variable.

   3. The function block that you implement is limited to __a single line of code__.

   4. After implementing the function return to the `main()` function. Uncomment the relevant
      `assert` statements, run your code, and confirm that the function behaves as expected.

2. Implement `clean_squad()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. Inside the function block create a two-item tuple literal `(< item_01, item_02 >)` comprising
      the country code and squad/country name derived from the passed in `squad` string as the
      following examples illustrate.

      __Examples__

      | `squad` argument | 2-item tuple to return |
      | :--------------- | :----------- |
      | "es Spain" | `("ES", "Spain")` |
      | "ie Rep. of Ireland" | `("IE", "Rep. of Ireland")` |

   2. Employ slicing to access the two letter country code in the string. As part of the expression
      call the appropriate `str` method to return a version of the slice converted to __upper case__
      (e.g., "ES"). Embed the expression in the tuple literal as the first item.

   3. Also employ slicing to access the squad name (e.g., "Spain"). Embed the expression in the
      tuple literal as the second item.

   4. Return the tuple directly to the caller _without_ first assigning it to a local variable. In
      other words, the function block that you implement is limited to __a single line of code__.

   5. After implementing the function return to the `main()` function. Uncomment the relevant
      `assert` statements, run your code, and confirm that the function behaves as expected.

### 4.3 Challenge 03 (30 points)

__Task__: Loop over the `players` list, call the functions `format_player_position()` and
`clean_squad()`, and mutate each "player" nested list with the return values provided by the
functions. Mutate `headers` to ensure that its elements remains synchronized with the nested lists
in `players`.

1. In `main()` call the appropriate `list` method to lookup the index values for each of the
   following elements in the `headers` list:

   * "Pos" (position)
   * "Squad" (squad/country)

   Assign the variables named `pos_idx` and `squad_idx` to their respective return values.

2. Loop over the `players` list, mutate each nested list by assigning new "Pos", "Country_Code", and
   "Squad" elements as specified below.

   __Requirements__

   1. Employ a standard `for` loop. Choose a readable loop variable name (e.g., `player`) to
      represent each nested list.

   2. Inside the loop block call the function `format_player_position()` and pass it the nested
      list's "Pos" element as the argument, employing subscript notation (`[]`) and `pos_idx` to
      access the element. Assign the return value "back" to the nested list's "Pos" element, again
      employing subscription notation and `pos_idx` to identify the element.

   3. Next, call the function `clean_squad()` and pass it the nested list's "Squad" element as the
      argument, employing subscript notation (`[]`) and `squad_idx` in the expression to access the
      element. __Unpack__ the return value and assign the variables `code` and `squad` to the
      unpacked items.

   4. Next, call the appropriate `list` method to add `code` to the nested list in the
      __fourth position__. Use the `squad_idx` variable to identify the position.

   5. Next, assign `squad` to the nested list's "Squad" element (now in the __fifth__ position),
      employing subscript notation (`[]`) and the appropriate index (`squad_idx + ?`) in the
      expression on the left-hand side of the assignment operator (`=`) to assign the `squad` value
      to the "Squad" element".

      :bulb: You can utilize an arithmetic expression to compute a index value
      (i.e, `some_sequence[<an_arithmetic_expression>]`).

3. Outside the loop block call the appropriate `list` method to add the string "Country_Code" to the
   `headers` list in the __fourth position__. This ensures that the `headers` list remains
   synchronized with each `players` nested list as regards element order and list length.

4. Next, increment `squad_idx` by one (`1`) using __addition assignment__. This ensures that the
   value assigned to `squad_idx` reflects the new position of the "Squad" element in the `headers`
   list.

5. Call the function `write_csv()` and pass it the filepath "stu-players.csv" along with
   the other arguments it requires __by position__.

6. Run your code and confirm that the file was written to the current working directory. Then
   compare the CSV file to the matching fixture file (`fxt-*.csv`). If the files match proceed to
   the next challenge.

   :bulb: In VS Code you can compare or "diff" the file you generate against the appropriate test
   fixture file. After calling the `write_csv` function and generating a new file do the following:

   1. Hover over your `stu-*.csv` file with your cursor, then right click and choose the "Select for
      Compare" option.

   2. Next, hover over the appropriate `fxt-*.csv` test fixture file, then right click and choose
      the "Compare with Selected" option.

   3. Lines highlighted in red indicate row mismatches. If any mismatches are encountered close the
      comparison pane, revise your code, regenerate your file, and compare it again to the test
      fixture file. Repeat as necessary until the files match.

   :exclamation: Your output __must__ match the test fixture file line for line and character for
   character. Review the test fixture file; they are akin to answer keys and should be utilized for
   comparison purposes as you work your way through the assignment.

### 4.4 Challenge 04 (20 points)

__Task__: Implement the function named `get_multi_position_players()`. Retrieve players who play
multiple positions and write the data to a CSV file.

1. Implement `get_multi_position_players()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Requirements__

   1. In the function block implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list. Choose a readable
      loop variable name to represent each nested list.

   3. Inside the loop block, access each nested_list's "Pos" (i.e., position) element using the
      passed in `pos_idx` value. As part of the expression call the appropriate `str` method and
      pass to it the appropriate delimiter/separator value to split the string into a list. Assign
      a local variable to the return value (name your choice).

   4. Add an `if` statement that evaluates whether or not the "position" list includes multiple
      position elements (e.g., `["DF", "FW"]`). Perform an arithmetic comparison. If there are
      multiple elements in the "position" list __append__ the nested list representing the player to
      the accumulator list.

   5. After the loop terminates return the accumulator list to the caller.

2. Return to the `main()` function. Call the function `get_multi_position_players()` and pass it the
   appropriate arguments. Assign a variable named `multi_position_players` to the return value.

3. Call the function `write_csv()` and pass it the filepath "stu-players-multi_position.csv"
   along with the other arguments it requires __by position__.

4. Run your code and confirm that the file was written to the current working directory. Then
   compare the CSV file to the matching fixture file. If the files match proceed to the next
   challenge.

### 4.5 Challenge 05 (20 points)

__Task__: Implement the function named `get_team()`. Test the function by retrieving the Chinese
team and then write the team to a CSV file.

1. Implement `get_team()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function blook implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list. Choose a readable
      loop variable name to represent each nested list.

   3. Inside the loop block, add an `if` statement that evaluates whether or not the nested list's
      "Squad" element matches the passed in `squad` string. Perform a _case insensitive_ string
      comparison. If the strings match __append__ the nested list representing the player to the
      accumulator list.

      :bulb: Employ the subscript operator `[]` and the passed in `squad_idx` value to access the
      nested list's "Squad" element when constructing your `if` statement.

   4. After the loop terminates return the accumulator list to the caller.

2. Return to the `main()` function. Call the function `get_team()` and pass it the arguments
   required to return the Chinese women's national football team 🇨🇳. Assign a variable
   named `team_china` to the return value.

   :exclamation: Use VS Code's search feature to scan the `stu-players.csv` file for the Chinese
   team's "Squad" name to pass as an argument. The word "China" comprises only part of the name.
   Also use the `squad_idx` variable as an argument.

3. Call the function `write_csv()` and pass it the filepath "stu-team-china.csv" along with
   the other arguments it requires __by position__.

4. Run your code and confirm that the file was written to the current working directory. Then
   compare the CSV file to the matching fixture file. If the files match proceed to the next
   step.

### 4.6 Challenge 06 (20 points)

__Task__: Implement the function named `get_top_scorer()`. Retrieve the winner(s) of the ⚽ Golden
Boot award.

1. Implement `get_top_scorer()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function blook implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`. This list will hold the top scorer(s).  Also assign
      a local variable (name your choice) to an integer (choose an appropriate value) that will
      serve as the start value for the most goals scored count.

   2. Employ a standard `for` loop to iterate over the passed in `players` list.

   3. Inside the loop block retrieve each player's "Gls" (goals) element using the subscript
      operator `[]` and `gls_idx` in your expression. Assign a local variable (name
      your choice) to the expression (which resolves to a value).

   4. Don't assume that the "Gls" element's you retrieve is a number. Be prepared to
      convert it to an integer.

   5. After retrieving the player's goals scored value employ `if-elif-else` conditional logic to
      locate the top goal scorer(s). By now the pattern employed to identify either minimum or
      maximum values in a sequence as well as account for ties should be familiar to you.

   6. Whenever the accumulator list includes player elements that need to be replaced by a new
      leading scorer, adjust the __existing__ accumulator list. __Do not create a new list__.

   7. This challenge requires implementing a minor adjustment to the pattern. There are
      many World Cup players who did not score any goals during the tournament. The `if-elif-else`
      conditional logic must account for this possibility and filter out any players with a goal
      count of zero (`0`). Filtering out such players while continuing to evaluate those who scored
      one or more goals can be accomplished by implementing a __compound conditional statement__
      that employs the appropriate logical operator (e.g., `and`, `or`, `not`).

      :exclamation: Both your `if` and `elif` statements _must_ evaluate __two conditions__ using
      the appropriate logical operator (e.g., `and`, `or`, `not`). In other words, the conditional
      logic _must_ exclude players who did not score as well as identify players who scored the most
      goals during the tournament.

      __`if` statement conditions__

      * Did the player score at least one goal?
      * Is the player's goal count greater than the most goals scored count?

       If `True` update the most goals scored count, remove all players added previously to the
      accumulator list (without creating a new list), and then append the current player's nested
      list to the accumulator list. If `False` then evaluate the next condition.

      __`elif` statement conditions__

      * Did the player score at least one goal?
      * Is the player's goal count equal to the most goals scored count?

      If the equality comparison evaluates to `True` append the player's nested list to the
      accumulator list; otherwise, proceed to the next iteration of the loop.

   8. After the loop terminates return the top scorers list to the caller.

2. Return to the `main()` function. Call the appropriate `list` method to lookup the index value for
   the "Gls" (goals) element in the `headers` list. Assign the variables named `gls_idx` to the
   return value.

3. Call the function `get_top_scorer()` and pass it the arguments it requires to perform the
   computation.  Assign a variable named `top_scorers` to the return value.

4. Uncomment the `print()` call and run your code. If the object streamed to the terminal is a
   nested list that contains a list representation of the Japanese player Hinata Miyazawa 🇯🇵, winner
   of the 2023 Golden Boot Award (5 goals), then your function is behaving as expected.

### 4.7 Challenge 07 (30 points)

__Task__: Implement the function named `get_team_names()`. Retrieve a list of unique team names that
can serve double duty as country names. Then, identify each team's top scorer(s) and write the data
to a CSV file.

1. Implement `get_team_names()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function block implement the accumulator pattern. Assign a local variable
      (name your choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list.

   3. Inside the loop block, craft an `if` statement that allows you to accumulate a list of team
      names from `players` that contains __no duplicates__. In other words, append a nested list's
      "Squad" element to the accumulator list if, and only if, it has not been added previously.

      :bulb: Each nested list represents a player. Each player is associated with a
      squad/team/country (e.g., Australia). Given that each team can roster up to 23 players,
      duplicate "Squad" names exist throughout the `players` list.

   4. After the loop terminates return the list of team names to the caller.

2. Return to the `main()` function. Call the function `get_team_names()` and pass it the arguments
   required to return a list of unique team names. Since the team names correspond to country names
   assign a variable named `countries` to the return value.

3. Sort the `countries` list in ascending order, employing either the appropriate `list` method or
   appropriate built-in function.

   :bulb: The `list` method performs an in-place sort. It does not return a new list.

4. Uncomment the `print()` call and the `assert` statement. Run your code. Confirm that the function
   behaves as expected.

5. Still in the `main()` function, assign a variable named `team_top_scorers` to an empty list.

6. Next, implement a standard `for` loop that iterates over the `countries` list. Choose a readable
   loop variable name to represent each nested list.

7. Inside the loop block call the function `get_team()` and pass it the arguments it requires to
   return a nested list of players who competed for the current country. Assign a variable named
   `team` to the return value.

8. Also inside the loop block call the function `get_top_scorer()` and pass it the arguments it
   requires to return a nested list of the current country's top scorer(s). Assign a variable named
   `top_scorers` to the return value.

9. Once you have the team's top scorers call the appropriate `list` method to add `top_scorers`
   to the `team_top_scorers` list.

   :exclamation: Chose your `list` method call wisely. The mutated `team_top_scorers` list _must_
   match the following structure:

   ```python
   [[player_01], [player_02], [player_03], ...]
   ```

10. Call the function `write_csv()` and pass it the filepath "stu-team-top_scorers.csv" along with
   the other arguments it requires __by position__.

11. Run your code and confirm that the file was written to the current working directory. Then
   compare the CSV file to the matching fixture file. If the files match proceed to the next
   challenge.

### 4.8 Challenge 08 (35 points)

__Task__: Implement the function named `get_player_shooting_numbers()`.

1. Implement `get_player_shooting_numbers()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   :bulb: The shooting-related elements ⚽ are "Gls" (goals), "Sh" (shots), and "SoT" (shots on
   target). _Shots on target_ is defined as a shot taken that would have resulted in a
   goal if not blocked by the goalkeeper or another player considered the "last defender". Shots
   that strike the goal post or crossbar 🥅 are not considered a shot on target.

   __Requirements__

   1. Access the passed in `player` list's shooting-related elements using the subscript operator
      `[]` and the passed in `slice_` instance. Assign a local variable (name your choice) to the
      expression which resolves to a list comprising three (3) elements
      (i.e., the "shooting numbers").

      :bulb: The `slice` instance is passed to the function as an argument and bound to the
      parameter `slice_`. Use it as follows:

      ```python
      some_val = some_list[slice_]  # equivalent to some_sequence[8:11]

      # Implement loop
      ```

   2. Construct a `for` loop that iterates over a sequence of numbers whose length matches the
      length of the "shooting numbers" list. Access each element in the target list using the
      appropriate expression and __convert__ the element from a string to an integer. Assign the
      integer "back" to the list element.

   3. After the loop terminates return the "shooting numbers" list to the caller.

2. Return to the `main()` function. Uncomment the following variable assignment:

   ```python
   slice_ = slice(gls_idx, len(headers))  #  equivalent to slice(8, 11) or some_sequence[8:11]
   ```

   :bulb: This is an example of how to create a `slice` instance and then pass it to a function as
   an argument. Note that the stop value is set to the length of the `headers` list. This ensures
   that the last three (3) elements in the `player` list indexed 8, 9, and 10 are accessed.

3. Call the function `get_player_shooting_numbers()` and pass it the first "player" nested list in
   `players` together with the `slice_` instance. __Unpack__ the return value and assign the
   variables `goals`, `shots`, and `shots_on_target` to the unpacked items.

   :bulb: The Spanish midfielder Teresa Abelleira 🇪🇸 is the first player in the `players` list.

4. Uncomment the `print()` call and the three `assert` statements. Run your code. Confirm that the
   function and item unpacking behaves as expected.

### 4.9 Challenge 9 (35 points)

__Task__: Implement the function named `calculate_shot_conversion_rate()`. Compute the shooting
efficiency of all players who competed in the World Cup.

1. Implement `calculate_shot_conversion_rate()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

   __Requirements__

   1. Employ `try` and `except` blocks to ensure that a passed in shot value of zero (`0`) does not
      trigger a runtime exception (i.e., a `ZeroDivisionError` exception).

   2. Inside the `try` block divide the passed in `goals` by the passed in `shots`. Round the
      quotient to the number of decimal places specified by the passed in `precision` value. Return
      the rounded quotient directly to the caller _without_ first assigning it to a local variable.

   3. Inside the `except` block return the floating point value `0.0` directly to the caller.

2. Return to the `main()` function. Loop over the `players` list. Inside the loop block call the
   function `get_player_shooting_numbers()` and pass it the arguments required to return the current
   player's shooting numbers. __Unpack__ the return value and assign the variables `goals`, `shots`,
   and `shots_on_target` to the unpacked items.

3. Inside the loop block call the function `calculate_shot_conversion_rate()` and pass it the
   player's `goals` and `shots` values along with a `precision` value of three (`3`). Pass the
   arguments __by position__. Append the return value to the player's nested list.

4. Inside the loop block call `calculate_shot_conversion_rate()` a second time, passing it the
   player's `goals` and `shots_on_target` values along with a `precision` value of three (`3`) using
   __keyword arguments__ passed __by position__. Append the return value to the player's nested
   list.

5. Outside the loop block add the following list to the `headers` list:

   ```python
   ["shots_conv_rate", "shots_on_target_conv_rate"]
   ```

   :bulb: Adding the above elements to the `headers` list ensures that the list remains synchronized
   with the mutated nested lists in `players`.

6. Call the function `write_csv()` and pass it the filepath "stu-players-shooting_efficiency.csv"
   along with the other arguments it requires __by position__.

7. Run your code and confirm that the file was written to the current working directory. Then
   compare the CSV file to the matching fixture file. If the files match proceed to the next
   challenge.

## FINIS :tada:
