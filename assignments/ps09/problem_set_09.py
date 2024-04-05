import json
from pathlib import Path
from datetime import datetime


def convert_published_date_value(data):
    """Converts the value in each article pub_date key.

    Assume the pub_date value is a string. Convert this value to a datetime object using the
    datetime.strptime() or the datetime.fromisoformat() function with the datetime string formatted as

    '< Year >-< Month >-< Day >T< Hour >:< Minute >:< Second >< %z UTC offset >".

    Hint: This function employs a nested for loop to interact with an article's key-value pairs.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.

    Returns:
        data (list): Updated list of dictionaries, with the value for pub_date key
              converted properly.
    """

    for article in data:
        for key in article.keys():
            if key == article.
            article[key] = datetime.fromisoformat(article["pub_date"])
    return data

def create_headline_url_list(data):
    """Creates a list of article headlines and urls.

    Hint: the comprehension expression is a list comprehension that iterates through the data
    and creates a new list of tuples containing the desired elements.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.

    Returns:
        list: A list of tuples, each containing the article's headline and url.
    """

    result = [
        (article["headline"]["main"], article["web_url"])
        for article in data
    ]
    return result



def filter_articles(data, keys_to_exclude):
    """Filters each dictionary down to necessary information within the given < data >
    list based on the < keys_to_exclude > list.

    Hint: the comprehension expression is comprised of a dictionary comprehension
    nested within a list comprehension.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.
        keys_to_exclude (list): A list of key names to exclude from each article
                                dictionary.

    Returns:
        list: A list of dictionaries, each containing filtered information
              about a Technology themed New York Times article.
    """

    result = [
        {
            k: v
            for k,v in article.items()
            if k not in keys_to_exclude
        }
        for article in data
    ]
    return result



def filter_empty_keywords(data):
    """Filters out articles which have empty lists as values for the 'keywords' key.

    Hint: the comprehension expression is a list comprehension looping over the data.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Technology themed New York Times article.

    Returns:
        list: A list of dictionaries representing articles having keywords in them.
    """

    result = [
        article for article in data
        if len(article["keywords"]) > 0
    ]
    return result


def format_author_name(person):
    """Reformats an author's name given an article's byline person dictionary. Employs
    a formatted string literal to return a string containing the author's last name and
    first name with the first letter of both names capitalized per the format specified
    below.

    Format: "< Last name >, < First name >"

    Parameters:
        person (dict): A dictionary containing information
                        about an article's byline person list.

    Returns:
        str: A string containing the author's name seperated by a single space.
    """

    pass


def get_author_names(article):
    """Returns a list of article authors by employing a list comprehension. Delegates to
    the helper function < format_author_name() > the task of formatting each name added to the
    new list.

    Parameters:
        article (dict): A dictionary containing information about a technology-themed
        New York Times article.

    Returns:
        list: A list containing each author's first and last name, seperated by a single space.
    """

    pass


def get_articles_by_organization(articles, organization):
    """Filter articles based on the given organization.

    Hints: Using the comprehension expression to filter articles based on the given organization.

    Parameters:
        articles (list): A list of dictionaries, each containing information
                        about a technology-themed New York Times article.
        organization (str): String representing the organization of the article.

    Returns:
        list: A list containing the articles of the same, desired organization.
    """

    pass


def get_articles_by_topic(articles, topic):
    """Filter articles based on the given topic.

    Hints: Using the comprehension expression to filter articles based on the given topic.

    Parameters:
        articles (list): A list of dictionaries, each containing information
                        about a technology-themed New York Times article.
        topic (str): String representing the topic of the article.

    Returns:
        list: A list containing the articles of the same, desired topic.
    """

    pass


def get_organization_names(article):
    """Gets list of organizations mentioned in the 'keywords' section of the technology-themed New
    York Times article.

    Hint: the comprehension expression is a list comprehension looping over the article's keywords
    key. The loop variable must be named < keyword >.

    Parameters:
        article (dict): A dictionary containing information
                        about a technology-themed New York Times article.

    Returns:
        list: A list containing all the organization names present in the article (including repeated).
    """
    pass


