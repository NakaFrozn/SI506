# Problem Set 08

## Exploring New York Times Bestselling Books

## Background

The New York Times publishes several "bestselling books" lists that list America's most sold books
in various categories. It is a great honor for an author to have a book on a New York Times
Bestselling List.

Learn more: https://www.nytimes.com/books/best-sellers/

Your data this week comes from two NYT bestseller lists that are published weekly. Note that it is
very common for a book to remain on the bestselling list for multiple weeks.

- **data-young_adult_bestsellers-2024.json** contains the data from the "Young Adult Hardcover
  Bestsellers" lists from the last 8 weeks. These lists report the top 10 bestselling young adult
  hardcover books each week.

- **data-fiction_bestsellers-2024.json** contains the data from the "Hardcover Fiction Bestsellers"
  lists from the last 8 weeks. These lists report the top 15 bestselling hardcover fiction books
  each week.

:exclamation: We will be handling both bestselling _lists_ and Python _list_ objects this week.
**Be careful! In each JSON file, you'll see that the bestselling _list_ for a single week is**
**represented by a _dictionary_!** Spend plenty of time acquainting yourself with the data and
keeping your objects straight.

## Data

When read in, each JSON file comprises a **list of dictionaries**. Each dictionary represents the
bestselling books list published for a specific week. **Keys** of note within this "bestsellers
list" dictionary include `"list_name"`, `"published_date"`, `"normal_list_ends_at"`, and `"books"`.
You will be working primarily with the value of the `"books"` key, which is itself a **dictionary**.
Review this data structure carefully.

:bulb: Although these are large files, they are repetitive and fairly clean. We are confident you
can handle them!

Note: The books' prices were randomly generated. In the real data, each price was listed as '0.00'.

## Problems

The problems can generally be split into problems that work with `"young_adult_bestsellers-2024.json"`
(Problems 1-4) and problems that work with `"data-fiction_bestsellers-2024.json"` (Problems 5-9).

Your goals for `"data-young_adult_bestsellers-2024.json"` are to read in the file, clean the book
data within it, and write the cleaned data out to a new JSON file. Finally, you will find the
average price for books in the No. 1 position on the list and the No. 10 position spot on the list.

Your goal for `"data-fiction_bestsellers-2024.json"` is to score each publisher based on where and
how often its books appear on the bestsellers list. You will create a "scoreboard" dictionary with
all the publishers and their scores. You will write this scoreboard out to a new JSON file.

The program features a number of functions including a `main()` function that serves as the entry
point to the program and orchestrator of the program's work flow.

## Problem 1

**Task**: Use `read_json` function to read a JSON file and convert it into a Python list or
dictionary.

1. In `main` function, create a `Path` instance by passing to it the following filename:
"data-young_adult_bestsellers-2024.json". Then call the `Path` object's `resolve()` method to render
the path absolute. Assign the `Path` object to a variable named `filepath_young_adult`.

2. Call the `read_json` function and pass to it the following argument: `filepath_young_adult`.
Assign the return value to a variable named `young_adult_bestsellers`.

3. `young_adult_bestsellers` is a very large list. Use indexing to assign the first element of the
list that represents the first week's bestsellers list to the variable
`young_adult_bestsellers_week_1`

   `young_adult_bestsellers_week_1` _must_ start with:

   ```python
   {
      'list_name': 'Young Adult Hardcover',
      'list_name_encoded': 'young-adult-hardcover',
      'bestsellers_date': '2024-03-02',
      'published_date': '2024-03-17',
      'published_date_description': 'one_before_latest',
      'next_published_date': '2024-03-24',
      'previous_published_date': '2024-03-10',
      'display_name': 'Young Adult Hardcover',
      'normal_list_ends_at': 10,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 2,
            'weeks_on_list': 17,
            'asterisk': 0,
            'dagger': 0,
            'primary_isbn10': '1665954884',
            'primary_isbn13': '9781665954884',
            'publisher': 'Simon & Schuster',
            'description': 'Forbidden love is in the air when Paedyn, an Ordinary, and Kai, an Elite, become romantically involved.',
            'price': '21.35',
            'title': 'POWERLESS',
            ...
   ```

4. Create another `Path` instance by passing to it the following filename:
"data-fiction_bestsellers-2024.json". Then call the `Path` object's `resolve()` method to render
the path absolute. Assign the `Path` object to a variable named `filepath_fiction`.

5. Call the `read_json` function and pass to it the following argument: `filepath_fiction`. Assign
the return value to a variable named `fiction_bestsellers`.

