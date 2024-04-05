# SI 506 Week 11 Bonus Challenge

import json


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
    """Entry point for program. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # Get data
    nyt_articles = read_json("./data-nyt_climate_articles.json")

    # CHALLENGE 03

    keep_keys = ("web_url", "pub_date", "document_type", "type_of_material", "word_count")

    articles_slim = []
    for article in nyt_articles:
        dict_ = {}  # Note use of trailing underscore; avoids shadowing dict data type name
        for key, val in article.items():
            if key in keep_keys:
                dict_[key] = val
        articles_slim.append(dict_)

    # Last dictionary
    # print(f"\n3.1 articles_slim (len=(len={len(articles_slim)})) = {articles_slim[-1]}")

    # Alternative (for loop / dict comprehension)
    keep_keys = ("web_url", "pub_date", "document_type", "type_of_material", "word_count")

    articles_slim_v1 = []
    for article in nyt_articles:
        articles_slim_v1.append({key: val for key, val in article.items() if key in keep_keys})

    # Last dictionary
    # print(f"\n3.2 articles_slim_v1 (len=(len={len(articles_slim_v1)})) = {articles_slim_v1[-1]}")

    # Assert equality
    # TODO Uncomment
    # assert articles_slim == articles_slim_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles_slim_v1.json", articles_slim_v1)

    # CHALLENGE 04

    articles_slim_v2 = [
        {key: val for key, val in article.items() if key in keep_keys} for article in nyt_articles
    ]

    # Last dictionary
    # print(f"\n4.1 articles_slim_v2 (len=(len={len(articles_slim_v2)})) = {articles_slim_v2[-1]}")

    # Assert equality
    # TODO Uncomment
    # assert articles_slim == articles_slim_v1 == articles_slim_v2

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles_slim_v2.json", articles_slim_v2)


if __name__ == "__main__":
    main()
