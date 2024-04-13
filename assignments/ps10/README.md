# SI 506: Problem Set 10

## This week's Problem Set

This week's problem set includes ten (10) problems that focus on using the `requests` module to
load data from the [Star Wars API](https://swapi.py4e.com/).

❗Similar to last week, we have not included in this problem set template commented out `print()`
function calls or `assert` [statements](https://realpython.com/python-assert-statement/). At this
point in the course, you should be able to call the `print()` function yourself and/or craft your
own `assert` statements to test your code.

## Background

This week, you will create a Python representation of the
[opening scene from _"Star Wars: Episode IV – A New Hope"_](https://youtu.be/GHsnpo8QMro?t=50).
At the beginning of every Star Wars film there occurs the iconic opening crawl, which provides some
backstory and sets the stage for what's to come. This scene opens on the planet
[Tatooine](https://starwars.fandom.com/wiki/Tatooine?so=search#Description)
emerging from a total eclipse, as a [Rebel Blockade Runner](shorturl.at/bMPUV) races through space,
pursued by an
[Imperial Stardestroyer](https://starwars.fandom.com/wiki/Imperial_I-class_Star_Destroyer).

On board the Rebel Blockade Runner and caught in laserfire passing between Rebel troopers and
Imperial Stormtroopers, we meet two robots, [R2-D2](https://starwars.fandom.com/wiki/R2-D2/Legends)
and [C-3PO](https://starwars.fandom.com/wiki/C-3PO), who are struggling to avoid the chaos and escape
on a mission from another ship passenger,
[Princess Leia Organa](https://starwars.fandom.com/wiki/Princess_Leia_Organa). After a
tremendous blast, smoke fills the corridor and, once it clears, reveals a hole in the main passageway
as the starship is overtaken by more Stormtroopers and the infamous Dark Lord of the Sith,
[Darth Vader](https://en.wikipedia.org/wiki/Darth_Vader).

## Data

You will leverage the `requests` module and a provided utility function, called `get_swapi_resource()`,
to access [JSON documents](https://realpython.com/python-json/) that represent the film, its starships,
and its characters.

## 1.0 Problem 01

**Task**: Construct the URL pattern for three (3) SWAPI resource categories and leverage
`get_swapi_resource()` to access the JSON document that represents the film, A New Hope.

1. In `main()`, utilize the provided `ENDPOINT` variable and employ the URL pattern (`/api/:category/`)
   that retrieves a collection of resources by category. Assign the URL pattern for each of the
   following categories to their respective variables.

   | category  | variable          |
   | --------- | ----------------- |
   | films     | `SWAPI_FILMS`     |
   | starships | `SWAPI_STARSHIPS` |
   | people    | `SWAPI_PEOPLE`    |

2. Then, call the provided utility function, `get_swapi_resource()`, and assign its return value to
   the variable `swapi_new_hope`. Pass to it `swapi_films` and the search parameter `"new hope"`.

   :exclamation: SWAPI will return more data than the desired object, so be sure to extract the first
   value of the returned `"results"` in the JSON you receive from SWAPI.
   **This must be done in one line.**

   :bulb: Remember, `params` is of type `dict` and its key represents the action you are taking,
   such as `"search"`, and its value represents the value you"re searching for, such as `"new hope"`.

## 2.0 Problem 02

**Task**: Create a dictionary _literal_ that
represents a "thinned" version of `swapi_new_hope`

1. Navigate to Problem 02 in `main()`. Create a dictionary _literal_
   and assign it to the variable `new_hope`. Leverage `get()` when assigning values to each of the
   following keys:

   - `"title"`
   - `"episode_id"`
   - `"opening_crawl"`
   - `"director"`
   - `"release_date"`

   Additionally, include the key `"starships"` as the last key in your dictionary literal, with an
   empty list assigned as its value.

2. The function `write_json()` has been implemented for you. Call `write_json()` with the
   filepath of `"stu-newhope_filtered.json"` and the `new_hope` dictionary. The JSON document you
   generate _must_ match the provided `fxt-newhope_filtered.json` file.

## 3.0 Problem 03

**Task**: Define a function, `create_starship()`, that returns a dictionary _literal_ that
represents a "thinned" version of each starship accessed from SWAPI.

1. Define a function called `create_starship()`, which accepts one (1) parameter:

   - `starship` (dict): a dictionary representation of the decoded JSON that contains
     starship attributes.

2. The function should return a dictionary _literal_ that also leverages the `get()`
   method to access the corresponding values for each key defined in the dictionary. Refer to
   the docstring for additional details on the specific keys and their order.

   An example return value from this function is shown below:

   ```Python
   {
      "name": "CR90 corvette",
      "model": "CR90 corvette",
      "passengers": [],
      "max_atmosphering_speed": "950",
      "length": "150"
   }
   ```

3. After defining the function, navigate to Problem 03 in `main()`. Call the function
   `get_swapi_resource()` and `create_starship()` to create
   a representation of the Rebel Blockade starship:

   - Employ a dictionary literal to create a small dictionary to hold the search term
     `"CR90 corvette"` using the appropriate key. Assign the dictionary to the variable named
     `params`.

   - In the `get_swapi_resource()` function call, pass `SWAPI_STARSHIPS` and `params` as the arguments. Assign the return value to the
     variable `swapi_corvette`.

   - Then, call the function `create_starship()`. Pass the `swapi_corvette` data. Assign the return value to the
      variable `corvette`.

   :exclamation: When calling `get_swapi_resource()`, the API will return more data than just the
   desired object, so make sure to extract the first value of the returned `"results"` in the JSON
   you get back from the API. **This must be done in one line.**

4. Then, call the function
   `get_swapi_resource()` and `create_starship()` to create
   a representation of the Imperial Stardestroyer starship:

   - Employ a dictionary literal to create another small dictionary to hold the search term
   `"destroyer"` using the appropriate key. Assign the dictionary to the variable named
   `params`.

   - In the `get_swapi_resource()` function call, pass `SWAPI_STARSHIPS` and `params` as the arguments. Assign the
     variable `swapi_stardestroyer` to the return value.

   - Then, call the function `create_starship()`. Pass the `swapi_stardestroyer` data. Assign the variable
     `stardestroyer` to the return value.

## 4.0 Problem 04

**Task**: Define 2 functions, `get_homeworld()` and `create_person()`, that attempt to,
respectively, retrieve a SWAPI representation of a home planet using the provided `url` and return a
dictionary _literal_ that represents a "thinned" version of each person accessed from SWAPI .

1. Define a function called `get_homeworld()`, which accepts one (1) parameter:

   - `url` (str): the URL pattern for a resource category

   The function should return a dictionary _literal_ that also leverages the `get()` method
   to access the corresponding values for each key defined in the dictionary. Refer to the docstring
   for additional details on the specific keys and their order.

   An example return value from this function is shown below:

   ```Python
   {
      "name": "Naboo",
      "diameter": "12120",
      "climate": "temperate",
      "terrain": "grassy hills, swamps, forests, mountains",
      "population": "4500000000"
   }
   ```
2. Define a function called `create_person()` which accepts one (1) parameter:

   - `person` (dict): a dictionary representation of the decoded JSON that contains person attributes.

   The function should return a dictionary _literal_ that also leverages the `get()` method to
   access the corresponding values for each key defined in the dictionary. It also leverages the
   `get_homeworld()` function for the appropriate key. Refer to the docstring for additional details on
   the specific keys and their order.

   An example return value from this function is shown below:

   ```python
   {
      "name": "R2-D2",
      "height": "96",
      "mass": "32",
      "birth_year": "33BBY",
      "eye_color": "red",
      "homeworld": {
         "name": "Naboo",
         "diameter": "12120",
         "climate": "temperate",
         "terrain": "grassy hills, swamps, forests, mountains",
         "population": "4500000000"},
      "dialogue": []
   }
   ```
3. After defining both functions, navigate to Problem 04 in `main()`. You will now create person
representations of R2-D2, C-3P0, and Princess Leia via the functions `get_swapi_resource()` and
`create_person()`.

   1. Create the person representation of R2-D2.

      1. Employ a dictionary literal to create a small dictionary to hold the search term
     `"R2-D2"` using the appropriate key. Assign the dictionary to the variable named
     `params`.

      2. Call `get_swapi_resource()`. Pass `SWAPI_PEOPLE` and `params` as the arguments. Assign the
      variable `swapi_r2d2` to the return value.

      3. Call `create_person()`. Pass the `swapi_r2d2` data and `SWAPI_PEOPLE`.
      Assign the variable `r2d2` to the return value.

   2. Create the person representation of C-3P0.

      1. Employ a dictionary literal to create another small dictionary to hold the search term
     `"C-3PO"` using the appropriate key. Assign the dictionary to the variable named
     `params`.

      2. Call `get_swapi_resource()`. Pass `SWAPI_PEOPLE` and `params` as the arguments. Assign the
      variable `swapi_c3po` to the return value.

      3. Call `create_person()`. Pass the `swapi_c3po` data and `SWAPI_PEOPLE`.
      Assign the variable `c3po` to the return value.

   3. Create the person representation of Princess Leia.

      1. Employ a dictionary literal to create a third small dictionary to hold the search term
      `"Leia Organa"` using the appropriate key. Assign the dictionary to the variable named
      `params`.

      2. Call `get_swapi_resource()`. Pass `SWAPI_PEOPLE` and `params` as the arguments. Assign the
      variable `swapi_leia` to the return value.

      3. Call `create_person()`. Pass the `swapi_leia` data and `SWAPI_PEOPLE`.
     Assign the variable `leia` to the return value.

   :exclamation: When calling `get_swapi_resource()`, the API will return more data than just the
   desired object, so make sure to extract the first value of the returned `"results"` in the JSON
   you get back from the API. **This must be done in one line.**

4. Finally, uncomment the two `assert` statements to check your implementation of `get_homeworld()`.

## 5.0 Problem 05

**Task**: Define a function, `board_starship()`, that returns an updated dictionary of
key-value pairs representing a starship

1. Define a function called `board_starship()`, which accepts two (2) parameters:

   - `starship` (dict): a dictionary representation of the _decoded JSON_ that contains starship
     attributes (as generated by the `create_starship` function you implemented in **problem 03**).
   - `people` (list): a list of tuples, each with;
     - **(a)** a variable assigned to the _decoded
       JSON_ representing a person (as generated by the `create_person` function you implemented in
       **problem 05**) and,
     - **(b)** a `bool` value indicating whether they are
       an intruder is at the 1st index.

2. The function should return an updated version of the `starship` dictionary. Refer to the docstring
   for additional details on the function's implementation and which key-value pairs should be
   updated or created.

3. After defining the function, navigate to Problem 06 in `main()`. Assign a list of tuples to
   the variable `people`. The first tuple _must_ contain `r2d2` and `False`. The second tuple
   _must_ contain `c3po` and `False`. The third tuple _must_ contain `leia` and `False`

4. Call the function `board_starship()` and pass to it the `corvette` and the list of
   tuples assigned to `people`.

   The updated `corvette` _must_ mirror the example below:

   ```python
   {
      "name": "CR90 corvette",
      "model": "CR90 corvette",
      "passengers": [
         {
            "name": "R2-D2",
            "height": "96",
            "mass": "32",
            "birth_year": "33BBY",
            "eye_color": "red",
            "homeworld": {
               "name": "Naboo",
               "diameter": "12120",
               "climate": "temperate",
               "terrain": "grassy hills, swamps, forests,   mountains",
               "population": "4500000000"
               },
            "dialogue": []
         },
         {
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "birth_year": "112BBY",
            "eye_color": "yellow",
            "homeworld": {
               "name": "Tatooine",
               "diameter": "10465",
               "climate": "arid",
               "terrain": "desert",
               "population": "200000"
               },
            "dialogue": []
         },
         {
            "name": "Leia Organa",
            "height": "150",
            "mass": "49",
            "birth_year": "19BBY",
            "eye_color": "brown",
            "homeworld": {
               "name": "Alderaan",
               "diameter": "12500",
               "climate": "temperate",
               "terrain": "grasslands, mountains",
               "population": "2000000000"
               },
            "dialogue": []
         }
      ],
      "max_atmosphering_speed": "950",
      "length": "150"
   }
   ```

   :exclamation: There is no need to assign the return value from this function call to a new
   variable, since we simply want to update the decoded JSON object (`corvette`) _in place_.

## 6.0 Problem 06

**Task**: Utilize `read_csv_to_dicts()` to read in additional data from `"data-troopers.csv"` and call
`board_starship()` to update the `corvette` with its occupants.

1. In `main()`, call the provided function, `read_csv_to_dicts()` and pass to it the string
   `"data-troopers.csv"`. Assign the return value to the variable `troopers`.

2. Write a list comprehension that results in a list of nested tuples representing troopers and their
   "intruder" status. Assign the list comprehension to the variable `trooper_list`. Each tuple in the
   list contains:

   - **(a)** the dictionary representation of a trooper and,

   - **(b)** the trooper's "intruder" status, as shown below:

     ```commandline
     (< trooper: dict >, < intruder status: bool >)
     ```

   1. Convert the "intruder" status element for each tuple to an integer _before_ passing it to the
      built-in `bool()` function, converting the binary data to either `True` or `False`.
      _This operation _must_ be performed within the list comprehension._

      :exclamation: Open the `"data-troopers.csv"` file and review the data. Notice that the intruder
      status is represented as binary data (1 = True; 0 = False) and that this data will be read
      in as a `str`.

3. Call `board_starship` again to add the troopers in your `trooper_list` to the relevant values of
   the `corvette` object.

## 7.0 Problem 07

**Task**: Define a function, `capture_starship()`, that returns an updated dictionary representation
of the decoded JSON representing the attacking starship.

1. Define a function called `capture_starship()`, which accepts two (2) parameters:

   - `attacker` (dict): a dictionary representation of the decoded JSON that contains attributes of
     an attacking starship.
   - `prey` (dict): a dictionary representation of the decoded JSON that contains attributes of a
     starship that is being captured.

   :exclamation: Note that `prey` will be a _boarded starship_ dictionary object, created using
   `create_starship` and updated by `board_starship` in previous problems.

   1. The function _must_ return an updated version of the `attacker` dictionary. Refer to the
      docstring for additional details on the function's implementation and which key-value pairs
      should be updated or created.

2. After defining the function, navigate to `main()`. Call the function
   `capture_starship()` and pass to it the `stardestroyer` and the `corvette`,
   in that order.

3. The updated `stardestroyer` should contain a new key-value pair `"primary_docking_bay"`
   with the docked `corvette` as its value.

:exclamation: There is no need to assign the return value from this function call to a new
variable, since we simply want to update the decoded JSON object (`stardestroyer`) _in place_.

## 8.0 Problem 08

**Task**: Define a function, `insert_dialogue()`, that updates each character's
dictionary with their dialogue.

1. Define a function called `insert_dialogue()`, which accepts two (2) parameters:

   - `person` (dict): a dictionary representation of the decoded JSON that contains people attributes.
   - `dialogue` (dict): a dictionary whose key-value pairs each represent a person and their dialogue.

   Refer to the docstring for additional details on this function's tasks, parameters, and return
   value.

2. After defining the function, navigate to Problem 09 in `main()`. Call the function
   `insert_dialogue()` two (2) times:

   - In the first function call, pass `r2d2` and the provided `dialogue` dictionary.
   - In the second function call, pass `c3po` and the provided `dialogue` dictionary.

   :exclamation: Princess Leia is mentioned by C-3PO but not seen in the opening scene and has no
   dialogue. This is why we are not calling `insert_dialogue()` for our `leia` dictionary object.

   An example return value for the `insert_dialogue()` function is shown below:

   ```python
   {
      "name": "R2-D2",
      "height": "96",
      "mass": "32",
      "birth_year": "33BBY",
      "eye_color": "red",
      "homeworld": {
         "name": "Naboo",
         "diameter": "12120",
         "climate": "temperate",
         "terrain": "grassy hills, swamps, forests, mountains",
         "population": "4500000000"
      },
      "dialogue": [
         "beep, beep, boop.",
         "boop, beep, beep.",
         "boop, beeeep!"
      ]
   }
   ```

   :exclamation: There is no need to assign the return values from these function calls to a new
   variable, since we simply want to update the decoded JSON objects _in place_.

## 9.0 Problem 09

**Task**: Leverage each of the previously defined functions, in order to create a Python
representation of the Sith Lord, Darth Vader, and add him to the `corvette`.

1. Navigate to Problem 10 in `main()`. Repeat the series of function calls from the previous problems,
   in order to;

   - acquire the JSON object representing the Sith Lord, Darth Vader,

   - create a representation of a person utilizing the data accessed from SWAPI,

   - update the `"intruder"` key of the `corvette` with the decoded JSON object representing
     Darth Vader, and

   - insert Darth Vader's dialogue into the correct key-value pair in the decoded JSON object
     representing him.

   1. Call the function `get_swapi_resource()` and pass to it `SWAPI_PEOPLE` and the search parameter
      `vader`. Assign the variable `swapi_vader` to the return value.

      :exclamation: When calling `get_swapi_resource()`, the API will return more data than just the
      desired object, so make sure to extract the first value of the returned `"results"` in the
      JSON you get back from the API. **This must be done in one line.**

   2. Call the function `create_person()` and pass to it `swapi_vader` and `SWAPI_PEOPLE`. Assign the
      variable `vader` to the return value.

   3. Assign the variable `people` to a list with one tuple. The tuple _must_ contain `vader` and
      `True`. Call the function `board_starship()` and pass to it the `corvette` and the list
      `people`.

   4. Call the function `insert_dialogue()` and pass to it `vader` and the provided `dialogue`
      dictionary.

## 10.0 Problem 10

**Task**: Shh! The droids escape! Update the `starships` key-value pair of the `new_hope` dictionary
with the final `stardestroyer` dictionary. Update the droids" dictionary objects with an `end_vessel`
key and add the 2 droids to a new key in `new_hope` called `escaped_passengers`.

1. Access the `"starships"` key of the dictionary representation of `new_hope`.
   Append the `stardestroyer` to the empty list that was assigned to `"starships"`.

2. Uncomment the provided `droids` list. Using a standard for loop, loop over the droids list to
   add the key `"end_vessel"` with the value `"escape_pod"` to the `c3po` and `r2d2` dictionary
   objects.

3. After the for loop, add an `"escaped_passengers"` key to your `new_hope` dictionary object and
   assign the `droids` list as its value.

4. The function `write_json()` has been implemented for you. Call `write_json()` with the
   filepath of `'stu-newhope_final.json'` and the `new_hope` dictionary. The JSON document you
   generate _must_ match the provided `fxt-newhope_final.json` file.