6. `fiction_bestsellers` is a very large list. Use indexing to assign the last element of the list
that represents the eigth week's bestsellers list to the variable `fiction_bestsellers_week_8`.

   `fiction_bestsellers_week_8` _must_ start with:

   ```python
   {
      'list_name': 'Hardcover Fiction',
      'list_name_encoded': 'hardcover-fiction',
      'bestsellers_date': '2024-01-13',
      'published_date': '2024-01-28',
      'published_date_description': '',
      'next_published_date': '2024-02-04',
      'previous_published_date': '2024-01-21',
      'display_name': 'Hardcover Fiction',
      'normal_list_ends_at': 15,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 1,
            'weeks_on_list': 36,
            'asterisk': 0,
            'dagger': 0,
            'primary_isbn10': '1649374046',
            'primary_isbn13': '9781649374042',
            'publisher': 'Red Tower',
            'description': 'Violet Sorrengail is urged by the commanding general, who also is her mother, to become a candidate for the elite dragon riders.',
            'price': '0.00',
            'title': 'FOURTH WING'
            ...
   ```

   :exclamation: You will use `fiction_bestsellers` in later problems.

## Problem 2

**Task**: Implement the functions `convert_to_float()` to ensure that the book prices can be
manipulated as floats.

1. Implement the function named `convert_to_float`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

   **Requirements**

   1. Wrap your code in `try` and `except` statements to handle errors.

   2. Use a conditional statement to determine if the value is of the type `int`. If the value is
   an `int`, do _not_ convert it and return the `value` unchanged.

   3. If the value is not an integer, return a `float` version of the value, if possible.

   4. If the value cannot be converted to a `float`, return the `value` unchanged.

2. After implementing `convert_to_float()` return to the `main()` function

3. Uncomment the 3 assert statements. These will test your `convert_to_float()` function. Confirm
that `convert_to_float()` performs as expected and does not throw any errors.

## Problem 3

**Task**: Implement the function `clean_book()` to edit down the book dictionaries so that they are
easier to read and work with. You will use this function to clean the books within
`young_adult_bestsellers`.

1. Implement the function named `clean_book`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   **Requirements**

   1. Create an empty dictionary that will become the new book dictionary that you must return.

   2. Loop through the keys and values of the `book` dictionary using the appropriate dictionary
   method.

   3. If a `desired_keys` list was passed in, ensure that only keys that are in `desired_keys` are
   added to the new dictionary. Pass the values paired with these keys to `convert_to_float()` and
   assign the return value as the value in the new dictionary.

   4. If there are no `desired_keys`, add all the keys and values to the new dictionary,
   _at the same time_ calling `convert_to_float()` to convert the values.

   5. Return the new dictionary that was created.

2. After implementing `clean_book()` return to the `main()` function.

3. Use `clean_book()` to clean all the books in each of the 8 "bestsellers list" dictionaries in
`young_adult_bestsellers`.

   **Requirements and hints**

   1. Loop through `young_adult_bestsellers` to access the "bestsellers list" dictionaries one week
   at a time.

   2. You may want to access just the books from each week and assign the list of books to a
   variable that you can use going forward.

   3. Use a nested `for i in range()` to call `clean_book()` on each book and assign the cleaned
   book back to the book list in its place.

   4. When you call `clean_book()` you _must_ pass `keep_keys` as the second argument using a
   _keyword argument_.

   Your cleaned `young_adult_bestsellers_week_1` list _must_ now start with:

   ```python
   {
      'list_name': 'Young Adult Hardcover',
      'list_name_encoded': 'young-adult-hardcover',
      'bestsellers_date': '2024-03-02',
      'published_date': '2024-03-17',
      'published_date_description': 'one_before_latest',
      'next_published_date': '2024-03-24',
      'previous_published_date': '2024-03-10',
      'display_name': 'Young Adult Hardcover',
      'normal_list_ends_at': 10,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 2,
            'publisher': 'Simon & Schuster',
            'description': 'Forbidden love is in the air when Paedyn, an Ordinary, and Kai, an Elite, become romantically involved.',
            'price': 21.35,
            'title': 'POWERLESS',
            'author': 'Lauren Roberts',
            'isbns': [
               {
                  'isbn10': '1665954884',
                  'isbn13': '9781665954884'
               }
            ]
         },
         ...
   ```

4. Assign "stu-clean_young_adult_bestsellers-2024.json" to a variable called `filepath`.

5. Call the function `write_json` and pass to it as arguments `filepath` and
`young_adult_bestsellers`. Compare your output file to the test fixture file
`fxt-clean_young_adult_bestsellers-2024.json`. Both files _must_ match, line for line, and character
for character.

## Problem 4

**Task**: Our last task with the `young_adult_bestsellers` list is to implement a function that
finds the average price of the books of a given rank and then test your implementation by returning
the average price of books ranked No. 1 and books ranked No. 10.

