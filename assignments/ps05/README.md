# SI 506: Problem Set 05

## This week's Problem Set

This week's problem set includes eight (`8`) problems that focus on functions, loops, conditional
statements, and using the `main()` function.

## Background

For this week's problem set, you will analyze data from the
[University of Michigan Maize Pages]("https://maizepages.umich.edu/organizations") on activities
organized by student clubs in various categories.

You are provided with a list of strings named `club_events`. Each list element contains the
following information:

- Host Organization: Name of the student club
- Event Name: Name of the activity
- Date: The event start date is formatted as year/month/day.
- Start Time: Event start time
- Duration: Total number of hours of activity
- Location: Location of the event
- Theme: Type of activity/ event category

## Problem 01 (25 Points)

**Task:** Implement a function that converts each element in a list from a string to a list. Use
this function to update all elements in `club_events`.

1. Implement the function named `convert_str_to_list`.

   ```python
   """
   Converts each element in a list from a string to a list.

   Parameters:
       element (str): A string element of the list club_list.
       separator (str): A string that separates elements in the string.

   Returns:
       list: A list of strings.
    """
   ```

   **Requirements**

   1. The function _must_ be provisioned with two parameters in the following order: `element`
      (a string element of the list `club_list`) and `separator` (a string delimiter).

   2. Within the function block, use an appropriate string method to convert the
   string element to a list

   3. Return the converted list to the caller.

2. After implementing the function, return to `main()`. Using a `for` loop with the `range()` type,
   iterate over the elements in the `club_events` list.

   In the loop code block, call the `convert_str_to_list` function on each element in `club_events`.
   Make sure to pass the appropriate separator value as the second argument to your function call.
   Assign the return value of the function to the same index position in the `club_events` list as
   the element on which the function was called.

   :exclamation: After mutating the list, the `club_events` list _must_ match the list
   `club_events_check`(see setup code) after calling the list method.

3. Return to `main()` and uncomment the associated `assert` statement to confirm the variable
   matches the expected value.

## Problem 02 (25 Points)

**Task:** Implement two functions: one that retrieves event venue information and another that
retrieves the location when the event will occur. Use both functions to extract information from
`club_events`.

1. Define and implement a function named `get_duration`.

   ```python
   """
   Retrieves the duration of an event.

   Parameters:
       event_info (str): A string representing the duration of an event.

   Returns:
       float: A float representing the duration of the event.
   """
   ```

   **Requirements**

   1. The function _must_ be provisioned with a single parameter `event_info` (a list element of
      `club_events`).

   2. Return a float representing the event duration to the caller.

     :bulb: zutilize an appropriate string method to split the duration element, then extract the
     number.

2. Define and implement a function named `get_event_location`.

   ```python
   """
   Retrieves the location of an event.

   Parameters:
       event_info (str): A string representing the location of an event.

   Returns:
       str: A string representing the location of the event.
   """
   ```

   **Requirements**

   1. The function _must_ be provisioned with a single parameter `event_info`
      (a list element of `club_events`).

   2. Return a string representation of event location to the caller.

      :bulb: To check if you have implemented the functions correctly, navigate to `main()` and try
      calling `get_duration(club_events[1]` and `get_event_location(club_events[1])`. The correct
      return values _must_ match the `assert` statement values that are checked for equality.

   3. Return to `main()` and uncomment the associated `assert` statements to confirm the return
      value of each function call matches the expected value.

## Problem 03 (35 Points)

**Task:** Implement a function that determines which event(s) in the list `club_events` possess the
shortest duration.

1. Define a function named `event_with_shortest_duration`.

   ```python
   """
    Determines which event(s) in the list club_events has/have the shortest duration.

    Parameters:
        club_events (list): A list of nested event list.

    Returns:
        list: A list of tuples where each tuple contains the name of the event and its duration.
    """
   ```

    **Requirements**

   1. The function _must_ be provisioned with a single parameter `club_events` (a list of nested
      event lists). Do the following in the function code block:

   2. Assign a variable named `shortest_event` to an empty list.

   3. Assign a variable named `shortest_duration` to the integer `100`.

   4. Using a `for` loop and skipping the headers list, iterate over `club_events`.

   5. In the loop code block, call the `get_duration` function on the current event list
      to find the event duration. Assign a variable named `duration` to the return value of the
      function call.

   6. Next, construct an `if-elif` statement block comprising the following coditions:

      1. In the `if` block, check whether `duration` is less than the value of
         `shortest_duration`. If the `if` statement evaluates to `True`, update the value of
         `shortest_duration` to `duration`, clear the `shortest_event` list, then append to
         `shortest_event` a tuple containing event information in the following order:

         1. event name
         2. duration

      2. In the `elif` block, check whether `duration` is equal to the value of
         `shortest_duration`. If the `elif` statement evaluates to `True`, append to `shortest_event`
         a tuple containing event information in the following order:

         1. event name
         2. duration

   7. After the loop terminates, return `shortest_event`.

