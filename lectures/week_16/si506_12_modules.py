# SI 506: Modules, Caching, and Lambda functions

import copy
import pprint
import five_oh_six as utl

from datetime import datetime


# Constants
CACHE_FILEPATH = "./CACHE.json"
SWAPI_ENDPOINT = "https://swapi.py4e.com/api"
SWAPI_CATEGORIES = f"{SWAPI_ENDPOINT}/"
SWAPI_FILMS = f"{SWAPI_ENDPOINT}/films/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"

# Cache
cache = utl.create_cache(CACHE_FILEPATH)


def create_person(data):
    """Returns a new dictionary representation of a person from the passed in
    < data >. Calls < utl.get_swapi_resource() > to retrieve species data if
    cached data is not available.

    Type conversions:
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        species

    Parameters:
        data (dict): source data

    Returns:
        dict: new person dictionary
    """

    if data.get("species"):
        species_data = get_swapi_resource(data["species"][0])  # checks cache
        species = create_species(species_data)  # trim
    else:
        species = None

    return {
        "url": data.get("url"),
        "name": data.get("name"),
        "birth_year": data.get("birth_year"),
        "species": species,
    }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        "url": data.get("url"),
        "name": data.get("name"),
        "classification": data.get("classification"),
        "designation": data.get("designation"),
        "average_lifespan": utl.convert_to_int(data.get("average_lifespan")),
        "language": data.get("language"),
    }


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible. Delegates to the function
    < create_film > the task of creating film dictionaries.

    Type conversions:
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> top_speed_mglt (str to int)
        crew -> crew_size (str to int)
        armament -> armament (str to list)

    Key order:
        url
        name
        model
        starship_class
        hyperdrive_rating
        top_speed_mglt
        crew_size
        armament

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        "url": data.get("url"),
        "name": data.get("name"),
        "model": data.get("model"),
        "starship_class": data.get("starship_class"),
        "hyperdrive_rating": utl.convert_to_float(data.get("hyperdrive_rating")),
        "top_speed_mglt": utl.convert_to_float(data.get("MGLT")),
        "crew_size": utl.convert_to_int(data.get("crew")),
        "armament": utl.convert_to_list(data.get("armament"), ","),
    }


def get_swapi_resource(url, params=None, timeout=10, verify=True):
    """Retrieves a deep copy of a SWAPI resource from either the local < cache >
    dictionary or from a remote API if no local copy exists. Delegates to the function
    < utl.create_cache_key > the task of minting a key that is used to identify a cached
    resource. If the desired resource is not located in the cache, delegates to the
    function < get_resource > the task of retrieving the resource from SWAPI.
    A deep copy of the resource retrieved remotely is then added to the local < cache > by
    mapping it to a new < cache[key] >. The mutated cache is written to the file
    system before a deep copy of the resource is returned to the caller.

    WARN: Deep copying is required to guard against possible mutatation of the cached
    objects when dictionaries representing SWAPI entities (e.g., films, people, planets,
    species, starships, and vehicles) are modified by other processes.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds
        verify (bool): verify server's TSL certificate

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
    """

    key = utl.create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key])  # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout, verify)
        cache[key] = copy.deepcopy(resource)  # recursive copy of objects
        utl.write_json(CACHE_FILEPATH, cache)  # persist mutated cache
        return resource


