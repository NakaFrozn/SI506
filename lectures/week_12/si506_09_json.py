# SI 506: Nested data structures

import json

from pathlib import Path

from isort import file


def get_author(author):
    """Accesses the author's last name, first name, and middle name values and
    returns a name string to the caller. If middle name is < None > converts
    the value to blank <''> and then strips the string to remove the unnecessary
    space.

    String format:

    "< lastname >, < firstname > < middlename >"

    Falsy value handling:

    The possibility exists that < None > is assigned to < middlename >. An f-string
    will convert < None > to "None" which is no substitute for the missing middle name.

    Note the expression in the f-string < author['middlename'] or '' >. The logical
    < or > operator privileges the truthy blank value < '' > over a falsy
    author['middlename'] value (e.g., < None >), resulting in a value substitution.

    Calling `str.strip()` on the f-string then removes the space ensuring that only
    "< lastname >, < firstname >" is returned to the caller.

    Parameters:
        author (dict): representation of a byline author

    Returns:
        str: last name, first name plus middle name if the latter exists
    """

    return f"{author['lastname']}, {author['firstname']} {author['middlename'] or ''}".strip()


def has_keyword(keywords, name, values):
    """Determines if the passed in < keywords > list of keyword dictionaries contains
    at least one instance of the passed in < name > and a value in < values >. If a
    match is obtained < True > is returned; otherwise < False > is returned.

    keyword dict = {'name': < name >, 'value': < value >, ...}

    Parameters:
        keywords (list): nested keyword dictionaries
        name (str): keyword dictionary "name" value
        value (list): one or more keyword values to match on

    Returns:
        bool: returns True if a match is obtained; otherwise returns False
    """

    for keyword in keywords:
        if keyword["name"] == name and keyword["value"].lower() in values:
            return True
    return False


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding="utf-8", ensure_ascii=False, indent=2):
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

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # 2.3 CHALLENGE 01
    parentpath = Path(__file__).resolve().parent
    filepath = parentpath.joinpath("data-nyt-articles-research.json")  # TODO Assign Path() object
    print(f"\n2.3 filepath = {filepath}")

    # Get data
    articles = read_json(filepath)  # TODO Call function, replace empty list with return value
    print(f"\n2.3.1 All articles (n={len(articles)})")

    # Get 2024 articles only
    articles_2024 = []
    for article in articles:
        if article['pub_date'].find("2024") > -1:
            articles_2024.append(article)  # TODO Add if statement

    print(f"\n2.3.2 2024 articles (n={len(articles_2024)})")

    # Write to file
    # TODO Uncomment
    write_json("stu-nyt-articles-2024.json", articles_2024)

    # 3.0 NESTED LOOPS

    nums = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500],
        [1000, 2000, 3000, 4000, 5000],
    ]

    # TODO Uncomment
    # print(f"\n3.0 Nested loop example")
    # for i in nums:
    #     for j in i:
    #         print(sum(i) * j)  # sum the list element then multiply by each element

    # Function call
    paleo_articles = []
    for article in articles:
        if has_keyword(article["keywords"], "subject", ("dinosaurs", "fossils", "paleontology")):
            paleo_articles.append(article)

    # print(f"\n3.0.1 paleo_articles (n={len(paleo_articles)})")

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-paleo-articles-v1.json", paleo_articles)

    # Nested loop
    paleo_articles = []
    for article in articles:
        pass  # TODO Add nested loop

    # print(f"\n3.0.2 paleo_articles (n={len(paleo_articles)})")

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-paleo-articles-v2.json", paleo_articles)

    # 3.1 CHALLENGE 02

    dinosaur_count = 0

    # TODO Paste in paleo_articles code and refactor

    # TODO Uncomment
    # print(f"\n3.1 dinosaur_count = {dinosaur_count}")

    # 3.2 CHALLENGE 03

    dinosaur_articles = []

    # TODO Paste in Challenge 02 code and refactor

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-dinosaur_articles.json", dinosaur_articles)

    # ADDITIONAL CHALLENGES

    # 4.1 CHALLENGE 04

    keyword_values = {}

    # TODO Add nested loop and conditional statement

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-keyword_values-v1.json", keyword_values)

    # 4.2 CHALLENGE 05

    keyword_values = {
        "subject": [],
        "organizations": [],
        "glocations": [],
        "persons": [],
        "creative_works": [],
    }

    # TODO Paste in Challenge 04 code and refactor

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-keyword_values-v2.json", keyword_values)

    # BONUS: sort dictionary keys and values
    # TODO Uncomment
    # keyword_values_sorted = {
    #     k: v for k, v in sorted(keyword_values.items(), key=lambda x: (x[0], x[1].sort()))
    # }

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-keyword_values-v3.json", keyword_values_sorted)

    # 4.3 CHALLENGE 06

    # TODO Paste in Challenge 05 code and refactor

    # BONUS: sort nested dictionaries
    # TODO Uncomment
    # keyword_counts_sorted = {k: dict(sorted(v.items())) for k, v in sorted(keyword_counts.items())}

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-keyword_value_counts.json", keyword_counts_sorted)

    # 4.4 CHALLENGE 07

    paleo_authors = []
    for article in paleo_articles:
        pass  # TODO Implement nested loop, call get_author(), add conditional statement

    # Authors count
    # TODO Uncomment
    # print(f"\n3.6 paleo_authors (len={len(paleo_authors)})")

    # BONUS: Sort authors
    # TODO Uncomment
    # paleo_authors_sorted = [author for author in sorted(paleo_authors)]

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-paleo_authors.json", paleo_authors_sorted)

    # 4.5 CHALLENGE 08

    paleo_author_articles = {}
    for author in paleo_authors:
        for article in paleo_articles:
            pass  # TODO Implement nested loop, call get_author(), build dict, add conditional statments

    # Confirm authors count (check keys)
    # TODO Uncomment
    # print(f"\n3.7 paleo_authors_articles author keys (len={len(paleo_author_articles.keys())})")

    # BONUS: Sort authors and articles
    # TODO Uncomment
    # paleo_author_articles_sorted = {
    #     k: sorted(v, key=lambda x: x["pub_date"], reverse=True)
    #     for k, v in sorted(paleo_author_articles.items())
    # }

    # Write to file
    # TODO Uncomment
    # write_json("stu-nyt-paleo_author_articles.json", paleo_author_articles_sorted)


if __name__ == "__main__":
    main()