2. After defining the function, navigate to `main()`. Call the `event_with_shortest_duration`
   function passing to it the appropriate parameter value and assign the return value to a variable
   named `shortest_club_event`.

   :exclamation: The `shortest_club_event` list you create _must_ match the `assert` statement the
   list that is checked for equality.

3. Return to `main()` and uncomment the associated `assert` statement to confirm the variable matches
   the expected value.

## Problem 04 (30 Points)

**Task:** Create a function that returns a list of events that are happening in a specified location.

1. Define a function named `categorize_events_by_location`.

   ```python
   """
   Returns a list of events that are happening in a specified location.

   Parameters:
        club_events (list): A list of nested event list.
        location (str): A string representing the location of the event.

   Returns:
        list: A list of events that are held at the specified location.
    """
   ```

   **Requirements**

   1. The function _must_ be provisioned with two (`2`) parameters in the following order:
      `club_events` (a list of events) and `location` (a string representing the location).

   2. In the function code block, initialize an empty list named `events_by_location`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in
      `club_events`.

   4. In the loop code block, call the function `get_event_location` on the current event list
      to get a string representation of that event's location and store it in a variable
      named `event_location`.

   5. In the loop, using an `if` statement, check whether `event_location` is the same as the value
      of `location` we pass to the function `categorize_events_by_location`. If the `if` statement
      evaluates to `True`, append the event name _only_ to the `events_by_location` list.

   6. After the loop terminates, return the list `events_by_location`.

2. After implementing the function, navigate to `main()` and call the function, passing the
   `club_events` list and the string "Intramural Sports Building" as arguments. Assign a variable
   named `intramural_events` to the return value of the function call.

   :exclamation: The `intramural_events` list you create _must_ match the `assert` statement list
   that is checked for equality.

3. Return to `main()` and uncomment the associated `assert` statement to confirm the variable
   matches the expected value.

## Problem 05 (30 Points)

**Task:** Implement two functions. The first extracts events from a list that have a specified
theme while the second categorizes events by their theme.

1. Define a helper function named `has_theme`.

   ```python
   """
   Checks whether or not a provided < event > possesses a specified < theme >.

   Parameters:
        event (list): A list of events.
        theme (str): A string representing the theme of the event.

   Returns:
        bool: A boolean value indicating if the event has the specified theme.
    """
   ```

    **Requirements**

    1. The function _must_ be provisioned with two parameters in the following order: `event`
       (a list element of `club_events`) and `theme` (a string representing an event category).

    2. In the function code block, write an `if` statement to check whether the value of `theme`
       passed to the function is a substring of the string representing the theme in the `event`
       list. If the `if` statement evaluates to `True`, return `True`. Otherwise, return `False`.

2. Define a function named `categorize_events_by_theme`.

   ```python
   """
   Extracts events from a list filtered on a provided < theme >.

   Parameters:
       club_events (list): A list of nested event list.
       theme (str): A string representing the theme of the event.

   Returns:
       list: A list of events that have the specified theme.
   """
   ```

    **Requirements**

    1. The function _must_ be provisioned with two parameters in the following order: `club_events`
        (a list of events) and `theme` (a string representing an event category).

    2. In the function code block, assign a variable named `events_by_theme` to an empty list.

    3. Skipping the headers list, iterate over the event lists in `club_events` using a `for` loop.

    4. In the loop code block, call the `has_theme` helper function (implemented
        previously) in an `if` statement, to check whether the `theme` string exists in the
        current _event's_ theme string.
        If the `if` statement evaluates to `True`, append the event name to the
        `events_by_theme` list.

        :bulb: You _must_ use the helper function in your `if` statement appropriately.

    5. After the loop terminates, return the `events_by_theme`.

3. After implementing the functions, navigate to `main()`. Assign a variable named
   `specified_theme_events` to an empty list.

4. Iterate over the provided `themes` list using a `for` loop. Inside the loop code block, call the
   `categorize_events_by_theme` function on each element in the `themes` list. Make sure to pass
   `club_events` as the first argument to each `categorize_events_by_theme` function call. Append
   the return value from each function call to the `specified_theme_events` list.

   :exclamation: The `specified_theme_events` list you create _must_ match the list
   `specified_theme_events_check` (see setup code) after calling the list method.

5. Return to `main()` and uncomment the associated `assert` statement to confirm the variable
   matches the expected value.

## Problem 06 (25 Points)

**Task:** Implement a function that identifies events that have a specific start time and duration.

