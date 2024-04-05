# SI 506 Week 11 Bonus Challenges

## Gradescope URL

[https://www.gradescope.com/courses/569572](https://www.gradescope.com/courses/569572)

:bulb: You can resubmit your solution as many times as needed until the submission period expires.

## Code formatting

The autograder assumes that you have formatted your code submission(s) using VS Code's Black
Formatter extension and that you have set the maximum `line-length` to 100 characters. See the VS
Code [install guides](https://si506.org/guides/) for set up instructions.

## Challenge 03

__Task__: Replace an inner `for` loop with a dictionary comprehension.

1. Convert the following nested `for` loop to an (outer) `for` loop and an (inner)
   __dictionary comprehension__. Append each new dictionary created by the comprehension to
   `articles_slim_v1`. The inner loop block appends a new dictionary to `articles_slim` whose
   key-value pairs are limited to the keys specified in the tuple `keep_keys`.

   ```python
   keep_keys = ('web_url', 'pub_date', 'document_type', 'type_of_material', 'word_count')

   articles_slim = []
   for article in nyt_articles:
       dict_ = {} # Note use of trailing underscore; avoids shadowing dict data type name
       for key, val in article.items():
           if key in keep_keys:
               dict_[key] = val
       articles_slim.append(dict_)

   # Convert to
   articles_slim_v1 = []
   for article in nyt_articles:
       pass # TODO convert inner loop block to a dict comprehension
   ```

2. After populating `articles_slim_v1` uncomment the accompanying `assert` statement. Next uncomment
   `write_json()` to write the list to a JSON file. Run your code. Review the file output.

## Challenge 04

__Task__: Replace an outer `for` loop with a list comprehension.

:bulb: The general comprehension pattern that you will implement for this challenge is as follows:

```python
new_list = [expression for element in sequence]
```

However, for this challenge the dictionary comprehension created in Challenge 03 constitutes the
"expression" in the list comprehension that you will implement. In other words, you _must_
__locate__cthe dictionary comprehension __inside__ the list comprehension.

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
