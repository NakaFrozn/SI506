# SI 506: Comprehensions
import datetime as dt
import json

from pathlib import Path


def categorize_economy(country):
    """Combines The World Bank's Lower and Upper middle income categories into a
    single "Middle income" category. Returns a two-item tuple comprising the
    country name and the income group category ("High income", "Middle income',
    "Low income").

    Parameters:
        country (dict): representation of a country's economy

    Returns
       tuple: two-item tuple comprising the country name and income group
    """

    if country["income_group"] and country["income_group"].lower() == "high income":
        return (country["country_name"], "High income")
    elif country["income_group"] and country["income_group"].lower() in (
        "lower middle income",
        "upper middle income",
    ):
        return (country["country_name"], "Middle income")
    else:
        return (country["country_name"], "Low income")


def add_group(country, group):
    """Combines < country > and < group > data in a new dictionary if and only
    if the < country > country_code equals the < group > country_code. Otherwise
    returns None.

    If a match is obtained a selection of key-value pairs from the < country >
    and < group > dictionaries are inserted into the new dictionary in the
    following order: country_name, country_code, group_name, group_code, and
    income_group.

    Parameters:
        country (dict): represents a country
        group (dict): represents a World Bank group

    Returns:
        dict: combines country and group information in a select list of
              key-value pairs drawn from < country > and < group >
    """

    if country["country_code"].lower() == group["country_code"].lower():
        return {
            "country_name": country["country_name"],
            "country_code": country["country_code"],
            "group_name": group["group_name"],
            "group_code": group["group_code"],
            "income_group": country["income_group"],
        }


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


def get_stem(filepath):
    """Access the final component of a path excluding the suffix. This part is known as
    the stem. Other parts that can be extracted from a Path() instance include
    drive, root, anchor, parents, parent, name, suffix, and suffixes.

    See https://docs.python.org/3/library/pathlib.html#accessing-individual-parts

    Parameters:
        filepath (str): path to the resource

    Returns:
        str: that part of the path known as the stem
    """

    # return filepath.split("/")[-1][:-5]  # drops extension/suffix
    return Path(filepath).stem  # preferred


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


def to_uppercase(value):
    """Attempts to convert a string to uppercase. If a runtime AttribueError or
    ValueError exception is encountered, the function returns the value unchanged.

    Parameters:
        value (str): string to be converted

    Returns:
        str: Uppercase string else returns value unchanged
    """

    try:
        return value.upper()
    except (AttributeError, ValueError):
        return value


