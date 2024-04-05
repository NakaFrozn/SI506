# SI 506: Comprehensions

## Topics

1. The list comprehension
   1. Basic syntax
   2. Example
   3. Calling a function or object method
2. List comprehensions and conditional statements
   1. Challenge 01
   2. `if-else` statements
   3. `if-elif-else` statements
3. List comprehensions and nested loops
   1. Challenge 02
4. The dictionary comprehension
   1. Basic syntax
   2. Example
   3. Calling a function or object method
5. Dictionary comprehensions and conditional statements
   1. Challenge 03
   2. Challenge 04
   3. `if-else` statements
   4. `if-elif-else` statements
6. Dictionary comprehensions and nested loops
   1. Challenge 05
7. Working with dates and times

## Data

This week's data is sourced from [The World Bank](https://www.worldbank.org/en/home) and the
[New York Times](https://www.nytimes.com/).

### World Bank

The World Bank assigns the world's economies to four income groups based on the World Bank
[Atlas method](https://datahelpdesk.worldbank.org/knowledgebase/articles/378832-what-is-the-world-bank-atlas-method)
for calculating Gross National Income (GNI) per capita in current USD using data from the previous
year. The classifications are updated each year on 1 July. For the current fiscal year, the
classifications are delineated as follows:

| Fiscal Year | Classification | GNI per capita (2020) |
| :---------- | :------------- | :-------------------- |
| 2022-2023 | `Low income` | <= $1,085.00 (USD) |
| 2022-2023 | `Lower middle income` | between $1,086.00  and $4,255.00 (USD) |
| 2022-2023 | `Upper middle income` | between $4,256.00 and $13,205.00 (USD) |
| 2022-2023 | `High income` | >= $13,205.00 (USD) |

Source: World Bank Blogs,
["New World Bank country classifications by income level: 2022-2023"](https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2022-2023);
[World Bank Country and Lendings Groups](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups).

### New York Times

[The New York Times](https://www.nytimes.com/) provides an
[Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview)
(Application Programming Interface) that permits keyword searching and retrieval of JSON
representations of NY Times articles.

Today's data comprises a list of JSON objects that represent the most recent NY Times articles
published by the [Climate](https://www.nytimes.com/section/climate) Desk.

An example JSON document named `data-nyt-article-climate-example.json` is included in today's
lecture files. You should review it and familiarize yourself with its structure and name-value
pairs.

:bulb: Certain name-value pairs have been removed from the JSON documents in the interests of
brevity. In addition, a "person" object containing all `null` values has also been removed in order
to eliminate the need to introduce exception handling in your code.

## 1.0 The list comprehension

Python's comprehension syntax provides a terse yet economical way to interact with all the members
of an iterable in order to return either a dictionary, list, or set.

### 1.1 Basic syntax

```python
new_list = [expression for element in sequence]
```

### 1.2 Example

Assume that you need to create a list of
[ISO-3165-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country codes sourced from
the nested country dictionaries comprising the `countries` list.

You would likely write the following code after reading the data file:

```python
codes = []
for country in countries:
    codes.append(country['country_code'])
```

The code performs the following operations:

1. Assigns an empty "accumulator" list to the variable named `country_codes_v1`.
2. Loops over the `countries` list of nested dictionaries, each representing a country.
3. Append's each element's "country_code" value to the accumulator list.

The above represents a fine implementation that gets the job done. However, you can also utilize a
_list comprehension_ to accomplish the task&mdash;an approach that is arguably more elegant, and,
depending on the scenario, a more performant way to create a new list from an existing list.

```python
codes = [country['country_code'] for country in countries]
```

### 1.3 Calling a function or object method

However, when you inspect the new list you notice that roughly half the codes are rendered in
lowercase rather than uppercase as defined by the ISO-3165-1 alpha-3 specification. The lowercase
codes should by converted to uppercase.

You can call a function or an object method from inside a list comprehension to create a new list
that contains the transformed values.

```python
codes = [country['country_code'].upper() for country in countries]

codes = [to_uppercase(country['country_code']) for country in countries] # Alternative
```

## 2.0 List comprehensions and conditional statements

A list comprehension can specify one or more conditional statements in order to assign a subset of a
list to a new list.

```python
new_list = [expression for element in sequence if condition]
```

The following list comprehension returns only those economies located in the region "East Asia &
Pacific":

```python
east_asia = [country for country in countries if country['region'] == 'East Asia & Pacific']
```

### 2.1 Challenge 01

__Task__: Write a list comprehension that returns economies located in either
Latin America, the Carribbean or North America _and_ are categorized as lower middle income
economies by The World Bank.

1. Write a list comprehension that accesses all "lower middle income" economies located in either
   "Latin America & Caribbean" _or_ "North America". Perform a case insensitive comparison of the
   `income_group` strings.

   Assign the new list to a variable named `americas_lower_middle`.

   :exclamation: Venezuela's `income_group` is `None` so test the truth value of each country's
   `income_group` value.

   :bulb: If expressing the loop as a comprehension proves challenging, implement a "standard" `for`
   loop. Then see if you can decompose the loop into a comprehension.

2. After populating `americas_lower_middle` with new dictionaries uncomment `write_json()` to write
   the list to a JSON file. Run your code. Review the file output.

   :bulb: You can enhance readability by writing list comprehensions that exceed 80-100 characters
   and/or feature complex conditions or other expressions across multiple lines vertically.

   ```python
   new_list = [
       expression
       for element in sequence
       if condition
       ]
   ```

### 2.2 `if-else` statements

You can employ `if-else` logic in a list comprehension. The `if-else` logic is placed _before_ the
`for` statement and employs the _ternary_ form of the `if-else` operator.

```python
# ternary syntax: < value when True > if < expression > else < value when False >

new_list = [expression if condition else expression for element in sequence]
```

The example below returns a list of tuples that categorize economies as either "High income" or
"Middle/low income":

```python
two_categories = [
    (
        (country["country_name"], "High income")
        if country["income_group"] and country["income_group"].lower() == "high income"
        else (country["country_name"], "Middle/low income")
    )
    for country in countries
]
```

### 2.3 `if-elif-else` statements

The `elif` statement is _not_ recognized inside a list comprehension. You can mimic `if-elif-else`
logic by employing multiple `else` statements.

Dividing World economies into three categories ("High income", "Middle income", or "Low income")
can be accomplished by adding an additional `else` statement to the list comprehension:

```python
three_categories = [
    (
        (country["country_name"], "High income")
        if country["income_group"] and country["income_group"].lower() == "high income"
        else (
            (country["country_name"], "Middle income")
            if country["income_group"]
            and country["income_group"].lower()
            in ("lower middle income", "upper middle income")
            else (country["country_name"], "Low income")
        )
    )
    for country in countries
]
```

However, you may well conclude that the above comprehension's `if-else-else` leads to diminished
readability when compared to a `for` loop:

```python
three_categories_v1 = []
for country in countries:
    if country["income_group"] and country["income_group"].lower() == "high income":
        three_categories_v1.append((country["country_name"], "High income"))
    elif country["income_group"] and country["income_group"].lower() in (
        "lower middle income",
        "upper middle income",
    ):
        three_categories_v1.append((country["country_name"], "Middle income"))
    else:
        three_categories_v1.append((country["country_name"], "Low income"))
```

:bulb: If list comprehension readability is concern then consider relocating the business logic
(e.g., categorizing economies) to a function and then use it to transform the data by calling it
from inside a list comprehension.

```python
three_categories = [categorize_economy(country) for country in countries]
```

## 3.0 List comprehensions and nested loops

You can embed nested loops in a list comprehension. The outer loop is listed first followed by the
inner loop:

```python
new_list = [expression for outer_element in outer_sequence for inner_element in inner_sequence if
condition]
```

The World Bank also groups countries. After reading in the group data from the file
`data-wb-groups.json` we can retrieve economies characterized as members of the "Arab World"
(group code = "ARB") using a list comprehension that employs a nested loop:

:bulb: Review the two data sets to determine which key-value pair(s) can be used to link a country
to a group.

```python
arab_world_v1 = [
    country
    for group in groups
    for country in countries
    if group["group_code"].lower() == "arb"
    and group["country_code"].lower() == country["country_code"].lower()
]
```

### 3.1 Challenge 02

__Task__: Employ a list comprehension and a function to create a new list of Sub-Saharan African
economies that combine key-value pairs drawn from related country and group dictionaries.

1. Write a list comprehension that employs a nested loop in order to identify economies in the
   `countries` list that are located in Sub-Saharan Africa (group_code = "SSF").

   Base your list comprehension on the following nested loop:

   ```python
   sub_saharan_africa = []
   for group in groups:
        if group["group_code"].lower() == "ssf":
            for country in countries:
                if group["country_code"].lower() == country["country_code"].lower():
                    sub_saharan_africa.append(add_group(country, group))
    ```

   Transform the elements to be included in the new list by calling the function `add_group()`
   inside the comprehension. Assign the new list to a variable named `sub_saharan_africa`.

   bulb: The function `add_group()` combines a select list of key-value pairs drawn from the passed
   in `country` and `group` _if and only if_ the `country['country_code']` and
   `group['country_code']` values are equal. Review the function's docstring to better understand
   its behavior.

   If a match is obtained a dictionary comprising five (`5`) key-value pairs is returned to the
   caller (example below).

   ```json
   {
      "country_name": "Ghana",
      "country_code": "GHA",
      "region": "Sub-Saharan Africa",
      "income_group": "Lower middle income",
      "lending_category": "IDA"
   }
   ```

2. After populating `sub_saharan_africa` uncomment the accompanying `assert` statement. Next
   uncomment `write_json()` to write the list to a JSON file. Run your code. Review the file output.

## 4.0 The dictionary comprehension

The Python [glossary](https://docs.python.org/3/glossary.html) describes the dictionary
comprehension as a "compact way to process all or part of the elements in an iterable and return a
dictionary with the results".

### 4.1 Basic syntax

```python
new_dict = {key: val for element in iterable}

new_dict = {key: val for key, value in dict.items()}
```

### 4.2 Simple example

If you were asked to provide a JSON file comprising word counts for each
article in the `nyt_articles` list you might opt for the following simple
data structure:

:bulb: Each article "web_url" can serve as a unique identifier.

```python
article_word_counts = {}
for article in nyt_articles:
    article_word_counts[article["web_url"]] = article["word_count"]
```

You could obtain the same results employing a dictionary comprehension:

```python
article_word_counts_v1 = {article["web_url"]: article["word_count"] for article in nyt_articles}
```

### 4.3 Calling a function or object method

You can call a function or object method in a dictionary comprehension in order to transform values.
In the following `for` loop and dictionary comprehension examples both the article "web_url"
and "pub_date" values are transformed in order to return a dictionary in which a shortened
publication date (i.e., Year-Month-Day) is mapped to a key comprising the article URL reduced to
the resource path (e.g., "lula-brazil-rainforest-climate") minus the file extension (i.e., '.html'):

```python
article_pub_dates = {}
for article in nyt_articles:
    path = article["web_url"].split("/")[-1][:-5]  # drops extension/suffix
    # path = Path(article['web_url']).stem # better
    pub_date = article["pub_date"].split("T")[0]
    article_pub_dates[path] = pub_date
```

The dictionary comprehension is compact and expressive:

```python
article_pub_dates_v1 = {
    Path(article["web_url"]).stem: article["pub_date"].split("T")[0] for article in nyt_articles
}
```

## 5.0 Dictionary comprehensions and conditional statements

A dictionary comprehension can specify one or more conditional statements in order to assign a
subset of a dictionary to a new dictionary.

```python
new_dict = {key: val for element in iterable if condition}

new_dict = {key: val for key, value in dict.items() if condition}
```

The `nyt_articles` list contains multimedia listings. These records can be accessed by filtering on
the "document_type" as the following `for` loop illustrates:

```python
multimedia = {}
for article in nyt_articles:
    if article["document_type"].lower() == "multimedia":
        multimedia[article["web_url"]] = article
```

The same can be achieved by employing a dictionary comprehension:

```python
multimedia_v1 = {
    article["web_url"]: article
    for article in nyt_articles
    if article["document_type"].lower() == "multimedia"
}
```

:bulb: Note that the typical comprehension variables `key` and `val` or `k` and `v` are conventions;
you are free to employ variable names that better express the nature of the data as in the previous
example.

### 5.1 Challenge 03

__Task__: Replace an inner `for` loop with a dictionary comprehension.

1. Convert the following nested `for` loop to an (outer) `for` loop and an (inner) dictionary
   comprehension. Append each new dictionary created by the comprehension to `articles_slim_v1`.

   The inner loop block appends a new dictionary to `articles_slim` whose key-value pairs are
   limited to the keys specified in the tuple `keep_keys`.

   ```python
   keep_keys = ("web_url", "pub_date", "document_type", "type_of_material", "word_count")

   articles_slim = []
   for article in nyt_articles:
        dict_ = {}  # Note use of trailing underscore; avoids shadowing dict data type name
        for key, val in article.items():
            if key in keep_keys:
                dict_[key] = val
        articles_slim.append(dict_)

   # Convert to
   articles_slim_v1 = []
   for article in nyt_articles:
       articles_slim_v1.append(< dictionary_comprehension >)
   ```

2. After populating `articles_slim_v1` uncomment the accompanying `assert` statement. Next uncomment
   `write_json()` to write the list to a JSON file. Run your code. Review the file output.

### 5.2 Challenge 04

__Task__: Replace an outer `for` loop with a list comprehension.

:bulb: The general comprehension pattern that you will implement for this challenge is as follows:

```python
new_list = [expression for element in sequence]
```

However, for this challenge the dictionary comprehension created in Challenge 03 constitutes the
`expression` in the list comprehension that you will implement. In other words, you _must_ __nest__
the dictionary comprehension inside the list comprehension.

```python
new_list = [{dict_comprehension} for element in sequence]
```

:bulb: Recall that the job of the dictionary comprehension is to produce a slimmed down dictionary
representation of an article (i.e., the `element`) by creating a new dictionary
comprising only the article's key-value pairs whose keys are specified in the `keep_keys` tuple.

1. Copy your Challenge 03 code and paste it into the Challenge 04 section of `main()`.

2. Next, convert the outer `for` loop to a list comprehension. Nest the dictionary comprehension
   inside the list comprehension. Assign the comprehension to the variable named `articles_slim_v2`.

3. After populating `articles_slim_v2` uncomment the accompanying `assert` statement. Next uncomment
   `write_json()` to write the list to a JSON file. Run your code. Review the file output.

### 5.2 `if-else` statements

You can employ `if-else` logic in a dictionary comprehension. The `if-else` logic is placed _before_
the `for` statement and employs the _ternary_ form of the `if-else` operator.

```python
# ternary syntax: < value when True > if < expression > else < value when False >

new_dict = {
    key: (some_val_when_true if condition else some_other_val)
    for key, val in dict_.items()
    }

new_dict = {
    (key if condition else default_key): (some_val_if_true if condition else some_other_val)
    for key, val in dict_.items()
    }

```

The example below creates a new dictionary based on the articles in the `articles_slim` list. The
key is created by calling the function `get_stem()` and assigning it the passed in Web URL's "stem"
(e.g., "green-hydrogen-energy"). Depending on the word count the value (a `dict`) mapped to the key
defines the read time as either "LONG" or "SHORT".

```python
read_time = {
    get_stem(article["web_url"]): (
        {"word_count": article["word_count"], "read time": "LONG"}
        if (article["word_count"]) >= 750
        else {"word_count": article["word_count"], "read time": "SHORT"}
    )
    for article in articles_slim
    if article["document_type"].lower() == "article"
}
```

### 5.3 `if-elif-else` statements

The `elif` statement is _not_ recognized inside a dictionary comprehension. You can mimic
`if-elif-else` logic by employing multiple `else` statements.

Dividing the article read times into three categories (SHORT, MEDIUM, LONG) requires the following
adjustment:

```python
read_time = {
    article["web_url"].split("/")[-1][:-5]: (
        {"word_count": article["word_count"], "read time": "LONG"}
        if article["word_count"] >= 1000
        else (
            {"word_count": article["word_count"], "read time": "MEDIUM"}
            if 500 <= (article["word_count"]) < 1000
            else {"word_count": article["word_count"], "read time": "SHORT"}
        )
    )
    for article in articles_slim
    if article["document_type"].lower() == "article"
}
```

:bulb: If dictionary comprehension readability is concern then consider relocating the business
logic (e.g., categorizing economies) to a function and then use it to transform the data by calling
it from inside the dictionary comprehension.

## 6.0 Dictionary comprehensions and nested loops

You can embed nested loops in a dictionary comprehension. The outer loop is listed first followed by
the inner loop:

```python
new_dict = {key: val for outer_element in outer_loop for inner_element in inner_loop if condition}
```

In the following examples NYT article author names are extracted and stored in a list of
dictionaries:

```commandline
authors = {
    '< web_url >': [< author 01 >],
    '< web_url >': [< author 01 >, < author 02 >, ...],
    ...
}
```

Each author is accessed by looping over `article['byline']['person']` and passing each "person"
dictionary encountered as an argument to the function `get_author()`. Since an article can contain
coauthors the authors are stored in a list and mapped to the article's "web_url" identifier.

You could write a nested `for` loop to populate the `authors` list:

```python
authors = {}
for article in nyt_articles:
    people = []
    for person in article["byline"]["person"]:
        people.append(get_author(person))
    authors[article["web_url"]] = people  # new key-value pair
```

You could reimplement the nested loop as a dictionary comprehension that features a nested list
comprehension:

```python
authors_v1 = {
    article["web_url"]: [get_author(person) for person in article["byline"]["person"]]
    for article in nyt_articles
}
```

:bulb: Nested dictionary comprehensions can get ugly. Check out this example in
[stackoverflow.com](https://stackoverflow.com/questions/17915117/nested-dictionary-comprehension-python):

```python
data = {outer_k: {inner_k: myfunc(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in outer_dict.items()}
```

### 6.1 Challenge 05

__Task__: Build a dictionary of NYT climate articles that feature either Antarctica or the Arctic.
Implement a dictionary comprehension that features a nested loop to generate the specified data
structure.

1. Reimplement the following nested loop as a dictionary comprehension.

   ```python
   polar_articles = {}
   for article in nyt_articles:
        for keyword in article["keywords"]:
            if keyword["name"] == "glocations" and keyword["value"].lower() in (
                "antarctic regions",
                "arctic regions",
            ):
                key = get_stem(article["web_url"])
                val = trim_article(article)
                polar_articles[key] = val
                break  # prevents unnecessary inner loop iterations
   ```

   __Nested loop characteristics__

   :bulb: Last week featured a similar nested loop that retrieved articles related to
   Paleontology.

   1. The `if` statement filters on the Antarctic OR Arctic "glocations" (i.e., geo location) only.

   2. If the compound conditional statement evaluates to `True` a new key-value pair is added to
     `polar_articles`.

      1. The `key` is assigned the filepath "stem" returned by calling the function `get_stem()` and
         passing to it the article's web URL as the argument.

      2. The `value` is assigned a "trimmed" or slimmed down dictionary representation of the
         `article` returned by calling the function `trim_article()` and passing to it the `article`
         as the argument.

      3. The `break` statement is embedded in the `if` block to prevent unnecessary loop iterations
         (membership check is akin to an OR condition). The `break` statement is __not__ utilized in
         the comprehension.

2. Assign the dictionary comprehension you write to the variable named `polar_articles_v1`.

3. After populating `polar_articles_v1` uncomment the accompanying `assert` statement. Next
   uncomment `write_json()` to write the list to a JSON file. Run your code. Review the file output.

## 7.0 Working with dates and times

Each NYT article includes a publication date formatted as an
[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime string. The NYT article publication date
values are formatted as follows:

```commandline
YYYY-MM-DDThh:mm:ss+hhmm (i.e., Year-Month-DayThour:minute:second+UTC_offset)
```

```python
{
    ...
    "pub_date": "2024-02-15T15:30:13+0000",
    ...
}
```

In a previous lecture you leveraged `str.startswith()` to access the year component of the date/time
string. Accessing other components of the date/time string either individually or as part of a group
using only string methods or slicing is doable but tricky and inelegant.

The Python standard library includes a [`datetime`](https://docs.python.org/3/library/datetime.html)
module for working with dates and times (other useful standard modules include `calendar`, `time`,
and `zoneinfo`).

You must import the module in order to utilize it. You can either import the `datetime` module or
import the module's `datetime` class directly by employing the `from` keyword. You can create
datetime objects in a number of ways:

```python
import datetime as dt


lecture_now = dt.datetime(2024, 4, 2, 16, 0, 0) # 24 hr clock
now = dt.datetime.now()
utc_now = dt.datetime.now(dt.UTC)
today = dt.datetime.today()
```

Each NYT article's publication date can be converted to a `datetime` object by calling the object's
`fromisoformat()` _or_ `strptime()` method as outlined below:

```python
pub_date = dt.datetime.fromisoformat(article["pub_date"])
# or
pub_date = dt.datetime.strptime(article["pub_date"], "%Y-%m-%dT%H:%M:%S%z") # format defined
```

Once instantiated you can access a variety of `datetime` object
[attributes](https://docs.python.org/3/library/datetime.html#datetime-objects) such as year, month,
day, hour, minute, second, etc.

For example, if you needed to return all articles published during February 2024 you could write a
nested `for` loop to accomplish the task that leverages the `datetime` object's `year` and `month`
attributes as filters:

```python
feb_2024_articles = []
for article in nyt_articles:
    pub_date = dt.datetime.fromisoformat(article["pub_date"])
    if pub_date.year == 2024 and pub_date.month == 2:
        feb_2024_articles.append(trim_article(article))
```

You could also retrieve the articles utilizing a list comprehension:

```python
feb_2024_articles_v1 = [
    trim_article(article)
    for article in nyt_articles
    if dt.datetime.fromisoformat(article["pub_date"]).year == 2024
    and dt.datetime.fromisoformat(article["pub_date"]).month == 2
]
```

:bulb: This week's problem set features a challenge involving a date/time filter so take a moment to
explore the `datetime` object.
