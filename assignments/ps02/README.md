# SI 506: Problem Set 02

## This week's Problem Set

This week's problem set includes six (6) problems that focus on strings, lists, 
and string/list operations.

:bulb: As you work through the problem set make use of the commented out
 `print()` function calls and `assert` statements to check your work.

## Reference

- ["Python Built-in Functions"](https://www.w3schools.com/python/python_ref_functions.asp)
- ["Python Operators"](https://www.w3schools.com/python/python_operators.asp)
- ["Python List Methods"](https://www.w3schools.com/python/python_lists_methods.asp)
- ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)

## Background

The University of Michigan offers numerous resources that can help you and other
 students in their well-being journeys.We hope this assignment will increase your 
 awareness of the numerous resources that UMich offers for your benefit as 
 listed in the SI 506 [Syllabus](https://si506.org/syllabus/) (see Section 8.0).

:bulb: Learn more about U-M well-being resources by visiting
[https://wellbeing.studentlife.umich.edu/](https://wellbeing.studentlife.umich.edu/).

## 1.0 Problem 01 (25 Points)

**Task:** Create a master list of all wellbeing resources, then create sublists 
for different categories of resources.

1. You have been provided with a variable containing a single string expressed 
   across multiple lines (a multiline string) named `wellbeing_resources`. 
   Review each resource and note which character(s) delineate (separate) each 
   resource. Call the appropriate string method to return a list of resource
   elements. Assign the return value of the string method to the variable
   `resources`, and display its contents.

2. Assign the first three elements of the list named `resources` to a new 
   variable named `academic` using list slicing.

   :exclamation: You are limited to using a single statement that includes a 
   slicing expression.

3. Assign the fourth and fifth elements of the list `resources` to a new list 
   variable named `health` using list slicing.

   :exclamation: You are limited to using a single statement that includes a 
   slicing expression.

4. Assign the sixth, seventh, and eighth elements of the list `resources` 
   to a new list variable named `marginalized_comm` using list slicing and 
   negative index values.

   :exclamation: You are limited to using a single statement that slices the 
   list using negative index values.

5. Assign the last two elements of the list `resources` to a new list variable
   named `community` using list slicing and negative indexing.

   :exclamation: You are limited to using a single statement that slices the 
   list using negative index values.

## 2.0 Problem 02 (25 Points)

**Task:** Update some of your resource sublists with additional resources using various list
methods.

1. Call the appropriate `list` method to extend the list `health` 
   (which you created in 1.3) with the list `addl_health_resources`.

   :exclamation: The value assigned to `health` _must_ match the list 
   `health_check` (see Setup Code)  after calling the list method. Uncomment
   the associated `assert` statement to confirm the variable matches the 
   expected value.

2. Call the appropriate `list` method to add `embedded_caps` as the last 
   element of the `health` list.

3. Call the appropriate `list` method to insert `mesa` as the third element of 
   the `marginalized_comm` list (which you created in 1.4).

4. Using list indexing and string concatenation, mutate the list 
   `addl_academic_resources` by  concatenating _each_ element with the 
   respective phone numbers in `addl_academic_resource_numbers`.

   :exclamation: The value assigned to `addl_academic_resources` _must_ match 
   the list `addl_academic_resources_check` (see Setup Code) after concatenating
   the corresponding strings. Uncomment the associated `assert` statement to 
   confirm the variable matches the expected value.

5. Call the appropriate `list` method to extend the list `academic` 
   (which you created in 1.2) with `addl_academic_resources`.

   :exclamation: The value assigned to `academic` _must_ match the list 
   `academic_check` (see Setup Code). Uncomment  the associated `assert` 
   statement to confirm the variable matches the expected value.

## 3.0 Problem 03 (15 Points)

**Task:** Re-sort some of your resource sublists using various list methods. 
Create an additional list with resources from the `health` sublist.

1. Use the appropriate list method to _reverse_ the order of the list 
   `marginalized_comm` elements.

2. Use the appropriate list method to sort the order of the list `health` 
   elements in _ascending_ alphanumeric order.

3. Use the appropriate list method to sort the order of `academic` 
   elements in _descending_ alphanumeric order.

   :bulb: Be sure to also specify the parameter `reverse` in the relevant list 
   method as `True` `(reverse=True)`.

4. Using the appropriate list method, return the index value of
   `UMSI Embedded CAPS Psychologist|Ashley Evearitt` in `health`. Assign the 
   index value to the  variable `umsi_caps`.

5. Slice `UMSI Embedded CAPS Psychologist|Ashley Evearitt` and 
   `University Health Service (UHS)|734-764-8320` from `health` using 
   _positive index values_. You _must_ use the variable `umsi_caps` in your
   slicing expression. Assign the new list to a variable named 
   `student_focused_health_resources`.

   :exclamation: You are limited to using a single statement that utilizes the 
   variable `umsi_caps` in your slicing expression.

## 4.0 Problem 04 (10 Points)

**Task:** Using the built-in functions `str.split()` and `str.join()` to create 
tuples and variables.

1. Retrieve the third element from the list `academic` and then convert it into 
   a two-item tuple with the name as the first item and the phone number as the 
   second. Next, assign this tuple to a variable  named `third_academic_element`.
   Then uncomment the `assert` statement to confirm the variable matches the 
   expected value.

2. Retrieve the second to last element from the list `health` using 
   _negative index values_ and convert it into a two-item tuple with the name as
   the first item and the phone number as the second. Next, assign this tuple 
   to a variable named `second_last_health`.
   Then uncomment the `assert` statement to confirm the variable matches the 
   expected value.

3. Working with the list `marginalized_comm`, call the appropriate string method
   that accepts an  _iterable_ (e.g., a list) as an argument and returns a new 
   string composed of the `marginalized_comm` elements, each of which is 
   separated by a period/fullstop (.). Next, assign the new string to a variable
   named `marginalized_comm_str` Then uncomment the `assert` statement to 
   confirm the variable matches the expected value.

## 5.0 Problem 05 (15 Points)

**Task:** Create lists and find values using slicing.

1. Slice every odd-indexed value from the list `health` and assign the resulting
   list to a variable called `odd_index_health`.

   :bulb: Hint: Make sure to carefully choose the `step` value within a list slice.

2. Slice the 2nd, 3rd and 4th values in _reverse_ order from the list `academic`
   using **negative indexes**. Assign the resulting list to a variable named 
   `academic_sub_list`, and  uncomment the `assert` statement to confirm the 
   variable matches the expected value.

   :bulb: Hint: Make sure to carefully choose the `step` value within a list 
   slice along with the `start`   and `stop` values.

3. Reverse the list `marginalized_comm` using negative indexes. Assign the 
   resulting list to a variable called `marginalized_comm_reversed`.

   :exclamation: Your statement _must not_ use the `.reverse()` method.

## 6.0 Problem 06 (10 points)

**Task:** Return a slice of the list `academic` using various list methods.

1. Use the appropriate list method to return the index of the last element in 
   the list `academic` (i.e., `Dean of Students Office|734-764-7420`). Assign 
   the value to a variable named `student_dean_index`.

   :exclamation: You _must_ employ the appropriate list method to retrieve the 
   index value of this element.

2. Use `student_dean_index` in a slicing expression that slices two (`2`) 
   elements from `academic` _in the following order_:

   1. `Dean of Students Office|734-764-7420`
   2. `Office of the Ombuds|734-763-3545`

   Assign the slice to a variable named `academic_sub_list`, and uncomment the 
   associated `assert` statement to confirm the variable matches the expected 
   value.