def trim_article(article):
    """Returns a "trimmed" dictionary representation of a NYT article. The key-value
    pairs are limited to the main headline, author byline, web URL, and publication date.

    Parameters:
        article (dict): representation of a NYT article

    Returns:
        dict: trimmed or slimmed down representation of a NYT article
    """

    return {
        "headline_main": article["headline"]["main"],
        "byline": article["byline"]["original"],
        "web_url": article["web_url"],
        "pub_date": article["pub_date"],
    }


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

    # 1.0 LIST COMPREHENSION

    # Get Country data
    countries = read_json("./data-wb-economies.json")
    # print(f"\n1.0 countries (len={len(countries)})")

    # for loop
    codes = []
    for country in countries:
        codes.append(country["country_code"])

    # List comprehension
    codes_v1 = None  # TODO list comprehension

    # print(f"\n1.2 codes_v1 (len=({len(codes_v1)})) = {codes_v1[:12]}")

    # Assert equality
    # TODO Uncomment
    # assert codes == codes_v1

    # 1.3 CALL A FUNCTION OR OBJECT METHOD

    codes_v2 = [country["country_code"].upper() for country in countries]

    codes_v3 = None  # TODO list comprehension

    # print(f"\n1.3 codes_v3 (len=({len(codes_v3)})) = {codes_v3[:12]}")

    # Assert equality
    # TODO Uncomment
    # assert codes_v2 == codes_v3

    # 2.0 LIST COMPREHENSIONS AND CONDITIONAL STATEMENTS

    # for loop
    east_asia = []
    for country in countries:
        if country["region"].lower() == "east asia & pacific":
            east_asia.append(country)

    # Print slice
    # print(f"\n2.0.1 east_asia (n={len(east_asia)})\n = {east_asia[:2]}")

    # List comprehension (default sort = country_code)
    east_asia_v1 = None  # TODO list comprehension

    # print(f"\n2.0.2: east_asia_v1 (n={len(east_asia_v1)}) = {east_asia_v1[:2]}")

    # Assert equality
    # TODO Uncomment
    # assert east_asia == east_asia_v1

    # Write to file
    # TODO Uncomment
    # write_json("./stu-east_asia_pacific.json", east_asia_v1)

    # 2.1 CHALLENGE 01

    americas_low_middle = [
        country
        for country in countries
        if (country["income_group"] and country["income_group"] == "Lower middle income")
        and (country["region"].lower() in ["north america", "latin america & caribbean"])
    ]  # TODO list comprehension
    print(americas_low_middle)
    print(f"\n2.1 americas_low_middle (n={len(americas_low_middle)})")

    # Write to file
    # TODO Uncomment
    # write_json("./stu-americas-low_middle.json", americas_low_middle)

    # 2.2 IF-ELSE STATEMENTS

    two_categories = [
        (
            (country["country_name"], "High income")
            if country["income_group"] and country["income_group"].lower() == "high income"
            else (country["country_name"], "Middle/low income")
        )
        for country in countries
    ]

    # Print slice
    # print(f"\n2.2 two_categories (n={len(two_categories)}) = {two_categories[:12]}")

    # 2.3 IF-ELIF-ELSE (IF-ELSE-ELSE)

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

    # Print slice
    print(f"\n2.3.1 three_categories (n={len(three_categories)}) = {three_categories[:12]}")

    # Perhaps more readable
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

    # Print slice
    # print(
    #     f"\n2.3.2 three_categories_v1 (n={len(three_categories_v1)}) = {three_categories_v1[:12]}"
    # )

    # Pythonic!
    three_categories_v2 = None  # TODO list comprehension

    # Print slice
    # print(
    #     f"\n2.3.3 three_categories_v2 (n={len(three_categories_v2)}) = {three_categories_v2[:12]}"
    # )

    # Assert equality
    # TODO Uncomment
    # assert three_categories == three_categories_v1 == three_categories_v2

    # 3.0 LIST COMPREHENSIONS AND NESTED LOOPS

    groups = read_json("./data-wb-groups.json")
    # print(f"\n3.0 groups (len={len(groups)})")

    arab_world = []
    for group in groups:
        if group["group_name"].lower() == "arab world":
            for country in countries:
                if group["country_code"].lower() == country["country_code"].lower():
                    arab_world.append(country)
                    break

    # print(f"\n3.0.1 arab_world (n={len(arab_world)})")

    arab_world_v1 = None  # TODO list comprehension

    # print(f"\n3.0.2 arab_world_v1 (n={len(arab_world_v1)})")

    # Assert equality
    # TODO Uncomment
    # assert arab_world == arab_world_v1

    # Write to file
    # TODO Uncomment
    # write_json("./stu-arab_world-list.json", arab_world_v1)

    # 3.1 CHALLENGE 02

    ssf_count = len([group for group in groups if group["group_code"].lower() == "ssf"])
    # print(f"\n3.1.0 ssf_count = {ssf_count}")

    # Nested for loop example
    sub_saharan_africa = []
    for group in groups:
        if group["group_code"].lower() == "ssf":
            for country in countries:
                if group["country_code"].lower() == country["country_code"].lower():
                    sub_saharan_africa.append(add_group(country, group))

    print(f"\n3.1.1 sub_saharan_africa (n={len(sub_saharan_africa)})")

    # Challenge solution
    sub_saharan_africa_v1 = [
        add_group(country, group)
        for group in groups
        if group["group_code"].lower() == "ssf"
        for country in countries
        if group["country_code"].lower() == country["country_code"].lower()
    ]  # TODO list comprehension

    print(f"\n3.1.2 sub_saharan_africa_v1 (n={len(sub_saharan_africa_v1)})")

    # Assert equality
    # TODO Uncomment
    assert sub_saharan_africa == sub_saharan_africa_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-sub_saharan_africa.json", sub_saharan_africa_v1)

    # 4.0 DICTIONARY COMPREHENSION

    # Get data
    nyt_articles = read_json("./data-nyt-articles-climate.json")
    # print(f"\n4.0 articles (len={len(nyt_articles)})")

    # 4.2 SIMPLE EXAMPLE

    article_word_counts = {}
    for article in nyt_articles:
        article_word_counts[article["web_url"]] = article["word_count"]

    print(f"\n4.2.1 article_word_counts (len={len(article_word_counts)})")

    # dict comprehension
    article_word_counts_v1 = {
        article["web_url"]: article["word_count"] for article in nyt_articles
    }  # TODO dict comprehension

    print(f"\n4.2.2 article_word_counts_v1 (len={len(article_word_counts_v1)})")

    # Assert equality
    # TODO Uncomment
    assert article_word_counts == article_word_counts_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-article_word_counts.json", article_word_counts_v1)

    # 4.3 CALL A FUNCTION OR OBJECT METHOD

    article_pub_dates = {}
    for article in nyt_articles:
        # path = article["web_url"].split("/")[-1][:-5]  # drops extension/suffix
        path = Path(article["web_url"]).stem  # better
        pub_date = article["pub_date"].split("T")[0]
        article_pub_dates[path] = pub_date

    print(f"\n4.3.1 article_pub_dates (len={len(article_pub_dates)})")

    article_pub_dates_v1 = {
        Path(article["web_url"]).stem: article["pub_date"].split("T")[0] for article in nyt_articles
    }  # TODO dict comprehension

    print(f"\n4.3.2 article_pub_dates_v1 (len={len(article_pub_dates_v1)})")

    # Assert equality
    # TODO Uncomment
    assert article_pub_dates == article_pub_dates_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-article_pub_dates.json", article_pub_dates_v1)

    # 5.0 DICTIONARY COMPREHENSION AND CONDITIONAL STATEMENTS

    multimedia = {}
    for article in nyt_articles:
        if article["document_type"].lower() == "multimedia":
            multimedia[article["web_url"]] = article

    print(f"\n5.0.1 multimedia (n={len(multimedia)})")

    # Dictionary comprehension
    multimedia_v1 = {
        article["web_url"]: article
        for article in nyt_articles
        if article["document_type"].lower() == "multimedia"
    }  # dict comprehension

    print(f"\n5.0.2 multimedia_v1 (n={len(multimedia_v1)})")

    # Assert equality
    # TODO Uncomment
    assert article_pub_dates == article_pub_dates_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles-multimedia.json", multimedia)

    # 5.1 CHALLENGE 03

    keep_keys = ("web_url", "pub_date", "document_type", "type_of_material", "word_count")

    articles_slim = []
    for article in nyt_articles:
        dict_ = {}  # Note use of trailing underscore; avoids shadowing dict data type name
        for key, val in article.items():
            if key in keep_keys:
                dict_[key] = val
        articles_slim.append(dict_)

    # Last dictionary
    print(f"\n5.1.1 articles_slim (len=(len={len(articles_slim)})) = {articles_slim[-1]}")

    # Alternative (for loop / dict comprehension)
    keep_keys = ("web_url", "pub_date", "document_type", "type_of_material", "word_count")

    articles_slim_v1 = []
    for article in nyt_articles:
        articles_slim_v1.append(
            {key: val for key, val in article.items() if key in keep_keys}
        )  # TODO add dict comprehension

    # Last dictionary
    print(f"\n5.1.2 articles_slim_v1 (len=(len={len(articles_slim_v1)})) = {articles_slim_v1[-1]}")

    # Assert equality
    # TODO Uncomment
    assert articles_slim == articles_slim_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles_slim.json", articles_slim_v1)

    # 5.2 CHALLENGE 04

    articles_slim_v2 = [
        {key: val for key, val in article.items() if key in keep_keys} for article in nyt_articles
    ]  # TODO list comprehension with nested dict comprehension

    # Last dictionary
    print(f"\n5.2 articles_slim_v2 (len=(len={len(articles_slim_v2)})) = {articles_slim_v2[-1]}")

    # Assert equality
    # TODO Uncomment
    assert articles_slim == articles_slim_v1 == articles_slim_v2

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles_slim.json", articles_slim_v2)

    # 5.2 IF-ELSE

    # Read time estimated at 238 words/min.
    # https://thereadtime.com/#:~:text=How%20Long%20Does%20It%20Take,seconds%20to%20read%201000%20words.

    read_time = {}
    for article in articles_slim:
        if article["document_type"].lower() == "article":
            path = get_stem(article["web_url"])
            if (article["word_count"]) >= 750:
                read_time[path] = {"word_count": article["word_count"], "read time": "LONG"}
            else:
                read_time[path] = {"word_count": article["word_count"], "read time": "SHORT"}

    print(f"\n5.2.1 read_time (n={len(read_time)})")

    read_time_v1 = {
        get_stem(article["web_url"]): (
            {"word_count": article["word_count"], "read time": "LONG"}
            if (article["word_count"]) >= 750
            else {"word_count": article["word_count"], "read time": "SHORT"}
        )
        for article in articles_slim
        if article["document_type"].lower() == "article"
    }  # TODO dict comprehension

    print(f"\n5.2.1 read_time_v1 (n={len(read_time_v1)})")

    # Assert equality
    # TODO Uncomment
    assert read_time == read_time_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-read_time-v1p0.json", read_time_v1)

    # 5.3 IF-ELIF-ELSE

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

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-read_time-v1p1.json", read_time)

    # 6.0 DICTIONARY COMPREHENSION AND NESTED LOOPS

    # Get authors
    authors = {}
    for article in nyt_articles:
        people = []
        for person in article["byline"]["person"]:
            people.append(get_author(person))
        authors[article["web_url"]] = people  # new key-value pair

    print(f"\n6.0.1 authors (n={len(authors)})")

    # dictionary comprehension (with nested list comprehension)
    authors_v1 = {
        article["web_url"]: [get_author(person) for person in article["byline"]["person"]]
        for article in nyt_articles
    }  # TODO dict comprehension with nested list comprehension

    print(f"\n6.0.1 authors_v1 (n={len(authors_v1)})")

    # Assert equality
    # TODO Uncomment
    assert authors == authors_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-article_authors.json", authors)

    # 6.1 CHALLENGE 05

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

    print(f"\n6.1.1 polar_articles (n={len(polar_articles)})")

    polar_articles_v1 = {
        get_stem(article["web_url"]): trim_article(article)
        for article in nyt_articles
        for keyword in article["keywords"]
        if keyword["name"] == "glocations"
        and keyword["value"].lower()
        in (
            "antarctic regions",
            "arctic regions",
        )
    }  # TODO dict comprehension

    print(f"\n6.1.2 polar_articles_v1 (n={len(polar_articles_v1)})")

    # Assert equality
    # TODO Uncomment
    assert polar_articles == polar_articles_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles_polar.json", polar_articles_v1)

    # 7.0 WORKING WITH DATES AND TIMES

    lecture_now = dt.datetime(2024, 4, 2, 16, 0, 0)  # 24 hr clock
    print(f"\n7.0.0 lecture_date = {lecture_now}")

    now = dt.datetime.now()
    # print(f"\n7.0.1 now = {now}")

    utc_now = dt.datetime.now(dt.UTC)
    # print(f"\n7.0.2 utc_now = {utc_now}")

    today = dt.datetime.today()
    # print(f"\n7.0.3 today = {today}")

    article = nyt_articles[0]  # Access article
    pub_date = dt.datetime.fromisoformat(article["pub_date"])
    # print(f"\n7.0.4 pub_date (type={type(pub_date)}) = {pub_date}")

    # Alternative
    pub_date = dt.datetime.strptime(article["pub_date"], "%Y-%m-%dT%H:%M:%S%z")  # format defined
    # print(f"\n7.0.5 pub_date (type={type(pub_date)}) = {pub_date}")

    # Get February 2024 articles
    feb_2024_articles = []
    for article in nyt_articles:
        pub_date = dt.datetime.fromisoformat(article["pub_date"])
        if pub_date.year == 2024 and pub_date.month == 2:
            feb_2024_articles.append(trim_article(article))
    feb_2024_articles_v1 = [
        trim_article(article)
        for article in nyt_articles
        if dt.datetime.fromisoformat(article["pub_date"]).year == 2024
        and dt.datetime.fromisoformat(article["pub_date"]).month == 2
    ]

    # Assert equality
    # TODO Uncomment
    assert feb_2024_articles == feb_2024_articles_v1

    # Write to file
    # TODO Uncomment
    write_json("./stu-nyt-articles-202402.json", feb_2024_articles_v1)


if __name__ == "__main__":
    main()
