# SI 506: Problem Set 03

## This Week's Problem Set

This week's problem set includes eight (8) problems that focus on `for` loops,conditional
statements, and the `range()` type. Some topics from previous sections (e.g. methods, indexing,
slicing) are also included.

## Background

This week's problem set incorporates information about TV shows from various streaming platforms.
You are asked to iterate over two different lists to access and extract information.

You are provided with a list called `tv_shows`. Each list element contains the following
information:

- Show Name
- Genre
- Year of Release
- IMDB rating (0-10)
- Rotten Tomatoes rating (0-100)
- Streaming Platform

You are also given another list of TV shows named `new_tv_shows` which contains information about
shows not included in the `tv_shows` list.

## Problem 01 (10 points)

**Task:** Create two lists, `scifi_tv_shows` and `netflix_new_tv_shows`. Each should contain
elements that satisfy the specified condition.

1. Create an empty list named `scifi_tv_shows`.

2. Loop over the `tv_shows` list using a standard `for` loop. Inside the loop block write code to
   perform the following operations:

   1. Apply a conditional statement using a _case-insensitive_ check to verify the presence of the
      substring "scifi" within the string representation of the show.

   2. If the string contains the genre 'scifi', append the string representation of the show to the
      `scifi_tv_shows` list

   :exclamation: You _must_ append the entire string to the list `scifi_tv_shows`.

3. Create an empty list named `netflix_new_tv_shows`.

4. Utilize a `for` loop that iterates over an instance of `range()` (i.e., a sequence of numbers).
   Instantiate the `range()` object with a stop value equal to the length of `new_tv_shows`. Inside
   the loop block, write code to perform the following operations:

   1. Write a conditional `if` statement that performs a _case-insensitive_ equality check to
      determine whether or not the TV show being looped over is available for streaming on Netflix.

   2. If the show is available for streaming on Netflix, access the nested list and append the
      Netflix show name element to the `netflix_new_tv_shows` list.

   :exclamation: Append only the show name.

## Problem 02 (20 points)

**Task:** Create a new list named `cleaned_tv_shows` that represents a "cleaned" version of
`tv_shows` and `new_tv_shows`. This involves changing the data type of certain nested list elements
in `cleaned_tv_shows` and `new_tv_shows` before extending `cleaned_tv_shows` with `new_tv_shows`.

1. Create an empty list named `cleaned_tv_shows`.

2. Loop over `tv_shows` using a standard `for` loop. Inside the loop block write code that
   implements the following operations:

   1. Use the appropriate `str` method and the appropriate delimiter value to split each string
      element into a list.

   2. Append each new list to `cleaned_tv_shows`.

3. Utilize a `for` loop that iterates over an instance of `range()`. Instantiate the `range()`
   object with a stop value equal to the length of `cleaned_tv_shows`. Inside the loop block write
   code that implements the following operations:

   1. Convert the 4th and 5th elements of each nested list from type `str` to type `float` using the
      proper indexing method.

4. Implement another `for` loop that iterates over an instance of `range()`. Instantiate the
   `range()` object with a stop value equal to the length of `new_tv_shows`. Inside the loop block
   write code that implements the following operations:

   1. Convert the 4th and 5th elements from type `str` to type `float`.

5. Outside the loop block, use the appropriate `list` method to extend `cleaned_tv_shows`
   with the mutated `new_tv_shows` list.

## Problem 03 (20 points)

**Task:** Leverage the accumulator pattern to create a list named `crime_genre` that contains the
title, year, and the Rotten Tomatoes rating of each crime show.

1. Create an empty list named `crime_genre`.

2. Using a standard `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code
   that implements the following operations:

   1. Employ an `if` statement that features `str` method chaining to determine if a show is a
      member of the crime genre.

      :exclamation: The crime genre value may be spelled variously as "crime", "Crime",
      "crime ", "Crime ", etc. Use the appropriate string method to ensure that you identify all
      crime shows irrespective of the variations in the genre spelling.

   2. Inside the `if` block, if the conditional statement evaluates to `True`, utilizing slicing to
      append the show's title, year, and Rotten Tomatoes rating to `crime_genre`.

## Problem 04 (15 points)

**Task:** Use a `for` loop to add up all Rotten Tomatoes ratings. Then compute the
average Rotten Tomatoes rating across all TV shows.

1. Assign a sensible starting value to the variable `total_rotten_tomato_ratings`.

2. Using a `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code that
   implements the following operations:

   1. Add the Rotten Tomatoes rating for each show to `total_rotten_tomato_ratings`.

3. Outside the loop block, compute the average Rotten Tomatoes rating across all TV shows using
   `total_rotten_tomato_ratings`. Use the built-in function `round()` to round the average to one
   (`1`) decimal place and assign the rounded average to `avg_rotten_tomato_ratings`.

## Problem 05 (15 points)

**Task:** Accumulate a list of average rated TV shows by iterating over the `cleaned_tv_shows` list.

1. Create an empty list named `above_avg_rotten_tomato_ratings`.

2. Using a `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code that
   implements the following operations:

   1. Employ a conditional `if` statement to determine whether or not the TV show being evaluated
      possesses a Rotten Tomatoes rating that is _greater than_ the `avg_rotten_tomato_ratings`
      variable.

   2. If the conditional statement evaluates to `True`, append the **show name** to
      `above_avg_rotten_tomato_ratings`.

## Problem 06 (10 points)

**Task:** Group TV shows into two different categories by iterating over `cleaned_tv_shows` to find
those streamed by Netflix versus those streamed by other platforms.

1. Create an empty list named `select_content` and another empty list named `non_select_content`.

2. Using a `for` loop with the `range()` function, iterate over `cleaned_tv_shows`. Inside the loop
   block write code that implements the following operations:

   1. Employ `if-else` conditional statements and a case-insensitive equality check to determine if
   the TV show being evaluated is streaming on Netflix.

   2. If the conditional statement evaluates to `True`, append the list representation of the show
   to `select_content`.

   3. Otherwise, append the list representation of the show to `non_select_content`.

## Problem 07 (20 points)

**Task:** Find both the oldest and newest shows using a `for` loop and `if` statements.

1. Assign `max_year` and `min_year` sensible starting values.

2. Using a `for` loop, iterate over `cleaned_tv_shows`. Inside the loop block write code that
   implements the following operations:

   1. Create a variable named `year` and assign it the year of the show. Convert it from type `str`
      to type `int`.

   2. Employ an `if` statement that evaluates whether or not `year` is greater than `max_year`.

   3. If the conditional statement evaluates to `True`, assign `year` to `max_year` and assign the
      name of the show to `newest_show`.

   4. Employ a second `if` statement to check if `year` is less than `min_year`.

   5. Inside the `if` block, if the conditional statement evaluates to `True`, assign `year` to
      `min_year` and assign the name of the show to `oldest_show`.

## Problem 08 (15 points)

**Task:** Accumulate a list of all genres that appear in `cleaned_tv_shows` with no duplicates.

1. Create an empty list named `genres`.

2. Using a `for` loop with the `range()` function, iterate over `cleaned_tv_shows`. Inside the loop
   block, write code that implements the following operations:

   1. Write an `if` statement that evaluates whether or not a show's genre is a member of `genres`.
      Perform a case insensitive comparison of the two strings.

   2. If the show's genre element is not a member of the `genres` list append it to the list.

      :bulb: Note that certain show "genre" elements may contain spaces (e.g., "crime" and "crime ").
      Be sure to employ the appropriate `str` method to ensure that the genre string appended to the
      `genres` list contains no spaces.
