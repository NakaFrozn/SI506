# SI 506: Nested data structures

## Topics

1. JSON
   1. JSON data structures
   2. JSON value types
   3. JSON example
2. `json` module
   1. Reading JSON files (`json_load()`)
   2. Writing to a JSON file (`json_dump()`)
   3. Challenge 01
3. Nested loops
   1. Challenge 02
   2. Challenge 03
4. Additional challenges
   3. Challenge 04
   4. Challenge 05
   5. Challenge 06
   6. Challenge 07
   7. Challenge 08

## Data

[The New York Times](https://www.nytimes.com/) provides an
[Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview)
(Application Programming Interface) that permits keyword searching and retrieval of JSON
representations of NY Times articles.

Today's data comprises a list of 300+ JSON objects that represent the most recent NY Times articles
published by the [Science](https://www.nytimes.com/section/science) Desk that report on scientific
research findings.

An example JSON document named `nyt-article-example.json` is included in today's lecture
files. You should review it and familiarize yourself with its structure and name-value pairs.

:bulb: Certain name-value pairs have been removed from the JSON documents in the interests of
brevity. In addition, a "person" object containing all `null` values has also been removed in order
to eliminate the need to introduce exception handling in your code.

## 1.0 JSON

[JSON](https://www.json.org/json-en.html) (JavaScript Object Notation) is a lightweight data
interchange format for exchanging information between systems.

JSON consists of two basic data structures and several value types.

### 1.1 JSON data structures

1. An _unordered_ set of name-value pairs known as an _object_ and denoted by curly braces (`{}`).
2. An _ordered_ list of values known as an _array_ and denoted by square brackets (`[]`).

### 1.2 JSON value types

1. string (double quotes `""` only)
2. number
3. object `{}`
4. array `[]`
5. boolean (`true` | `false`)
6. `null`

### 1.3 JSON example

Below is an example JSON representation of a NYT article sourced from the NYT article search
[API](https://developer.nytimes.com/docs/articlesearch-product/1/overview).

:bulb: Certain name-value pairs have been removed from the JSON document below in the interest of
brevity. For instance only the top four (`4`) keywords (out of ten (`10`) have been included in the
example.

```json
{
  "abstract": "A new paper challenges the idea that the large, carnivorous Spinosaurus dived after prey rather than wading and plucking it out of the water.",
  "web_url": "https://www.nytimes.com/2024/03/06/science/spinosaurus-dinosaur-fossil-dive.html",
  "snippet": "A new paper challenges the idea that the large, carnivorous Spinosaurus dived after prey rather than wading and plucking it out of the water.",
  "lead_paragraph": "Spinosaurus was one of the largest carnivorous dinosaurs, and it ate fish. That much paleontologists agree on.",
  "source": "The New York Times",
  "headline": {
    "main": "A Swimming Dinosaur? Maybe Not, Study Says",
    "kicker": null,
    "content_kicker": null,
    "print_headline": "Doubts Raised About Idea of a Swimming Dinosaur",
    "name": null,
    "seo": null,
    "sub": null
  },
  "keywords": [
    {
      "name": "subject",
      "value": "Paleontology",
      "rank": 1,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Dinosaurs",
      "rank": 2,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Fossils",
      "rank": 3,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Research",
      "rank": 4,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Statistics",
      "rank": 5,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Bones",
      "rank": 6,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Fish and Other Marine Life",
      "rank": 7,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Endangered and Extinct Species",
      "rank": 8,
      "major": "N"
    },
    {
      "name": "organizations",
      "value": "PLoS One (Journal)",
      "rank": 9,
      "major": "N"
    },
    {
      "name": "persons",
      "value": "Myhrvold, Nathan",
      "rank": 10,
      "major": "N"
    }
  ],
  "pub_date": "2024-03-06T19:00:05+0000",
  "document_type": "article",
  "news_desk": "Science",
  "section_name": "Science",
  "byline": {
    "original": "By Kenneth Chang",
    "person": [
      {
        "firstname": "Kenneth",
        "middlename": null,
        "lastname": "Chang",
        "qualifier": null,
        "title": null,
        "role": "reported",
        "organization": "",
        "rank": 1
      }
    ],
    "organization": null
  },
  "type_of_material": "News",
  "word_count": 1016
}
```

## 2.0 `json` module

Like the `csv` module the Python standard libary's `json` module provides enhanced functionality for
working with JSON files. JSON is a lightweight data interchange format for exchanging information
between systems.

To use the `json` module you must import it:

```python
import json
```

There are four `json` module functions; two of which are of particular interest to us:

| Function          | Purpose                                                                                                |
|:------------------|:-------------------------------------------------------------------------------------------------------|
| __`json.load()`__ | _Deserialize_ (decode) a text or binary file that contains a JSON document to a `dict` or `list`.      |
| __`json.dump()`__ | _Serialize_ (encode) a Python object as a JSON formatted stream to be stored in a file.                |
| `json.loads()`    | _Deserialize_ (decode) a string, bytes, or bytearray containing a JSON document to a `dict` or `list`. |
| `json.dumps()`    | _Serialize_ (encode) a Python object to a JSON formatted string.                                       |

Since you will also be working with JSON documents between now and the end of the semester
implmenting a function that can read a JSON document as well one that can write a JSON document to
a file will prove useful.

### 2.1 Reading JSON files (`json_load()`)

The function `read_json()` reads a JSON document per the provided filepath, calls the json module's
`json.load()` function in order to _decode_ the file data as a `dict` or a `list` (of dictionaries),
before returning the decoded data to the caller.

```python
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)
```

### 2.2 Writing to a JSON file (`json_dump()`)

The function `write_json()` accepts a dictionary or a list of dictionaries, calls the json module's
`json.dump()` function in order to _encode_ the passed in data as JSON before writing the encoded
data to the target file.

```python
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)
```

### 2.3 Challenge 01

__Task__: Read in the NY Times JSON article, extract articles written in 2024, and write the
articles that meet the filter condition to a file as JSON.

1. In `main()`, create a `Path` instance by passing to it the following filename:
   `"data-nyt-articles-research.json"`. Then call the `Path` object's `absolute()` _or_ `resolve()`
   method to render the path absolute. Assign the `Path` object to a variable named `filepath`.

2. Call the function `read_json()` and pass to it the following argument: `filepath`. You will
   retrieve NYT Science Desk articles filtered on the subject "Research". Assign the return
   value to a variable named `articles`.

3. Loop over `articles` and in the loop block write an `if` statement that identifies
   articles with a 2024 `pub_date` year value. Append each 2024 article to a list (name your
   choice).

   :bulb: __Slice__ the `pub_date` value to access the year. Each article dictionary contains an
   [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) date string formatted as the follows:

   ```python
   {
     ...
     "pub_date": "2024-03-11T10:00:23+0000",
     ...
   }
   ```

4. After exiting the loop, call the function `write_json` and pass to it the following arguments:

   * `"stu-nyt-articles-2024.json"`
   * `articles_2024`

   Run your code. Review the file output.

## 3.0 Nested loops

A nested loop refers to a loop located within the code block of another loop. During each
iteration of the "outer" loop, the "inner" loop will execute, completing all its iterations (unless
terminated early) _prior_ to the outer loop commencing its next iteration, if any.

```commandline
for < element > in < sequence >:
    # indented block
    for < element > in < element (itself a sequence) >
        < statement A >
        < statement B >
        ...
```

The following example illustrates the concept. Loop over the nested lists and print the result of
summing the list elements multipled by each individual element.

```python
nums = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500],
        [1000, 2000, 3000, 4000, 5000]
    ]

    for i in nums:
        for j in i:
            print(sum(i) * j) # sum the list element then multiply by each element
```

Returning to the NYT articles, what if you were asked to identify articles in the `articles` list
that possess one or more keywords?

:bulb: As an article search aid the NYT utilizes five (`5`) keyword "name" values:

```python
['subject', 'organizations', 'glocations', 'persons', 'creative_works']
```

If I asked you to return a subset of the `articles` list comprising articles tagged with the
following _subject_ keywords

```python
{
  ...
  "keywords": [
    {
      "name": "subject",
      "value": "Dinosaurs",
      "rank": 1,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Fossils",
      "rank": 2,
      "major": "N"
    },
    {
      "name": "subject",
      "value": "Paleontology",
      "rank": 3,
      "major": "N"
    },
    ...
  ],
  ...
}
```

you might choose to write a function that performs a keyword look up (e.g.,
`has_keyword(keywords, name, value)`) and then call the function from inside a `for` loop in order to
identify all the paleontology-related articles.

```python
paleo_articles = []
for article in articles:
   if has_keyword(article["keywords"], "subject", ("dinosaurs", "fossils", "paleontology")):
      paleo_articles.append(article)
```

Alternatively, you could implement a nested loop as the example below illustrates:

```python
paleo_articles = []
for article in articles:
   for keyword in article["keywords"]:
      if keyword["name"] == "subject" and keyword["value"].lower() in (
            "dinosaurs",
            "fossils",
            "paleontology",
      ):
            paleo_articles.append(article)
            break  # avoid appending duplicates due to either/or membership check
```

In the example above, the outer loop iterates over the `articles` list. The inner loop iterates over
each article dictionary's `keywords` list. If the keyword name equals "subject" and the keyword
value is found in the provided tuple of values a match is obtained and the article is appended to
the list `paleo_articles`.

:exclamation: Note the use of the `break` statement inside the inner loop. Since an article
can contain any of the keyword values it is imperative that no additional loop iterations occur
after the first match is obtained otherwise duplicate elements will be appended to the list.

### 3.1 Challenge 02

__Task__: Everybody loves dinosaurs. Adapt the code from the previous example to return a count of
the number of dinosaur-related articles in `paleo_articles`.

1. Copy the nested loop code used to populate the `paleo_articles` list and paste it into the
   Challenge 02 section of `main()`.

2. Replace the empty accumulator `paleo_articles` list with a variable named `dinosaur_counts`. A
   numeric count of articles tagged with the subject keyword "dinosaurs" will be assigned to it.

   :exclamation: Assign a sensible start value to the new variable.

3. Adjust the nested loop as follows:

   1. Outer loop: replace `articles` with `paleo_articles`.

   2. Inner loop: modify the compound conditional statement. Replace the trailing membership test
      with a conditional expression that evaluates whether or not the keyword dictionary's "value"
      key is assigned the string "dinosaurs".

   3. `if` block: replace the `list.append()` call with a variable assignment that increments
      `dinosaur_count` by one (`1`).

4. Uncomment `print()` and run your code. Review the terminal output.

### 3.2 Challenge 03

__Task__: Return a list of dinosaur article dictionaries. Each dictionary added to the list will
contain a subset of the available key-value pairs that describe the article.

:bulb: The goal is to create a list of dictionaries structured as follows:

   ```json
   [
     {
       "headline_main": "An Asteroid Wiped Out Dinosaurs. Did It Help Birds Flourish?",
       "byline": "By Carl Zimmer",
       "web_url": "https://www.nytimes.com/2024/02/12/science/bird-evolution-asteroid-dinosaurs.html",
       "pub_date": "2024-02-12T20:00:14+0000"
     },
     ...
  ]
  ```

1. Copy your Challenge 02 code and paste it into the Challenge 03 section of `main()`.

2. Replace the `dinosaur_count` variable assignment with an empty accumulator list named
   `dinosaur_articles`.

3. Adjust the nested `if` block as follows:

   1. Remove the `dinosaur_count` variable assignment.

   2. Append a new dictionary to `dinosaur_articles` comprising the following key-value pairs:

      * "headline_main": < article's "main" headline value >
      * "byline": < article's "original" byline value >
      * "web_url": < article's "web_url" value >
      * "pub_date": < article's "pub_date" value >

      :bulb: Review `data-nyt-article-example.json` to better understand each article's data
      structure and what key(s) you need to reference to access the associated value. Employ
      __subscript operator chaining__ as required to retrieve the specified values.

4. Uncomment `write_json()` and write `dinosaur_articles` to a JSON file. Run your code. Review the
   file output.

## 4.0 Additional challenges

### 4.1 Challenge 04

__Task__: Create a keyword name dictionary consisting of empty list values that will be used in a
later challenge to hold the associated keyword values. Then write the dictionary to a JSON file.

:bulb: The goal is to create a dictionary comprising the following key-value pairs:

   ```python
   {
     "subject": [],
     "organizations": [],
     "glocations": [],
     "persons": [],
     "creative_works": []
   }
   ```

1. Loop over the `articles` list.

2. Inside the loop block, implement a nested loop that loops over each article's `keywords` list.

3. Inside the nested loop block assign the keyword's `name` to a variable named `name`.

4. Write an `if` statement that checks if `name` is a key in the accumulator dictionary
   `keyword_values`.

   If `name` is __not__ a key in `keyword_values` assign a new key-value pair to the dictionary
   structured as follows:

   * key = `name`
   * value = empty `list`

5. Uncomment `write_json()` and write `keyword_values` to a JSON file. Run your code. Review the
   file output.

### 4.2 Challenge 05

__Task__: Refactor your Challenge 04 code so that you can populate the empty lists with keyword
values. Then write the dictionary to a JSON file.

:bulb: The goal is to adjust the code so that it can insert the appropriate keyword values into
each of the empty keyword name lists:

```python
{
   "subject": ["ACNE", ...],
   "organizations": ["AGENCY FOR HEALTHCARE RESEARCH AND QUALITY", ...],
   "glocations": ["AFRICA", ...],
   "persons": ["Aiden, Erez", ...],
   "creative_works": ["Breaking the Age Code: ...", ...]
}
```

1. Copy your Challenge 04 nested loop code and paste it into the Challenge 05 section of `main()`
   below the `keyword_values` variable assignment.

2. Inside the nested loop __insert a new line__ after the variable assignment
   `name = keyword["name"]` and assign the current keyword's `value` to a variable named `value`.

3. Modify the conditional logic inside the nested list as follows:

   1. If `name` is __not__ a key in `keyword_values` assign the following key-value pair to the
      `keyword_values` dictionary:

      * key = `name`
      * value = a `list` containing `value` as an element

   2. Otherwise, if `name` is a key in `keyword_values` append the related `value` to the list
      assigned to `name`, __if and only if__, `value` is __not__ already a member of the list.

4. Uncomment `write_json()` and write `keyword_values` to a JSON file. Run your code. Review the
   file output.

5. __Bonus__: Uncomment the `article_keywords_sorted` variable assignment and companion call to
   `write_json()`. Run your code. Review file output.

### 4.3 Challenge 06

__Task__: Create a dictionary that holds keyword counts. Populate the dictionary by implementing a
nested loop. Then write the dictionary to a JSON file.

:bulb: The goal is to adjust the code so that it can assign to each keyword name a dictionary of
key-value pairs that hold counts of the number of articles associated with each keyword value:

```python
{
   "subject": {"ACNE": 1, ...},
   "organizations": {"AGENCY FOR HEALTHCARE RESEARCH AND QUALITY": 1, ...},
   "glocations": {"AFRICA": 2, ...},
   "persons": {"Aiden, Erez": 1, ...},
   "creative_works": {"Breaking the Age Code: ...": 1, ...}
}
```

1. Copy your Challenge 05 nested loop and paste it into the Challenge 06 section of `main()`.

2. Modify the conditional logic inside the nested list as follows:

   1. Change all `keyword_values` references to `keyword_counts`.

   2. `if` statement: if `name` is __not__ a key in `keyword_counts` create a new `keyword_counts`
      key-value pair structured as follows:

      * key = `name`
      * value = a new `dict` featuring `value` as the key and `1` as the value

   3. `elif` statement: if `value` does __not__ not match an existing `keyword_counts[name]` key
        assign a new key-value pair to the `keyword_counts[name]` dictionary :

      * key = `value`
      * value = `1`

   4. `else` statement: increment `keyword_counts[name][value]` by `1`.

3. Uncomment the `keywords_counts_sorted` variable assignment and companion call to `write_json()`.
   Run your code. Review the file output.

### 4.4 Challenge 07

__Task__: Extract a list of authors from `paleo_articles`. Then write the list to a JSON file.

:bulb: the goal is to create a list structured as follows:

```python
[
  "Andrews, Robin George",
  "Chang, Kenneth",
  ...
]
```

1. Implement a nested loop that loops over `paleo_articles` (outer loop) and for each article
   encountered in the outer loop, loop over the article's "byline" "person" list (inner loop).

   * :bulb: Outer loop variable name: recommend `article`
   * :bulb: Inner loop variable name: recommend `person`

   :bulb: Employ subscript operator chaining in your loop to access the byline "person" list.

2. Do the following inside the __inner loop__:

   1. Call the function `get_author()` and pass to it the following argument: the `person`
      dictionary element. Assign the return value to a variable named `author`.

      :bulb: Review the `get_author()` docstring. It describes a handy approach for dealing with
      falsy values like `None` when building strings.

   2. Append `author` to the accumulator `paleo_authors` list __if and only if__ the string has not
      been previously appended to the list.

      :exclamation: Do not append duplicate values to the list.

3. Uncomment the `paleo_authors_sorted` variable assignment and companion call to `write_json()`.
   Run your code. Review the file output.

### 4.5 Challenge 08

__Task__: Create a dictionary that links each author in `paleo_authors` to the articles that they
have authored. Then write the dictionary to a JSON file.

:bulb: the goal is to create a dictionary structured as follows:

```python
{
  ...,
  "Golembiewski, Kate": [
    {
       "headline_main": "Scaly Fossil Is the Oldest-Known Piece of Skin",
       "byline": "By Kate Golembiewski",
       "web_url": "https://www.nytimes.com/2024/01/11/science/fossil-skin-oldest-lizard.html",
       "pub_date": "2024-01-11T16:00:08+0000"
     },
     {
       "headline_main": "Amber Fossils Suggest Male Mosquitoes Were Once Bloodsuckers",
       "byline": "By Kate Golembiewski",
       "web_url": "https://www.nytimes.com/2023/12/04/science/male-mosquito-amber-fossil-blood.html",
       "pub_date": "2023-12-04T18:35:56+0000"
     },
     {
       "headline_main": "Clue to Pterosaur Origins Found in Fossil of Flightless 'Rabbit Reptile'",
       "byline": "By Kate Golembiewski",
       "web_url": "https://www.nytimes.com/2023/08/16/science/pterosaur-fossil-brazil.html",
       "pub_date": "2023-08-16T15:00:14+0000"
     },
    ...
  ],
  ...
}
```

1. Implement an outer loop and two (`2`) nested loops.

   * Outer loop: loop over each author in `paleo_authors`.
   * Inner loop (01): loop over each article in `paleo_authors`.
   * Inner loop (02): loop over each person in the article's "byline" "person" list.

   :bulb: The author name will be employed to link the outer loop to the innermost loop.

2. Inside the innermost loop, write a conditional statement that evaluates whether or not the
   outer loop `author` string __equals__ the string returned by calling the function `get_author()`
   and passing to it the following argument: the innermost loop's `person` dictionary.

   1. If the conditional statement evaluates to `True` create the following dictionary literal
      inside the `if` block:

      ```python
      article = {
         "headline_main": article["headline"]["main"],
         "byline": article["byline"]["original"],
         "web_url": article["web_url"],
         "pub_date": article["pub_date"],
      }
      ```

   2. Assign the dictionary to the relevant `author` key in `paleo_author_articles` per the
      following conditions:

      1. If `author` matches an existing `paleo_author_articles` key __append__ the `article` to
         the list assigned to the matching key.

      2. Otherwise, create a new `paleo_author_articles` key-value pair structured as follows:

         * key = `author`
         * value = a new `list` containing the `article` dictionary

3. Uncomment the `paleo_author_articles_sorted` variable assignment and companion call to
   `write_json()`. Run your code. Review the file output.
