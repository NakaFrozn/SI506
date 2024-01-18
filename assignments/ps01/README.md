
# SI 506: Problem Set 01

## This week's Problem Set

This week's problem set includes five (5) problems that focus on variable assignments, using built-in functions, and basic string operations.

:bulb: In order to check your work, try utilizing the built-in function `print()` to print the
passed in argument to the screen.

## Background

This week's problem set utilizes data on the diverse range of tantalizing restaurants and eateries located in Ann Arbor, and features some of Central Campus' most popular spots.

## 1.0 Problem 01

**Task:** Identify and create valid variable assignments for some of the popular restaurants located in Ann Arbor.

1. You have been provided with ten (10) commented out lines of code that attempt to assign a
   restaurant's name to a variable. Only some of the lines contain valid variable assignments.
   Uncomment the statements that contain valid variable assignments.

2. Create a new variable called `cottage_inn` and assign to it a string representation of the
   restaurant **Cottage Inn Pizza**.

   :exclamation: Make sure that you treat the restaurant name as a title (i.e., capitalize the first
   letter of every word).

3. Similarly, create a new variable called `madras_masala` and assign to it a string representation
   of the restaurant **Madras Masala**.

   :exclamation: Make sure that you treat the restaurant name as a title (i.e., capitalize the first letter of every word).

## 2.0 Problem 02

**Task:** Leverage several string methods that exhibit the requested behaviors in order to return a
modified version of each string indicated below.

1. Call the appropriate `str` method to return a version of the string assigned to `hopcat` that
   converts all its characters to **_lower_** case. Assign the return value to a new variable named
   `hopcat_all_lower`.

2. Call the appropriate `str` method to return a version of the string assigned to `jerk_pit` that
   converts all its characters to **_upper_** case. Assign the return value to a new variable named `jerk_pit_all_upper`.

3. Call the appropriate `str` method that can sum the number of times the letter `"m"` appears in
   the string assigned to `madras_masala`. Assign the return value to a new variable named
   `madras_masala_count_m`.

4. Call the appropriate `str` method that can be used to check whether the string assigned to
   `fleetwood_diner` ends with `"Diner"`. Assign the return value to a new variable named
   `has_diner`.

5. Call the appropriate `str` method to check whether the string assigned to `hola_seoul` starts
   with `"Seoul"`. Assign the return value to a new variable named `starts_seoul`.

6. Call the appropriate `str` method that can return a version of the string `comment` that
   substitutes the substring `" and "` for the character `"&"`. Assign the return value to a new
   variable named `updated_comment`.

   :bulb: Ensure you are passing the correct argument to the string method in order to account for any spacing errors in the original comment. A space is also a character in a string.

## 3.0 Problem 03

**Task:** Leverage some of Python's built-in functions that exhibit the behaviors specified below in
order to complete the requested tasks.

1. Count the total number of characters in the string assigned to the variable `updated_comment` and
   assign it to a new variable called `num_chars`.

    :bulb: Utilize the built-in function that will help you determine the length of the string.

2. A food critic would like to visit each of the most popular restaurants in Ann Arbor. They
   collected the restaurant names and stored them in the `restaurants` list. Call the built-in
   `print()` function and pass it the following argument: an expression that involves calling a
   built-in function that returns the data type of the object assigned to the variable
   `restaurants`.

3. Please also help the food critic count how many restaurants are listed in the `restaurants` list.
   Assign the return value to a new variable called `num_restaurants`.

   :bulb: You should utilize the built-in function that will help you count.

## 4.0 Problem 04

**Task:** Perform various arithmetic operations to assist the food critic in calculating the total
bill for a meal with a group of their friends.

1. The food critic would like to invite six (6) of their friends to the restaurant, New York Pizza
   Depot. Before they visit the restaurant, the critic checks the menu online. Below is a table that
   shows the popular dishes the restaurant offers:

   | Food & Drinks        | Price  |
   | -------------------- | ------ |
   | Plain Cheese Pizza   | $18.99 |
   | Garlic Knots         | $6.99  |
   | Soda                 | $7.00  |
   | Oreo Cookie Shake    | $10.49  |
   | White Pizza          | $22.25 |
   | Mozzarella Sticks    | $17.99 |

   The food critic orders the following items for the group:

   * four (4) Plain Cheese Pizzas
   * five (5) orders of Garlic Knots
   * two (2) Sodas
   * five (5) Oreo Cookie Shakes
   * one (1) White Pizza
   * and two (2) orders of Mozarella Sticks for the group

   <br />

   Calculate the total price of the order. Assign the return value to a variable called
   `total_price`.

   :exclamation: **Do not** consider taxes and tips for this problem.

2. Given that the state sales tax rate for Michigan is 6%, and the diners are willing to give the
   server a 15% tip based on the total price, before taxes, what should be the total amount the
   group needs to pay for this meal? Assign the return value to a variable called `total_bill`.

   :exclamation: Please use the variable `total_price` to calculate the total amount they need to
   pay.

3. The food critic and his six (6) friends decide to split the entire bill evenly. What would be the
   amount that each person pays? Assign the return value to a variable called `each_pay`.

    :exclamation: Please use the variable `total_bill` to calculate the amount each person must pay
    and keep all digits after the decimal.

## 5.0 Problem 05

**Task:** Pass a formatted string literal (f-string) to the built-in `print()` function.

1. Utilize an f-string and the variables `updated_comment` and `jerk_pit_all_upper` to print out the
following sentence:

   ```markdown
   Someone said "Great Jamaican food and drinks" on Yelp for the restaurant JAMAICAN JERK PIT.
   ```

   :exclamation: The _comment_ **Great Jamaican food and drinks** in the sentence must be
   surrounded by single quotes. The f-string must be on one line.
