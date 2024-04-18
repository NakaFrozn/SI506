# SI 506 Exam 03 Review

## 1.0 Challenge 01

1. Separate the string named `orbital` into a list of words. Assign the variable `words` to the new
   list.

2. Loop over the _same_ expression used to create the list `words`. Access the __first letter__ of
   each word and assign it to the string named `acronym` using addition assignment. When complete
   `acronym` must equal `"ISS"`.

## 2.0 Challenge 02

1. Call the function `read_csv()` and return the data contained in the file named "data-nasa-planets.csv".
   Assign the variable named `data` to the list returned by the function call.

2. Retrieve the headers row from `data`. Assign the list to the variable named `headers`.

3. Retrieve the indexes for the header elements "name" and "length_of_day_hours".  Assign the return
   values to `name_idx` and `len_day_idx`.

4. Loop over the planets in `data` employing a "standard" `for` loop.

5. If a planet's length of day in hours is between `8.0` and `32.0` (exclusive), append the name of
   the planet to an accumulator list named `planets`.

## 3.0 Challenge 03

1. Take the `for` loop you implemented for the previous challenge and re-implement as a list
   comprehension.  Assign the variable `planets` to the new list.

## Challenge 04

1. Loop over the planets in `data` employing a "standard" `for` loop.

2. Inside the loop block, __unpack__ the last two planet elements into the variables `has_rings` and
   `has_mag_field`.

3. If a planet does not possess a ring system (i.e., `"False"`) but possesses a global magnetic
   field (i.e., `"True"`) append the planet's __name__ to the accumulator list named `planets`.

   :bulb: Recall that `name_idx` is available for use.

## 5.0 Challenge 05

1. Loop over a sequence of numbers provided by the `range` type. Instantiate an instance of`range`
   with a start value of `1` and stop value equal to the length of `data`.

2. Inside the loop block check if the truth value of the last element of each planet (i.e.,
   "global_magnetic_field") in `data` is `Falsy`. Employ the logical `not` operator in your expression.

3. If the planet's "global_magnetic_field" truth value is "Falsy" (i.e., `False`), append the
   planet's name to the accumulator list named `planets`.

## 6.0 Challenge 06

1. In `main()`, create an instance of `Path` that provides the __absolute__ path to the
   __parent directory__ of __this__ Python script. Assign the variable `parent_path` to the `Path`
   object.

2. Create a new `Path` object by joining `parent_path` to the filename "data-nasa-planets.csv". Call
   a `Path` method to accomplish the task. Assign the variable `filepath` to the new `Path` object.

## 7.0 Challenge 07

1. Implement the function named `planet_mass`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

   :exclamation: Code defensively. If the caller passes a value to the function that would trigger a
   runtime exception during the conversion process, the exception _must_ be "caught" and the value
   `None` returned to the caller instead of the original value.

2. Call the built-in function `sorted()` and pass it the arguments required to sort `data` by the
   mass of each planet in __reverse order__.  Assign the variable named `planets` to the new list.

## 8.0 Challenge 08

1. Call the function `read_json` and pass it the argument "data-nasa-planets.json". Assign the
   variable `data` to the return value.

   :bulb: You are now working with a list of nested planet dictionaries.

2. Access the "number_of_moons" value of the fifth planet in the list (i.e., Jupiter). Assign the
   value accessed to the variable `jupiter_num_moons`.

3. Next, access the "orbital_period_days" value of the second to last planet in the list (i.e., Neptune). Assign the value accessed to the variable `neptune_orbit_period_days`.

## 9.0 Challenge 09

1. Create a list comprehension that creates a new list of planet dictionaries in which only the
   planet "name" and "number_of_moons" constitute the key-value pairs of each nested dictionary.
   Structure each nested dictionary as follows:

   ```python
   [
       {
           "name": < "name" value >,
           "moon_count": < "number_of_moons" value >
       },
       ...
   ]
   ```

2. Assign the variable `planets` to the new list.

3. Uncomment the call to `write_json()` and check the output.

## 10.0 Challenge 10

1. You have been provided with an the empty accumulator list named `planets`. Your task is to
   populate the dictionary with nine (`9`) planet dictionaries sourced from `data` structured as
   follows:

   ```python
   planets = {
       "Mercury": {
          "mass_1024kg": 0.33,
          "diameter_km": 4879,
          ...
          },
       "Venus": {
          "mass_1024kg": 4.87,
          "diameter_km": 12104,
          ...
          },
       ...
   }
   ```

2. Loop over the planets in `data` employing a "standard" `for` loop. Each nested planet dictionary
   is structured currently as follows:

   ```python
   [
      {
         "name": "Mercury",  # utilize as the new key
         "mass_1024kg": 0.33,
         "diameter_km": 4879,
         ...
      },
      ...
   ]
   ```

3. Inside the loop access each planet's name value. Assign the variable `name` to the planet name.
   Then create a nested dictionary employing `name` as the key and an __empty dictionary__ as
   the value.

4. Next, add an __inner loop__ that loops over each planet dictionary's items (i.e, key and value).
   Check each key. If the key __does not equal "name"__ add the key-value pair to the new planet
   dictionary in `planets`.

5. Uncomment the call to `write_json()` and check the output.

## 11.0 Challenge 11

1. Re-implement the nested `for` loop that you created in the previous challenge using a dictionary
   comprehension.

   :bulb: You will need to implement a nested dictionary comprehension to properly assign the
   dictionary of key value pairs to each planet key.

2. Uncomment the call to `write_json()` and compare the output to the previous challenge's output.

## 12.0 Challenge 12

1. Write a dictionary comprehension based on `planets` that creates a new dictionary containing only
   those planets whose "mean_temperature_c" is greater than zero (`0`).

2. If a planet meets the above criteria utilize the current key (e.g, the planet's name) as the key.
   Restrict the value assigned to the key to __only__ the planet's "mean_temperature_c" value.

3. Assign the new dictionary created by the comprehension to a variable named `cold_planets`.

   :exclamation: This is the dictionary that you __must__ create:

   ```python
   {
       "Mars": -65,
       "Jupiter": -110,
       "Saturn": -140,
       "Uranus": -195,
       "Neptune": -200,
       "Pluto": -225
    }

4. Uncomment the call to `write_json()` and check the output.
