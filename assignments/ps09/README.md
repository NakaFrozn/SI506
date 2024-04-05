# SI 506: Problem Set 09

## This week's Problem Set

This week's problem set focuses on
[list](https://www.w3schools.com/python/python_lists_comprehension.asp)
and [dictionary](https://www.datacamp.com/tutorial/python-dictionary-comprehension) comprehensions.

❗Unlike previous weeks, we have not included in this problem set
  template commented out `print()` function
calls or `assert` statements. At this point in the course, you should be
 able to call the `print()`
function yourself and/or craft your own `assert` statements to test your code.

## Background

The data from this week consists of New York Times articles that focus on technology usage in
different countries around the world.

## Heed this suggestion

:bulb: If you are new to writing Python list and dictionary comprehensions, the teaching team
recommends that you first implement a standard `for` loop (nested or otherwise) to ensure that your
code is behaving as expected. Once you have a working `for` loop, comment it out, and then use the
commented out code to construct the appropriate list or dictionary comprehension. This approach was
demonstrated in class and should help ease the transition to writing comprehensions.

## Black Formatter and auto grader behavior

:exclamation: The majority of the list and dictionary comprehensions that you implement for this
assignment will comprise single line comprehensions. However, single
line comprehensions that exceed
`100` characters in length will be reformatted to span multiple lines after you run the Black
Formatter. This is expected behavior designed to enhance readability.

:bulb: Remember, the Black Formatter is your friend; use it to reformat your code prior
to uploading your submission to Gradescope.

:exclamation: Pay particular attention to variable naming requirements. Loop variable names will be
specified and failure to utilize the specificed names will result in test failures and loss of
points.

## Problem 01

**Task**: Create a list of New York Times technology-themed article headlines and website urls.

1. In the `main()` function, create a `Path` instance by passing the following filename:
   `"data-nyt-articles-tech.json"`. Then call the `Path` object's `resolve()` method to render the
   path absolute. Assign the `Path` object to a variable named `filepath`.

2. Call the provided `read_json()` and pass the following argument: `filepath`. Assign the return
   value to a variable named `nyt_tech_raw`.

3. Implement the function named `create_headline_url_list()`.
   Review the function's docstring regarding its expected behavior,
   parameters, and return value (if any). Ensure the implementation
   is performed using a single list comprehension.

   **Requirements**

   1. Write a list comprehension that loops over `data`.

      :exclamation: Your loop variable **must** be named `article`
       and the function block is limited
       to a single `return` statement.

   2. For each `article`, return **a tuple** containing
      the corresponding `"main"` headline (value
      from the nested `"headline"` dict) and `"web_url"`

      :exclamation: Access the article's `"main"` value from `"headline"` using double subscript
       notation.

   3. Return the list created by this comprehension
      directly to the caller (single line function
      block only).

4. After implementing `create_headline_url_list()`, return to `main()`.
   Call the function`create_headline_url_list()` passing the following
   argument: `nyt_tech_raw`. Assign the
   return value to a variable named `headline_url_list`.

5. Assign the string `"stu-headline-url-list.json"` to a
   variable named `filename`.

6. Call the function `write_json` and pass `filename` and `headline_url_list` as arguments. Compare
   the output file to the test fixture file `fxt-headline-url-list.json`. Both files _must_ match,
   line for line, and character for character.

## Problem 02

**Task**: Filter the list of New York Times technology-themed
          articles to obtain a clean subset of
          articles employing a dictionary comprehension nested in a list comprehension.

1. Implement the function named `filter_articles()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value (if any).

   **Requirements**

   1. Write a dictionary comprehension nested within a list comprehension that retains only the
      key-value pairs that are **not** members of the `keys_to_exclude` list.

      :bulb: The teaching team recommends highly that you first implement a standard **nested**
      `for` loop before attempting to implement the alternative dictionary comprehension nested
      inside a list comprehension as described below **before** attempting to craft the nested
      comprehension.

      Assign an empty list to a local variable in order to accumulate the filtered articles. Then
      implement a nested loop per the requirements below:

      * Outer loop: iterate over the articles.

        :exclamation: The loop variable **must** be named `article`.

      * Inner loop: iterate over each article dictionary's key-value pairs. Call the appropriate
        dictionary method to access each key and its associated value. Retain only the key-value
        pairs whose keys are not found in the `keys_to_exclude` list (filter with an `if`
        statement). The goal is to construct a slimmer dictionary representation of each article.

        :exclamation: The loop variables **must** be named `k` and `v` respectively.

      After the loop terminates return the accumulator list of filtered articles to the caller.

   2. After implementing the nested loop return to `main()` and implement steps 2.2-2.4. Call the
      function `filter_articles()` and assign the return value to a variable named
      `filtered_articles`. Then call the function `write_json()` and write `filtered_articles`
      to a file named `"stu-nyt-tech-filtered.json"`. Compare the output file to the test fixture
      file.

   3. If the files match, return to `filter_articles()`.
      Comment out the empty list variable
      assignment and the standard nested loop. Utilize the commented out code to construct the
      required dictionary comprehension nested within a list comprehension. Run your code and
      compare the output file to the test fixture file. If the files match, submit your code to
      Gradescope for scoring after formatting it using Black.

2. After implementing `filter_articles()` return to the `main()` function and call the function
   `filter_articles()` passing the `nyt_tech_raw` list and the `keys_to_exclude` list to it as
   arguments. Assign the return value to a variable named `nyt_tech_filtered`.

3. Assign the string `"stu-nyt-tech-filtered.json"` to a variable named `filename`.

4. Call the function `write_json` and pass `filename` and `nyt_tech_filtered` to it as arguments.
   Compare the output file to the test fixture file `fxt-nyt-tech-filtered.json`. Both files _must_
   match, line for line, and character for character.

## Problem 03

**Task**: Filters out articles which have empty lists as values and 
          convert publication dates to datetime objects.

1. Implement the function named `filter_empty_keywords()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value (if any). Ensure that the
   implementation is performed using a single list comprehension.

   **Requirements**

   1. Create a new list of articles from the list of dictionaries `data` that do not have empty
      lists as values for the `"keywords"` key.

      :bulb: Your loop variable _must_ be named `article`.

   2. Return the list created by this comprehension. Note that this function _must_ only
      consist of a `return` statement.

2. After implementing `filter_empty_keywords()`, return to the `main()` function. Call the
   function `filter_empty_keywords()` passing the following argument: `nyt_tech_filtered`.
   Assign the return value to a variable named `nyt_tech_cleaned`.

3. Implement the function named `convert_published_date_value()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value (if any).
   This question does _not_ involve comprehensions, only a standard nested `for` loop.

   **Requirements**

   1. Loop through `data` using a standard for loop.

   2. Nested within this loop, write a standard for loop that iterates over the keys of each
      `article`.

   3. Write an `if` statement that implements the appropriate dictionary method to check
   whether the current key is equal to `"pub_date"`.

   4. If the current key is `"pub_date"`, convert the string value of `"pub_date"` to a `datetime`
      object using the `strptime()` _or_ `fromisoformat()`method.

      :bulb: The `datetime.strptime()` method takes a string and
      converts it to a a `datetime` object.
      The first parameter is the date string. The second parameter is `"%Y-%m-%dT%H:%M:%S%z"`.

      :bulb: The `datetime.fromisoformat()` method takes a string and converts it to a `datetime`
      object. Pass the string with a colon inserted at the third to last
      position using index splicing
      and string concatenation. For example, if the last four characters
      of the string are `"0000"`,
      the colon should be inserted as `"00:00"`.

   5. After the for loop, return `data`.

4. After implementing `convert_published_date_value()`, return to `main()` and call the function
   `convert_published_date_value()` passing the following argument: `nyt_tech_cleaned`. Assign the
   return value to a variable named `nyt_tech`.

5. Assign the string `"stu-nyt-tech-cleaned.json"` to a variable named `filename`.

6. Call the function `write_json` and pass `filename` and `nyt_tech` as
   arguments. Compare the output
   file to the test fixture file `fxt-nyt-tech-cleaned.json`. Both files
   _must_ match, line for line, and character for character.

## Problem 04

**Task**: Obtain a list of organizations mentioned in the New York technology-themed articles.

1. Implement the function named `get_organization_names()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value (if any).

   **Requirements**

   1. Implement a list comprehension that creates a list with the values
      corresponding to the `"value"` key in an `article`'s keywords.

      :bulb: Your loop variable _must_ be named `keyword`.

   2. Write an `if` statement in the comprehension that checks if the value corresponding to the
      `"name"` key within `"keywords"` is equal to `"organizations"`.

   3. Return the list created by this comprehension. Note that this
      function _must_ only consist of a
      `return` statement.

2. After implementing `get_organization_names()`, implement `get_organization_by_type()`.
   Review the function's docstring regarding
   its expected behavior, parameters, and return value (if any).

   1. Create an empty list named `tech_organizations`.

   2. Iterate through the `articles` list using a standard for loop.

   3. Within the loop, call the `get_organization_names()` function
      passing the `article` dictionary
      as an argument and assign the return value to a variable named `org_names`.

   4. Still within the loop, write an `if` statement to check that `org_names` is _truthy_
      (e.g., not `None`, 0, `False`, etc.).

   5. If `org_names` is _truthy_, create a nested, standard for loop
      that iterates through `org_names`.

   6. Within the for loop, write an `if` statement to check that each   name in `org_names` does not
      already exist in `tech_organizations`.

   7. In the case that the name does not already exist in
      `tech_organizations`, append it to the list.

3. After implementing functions, return to `main` and call
   `get_organization_by_type()` by accessing the `nyt_tech` to a
   variable named `tech_organizations`.
4. Assign the string `"stu-unique-tech-organizations.json"` to a variable named `filename`.

5. Call the function `write_json` and pass `filename` and
   `tech_organizations` as arguments. Compare
   the output file to the test fixture file
   `fxt-unique-tech-organizations.json`. Both files _must_
   match, line for line, and character for character.

## Problem 05

**Task**: Filter New York Times technology-themed articles based on location.

1. Implement the function named `get_news_by_location()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value (if any). Ensure that the implementation is
   performed using a single list comprehension.

   **Requirements**

   1. This list comprehension contains a nested loop and a compound conditional if statement.

   2. The comprehension's outer loop iterates though each `article` in `data`, and the inner loop
      iterates though each `keyword` in its `"keywords"` values.

      :bulb: Your outer loop variable _must_ be named `article` and your
      inner loop variable _must_ be named `keyword`.

   3. The `if` condition checks if the value corresponding to the `"name"` key within `keyword` is
      equal to the string `"glocations"` _and_ if the location is in the
      list of values corresponding
      to the `"value"` key within `keyword`.

      :exclamation: Your if statement _must_ evaluate
      two conditions using the appropriate logical
      operator (e.g., and, or, not). Note that due to short-circuiting, it is best practice to list
      the more general of the two conditions first.

   4. Return the list created by this comprehension.
      Note that this function _must_ only consist of a
      `return` statement.

2. After implementing `get_news_by_location()`, return to `main()`. Call
   the `get_news_by_location()`
   function and pass `nyt_tech` and the string `"Calif"` as arguments. Assign the return value to
   `calif_news`.

3. Assign the string `"stu-nyt-calif-tech-articles.json"` to a variable named `filename`.

4. Call the function `write_json` and pass `filename` and `calif_news` as arguments. Compare the
   output file to the test fixture file `fxt-nyt-calif-tech-articles.
   json`. Both files _must_ match,
   line for line, and character for character.

## Problem 06

**Task**: Obtain a list that classifies New York Times technology-themed
          article headlines as active or archived.

1. Implement the function named `show_archival_status()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value (if any). Ensure that the implementation is
   performed using a single list comprehension.

   **Requirements**

   1. This list comprehension employs `if-else` logic.

      :bulb: Your loop variable _must_ be named `article`.

   2. Access the `"headline" "main"` key using double subscript notation. The function returns a
      list of tuples that categorizes each article headline as either `"Active"` or `"Archived"`.

   3. The `if` condition checks if the value corresponding to the `"pub_date"` key within the
      `article` is greater than or equal to `active_year_threshold`.

      :exclamation: Note that the `data` parameter specific to this
      function is a list of dictionaries
      with `"pub_date"` converted to `datetime` object. To extract the
      year from a datetime object in
      Python, simply call `.year` on the DateTime object and the year
      will be returned as an integer.

   4. If the above condition is satisfied, the article is classified as `"Active"`. Create a tuple
      containing the article's main headline and corresponding status.
      Access the `"headline" "main"`
      value using double subscript notation.

   5. In the case that the value corresponding to the `"pub_date"` key within the `article` is less
      than `active_year_threshold`, classify the article's status as `"Archived"` by creating a
      tuple containing the article's main headline and appropriate status. Access the `"headline"
      "main"` value using double subscript notation.

   6. Return the list created by this comprehension. Note that this
      function _must_ only consist of a
      `return` statement.

2. After implementing `show_archival_status()`, return to `main()`. Call
   the `show_archival_status()`
   function and pass `nyt_tech` and the integer `2022` as arguments. Assign the return value to
   `article_status`.

3. Assign the string `"stu-article-status.json"` to a variable named `filename`.

4. Call the function `write_json` and pass `filename` and
   `article_status` as arguments. Compare the
   output file to the test fixture file `fxt-article-status.json`. Both
   files _must_ match, line for
   line, and character for character.

## Problem 07

**Task**: Obtain a list of authors of New York Times technology-themed articles.

1. Implement the function named `format_author_name()`. Review the
   function's docstring regarding its
   expected behavior, parameters, and return value (if any).

   **Requirements**

      1. This function does not employ a list comprehension.

      2. You must employ an f-string to return the author's name formatted as described in the
         docstring.

      3. Ensure that the first character of the first and last names is uppercase
         (e.g. `"biersdorfer"` to `"Biersdorfer"`).

         :bulb: Review the w3schools string methods page for hints on the string method to employ.

   After implementing `format_author_name()`, return to the `main()`
   function. Call the function and
   make sure it works as expected.

2. After implementing `format_author_name()`, implement the function named `get_author_names()`.
   Review the function's docstring regarding its expected behavior, parameters, and return value
   (if any).

   **Requirements**

   1. Implement a list comprehension that loops over an article's byline person list and calls
      the author name formatter function defined earlier.

      :bulb: Your loop variable _must_ be named `person`.

   2. Return the list created by this comprehension. Note that this
      function _must_ only consist of a `return` statement.

   After implementing `get_author_names()`, return to the `main()` function. Call the function and
   make sure it works as expected.

3. After implementing `format_author_name()` and `get_author_names()`, implement the function named
   `get_unique_authors()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value (if any).

   **Requirements**

   1. Iterate through the `articles` list using a standard for loop.

   2. Within the loop, call the `get_author_names()` function passing the `article` dictionary
      as an argument and assign the return value to a variable named `authors`.

   3. Still within the loop, write an `if` statement to check that `authors` is _truthy_ (e.g., not
      `None`, 0, `False`, etc.).

   4. If `authors` is _truthy_, create a nested, standard for loop that iterates through `authors`.

   5. Within the for loop, write an `if` statement to check that each
      name in `authors` is not `None`
      and does not already exist in `unique_authors`.

   6. In the case that the name does not already exist in `unique_authors`, append it to the list.

4. After implementing `get_unique_authors()`, return to the `main()` function. Call the function
   `get_unique_authors()` and pass `nyt_tech` as an argument. Assign the return value to a variable
   named `unique_authors`.

5. Assign the string `"stu-unique-authors.json"` to a variable named `filename`.

6. Call the function `write_json` and pass `filename` and
   `unique_authors` as arguments. Compare the
   output file to the test fixture file `fxt-unique-authors.json`. Both
   files _must_ match, line for line, and character for character.


## Problem 08

**Task**: Filter New York Times technology-themed articles based on topic and organization.

1. Implement the function named `get_articles_by_topic()`  Review the
   function's docstring regarding
   its expected behavior, parameters, and return value (if any). Ensure that the implementation is
   performed using a single list comprehension.

   **Requirements**

   1. This list comprehension contains a nested loop and a compound conditional if statement.

   2. The comprehension's outer loop iterates though each `article` in
      `articles`, and the inner loop
      iterates though each `keyword` in its `article[keywords]` values.

      :bulb: Your outer loop variable _must_ be named `article` and your
      inner loop variable _must_ be named `keyword`.

   3. The `if` condition checks if the value corresponding  to the 
      `"name"` key within `keyword` is
      equal to the string `"subject"` _and_ if the `topic` is in the list of values corresponding
      to the `"value"` key within `keyword`.

      :exclamation: Your if statement _must_ evaluate two conditions using the appropriate logical
      operator (e.g., and, or, not). Note that due to short-circuiting, it is best practice to list
      the more general of the two conditions first.

   4. Return the list created by this comprehension. Note that this
      function _must_ only consist of a
      `return` statement.

   After implementing `get_articles_by_topic()`, return to the `main()`
   function. Call the function and
   make sure it works as expected.

2. After implementing `get_articles_by_topic()`, implement the function
   named`get_articles_by_organization()`.
   Review the function's docstring regarding its expected behavior,
   parameters, and return value (if any).
   Ensure that the implementation is performed using a single list comprehension.

   **Requirements**

   1. This list comprehension contains a nested loop and a compound conditional if statement.

   2. The comprehension's outer loop iterates though each `article` in
      `articles`, and the inner loop
      iterates though each `keyword` in its `article[keywords]` values.

      :bulb: Your outer loop variable _must_ be named `article` and your
      inner loop variable _must_ be named `keyword`.

   3. The `if` condition checks if the value corresponding to the
      `"name"` key within `keyword` is
      equal to the string `"organization"` _and_ if the
      `organization` is in the list of values corresponding
      to the `"value"` key within `keyword`.

      :exclamation: Your if statement _must_ evaluate two conditions using the appropriate logical
      operator (e.g., and, or, not). Note that due to short-circuiting, it is best practice to list
      the more general of the two conditions first.

   4. Return the list created by this comprehension. Note that this
      function _must_ only consist of a `return` statement.

   After implementing `get_articles_by_organization()`, return to the
   `main()` function. Call the function and
   make sure it works as expected.

3. After implementing `get_articles_by_topic()` and
   `get_articles_by_organization()`,
   return to `main()`. Call the `get_articles_by_topic()`
   function and pass `nyt_tech`
   and the string `"Artificial Intelligence"` as arguments.
   Assign the return value to `ai_articles`.

4. Now access all `ai_articles` about OpenAI.
   Call `get_articles_by_organization()` and pass `ai_articles`
   and the string `"OpenAI Labs"`. Assign the return value to
   `openai_articles`.

5. Assign the string `"stu-nyt-openai-tech-articles.json"` to 
   a variable named `filename`.

6. Call the function `write_json` and pass `filename` and `openai_articles` as arguments.
   Compare the output file to the test fixture file
   `fxt-nyt-openai-tech-articles.json`.
   Both files _must_ match,line for line, and character for character.