1. Implement the function named `get_average_price_by_rank`. Review the function's docstring
regarding its expected behavior, parameters, and return value.

   **Requirements**

   1. Assign a sensible starting value to a variable named `total_price`.

   2. Use nested `for` loops to loop through all the books in the eight "bestsellers list"
   dictionaries.

   3. The outer `for` loop should be a standard loop through `bestseller_lists`. The inner for loop
   should loop through the values from the `'books'` key in each value of `bestseller_lists`.

      :bulb: Use subscript notation to access the key.

   4. If the book's `'rank'` is equivalent to the passed-in `rank`, add the price of that book to
   the `total_price` using the addition assignment.

   5. Once the `total_price` has fully accumulated (the looping has ended), return the average price
   of the books of the given rank, rounded to the nearest cent (hundreths place).

      :exclamation: Remember that there are 8 weeks of bestsellers lists, so there will be 8 books
      of each rank.

2. After implementing `get_average_price_by_rank()`, return to the `main()` function.

3. Call the function `get_average_price_by_rank()` and pass to it the `young_adult_bestsellers` list
and the integer, 1, as arguments. Assign the return value to the variable named `rank_1_avg`.

   Uncomment the `assert` statement. The `rank_1_avg` value _must_ match the value of the
   `rank_1_avg_test` variable

   :exclamation: You must use the _positional arguments_ in the function call to pass the autograder.

4. Call the function `get_average_price_by_rank()` and pass to it the `young_adult_bestsellers` list
and the integer, 10, as arguments as keyword arguments in _reverse order_. Assign the return value
to the variable named `rank_10_avg`.

   Uncomment the `assert` statement. The `rank_10_avg` value _must_ match the value of the
   `rank_10_avg_test` variable

   :exclamation: You must use the keyword arguments in reverse order in the function call to pass
   the autograder.

## Problem 5

**Task**: Problems 5-9 handle data from `fiction_bestsellers.json`. Implement a function that
retrieves all the books for any given publisher. Call the function to find all the books published
by Doubleday and print their titles and ranks.

1. Implement the function named `get_books_by_publisher`. Review the function's docstring regarding
its expected behavior, parameters, and return value.

   **Requirements**

   1. Use the accumulator pattern. (An empty list to which objects are appended.)

   2. Use nested `for` loops to access all the books in the `"bestsellers_list"` list of
   dictionaries.

   3. The outer `for` loop should be a standard loop through the `'bestseller_lists'` list. The
   inner for loop should loop through the values from the `'books'` key in each value of
   `bestseller_lists`.

   4. The `if` statement that compares a book's publisher and the passed in `publisher` parameter
   _must_ use a case-insensitive equality comparison.

   5. The list that this function returns _must_ include dictionaries for the same book that come
   from different weeks' lists. For example, it might include
   `{'rank': 1, 'title': 'Where the Wild Things Are'}` from week 1,
   `{'rank': 1, 'title': 'Where the Wild Things Are'}` from week 3,
   and `{'rank': 8, 'title': 'Where the Wild Things Are'}` from week 4.

2. After implementing `get_books_by_publisher()`, return to the `main()` function.

3. Now, call the function `get_books_by_publisher()` and pass to it the `fiction_bestsellers` list
and the publisher, `'Doubleday'`. Assign the return value to the variable named `doubleday_books`.

4. Let's make this data a little more readable. Your goal is to print the title and rank for each of
the books in the `doubleday_books` list. Uncomment the `for` loop and replace the question marks (?)
with expressions that will resolve into the `'title'` and the `'rank'` for each book.

   **Requirements**

   1. You _must_ access the `'title'` from the book dictionary using its associated key.

      :exclamation: Note that because the f-string is enclosed in double quotes, you must use single
      quotes when typing the key of the dictionary.

   2. You _must_ access the `'rank'` from the book dictionary using a _dictionary method_.

## Problem 6

