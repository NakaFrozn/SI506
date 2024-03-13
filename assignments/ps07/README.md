# SI 506: Problem Set 7

## This week's Problem Set

This week's problem set will focus on dictionaries (associative arrays).

## Background

For this problem set, you are provided with a CSV file containing horror movies data sourced from
the Open Movie Database's API ([OMDb API](https://www.omdbapi.com/)) and a CSV containing
information about the amount of [jump scares](https://en.wikipedia.org/wiki/Jump_scare) in the movie
sourced from [Where's the Jump?](https://wheresthejump.com/full-movie-list/). The 'Where's the Jump?'
site also maps out the time of each jump scare.

- `data-horror_movies.csv`: Each row contains information about a horror movie.
- `data-movie_jumpscares.csv`: Each row contains information about the movie's number of jump scares
  and jump scare rating.

## Problem Set Setup

The functions `read_csv_to_dicts()` and `write_dicts_to_csv()` have been defined for you. Details on
the functionality of these are provided in the docstring of the function.

:bulb: Note that the `pprint` module has been imported for you. While not required to pass the
autograder, you may find it helpful to construct an instance of `PrettyPrinter` to display
your output in a more human-readable format since the output will be a list of dictionaries,
where each dictionary is one row from the csv file.

The `horror_movies` contain the following element(s):

```python
[
{
"Title": "< Movie Title >",
"Year": "< Movie Year >",
"Rated": "< Viewer Rating >",
"Released": "< Movie Release Date >",
"Runtime": "< Movie Runtime >",
"Genre": "< Movie Genre >",
"Director": "< Movie Director >",
"Writer": "< Movie Writer >",
"Actors": "< Movie Actors >",
"Plot": "< Movie Plot >",
"Language": "< Movie Language >",
"Country": "< Country of Movie >",
"Awards": "< Movie Awards >",
"imdbRating": "< Movie IMDB Rating >"
},
...
]
```

The `jumpscares` contain the following element(s):

```python
[
{
"Movie Name": "< Movie Title >",
"Director": "< Movie Director >",
"Year": "< Movie Year >",
"Jump Count": "< Movie Count of Jump Scares >",
"Jump Scare Rating": "< Movie Jump Scare Rating >",
"Netflix (US)": "< Movie Availability on Netflix >"
},
...
]
```

## Problem 01 (30 Points)

**Task:** Clean the `horror_movies` list using a couple of helper functions.

1. Within the `main()` function call `read_csv_to_dicts()`.

   1. Instantiate absolute Path() instances for the horror movies CSV file (**'data-horror_movies.csv'**)
   and the jump scare data CSV file (**'data-movie_jumpscares.csv'**), assigning them to the variables
      `filepath_movies` and `filepath_jumpscare` respectively.

   2. Pass the filepath object for the horror movies data to `read_csv_to_dicts()` and assign the variable
      `horror_movies` to the return value.

   3. Pass in the filepath object for the jump scare data to `read_csv_to_dicts()` and assign the variable
      `jumpscares` to the return value.

2. Implement `clean_runtime()`. Review the function's docstring regarding its expected behavior, parameters,
   and return value.

   _Requirements_

   1. Inside the clean_runtime function, access the value associated with the `"Runtime"` key in the
      provided movie dictionary. This value should be a string representing the runtime of the movie,
      such as "120 min."
   2. Use the appropriate string method to separate the numeric part and the unit.
      Assign only the first element of the resulting list (the numeric part) back to the `"Runtime"`
      key in the movie dictionary.

      :bulb: The `split()` method and assignment of the resulting list _must_ be done in one line.

   3. Return the modified movie dictionary.

3. Implement `convert_to_int()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   _Requirements_

   1. Inside the function, loop through the key-value pairs of the movie dictionary using the
      appropriate dictionary method.
   2. For each key-value pair, use a `try` and `except` block to handle conversion attempts. This will
      allow you to safely attempt to convert values to integers.
   3. Inside the `try` block, use the appropriate built-in `type` function to try to convert the value
      to an integer. If the conversion is successful, update the key in the movie dictionary with the
      integer value.
   4. In the `except` block, catch any the appropriate exception that may occur. Leave the key-value
      pair unchanged if the value cannot be converted to an integer.

4. Implement `clean_row()`. The purpose of this function is to apply two helper functions,
   `clean_runtime()` and `convert_to_int()`, to the movie dictionary. Review the function's
   docstring regarding its expected behavior, parameters, and return value.

5. After implementing `clean_row()` and its helper functions, return to the `main()` function.
   Call `clean_row()` on each dictionary in `horror_movies` and `jumpscares`.

## Problem 02 (30 Points)

**Task:** Filter the `horror_movies` to obtain movies assigned to the action and horror genre.

1. Implement `filter_movie_by_genre()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value.

   _Requirements_

   1. In the function block implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" list.
   2. Use a standard for loop to iterate through the `movies` parameter, which is a list of
   dictionaries representing different movies.
   3. Inside the loop, check if the `genre` is included in the `"Genre"` key of each dictionary
      representing a movie within the `horror_movies` list using case-insensitive matching.
   4. If the condition is met (i.e., the movie's genre matches the specified genre), append the
      dictionary to the accumulator list.

2. After implementing `filter_movie_by_genre()`, return to the `main()` function. Test
   `filter_movie_by_genre()` by passing to it `horror_movies` and the genre `"action"`
   and assigning the return value to the variable `action_movies`.

3. In our `horror_movies` list, some movies may not explicitly mention "Horror" in their genre strings.
To ensure the accuracy of our `horror_movies` list, we can use the `filter_movie_by_genre()` function
as follows:
   1. Pass the `horror_movies` list of dictionaries as an argument.
   2. Provide the genre string "horror" to the function.
   3. Assign the function's return value back to the `horror_movies` variable.

## Problem 03 (25 Points)

**Task:** Create a dictionary which has the count of movies for each viewer rating.

1. Implement `count_movie_by_rating()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value.

   _Requirements_

   1. Create an accumulator variable (name of your choice) and set it to 0.
   2. Iterate through the `movies` list, where each element is a dictionary representing a movie.
   3. For each movie dictionary, check if the value of the `"Rated"` key matches the `target_rating`
      using case-insensitive matching. If they match, increment the accumulator variable by 1.

2. After implementing `count_movie_by_rating()`, return to the `main()` function. Create an empty
   dictionary called `movie_ratings_count`.

3. Loop over the provided `unique_ratings` list (given in the code) and create new keys in the
   `movie_ratings_count` dictionary for each rating. Assign the count of movies with their respective
   rating by calling the `count_movie_by_rating()` function.

The resulting `movie_ratings_count` dictionary should contain the key-value pairs,

```python
{"PG": "< int >", "PG-13": "< int >", "R": "< int >", "Not Rated": "< int >", "Passed": " < int > ",
"Unrated": "< int >"}
```

## Problem 04 (20 Points)

**Task:** Add a new key-value pair to the `horror_movies` list for `Jumpscare_count` and
`Jumpscare_rating`.

1. Implement `get_jumpscares()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

   _Requirements_

   1. Iterate through the `jumpscares` list using a standard for loop, where each element is a
      dictionary representing jump scare information.
   2. For each dictionary in the list, check using the appropriate key if the movie name matches the
      `movie_title` parameter passed to the function using case-insensitive matching. If they match,
      return a tuple with the first value as the jump count and the second value as the jump scare
      rating from the dictionary. Use the keys `"Jump Count"` and `"Jump Scare Rating"` to access
      these values.
   3. If the movie name is not found, return a tuple with both values as `None`. This indicates that
      the movie name was not found in the jumpscare data.

2. After implementing `get_jumpscares()`, return to the `main()` function. Call the function
   `get_jumpscares()` on each movie dictionary in the `horror_movies` list and use sequence unpacking to
   extract the jump count and jump scare rating. Create two new keys in each movie dictionary,
   `"Jumpscare_count"` and `"Jumpscare_rating"`, and assign the jump count and jump scare rating return
   values to these keys.

## Problem 05 (30 Points)

**Task:** Find all horror movies in the `horror_movies` list with a release year between 2018 and
2023 (inclusive) and have an imdb score greater than 7.0 (inclusive).

1. Implement `filter_movies_by_year_and_imdb()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value (if any).

   _Requirements_

   1. Create an empty accumulator list to store the dictionaries of horror movies that meet the
      filtering conditions.
   2. Iterate through the `movies` list parameter using a range type `for` loop. Each element in the
      `movies` list parameter is a 'movie' represented as a dictionary.
   3. For each 'movie' dictionary, extract the release year and IMDb score. You can
      use the keys `"Year"` and `"imdbRating"` in the dictionary.
   4. Check if the movie's release year is within the specified lower and upper limits and if its
   IMDb score meets or exceeds the provided threshold, using a single reference to the `release_year`
   variable.
   5. If the movie meets both conditions, append the 'movie' dictionary to your accumulator list.

2. After implementing `filter_movies_by_year_and_imdb()` return to the `main()` function. Call the
   `filter_movies_by_year_and_imdb()` on `horror_movies` to filter horror movies that were released
   between 2018 and 2023 (inclusive) **and** have an imdb score greater than 7.0 (inclusive). Assign
   the return value to the variable `all_recent_movies`

## Problem 06 (30 Points)

**Task:** Check for all horror movies in the `horror_movies` list with writers that have a name
belonging to a predefined list _and_ have a runtime greater than 100 minutes.

1. Implement `search_movie_writer()`. Review the
   function's docstring regarding its expected behavior, parameters, and return value.

   _Requirements_

   1. Loop through the `search_terms` using a standard `for` loop. For each element/keyword in the
      `search_terms` list, check whether it appears in the movie's writers using a case-insensitive
      search.
   2. If the element/keyword is found within the "Writer" value, return `True`. If none of the
      `search_terms` match any of the movie's writers, the function should return `False` after
      checking all the search terms.

2. After implementing `search_movie_writer()` return to the `main()` function. Iterate over
   `horror_movies` and call the function `search_movie_writer()` on each movie dictionary. Use the
   list, assigned to the variable `writer_names` (provided for you), as the `search_terms`
   parameter to return all movie dictionaries that include these writer names in their writers.
   Implement a conditional to check whether `search_movie_writer()` returns `True`; if the
   condition is met, add the movie dictionary to the variable `writer_movies`.

3. Implement `check_movie_runtime()`. Review the
   function's docstring regarding its expected behavior, parameters, and return value.

   _Requirements_

   1. Create an accumulator list to store horror movies that satisfy the condition.
   2. Use a standard `for` loop to iterate through the `horror_movies` list, and for each movie
      represented as a dictionary:

      - Extract the runtime value from the movie dictionary using the key `"Runtime"`, converting
         it to an integer.
      - Check if the extracted movie runtime is greater than or equal to the `runtime` threshold
        provided as an argument to the function.
      - If the condition is met, append the current movie dictionary to the accumulator list.

   3. Return the final accumulator list

4. Call `check_movie_runtime()` and pass to it the `writer_movies` list and filter for horror movies
   that have a run time greater than 100 minutes (inclusive). Assign the return value to
   `long_writer_movies`.

## Problem 07 (75 Points)

**Task:** Create a list of dictionaries with movie data that have an above average imdb and jumpscare
rating.

1. Implement `get_value()`. This function checks if a certain
   value exists in a dictionary using its key. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   _Requirements_

   1. Inside the function, check if a parameter value exists in the dictionary. If the value exists,
      return the value. If not, return `None`.

2. Return to `main()`. And call `get_value()`.

   1. Extract the value stored in the `"Title"` key by calling `get_value()` and passing the fourth
      element in the `horror_movies` list and the key `"Title"` Assign the output to the variable
      `movie_title`.
   2. Extract the value stored in the `"Rated"` key by `calling get_value()` and passing the fourth
      element in the `horror_movies` list and the key `"Rated"` Assign the output to the variable
      `movie_viewer_rating`.

3. Implement `calculate_avg()` which will be used to calculate the average imdb
   and jumpscare scores. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   _Requirements_

   1. Initialize a counter variable with an appropriate start value. This variable will be used to
      accumulate the total score based on the parameter passed.

   2. Utilize a standard `for` loop to iterate through the `movies` list parameter. For each movie
      dictionary element within `movies` representing a 'movie':

      - Access the specific type of score (e.g., "imdbRating", "Jump Scare Rating") specified by
        the `score_type` argument.
      - For each movie dictionary extract the score using the helper function `get_value()` to
        extract the score value. This is necessary to handle cases where the score might not exist.
      - If the condition is met, convert the extracted score to a floating-point number and add
        its value to the counter accumulator variable.

   3. After looping through all the `horror_movies`, calculate the average score by dividing the
      resulting accumulator value by the total number of horror movies in the `horror_movies` list.

   4. Return the calculated average score as a floating-point value rounded to one decimal point.
      This serves as the result of the function.

4. After defining the `calculate_avg()` function, return to the `main()` function and call the
   `calculate_avg()` function twice, once to calculate the average IMDb rating and once to calculate
   the average jumpscare rating. Assign the outputs to `avg_imdb_rating` and `avg_jumpscare_rating`
   respectively.
5. Use both `avg_imdb_rating` and `avg_jumpscare_rating` to create a list of dictionaries containing
   horror movies with above average imdb rating and jumpscare rating.

   1. Create an empty list named `high_rated_movies` to store high-rated horror movies.
   2. Set up a standard `for` loop to iterate over each dictionary representing a movie in `movies`.
   3. Inside the loop, use `get_value()` to extract the IMDb and jumpscare ratings for the current
      movie. Verify that both ratings are not None.
   4. Use conditional statements to compare the extracted IMDb and jumpscare ratings with the average
      IMDb and jumpscare ratings calculated earlier. Movies are considered "high-rated" if both the
      IMDb and jumpscare ratings are greater than the respective averages.

      :bulb: Ensure that you are converting each movie's IMDb and jumpscare rating into the correct
      format when making the comparison to their respective averages.

   5. If a movie meets the criteria (high-rated), create a dictionary literal for that movie
      containing its title, IMDb rating, and jumpscare rating and append the dictionary to
      `high_rated_movies` list. Example of key-value pairs to include:

      ```python
      {
      "Title": "< Movie Title >",
      "IMDb_rating": "< Movie IMDb Rating >",
      "Jumpscare_rating": "< Movie Jump Scare Rating >"
      }
      ```

## Problem 08 (10 Points)

**Task:** Create a list of dictionaries with movie data that have been nominated for or have won an
Oscar.

1. Implement `get_awards()` which will be used to check if a movie has any Oscars
   related information. Review the function's docstring regarding its expected behavior, parameters,
   and return value.

   _Requirements_

   1. Extract the value associated with the `award_key` from the `movie` dictionary.
   2. Check if the words "oscar" or "oscars" are present in the extracted value. If "oscar" or
      "oscars" is found in the awards, we return its original value associated with the `award_key`,
      if not return `False`.

2. After defining the `get_awards()` function, return to `main()` and create a `for` loop that
   iterates through all the items of `horror_movies`. On each movie, call the `get_awards()`
   function and pass it the appropriate parameters. Store the resulting value in a variable called
   `no_of_awards`.

3. Add a conditional check to see if the `no_of_awards` variable has a value, or is false. If it
   does have a value, append a dictionary comprising the following key-value pairs.

   ```python
   {
   "Title": "< Movie Title >",
   "Director": "< Movie Director >",
   "Oscars Record": "< no_of_awards >"
   }
   ```

4. Lastly, call `write_dicts_to_csv()` and pass to it the following three arguments: the filepath
   `stu-oscar_movies.csv`, the list `oscar_movies`, and the appropriate `dict_keys` object that
   provides the "fieldnames" for the CSV file.