def main():
    """Entry point for the script.

    Paramters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # DEMO: MODULE/CACHING

    # Get Luke
    # TODO Uncomment
    response = get_swapi_resource(f"{SWAPI_PEOPLE}", params={"search": "Luke Skywalker"})
    luke = create_person(response["results"][0])  # retrieves species from SWAPI

    # Get Leia
    # TODO Uncomment
    response = get_swapi_resource(f"{SWAPI_PEOPLE}", params={"search": "Leia Organa"})
    leia = create_person(response["results"][0])  # retrieves species from cache

    # Get Obi-wan Kenobi
    # TODO Uncomment
    response = get_swapi_resource(f"{SWAPI_PEOPLE}", params={"search": "Obi-wan Kenobi"})
    obi_wan = create_person(response["results"][0])  # retrieves species from cache

    # Write to file
    # TODO Uncomment
    utl.write_json("./stu-heroes.json", [luke, leia, obi_wan])

    # 1.0 MODULES

    # 1.3 GET MODULE NAME

    module_name = utl.__name__

    print(f"\n1.1: utl module name = {module_name}")

    # 1.1 IMPORTING MODULES

    # Get the SWAPI representation of the ice planet Hoth

    # Unaliased module
    # TODO Uncomment
    # import five_oh_six

    num = utl.convert_to_int("506")
    print(f"\n1.1.1 num = {num}")

    # Aliased module
    # TODO Uncomment
    # import five_oh_six as utl

    num = utl.convert_to_float("22.27")
    print(f"\n1.1.2 num = {num}")

    # Import module names directly using the < from > keyword
    # TODO Uncomment
    from five_oh_six import convert_to_list

    sentences = convert_to_list("Try not. Do or do not. There is no try.")
    print(f"\n1.1.3 Yoda to Luke = {sentences}")

    # Assign aliases to imported names
    # TODO Uncomment
    from five_oh_six import get_resource as get

    swapi_dagobah = get(SWAPI_PLANETS, {"search": "dagobah"})["results"][0]
    print(f"\n1.1.4: Planet Dagobah={swapi_dagobah}")

    # Import all names from a module
    from five_oh_six import (
        convert_to_float,
        convert_to_int,
        convert_to_list,
        create_cache,
        create_cache_key,
        get_resource,
        read_csv_to_dicts,
        read_json,
        write_json,
    )  # (...) permits import statement to be expressed across multiple lines

    # Wildcard import (AVOID)
    # from five_oh_six import *

    # 1.3 BUILT-IN DIR() FUNCTION

    utl_names = dir(utl) # Call function: return a list containing a module's definitions and statement

    print(f"\n1.3 utl module's names = {utl_names}")

    # 2.2 SORTING A LIST OF STRINGS

    people = [
        "Obi-Wan Kenobi",
        "Luke Skywalker",
        "Chewbacca",
        "Leia Organa",
        "Han Solo",
        "Rey",
        "Lando Calrissian",
        "Poe Dameron",
        "Yoda",
    ]

    # Alphanumeric sort
    people_sorted = sorted(people, key=lambda x:x[0])  # TODO Call function pass lambda

    print("\n2.0.1 Alphanumeric sort")
    pp.pprint(people_sorted)

    # Alphanumeric sort reversed
    people_sorted = sorted(people, key=lambda x: x[0], reverse=True)  # TODO Call function pass lambda

    print("\n2.0.2 Alphanumeric sort reversed")
    pp.pprint(people_sorted)

    # Alphanumeric sort on last name
    people_sorted = sorted(people, key=lambda x: x.split()[-1])  # TODO Call function pass lambda

    print("\n2.0.3 Alphanumeric sort on last name")
    pp.pprint(people_sorted)

    # Alphanumeric in-place sort
    # TODO Uncomment, replace None
    people.sort(key=lambda x:x.split()[-1])

    print("\n2.0.3 Alphanumeric sort on last name")
    pp.pprint(people)

    # 2.2 SORTING A LIST OF DICTIONARIES

    people = [
        {"name": "Obi-Wan Kenobi", "force_sensitive": True},
        {"name": "Rey", "force_sensitive": True},
        {"name": "Luke Skywalker", "force_sensitive": True},
        {"name": "Leia Organa", "force_sensitive": True},
        {"name": "Han Solo", "force_sensitive": False},
        {"name": "Yoda", "force_sensitive": True},
        {"name": "Chewbacca", "force_sensitive": False},
        {"name": "Lando Calrissian", "force_sensitive": False},
        {"name": "Poe Dameron", "force_sensitive": False},
        {"name": "Finn", "force_sensitive": False},
    ]

    # Sort by name
    # TODO Uncomment, replace None
    people_sorted = sorted(people, key=lambda x: (
        x["force_sensitive"],
        x["name"]
    ))

    print("\n2.0.3 people_sorted by name")
    pp.pprint(people_sorted)

    # Sort by force_sensitive (False = 0; True = 1), name
    # TODO Uncomment, replace None
    people_sorted = sorted(people, key=lambda x: (
        x["force_sensitive"],
        x["name"]
    ))

    print("\n2.0.4 Alphanumeric sort by force sensitivity (False, True), name")
    pp.pprint(people_sorted)

    # Sort by force_sensitive, name
    # TODO Uncomment, replace None
    people_sorted = sorted(people, key=lambda x: (x["force_sensitive"], x["name"]), reverse=True)

    print("\n2.0.5 Reverse sort by force sensitivity, name")
    pp.pprint(people_sorted)

    # Bidirectional sort by force_sensitive (True (1) then False (0)), name
    # TODO Uncomment, replace None
    people_sorted = sorted(people, key=lambda x: (-x["force_sensitive"], x["name"]))

    print("\n2.0.6 Bidirectional sort by force sensitivity (True, False), name")
    pp.pprint(people_sorted)

    # 2.4 LAMBDAS AND CONDITIONAL LOGIC

    # Note: planet https://swapi.py4e.com/api/planets/28/ named "unknown" removed from the data set
    # TODO Uncomment
    planet_data = utl.read_json("./data-planets.json")

    # Sort by population
    # WARN triggers exception
    # TODO Uncomment (Fails)
    # planets = sorted(planet_data, key=lambda x: x["population"]) # Fails NoneType encountered

    # Ternary operator
    # TODO Uncomment, replace None
    planets = sorted(planet_data, key=lambda x: x["population"] if x["population"] else 0)

    # Write to file
    # TODO Uncomment
    pp.pprint(planets)
    utl.write_json("./stu_planets-v1p0.json", planets)

    # Sort population in reverse order: bidirectional alternatives
    # TODO Uncomment
    # planets = sorted(planet_data, key=None, reverse=True)
    planets = sorted(planet_data, key=lambda x: -x["population"] if x["population"] else 0)
    # planets = sorted(planet_data, key=lambda x: -x["population"] if x["population"] else False)

    # Write to file
    # TODO Uncomment
    utl.write_json("./stu_planets-v1p1.json", planets)

    # Sort by population (descending), then name (ascending)
    # TODO Uncomment, replace None
    # planets = sorted(planet_data, key=None)

    # Write to file
    # TODO Uncomment
    # utl.write_json("./stu_planets-v1p2.json", planets)

    # TODO Compare v1p2 against v1p1 to demonstrate impact of multiple conditions

    # 3.0 CHALLENGES

    film_data = utl.read_json("./data-films.json")

    # 3.1 CHALLENGE 01

    # Sort by episode (descending)

    films = None  # Call function

    # Write to file
    # TODO Uncomment
    # utl.write_json("./stu_films-v1p0.json", films)

    # 3.2 CHALLENGE 02

    # Sort by release_date year (ascending)
    # TODO Uncomment
    films = None  # Call function

    # Write to file
    # TODO Uncomment
    # utl.write_json("./stu_films-v1p1.json", films)

    # 3.3 CHALLENGE 03

    # Sort by director's last name (ascending), then by episode (ascending)
    films = None  # TODO Call function
    # Write to file
    # TODO Uncomment
    # utl.write_json("./stu_films-v1p2.json", films)

    # 3.4 CHALLENGE 04

    # Sort by director's last name (ascending), then by release date year (descending)
    # Bidirectional
    films = None  # TODO Call function

    # Write to file
    # TODO Call function
    # utl.write_json("./stu_films-v1p3.json", films)

    # 3.5 CHALLENGE 05

    # Sort by the number of producers (descending), episode (descending)
    films = None  # TODO Call function

    # Write to file
    # TODO Call function
    # utl.write_json("./stu_films-v1p4.json", films)

    # 3.6 CHALLENGE 06

    # In-place sort of films_data by year of release descending
    # TODO Uncomment, pass arguments
    # film_data.sort(????)

    # Write to file
    # TODO Uncomment
    # utl.write_json("./stu_films-v1p5.json", film_data)

    # 3.7 CHALLENGE 07

    # TODO Uncomment
    # assert utl.convert_to_float("500") == 500.0
    # assert utl.convert_to_float("500.9999") == 500.9999
    # assert utl.convert_to_float("500,000,000.9999") == 500000000.9999

    # TODO Uncomment
    # assert utl.convert_to_int("500") == 500
    # assert utl.convert_to_int("500,000,000") == 500000000

    # 3.8 CHALLENGE 08

    # assert utl.convert_to_int("500,000,000") == 500000000
    # assert utl.convert_to_int("500,000,000.9999") == 500000000

    # 3.9 CHALLENGE 09

    # TODO Uncomment
    # assert utl.convert_to_list("Use the Force") == ["Use", "the", "Force"]

    # assert utl.convert_to_list(
    #     "tundra|ice caves|mountain ranges",
    #     "|") == ["tundra", "ice caves", "mountain ranges"]

    # assert utl.convert_to_list(
    #     "tundra, ice caves, mountain ranges",
    #     ", ") == ["tundra", "ice caves", "mountain ranges"]

    # 3.10 CHALLENGE 10

    swapi_starships = utl.read_json("./data-episode_iv_starships.json")
    wookiee_starships = utl.read_csv_to_dicts("./data-wookieepedia_starships.csv")

    # Combine data (in-place update)

    # TODO Implement nested loop

    # Write to file
    # TODO Uncomment
    # utl.write_json("stu-starships_v1p0.json", swapi_starships)

    # 3.11 CHALLENGE 11

    starships = None  # TODO comprehension

    # Write to file
    # TODO Uncomment
    # utl.write_json("stu-starships_v1p1.json", starships)

    # 3.12 CHALLENGE 12
    # TODO Uncomment, pass arguments
    # starships.sort(????)

    # Write to file
    # TODO Uncomment
    # utl.write_json("stu-starships_v1p2.json", starships)

    # 3.13 CHALLENGE 13

    # TODO Uncomment, pass arguments
    # hyperdrive_ratings = sorted(????)

    # Write to file
    # TODO Uncomment
    # utl.write_json("stu-starships_v1p3.json", hyperdrive_ratings)


if __name__ == "__main__":
    main()