1. Define a function named `categorize_events_by_time`.

   ```python
   """
   Extracts events from a list that occur at a specified time.

   Parameters:
       club_events (list): A list of nested event list.
       time (str): A string representing the time of the event with default value of "7 PM".
       duration (int): An integer representing the duration of the event with default value of 1.

   Returns:
       list: A list of events that occur at the specified time.
   """
   ```

   **Requirements**

   1. The function _must_ be provisioned by three parameters in the following order: `club_events`
      (a list of events), an optional argument `time` (a string representing the event start time)
      with default value `"7 PM"` and another optional argument `duration` (an integer representing
      the event duration) with default value `1`.

   2. In the function code block, initialize an empty list named `events_by_time`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in
      `club_events`.

   4. In the loop code block, using a compound `if` statement, check whether the current
      event start time is the same as the value of `time` and whether the current event duration is
      **greater than or equal to** the value of `duration`. If the `if` statement evaluates to
      `True`, append **only** the _event name_ to the `events_by_time` list.

   5. After the loop terminates, return the `events_by_time` list.

2. After defining the function, return to `main()`. Call the function `categorize_events_by_time`,
   passing the `club_events` list as its required argument. Assign the return value of the function
   call to a variable named `evening_events`.

   :exclamation: The `evening_events` list you create _must_ match the `assert` statement list
   that is checked for equality.

3. Return to `main()` and uncomment the associated `assert` statement to confirm the variable matches
   the expected value.

## Problem 07 (20 Points)

**Task:** Implement a function that identifies the number of events hosted by a specific student
organization.

1. Define a function named `calculate_num_events`.

   ```python
   """
   The function calculates the number of events hosted by a specified organization.

   Parameters:
        club_events (list): A list of nested event list.
        host_org (str): A string representing the host organization.

   Returns:
        int: An integer representing the number of events hosted by the specified organization.
   """
   ```

   **Requirements**

   1. The function _must_ be provisioned with two parameters in the following order: `club_events`
      (a list of events), `host_org` (a string representing the student organization's name).

   2. In the function code block, Assign a variable named `num_events` to the integer `0`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in
      `club_events`.

   4. In the loop code block, if the name of the student organization pertaining to the current
      event is the same as the value of `host_org`, increment the value of `num_events` by one
      (`1`).

   5. After the loop terminates, return the `num_events`.

2. After implementing the function, navigate to `main()`. Call the function `calculate_num_events`,
   passing the `club_events` list and the string `"A2 Movimiento Latino"` as arguments. Assign the
   variable named `num_events_for_a2` to the returnn value of the function call.

   :exclamation: The `num_events_for_a2` variable you create _must_ match the `assert` statement
   value that is checked for equality.

3. Return to `main()` and uncomment the associated `assert` statement to confirm the variable matches
   the expected value.

## Problem 08 (10 points)

**Task:** Implement a function that identifies events of a particular theme (or type of event).
Unpack the function's return value into multiple variables.

1. Define a function named `categorize_events_by_specific_theme`.

   ```python
   """
   Identifies events of a particular theme (or type of event).

   Parameters:
       club_events (list): A list of nested event list.
       theme (str): A string representing the theme of the event.

   Returns:
       list: A list of events that have the specified theme.
   """
   ```

    **Requirements**

    1. The function _must_ be provisioned with two parameters in the following order: `club_events`
       (a list of events) and `theme` (a string representing an event theme).

    2. In the function code block, assign a variable named `events_at_theme` to an empty list.

    3. Using a `for` loop, iterate over each event in club_events (skipping the header).

    4. In the for loop block, extract the theme of the current event and assign a variable
       named `event_theme` to it.

    5. Using an `if` statement, check whether `event_theme` is the same as the value of `theme` we
       pass to the function `categorize_events_by_specific_theme`. If the `if` statement evaluates
       to `True`, append `events_at_theme` with a tuple containing the following contents
       (in the order specified):

       1. event name
       2. event date
       3. event theme.

    6. After the loop terminates, return `events_at_theme`.

2. After implementing the function, navigate to `main()`. Call `categorize_events_by_specific_theme`
    and pass it the following arguments: `club_events` and `'social'` (all lowercase). Assign the
    variable named `social_events` to the return value of the function call.

3. While still in `main()`, unpack `social_events` into the following variables: `social_event_1`,
    `social_event_2`, and `social_event_3`.

    :exclamation: This step _must_ be completed using a single statement on a single line of code.

    :exclamation: The variables `social_event_1`, `social_event_2` and `social_event_3` you create
    _must_ match the `assert` statement tuples that are checked for equality.

4. Return to `main()` and uncomment the associated `assert` statements to confirm the variable
   matches the expected value.