**Task**: Implement a function that returns a score for a given book depending on its rank (in one
week's list). Call the function to score the first and penultimate books from `doubleday_books`.

:bulb: "Penultimate" is another word for second-to-last.

1.  Implement the function named `score_book`. Review the function's docstring regarding its
expected behavior, parameters, and return value.

    **Requirements**

    1. Use `if - elif - else` statements to sort the book according to its rank, then return the
    appropriate score.

2.  After implementing `score_book()` return to the `main()` function.

3.  Call `score_book()` passing it the
    first book from the `doubleday_books` list using indexing. Assign the return value to a variable
    named `first_book_score`.

    Replace the "?first book title?" substring in the f-string with an expression that will resolve
    to the **first** book's title from the `doubleday_books` list.

      :exclamation: Note that because the f-string is enclosed in double quotes, you must use single
      quotes when typing the key of the dictionary.

    Uncomment the `assert` statements. The title of the first book _must_ match the value of the
    `first_doubleday_book_title_test` variable and the score of the first book in variable
    `first_book_score` _must_ match the value of the `first_doubleday_book_score_test` variable.

4.  Call `score_book()` passing it the
    penultimate book from the `doubleday_books` list. Assign the return value to a variable named
    `penultimate_book_score`.

    Replace the "?penultimate book title?" substring in the f-string with an expression that will
    resolve to the **penultimate** book's title from the `doubleday_books` list.

      :exclamation: Note that because the f-string is enclosed in double quotes, you must use single
      quotes when typing the key of the dictionary.

    Uncomment the `assert` statements. The title of the penultimate book _must_ match the value of
    the `penultimate_doubleday_book_title_test` variable and the score of the penultimate book in
    variable `penultimate_book_score` _must_ match the value of the
    `penultimate_doubleday_book_score_test` variable.

## Problem 7

**Task**: Implement a function that returns a score for a given publisher which is the total of the
scores of all its books over the whole eight week period. Call the function to determine the score
for Doubleday.

1. Implement the function named `score_publisher`. Review the function's docstring regarding its
expected behavior, parameters, and return value.

   **Requirements**

   1. Assign a sensible starting value to a variable named `score`.

   2. Use the accumulator pattern.

   3. Call `get_books_by_publisher()` to access all the books published by the given publisher,
   passing to it the relevant arguments. Loop through the return value of this function call.

   4. Call `score_book()` on each book returned in the `get_books_by_publisher()` list. Add the
   return value to the `score` variable in each iteration of the loop.

2. After implementing `score_publisher()` return to the `main()` function.

3. Call `score_publisher()` passing it the
   `fiction_bestsellers` list and publisher `"Doubleday"`, _using keyword arguments in reverse order_.
   Assign the return value to a variable named `doubleday_score`.

   Uncomment the `assert` statement. The Doubleday publisher score _must_ match the value of the
   `doubleday_score_test` variable

## Problem 8

**Task**: Implement a function that returns a list of each of the publishers that appears in any of
the eight "bestsellers list" dictionaries. Call the function to find which publishers have had a
book on the NYT fiction bestsellers list in the past 8 weeks.

1. Implement the function named `find_publishers`. Review the function's docstring regarding its
expected behavior, parameters, and return value.

   **Requirements**

   1. Use the accumulator pattern. (An empty list to which objects are appended.)

   2. Use nested `for` loops to access all the books in the "bestsellers list" dictionaries. The
   outer `for` loop should be a standard loop through the `'bestseller_lists'` list. The inner for
   loop should loop through the values from the `'books'` key in each value of `bestseller_lists`.

   3. Append each publisher name to the list, but be sure to use a conditional statement to avoid
   adding repeats of names that are already in the list.

2. After implementing `find_publishers()` return to the `main()` function.

3. Call `find_publishers()` passing it the
   `fiction_bestsellers` list. Assign the return value to a variable named `fiction_publishers`.

   Uncomment the `assert` statement. The `fiction_publishers` list _must_ match the value of the
   `fiction_publishers_test` variable

## Problem 9

**Task**: Implement a function that returns a dictionary "scoreboard" in which each key is a
publisher and each value is that publisher's score, based on their books' rankings. Call the
function to create a "publisher scoreboard" based on the NYT fiction bestsellers lists from the past
8 weeks.

1. Implement the function named `create_scoreboard`. Review the function's docstring regarding its
expected behavior, parameters, and return value.

   **Requirements**

   1. Use the accumulator pattern with a dictionary, as explained below.

   2. Create an empty dictionary and assign it to a variable named `scoreboard`.

   3. Call `find_publishers()` and pass to it `bestseller_lists`.

   4. Loop through the return value of the function call to access each `publisher`.

   5. Within the loop, add a new key-value pair to the `scoreboard` dictionary. The key must be the
   `publisher` loop variable and the value must be the return value of `score_publisher()` when
   passing `bestseller_lists` and the `publisher` loop variable as arguments.

   6. Return the `scoreboard` dictionary.

2. After implementing `create_scoreboard()` return to the `main()` function.

3. Call `create_scoreboard()` passing it the `fiction_bestsellers` list. Assign the return value to
a variable named `fiction_publishers_scoreboard`.

   Uncomment the `assert` statement. The `fiction_publishers_scoreboard` list _must_ match the value
   of the `fiction_publishers_scoreboard_test` variable

4. Assign the value "stu-fiction_publishers_scoreboard-2024.json" to a variable named `filepath`.

5. Call the function `write_json` and pass to it as arguments `filepath`, `fiction_publishers_scoreboard`.
Compare your output file to the test fixture file `fxt-fiction_publishers_scoreboard.json`. Both
files _must_ match, line for line, and character for character.

## End of Problem Set 08
