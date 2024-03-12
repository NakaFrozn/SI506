# SI 506: Dictionaries

## Topics

1. The dictionary
2. Creating dictionaries
   1. Assign an empty dictionary to a variable
   2. Dictionary literal
   3. Built-in `dict()` function
3. Working with dictionaries
   1. Accessing a value
   2. Accessing a nested value
   3. Add a key-value pair
   4. Modify an existing value
   5. Delete a key-value pair
4. Select dictionary methods
   1. `dict.get()` method
   2. `dict.keys()` method
   3. `dict.values()` method
   4. `dict.items()` method
   5. Challenge 01
5. Dictionaries and the `csv` module
   1. The `DictReader()` class
   2. The `DictWriter()` class
   3. Challenge 02
   4. Challenge 03
6. The accumulator pattern revisted
   1. Accumulating values from a dictionary
   2. Storing accumulated values in a dictionary
   3. Challenge 04
7. Additional challenges
   1. Challenge 05
   2. Challenge 06
   3. Challenge 07

## Reference

Boomark the following [w3schools](https://www.w3schools.com/) reference page:

1. w3schools, ["Python Dictionary Methods"](https://www.w3schools.com/python/python_ref_dictionary.asp)

## Data

The file `data-whc-sites.csv` provides a listing of UNESCO World Heritage
sites.

Source: [UNESCO World Heritage Convention](https://whc.unesco.org/en/syndication)

:exclamation: Forty-three (`43`) Heritage Sites (including one endangered site) that span multiple
countries have been removed from the data set in order to simplify querying. In addition, columns
not relevant to today's discussion such as French translations of certain string fields have also
been removed in order to reduce the size of the data set.

## 1.0 The dictionary

Lists and tuples are robust data structures but one downside that they both share is that neither
provides explicit hints as regards the meaning of each element or item.

```python
site = [
    527,
    "Cultural",
    "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra",
    "Designed to rival Hagia Sophia in Constantinople . . . .",
    1990,
    0,
    30.51686,
    50.45258,
    28.52,
    "Europe and North America",
    "Ukraine",
    "UKR"
    ]
```

While a few of the elements in the above list are likely comprehensible, discerning the
meaning of the other elements may require "insider" knowledge or an accompanying data dictionary.
Such a situation is rarely ideal when working with data.

The Python dictionary (`dict`) provides an alternative data structure for both _describing_ data
and storing values. Python dictionaries (type: `dict`) are considered _associative arrays_, wherein
each specified value is associated with or mapped to a defined key that is used to access the value.

The beauty of the dictionary is the ability to identify data values by a label or key, usually
rendered as a readable string though not always (integers and tuples are also used as keys). In
other words, you can embed meaning into a data structure.

:bulb: You'll often hear people refer to dictionaries as unordered sets of _key-value pairs_.
However, since Python 3.7 dictionary order is now guaranteed to be the insertion order of its
key-value pairs.

Dictionaries are defined by enclosing a comma-separated sequence of  key-value pairs within curly
braces (`{}`).

```python
{
    < key >: < value >,
    < key >: < value >,
    ...
}
```

Each key-value pair is separated by a colon (`:`). Each value specified is
referenced by its associated key rather than by its numercial position within the dictionary.

Below is a simple dictionary representation of Kyiv"s 🇺🇦 two UNESCO World Heritage sites: Saint-Sophia
Cathedral and Kyiv-Pechersk Lavra (Monastery of the Caves):

```python
site = {
    "id_no": 527,
    "category": "Cultural",
    "name_en": "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra",
    "short_description_en": "Designed to rival Hagia Sophia in Constantinople . . . .",
    "date_inscribed": 1990,
    "endangered": 0,
    "longitude": 30.51686,
    "latitude": 50.45258,
    "area_hectares": 28.52,
    "region_en": "Europe and North America",
    "states_name_en": "Ukraine",
    "undp_code": "UKR"
    }
```

:bulb: Python dictionary objects are _iterables_ with a length or size that can be accessed by
calling the built-in function `len()`.

:bulb: A dictionary can also be provisioned with a _composite_ key, that is, a key comprising two or
more values. The composite key must be _hashable_, that is, it must never change during its
lifetime. Tuples that contain hashable values can be employed as a dictionary key as the following
example illustrates

```python
# Tuple (< longitude >, < latitude >)
location = {
    (30.51686, 50.45258): "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra"
}
```

You can check if an object is hashable by passing it to the built-in `hash()` function. Both
strings and tuples possess a hash value; lists and dictionaries do not.

```python
# Tuple is hashable
hash_value = hash((30.51686, 50.45258)) # -4047005574466108915

# List is not hashable
hash_value = hash([30.51686, 50.45258]) # TypeError: unhashable type: 'list'
```

## 2.0 Creating a dictionary

There are several ways to create a dictionary.

### 2.1 Assign an empty dictionary to a variable

You can create a dictionary by assigning an empty dictionary to a variable and
then adding key-value pairs one at a time to the dictionary using the subscript operator (`[]`).

:bulb: note the nested dictionary assigned to the key `geo_coordinates`.

```python
site = {}
site["id_no"] = 1330
site["category"] = "Cultural"
site["name_en"] = "Residence of Bukovinian and Dalmatian Metropolitans"
site["short_description_en"] = "[R]epresents a masterful synergy of architectural styles built by Czech architect Josef Hlavka from 1864 to 1882. . . ."
site["date_inscribed"] = 2011
site["endangered"] = 0
site["geo_coordinates"] = {} # nested dict
site["geo_coordinates"]["longitude"] = 25.9247222222
site["geo_coordinates"]["latitude"] = 48.2966666667
site["area_hectares"] = 8.0
site["region_en"] = "Europe and North America"
site["states_name_en"] = "Ukraine"
site["undp_code"] = "UKR"
```

### 2.2 Dictionary literal

You can create a dictionary by defining a dictionary _literal_ and assigning
keys and values separated by a colon (`:`).

```python
site = {
    "id_no": 865,
    "category": "Cultural",
    "name_en": "L'viv – the Ensemble of the Historic Centre",
    "short_description_en": "The city of L'viv, founded in the late Middle Ages, was a flourishing administrative, religious and commercial centre for several centuries. The medieval urban topography has been preserved virtually intact . . . .",
    "date_inscribed": 1998,
    "endangered": 0,
    "geo_coordinates": {
        "longitude": 24.03198,
        "latitude": 49.84163
        },
    "area_hectares": 120.0,
    "region_en": "Europe and North America",
    "states_name_en": "Ukraine",
    "undp_code": "UKR",
    }
```

### 2.3 Built-in `dict()` function

You can also call the built-in `dict()` function to define a dictionary. You can pass in a sequence
of keyword arguments separated by commas or pass in a sequence of tuples.

```python
# Pass in keyword arguments (note use of nested dict())
site = dict(
    id_no=1411,
    category="Cultural",
    name_en="Ancient City of Tauric Chersonese and its Chora",
    short_description_en="The site features the remains of a city founded by Dorian Greeks in the 5th century BC on the northern shores of the Black Sea. . . .",
    date_inscribed=2013,
    endangered=0,
    geo_coordinates=dict(longitude=33.4913888889, latitude=44.6108333333),
    area_hectares=259.3752,
    region_en="Europe and North America",
    states_name_en="Ukraine",
    undp_code="UKR"
    )

# Pass in tuples (note used of nested dict())
site = dict(
    [
        ("id_no", 1411),
        ("category", "Cultural"),
        ("name_en", "Ancient City of Tauric Chersonese and its Chora"),
        ("short_description_en", "The site features the remains of a city founded by Dorian Greeks in the 5th century BC on the northern shores of the Black Sea. . . ."),
        ("date_inscribed", 2013),
        ("endangered", 0),
        ("geo_coordinates", dict([("longitude", 33.4913888889), ("latitude", 44.6108333333)])),
        ("area_hectares", 259.3752),
        ("region_en", "Europe and North America"),
        ("states_name_en", "Ukraine"),
        ("undp_code", "UKR")
        ]
    )
```

## 3.0 Working with dictionaries

Dictionaries, like lists, are mutable and capable of modification. Utilize the subscript operator
`[]` and a key value to interact with a dictionary and its individual key-value pairs.

### 3.1 Accessing a value

A dictionary value is accessed by its associated key using the subscript operator.

```python
site = {
        "id_no": 527,
        "category": "Cultural",
        "name_en": "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra",
        "short_description_en": "Designed to rival Hagia Sophia in Constantinople . . . .",
        "date_inscribed": 1990,
        "endangered": 0,
        "geo_coordinates": {
            "longitude": 24.03198,
            "latitude": 49.84163
            },
        "area_hectares": 28.52,
        "region_en": "Europe and North America",
        "states_name_en": "Ukraine",
        "undp_code": "UKR"
        }

    # Accessing a value
    site_name = site["name_en"]
```

:exclamation: If you attempt to access a dictionary value with a non-existent key you will trigger
a `KeyError` exception.

```python
site_name = site["name"] # raises KeyError: 'name'
```

### 3.2 Accessing a nested value

Besides strings, numbers, and booleans, dictionaries can reference more complex data
structures such as lists, tuples, and other dictionaries. This is often referred to as _nesting_.

To access nested values you can "chain" the subscript operator `[]` by providing each bracket with
appropriate the key, index, or slice as determined by the type of nested object.

```python
# Accessing a nested dictionary value
site_latitude = site["geo_coordinates"]["latitude"]
```

### 3.3 Add a key-value pair

You can add a _new_ key-value pair to an _existing_ dictionary by assigning a new value to the
dictionary using the subscript operator (`[]`) and specifying a key.

```python
# Add key-value pair
site["subregion_en"] = "Eastern Europe"
```

The new key-value pair is appended to the dictionary's key-value pair sequence.

The above approaches holds true for nested objects as well. Use subscript chaining to reference
the relevant key-value pair.

```python
# Add nested key-value pairs
  site["street_address"] = {}
  site["street_address"]["Saint-Sophia Cathedral"] = "Volodymyrska St, 24, Kyiv, Ukraine, 01001"
  site["street_address"]["Kyiv Pechersk Lavra"] = "Lavrska St, 15, Kyiv, Ukraine, 01015"
```

### 3.4 Modify an existing value

If you need to _modify_ an existing value you can assign a new value by referencing the
relevant key:

```python
# Modify existing key-value pair
site["endangered"] = 1
```

### 3.5 Delete a key-value pair

If you need to delete a key-value pair you can use the built-in `del()` function.

```python
# Delete key-value pair
del(site["undp_code"])
```

## 4.0 Select dictionary methods

The Dictionary object is provisioned with several useful
[methods](https://www.w3schools.com/python/python_ref_dictionary.asp) of which the following are
relevant to today's discussion:

* `dict.get()`
* `dict.keys()`
* `dict.values()`
* `dict.items()`

### 4.1 `dict.get()` method

You can guard against `KeyError` runtime exceptions by accessing dictionary values using
the `dict.get()` method.

```python
dict.get(< key >[, < default value >])
```

The `dict.get()` method defines two parameters: a key and an optional default value to return if
the passed in key has no associated value. If a default value is not specified, the optional
default value defaults to `None`. This behavior prevents `dict.get()` from triggering a `KeyError`
if a non-existent key is passed to it.

```python
site_type = site.get("category") # returns str

# TODO Uncomment
# site_type = site["type"] # triggers KeyError

site_type = site.get("type") # returns None

site_type = site.get("type", "Undefined") # returns default value
```

### 4.2 `dict.keys()` method

You can retrieve all the keys in a dictionary by calling `dict.keys()`. The method returns a
`dict_keys` object, an object that provides a _view_ or a pointer to the dictionary's keys. While
you can loop over a `dict_keys` object you _cannot_ modify either the referenced keys or the
associated dictionary.

:bulb: you can create a copy of the `dict_keys` object using the built-in `list()` function. Passing
the `dict_keys` object to `list()` will return a list of keys. Doing so simplifies working with the
keys.

The following Ukraine 🇺🇦 dictionary comprising basic country data compiled by the
[United Nations](https://data.un.org/en/iso/ua.html) illustrates basic use of the `dict.keys()`
method.

```python
country = {
    "name": "Ukraine",
    "region": "Eastern Europe",
    "population": 43467000,
    "urban_population_pct": 69.5,
    "surface_area_km2": 603500,
    "capital_city": "Kyiv",
    "un_membership_date": "1945-10-24"
}

# Loop over dict_keys object
for key in country.keys():
    print(key)

# Convert dict_keys to a list
country_keys = list(country.keys())

# Loop over list of keys; print associated values
for key in country_keys:
    print(country[key])
```

### 4.3 `dict.values()` method

You can retrieve all the values in a dictionary by calling `dict.values()`. The method returns a
`dict_values` object, an object that provides a _view_ or a pointer to the dictionary's values. While
you can loop over a `dict_values` object you _cannot_ modify either the referenced values or the
associated dictionary.

:bulb: you can create a copy of the `dict_values` object using the built-in `list()` function. Passing
the `dict_values` object to `list()` will return a list of values. Doing so simplifies working with the
values.

```python
# Loop over dict_values object
for value in country.values():
    print(value)

# Convert to a list
country_values = list(country.values()) # convert to a list

# Print value types
for value in country.values():
    print(type(value))
```

:bulb: You can also unpack a dictionary's values. Recall the Heritage site's `geo_coordinates`
is a dictionary comprising the site's latitude and longitude. The values can be unpacked and
assigned to variables.

```python
# Unpacking
site_longitude, site_latitude = site["geo_coordinates"].values()

print(f"\n4.3.5 Site Geo coordinates = {site_longitude}, {site_latitude}")
```

### 4.4 `dict.items()` method

You can loop over a dictionary's keys _and_ values by calling the `dict.items()` method.
`dict.items()` returns a `dict_items` object, a list-like object composed of key-value tuples. Call
`dict.items()` whenever you need to filter on specific keys in order to access a subset of the
dictionary's values.

```python
# Looping over a dictionary's items
for key, val in country.items():
    print(f"key: {key}, val: {val}")
```

### 4.5 Challenge 01

__Task__: Convert the `country` dictionary's numeric values masquerading as strings to either an
integer or a float.

1. In the `main()` function block, loop over the `country` dictionary's items (keys and values) and
   utilize conditional logic to convert the following string values to either `int` or `float`:

   | Key                    | Convert value to |
   |:-----------------------|:-----------------|
   | "population"           | `int`            |
   | "surface_area_km2"     | `int`            |
   | "urban_population_pct" | `float`          |

2. Uncomment the `print()` and `pp.pprint()` functions to check your output.

## 5.0 The `csv` module (`csv.DictReader()`, `csv.DictWriter()`)

The `csv` module provides two classes for _decoding_ CSV row data into dictionaries and _encoding_
dictionaries into CSV row data.

### 5.1 The `DictReader()` class

The `DictReader()` class returns a reader-like object that maps row data to a `dict` whose keys are
provided by the optional `fieldnames` parameter.

```python
def read_csv_to_dicts(filepath, encoding="utf-8", newline="", delimiter=","):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline "\n"
                       or "\r\n" (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, "r", newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data
```

### 5.2 The `DictWriter()` class

Likewise, the `DictWriter()` class returns a writer-like object that maps dictionaries into row data
using the `fieldnames` parameter to determine the order in which each dictionary's key-value pairs
are written to each row in the target file. The writer includes a `writeheader()` method for writing
the CSV's header row (1st row) based on the passed in `fieldnames` elements and a `writerow()`
method for writing each dictionary's key-value data as CSV row data.

```python
def write_dicts_to_csv(filepath, data, fieldnames, encoding="utf-8", newline=""):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline "\n"
                       or "\r\n" (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)
```

### 5.3 Challenge 02

__Task__: Call the two utility functions that utilize the `csv.DictReader` and `csv.DictWriter`
objects to convert CSV rows to dictionaries and dictionaries to CSV rows.

1. In the `main()` function block, call the function `read_csv_to_dicts` and pass it the filepath
   "./data-whc-sites.csv" as the lone argument. Assign the return value to a variable named
   `sites`.

2. Loop over the `sites` list and in the loop block write a conditional statement that identifies
   Ukrainian World Heritage sites employing one of the following key-value pairs in your `if`
   statement:

   | Key              | Value     |
   |:-----------------|:----------|
   | "states_name_en" | `"Ukraine"` |
   | "undp_code"      | `"ukr"`     |

3. If the `if` statement evaluates to `True` append the dictionary to the `ukraine_sites`
   "accumulator" list.

4. After exiting the loop access the first dictionary in the `ukraine_sites` list and call its
   `.keys()` method. Assign the return value, a "view" object of the dictionary's keys, to a
   variable named `fieldnames`.

5. Call the function `write_dicts_to_csv` and pass it the following arguments in the specified
   order:

     1. "stu-whc-sites-ukraine.csv"
     2. `ukrainian_sites`
     3. `fieldnames`

   Confirm that the new CSV file was created in your lecture directory.

### 5.4 Challenge 03

__Task__: Retrieve UNESCO Heritage Sites located in the United States that are categorized as either
"Natural" or "Mixed" and then write the data to a CSV file.

The heritage site categories are defined as follows:

* __Cultural__: "Cultural heritage includes artefacts, monuments, a group of buildings and sites,
  museums that have a diversity of values including symbolic, historic, artistic, aesthetic,
  ethnological or anthropological, scientific and social significance. It includes tangible heritage
  (movable, immobile and underwater), intangible cultural heritage (ICH) embedded into cultural, and
  natural heritage artefacts, sites or monuments. The definition excludes ICH related to other
  cultural domains such as festivals, celebration etc. It covers industrial heritage and cave
  paintings."

* __Natural__: "Natural heritage refers to natural features, geological and physiographical
  formations and delineated areas that constitute the habitat of threatened species of animals and
  plants and natural sites of value from the point of view of science, conservation or natural
  beauty. It includes private and publically protected natural areas, zoos, aquaria and botanical
  gardens, natural habitat, marine ecosystems, sanctuaries, reservoirs etc."

* __Mixed__: Combines elements of both cultural and natural significance.

Source: UNESCO Institute for Statistics [glossary](http://uis.unesco.org/en/glossary).

1. Implement the function named `get_country_sites`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Implement a `for` loop that includes an `if` statement that filters sites on the passed in
      `undp_code` _and_ `categories` tuple containing one or more heritage categories (e.g.,
      Cultural, Mixed, and/or Natural).

   2. Each site dictionary contains a "undp_code" and a "category" key-value pair. Consider
      carefully how to evaluate a site's category if the passed in tuple contains more than one
      heritage category item.

      ```python
      {
        "unique_number": "31",
        "id_no": "28",
        "category": "Natural",
        "name_en": "Yellowstone National Park",
        . . .
        "undp_code": "usa"
      }
      ```

2. After implementing `get_country_sites()` return to `main()`.

3. Call the function and pass it the following arguments in the order specified:

   1. `sites`
   2. "usa"
   3. two-item tuple comprising the following strings: "Mixed" and "Natural"

   Assign the return value to a variable named `usa_sites`.

4. Call the function `write_dicts_to_csv` and pass it the following arguments in the order
   specified:

   1. "stu-usa-mix_nat.csv" (filepath)
   2. the USA sites list (data)
   3. a `dict_keys` object obtained from one of the nested dictionaries in the list (fieldnames)

5. Call the function `get_country_sites` a second time and pass it the following arguments in the
   order specified:

   1. `sites`
   2. "ind" (UNDP code for India)
   3. single-item tuple comprising the string "Cultural"

6. Call the function `write_dicts_to_csv` again and pass it the following arguments in the order
   specified:

   1. "stu-ind_cultural.csv" (filepath)
   2. the India sites list (data)
   3. a `dict_keys` object obtained from one of the nested dictionaries in the list (fieldnames)

7. Review the two files you created.

## 6.0 The accumulator pattern revisited

### 6.1 Accumulating values from a dictionary

Say you were interested in retrieving the first Chinese site(s) that were added to the UNESCO
[World Heritage List](https://whc.unesco.org/en/list) and writing the data to a new CSV file. First,
you need to retrieve the heritage sites data by calling the function `read_csv_to_dicts()` and
passing to it the filepath to the `data-whc-sites.csv` file. The return value is a list
of dictionaries.

```python
# Get UNESCO World heritage sites
sites = read_csv_to_dicts("data-whc-sites.csv")
```

Once the data is acquired you will need to check the following key-value pairs in each
dictionary:

* `states_name_en`
* `date_inscribed`

This is an "accumulation" problem. However, while the country is known (e.g., China) the earliest
inscription date is _unknown_. This date (a year) will need to be discovered when looping over the
sites. Decrementing the year value until the earliest year is uncovered will require a "tracking"
variable located outside the loop to which the (declining) "date_inscribed" year value is assigned
whenever the current `date_inscribed` value is less than the previous `year` value.

You've worked with this pattern before. What's new in the example below is the use of the `datetime`
module to assign a start date that is always equal to the current year&mdash;no matter what the
current year is this code when run will find the target country site(s) with the earliest
inscription date.

```python
china_sites = []
year = dt.today().year # Return current year
# year = dt.now().year # Alternative
for site in sites:
    date_inscribed = int(site["date_inscribed"]) # convert
    if site["states_name_en"].lower() == "china" and date_inscribed < year:
        year = date_inscribed
        china_sites.clear() # reset
        china_sites.append(site)
    elif site["states_name_en"].lower() == "china" and date_inscribed == year:
        china_sites.append(site)
```

After retrieving the earliest inscribed Chinese sites, you can write the data out to a file by
calling the function `write_dicts_to_csv` and passing to it the following required arguments:

* "stu-china-earliest.csv" (filepath)
* `china_sites` (the data)
* `china_sites[0].keys()` (fieldnames used to reconstitute the "header" row)

:bulb: Note that you can retrieve the "fieldnames" required by `write_dicts_to_csv()` by returning
the keys from the first dictionary in the list and passing the `dict_keys` object to the function.

```python
write_dicts_to_csv("stu-china-earliest.csv", china_sites, china_sites[0].keys())
```

### 6.2 Storing accumulated values in a dictionary

When exploring data and compiling descriptives statistics (e.g., counts, mean, min, or max
values) or when grouping data, consider using a dictionary to hold the values.

For example, if you needed a count of the number of Chinese heritage sites inscribed each year
by UNESCO you could employ a dictionary to hold the counts with each year serving as a key to which
the annual count is mapped.

```python
{
    "< Year A >": < count >,
    "< Year B >": < count >,
    ...
}
```

For the Chinese heritage sites you could write the following code:

```python
china_counts = {}
for site in sites:
    if site["states_name_en"].lower() == "china":
        year = site["date_inscribed"] # str
        if year not in china_counts.keys():
            china_counts[year] = 1 # seed value
        else:
            china_counts[year] += 1 # increment

# WARN: must pass a list of dictionaries
write_dicts_to_csv("stu-china-counts.csv", [china_counts], china_counts.keys())
```

__BONUS__ If you check the file `stu-china-counts.csv` you'll notice that the data is not ordered
by year. This reflects the lack of strict ordering in the original UNESCO Heritage Sites list. To
reorder the Chinese site counts by year before writing the data to a CSV file create a new
dictionary employing either the built-in function `dict()` or a dictionary comprehension.

:bulb: Sorting using an anonymous `lambda` function is actually out of scope for this week but
seeing how its done should spark your curiosity about how to use lambda functions. For a useful
article on lambdas see Andre Burgaud,
["How to Use Python Lambda Functions"](https://realpython.com/python-lambda/) (Real Python, June
2019).

```python
# Employ the built-in sorted() function and a lambda function that sorts on the key
# Sort by key (x[0]); sort by value (x[1])
# Then convert the list returned by sorted() with the built-in dict() function
china_counts = dict(sorted(china_counts.items(), key=lambda x: x[0]))
```

or

```python
# Preferred: Employ a dictionary comprehension along with sorted() and a lambda function
# Sort by key (x[0]); sort by value (x[1])
china_counts = {k: v for k, v in sorted(china_counts.items(), key=lambda x: x[0])}
```

### 6.3 Challenge 04

__Task__: Create a dictionary that holds counts of UNESCO Heritage Sites by region.

1. In `main()` create an empty dictionary named `region_counts`. Loop over `sites` and accumulate
   site counts by region.

   :bulb: Retrieve each site's "region_en" value and assign the string to a variable. Next, check if
   the "region" has been added as a key in the `region_counts` dictionary (call its `keys()`
   method). If the key was previously added increment the count assigned to the key. If the key
   does not exist add a new "region" key to the dictionary and assign `1` as its value.

2. Uncomment the `print()` and `pp.pprint()` functions and check your work. The dictionary
   _must_ contain the following key-value pairs.

   ```python
   {
      "Asia and the Pacific": 273,
      "Europe and North America": 516,
      "Arab States": 88,
      "Africa": 92,
      "Latin America and the Caribbean": 143
   }
   ```

3. __BONUS__: Uncomment the second `region_counts` variable assignment. A new dictionary is assigned
   to the variable utilizing a dictionary comprehension that employs an anonymous lambda function
   passed to the built-in function `sort()` to reorder the key-value pairs.

   :bulb: You will learn how to write list and dictionary comprehensions later in the course.

   ```python
   region_counts = {k: v for k, v in sorted(region_counts.items(), key=lambda x: x[1], reverse=True)}
   ```

## 7.0 Additional challenges

### 7.1 Challenge 05

__Task__: Retrieve UNESCO Heritage Sites designated as endangered per
[Article 11, paragraph 4](https://whc.unesco.org/en/conventiontext/#Article11.4) of the UNESCO
[Convention Concerning the Protection of the World Cultural and Natural Heritage](https://whc.unesco.org/en/conventiontext/).
Create a list of new dictionaries comprising a subset of the available key-value pairs and then
write the data to a CSV file.

1. In `main()` create an empty "accumulator" list named `endangered_sites`. Loop over
   the `sites` list. In the loop block write a conditional statement that identifies heritage sites
   considered endangered (i.e., `"endangered": "1"`). Append each site that meets the conditions to
   your accumulator list constructing a new dictionary where you map the appropriate
   values to the following keys:

   1. "id_no"
   2. "category"
   3. "name_en"
   4. "region_en"
   5. "states_name_en"

   :bulb: As noted in the previous lecture there are several ways to create a dictionary and assign
   it key-value pairs. I recommend that you create the new dictionary inside the loop using a
   dictionary _literal_.

2. After exiting the loop, call the function `write_dicts_to_csv` and pass it the following
   arguments:

   1. "stu-endangered.csv" (filepath)
   2. accumulator list of dictionaries (data)
   3. the `dict_keys` object obtained from one of the nested dictionaries (fieldnames)

   Then review the file output.

### 7.2 Challenge 06

__Task__: Create a dictionary that holds counts of endangered UNESCO Heritage Sites by region. Then
loop over the dictionary and replace each regional count with the corresponding percentage value
rounded to the second decimal place.

1. In `main()` create an empty dictionary named `endangered_counts`. Loop over `endangered_sites`
   and accumulate site counts by region ("region_en").

   :exclamation: Remember to check for the absence of a key in `endangered_counts` before you
   accumulate values.

2. Uncomment the `print()` and `pp.pprint()` functions and check your work. The dictionary
   _must_ contain the following key-value pairs.

   ```python
   {
     "Asia and the Pacific": 6,
     "Europe and North America": 4,
     "Latin America and the Caribbean": 6,
     "Africa": 14,
     "Arab States": 21
   }
   ```

3. BONUS: Uncomment the second `endangered_counts` variable assignment. A new dictionary with
   its key-value pairs reordered is assigned by passing the `endangered_counts` key-value pairs
   (items) along with a lambda expression to the built-in `sorted()` function which is then passed
   to the built-in `dict` function.

   ```python
   endangered_counts = dict(sorted(endangered_counts.items(), key=lambda x: x[1], reverse=True))
   ```

   This is yet another way create a new dictionary with sorted key-value pairs. That said, the
   preferred approach is to employ a dictionary comprehension rather than the built-in `dict()`
   function both because it's easier to read and the comprehension is more performant (it avoids
   the lookup costs associated with built-in functions).

4. Uncomment the `print()` and `pp.pprint()` functions and check your work. The new dictionary
   _must_ contain the following (reordered) key-value pairs.

   ```python
   {
        "Arab States": 21,
        "Africa": 14,
        "Asia and the Pacific": 6,
        "Latin America and the Caribbean": 6,
        "Europe and North America": 4
   }
   ```

### 7.3 Challenge 07

__Task__: Increase the count of endangered World Heritage Sites to include four Ukrainian Heritage
sites.

1. Currently, four (`4`) Ukrainian Heritage Sites are located in a conflict zone as a result of the
   Russian invasion of Ukraine that occurred on Thursday, 24 February 2022. Update the
   `endangered_counts` "Europe and North America" key-value pair value to reflect this new reality.

2. Call the appropriate `dict` method that returns `endangered_sites` __values__ (an _iterable_) and
   pass the expression to a [built-in function](https://docs.python.org/3/library/functions.html)
   that sums each of the iterable's items and returns the total amount. Assign the return value to
   the variable named `count`.

3. Loop over the `endangered_sites` items (keys and values). For each key-value pair encountered
   replace the value with the corresponding percentage value rounded to the 2nd decimal place
   computed from the following equation:

   ```Commandline
   < value > / < count > * 100 (rounded to the 2nd decimal place)
   ```

   :exclamation: Be prepared to convert string values to integers.

4. Uncomment the `print()` and `pp.pprint()` functions and check your work. The mutated dictionary
   _must_ contain the following key-value pairs.

   ```python
   {
      "Arab States": 38.18,
      "Africa": 25.45,
      "Asia and the Pacific": 10.91,
      "Latin America and the Caribbean": 10.91,
      "Europe and North America": 14.55
   }
   ```
