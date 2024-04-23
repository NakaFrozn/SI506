import five_oh_six as utl


# key_map: maps old keys to new keys
# key-value pairs excluded = 1 (producers)
# key-value pairs renamed = 2 (episode->episode_number, opening_crawl->crawl)
# key-value pairs reordered

KEY_MAP = {
    "episode": "episode_number",
    "title": "title",
    "opening_crawl": "crawl",
    "director": "director",
    "release_date": "release_date",
    "url": "url",
}


def create_entity(data, keys):
    """Create a new entity from the given data and keys.

    Parameters:
        data (dict): data available for the entity
        keys (dict): mappings between old and new keys

    Returns:
        dict: the transformed data
    """

    pass  # TODO implement


def main():
    """Entry point of program. Orchestrates workflow

    Parameters:
        None

    Returns:
        None
    """

    # Get films
    films = None  # TODO read data-films.json

    # Transform films
    star_wars_films = None  # TODO employ a list comprehension to transform films data

    # Sort films by episode number (descending)
    # Note: episode number does not correspond to release order

    # TODO: in-place sort

    # Write films to file
    utl.write_json("star-wars-films.json", star_wars_films)


if __name__ == "__main__":
    main()