def get_news_by_location(data, location):
    """Filter articles based on the given location.

    Hint: the comprehension expression is a list comprehension which loops over the data and
    checks if the location is matching. Note that your loop variable for the outer loop must be
    < article >, and your loop variable for the inner loop must be < keyword >.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.
        location (str): String representing the location of the article.

    Returns:
        list: A list containing the articles of the same, desired location.
    """
    pass


def get_organization_by_type(articles):
    """Get a list of unique organizations mentioned in the 'keywords' section
    of the specific themed New York Times articles.

    Hints: Using the accumulator structure to store unique organizations mentioned
    in the 'keywords' section of the themed New York Times articles.

    Parameters:
        articles (list): A list of dictionaries, each containing information about a
        specific themed New York Times article.

    Returns:
        list: A list of unique organizations mentioned in the 'keywords' section of
        the specific themed New York Times articles.
    """
    pass


def get_unique_authors(articles):
    """Get a list of unique authors from the articles.

    Hints: Using the accumulator structure to store unique authors from the articles.

    Parameters:
        articles (list): A list of dictionaries, each containing information about a
        specific themed New York Times article.

    Returns:
        list: A list of unique authors from the articles.
    """
    pass


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        return json.load(file_obj)


def show_archival_status(data, active_year_threshold):
    """Classifies the article as active or archived depending on specified threshold.

    Hint: the comprehension expression implements an if-else in a list comprehension iterating
    through the data.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Technology themed New York Times article
                     with pub_date converted to datetime object.
        active_year_threshold (int): An integer representing the earliest year an article can be
                                     published in to be considered active.

    Returns:
        list: A list of tuples containing the article headline and its status.
    """

    pass


def write_json(
    filepath,
    data,
    encoding="utf-8",
    ensure_ascii=False,
    indent=4,
    sort_keys=True,
    default=str,
):
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
        json.dump(
            data,
            file_obj,
            ensure_ascii=ensure_ascii,
            indent=indent,
            sort_keys=sort_keys,
            default=default,
        )


# Entry
def main():
    """Entry point for the program. Orchestrates the workflow.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0
    print("Problem 1:\n")

    # 1.1
    filepath = Path("data-nyt-articles-tech.json").resolve()
    # 1.2
    nyt_tech_raw = read_json(filepath)
    # 1.4
    headline_url_list = create_headline_url_list(nyt_tech_raw)
    # 1.5
    filename = "stu-headline-url-list.json"
    # 1.6
    write_json(filename, headline_url_list)
    # 2.0
    print("Problem 2:\n")

    keys_to_exclude = [
        "abstract",
        "web_url",
        "snippet",
        "lead_paragraph",
        "source",
        "document_type",
        "news_desk",
        "type_of_material",
    ]

    # 2.2
    nyt_tech_filtered = filter_articles(nyt_tech_raw, keys_to_exclude)
    
    # 2.3
    filename = "stu-nyt-tech-filtered.json"
    # 2.4
    write_json(filename, nyt_tech_filtered)

    # 3.0
    print("Problem 3:\n")

    # 3.2
    nyt_tech_cleaned = filter_empty_keywords(nyt_tech_filtered)
    # 3.4

    # 3.5

    # 3.6

    # 4.0
    print("Problem 4:\n")

    # 4.2

    # 4.3

    # 4.4

    # 5.0
    print("Problem 5:\n")

    # 5.2

    # 5.3

    # 5.4

    # 6.0
    print("Problem 6:\n")

    # 6.2

    # 6.3

    # 6.4

    # 7.0
    print("Problem 7:\n")

    # 7.3

    # 7.3.1-7.3.6

    # 7.4

    # 7.5

    # 8.0
    print("Problem 8:\n")

    # 8.3

    # 8.4

    # 8.5

    # 8.6


if __name__ == "__main__":
    main()
