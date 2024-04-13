# SI 506: Web API

import csv
import json
import pprint
import requests


def convert_to_int(value):
    """Attempts to convert a string, number or boolean < value > to an int. If a runtime
    ValueError exception is encountered, the function returns the < value > unchanged.

    WARN: This function does not convert a float value masquerading as a string to an
    integer (e.g., "506.5" -> 506). This is due to the presence of a non-numeric character
    (a period) in the string. That said, the function will happily convert a float to
    an integer (e.g., 506.5 -> 506)

    Parameters:
        value (str|bool|float): string, boolean, or float value to be converted

    Returns:
        int|any: returns int if value successfully converted; otherwise returns the value
                 unchanged
    """

    try:
        return int(value)
    except ValueError:
        return value


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
        species_data = get_swapi_resource(data["species"][0])
        species = create_species(species_data)
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
        "average_lifespan": convert_to_int(data.get("average_lifespan")),
        "language": data.get("language"),
    }


def drop_data(entity, keys):
    """Deletes < entity > dictionary key-values pairs if a key matches a key in the
    passed in < keys > tuple. Checks each key in < keys > before attempting to delete
    the associated < entity > key-value pair in order to avoid runtime KeyError
    exceptions.

    Parameters:
        entity (dict): dictionary with key-value pairs to drop (i.e., delete)
        keys (tuple): key-value pairs to remove from < entity >

    Returns:
        dict: dictionary with matching key-value pairs removed
    """

    pass  # TODO implement


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    content of one or more SWAPI entities to be found in ["results"] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


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
            data.append(line)  # OrderedDict
            # data.append(dict(line)) # convert OrderedDict to dict
        return data


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


def sort_by_length(entity):
    """Tries to return an < entity > dictionary's length value converted to
    an integer. If the < entity > length value cannot be converted to an integer
    the function returns zero (0.0) to the caller.

    Parameters:
        entity (dict): dictionary to parse

    Returns:
        float: returns a float if the original value can be cast to a string;
             otherwise, returns zero (0.0).
    """

    pass  # TODO Implement


def sort_by_population(entity):
    """Tries to return an < entity > dictionary's population value converted to
    an integer. If the < entity > population value cannot be converted to an integer
    the function returns zero (0) to the caller.

    Parameters:
        entity (dict): dictionary to parse

    Returns:
        int: returns an integer if the original value can be cast to a string;
             otherwise, returns zero (0).
    """

    try:
        return int(entity["population"])
    except:
        return 0


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
    """Program entry point. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # 1.0 TEST PIP INSTALL OF REQUESTS PACKAGE
    # Run swapi_request_solution.py

    # 3.0 SWAPI ENDPOINT (REMOTE SERVICE)
    # Only accepts GET requests (no PUT, POST, DELETE requests accepted)

    endpoint = "https://swapi.py4e.com/api"

    # 3.1 SWAPI: RETURN DICT OF AVAILABLE RESOURCES (n=6)
    # /api/
    response = requests.get(endpoint+"/") # TODO Call function
    resources = response.json() # TODO Call function # convert message content to dict

    # TODO Uncomment
    print(f"\n3.1 SWAPI Resources (n={len(resources)})")
    for key, val in resources.items():
        print(f"{key.capitalize()}: {val}")

    # Write to file
    # TODO Uncomment
    write_json("stu-swapi_resources.json", resources)

    # 3.2 SWAPI: REQUEST RESOURCES BY CATEGORY (PAGED RESPONSE n=10 records)
    # /api/:category/

    response = None  # TODO Call function
    content = None  # TODO Call function
    content_count = None  # TODO Access resource count
    people_returned = None  # TODO Access people (SWAPI only returns max 10 records per request)
    people = None  # TODO Retrieve people elements

    # print(f"\n3.2.1: content count = {content_count}; People returned = {people_returned}\n")

    # TODO Uncomment
    # print("\n3.2.2: People returned (names only)")
    # for person in people:
    #     print(person["name"])

    # Write to file
    # TODO Uncomment
    # write_json("stu-swapi_people_page_01.json", people)

    # 3.3 SWAPI: REQUEST SINGLE RESOURCE BY ID
    # /api/:category/:id/

    response = None  # TODO Get JSON representation of Luke Skywalker by Id
    person = None  # TODO decode to dict

    # print(f"\n3.3: Request person by id = {person}")

    # Write to file
    # TODO Implement
    # write_json("stu-swapi_luke_skywalker.json", person)

    # 3.4 SWAPI: SEARCH CATEGORY FOR RESOURCE(S)
    # /api/:category/?search=<search term>

    url = f"{endpoint}/starships/"
    params = None  # TODO create dict
    response = requests.get(url, params)

    content = None  # TODO Decode
    starships = None  # TODO Access starships

    # print(f"\n3.4: Search Starships ("wing") = {starships[0]}") # first element only

    # Write to file
    # TODO Uncomment
    # write_json("./stu-swapi_starships_wing.json", starships)

    # 3.6 CHALLENGE 01

    response = requests.get("https://swapi.py4e.com/api/people/",{"search":"chewbacca"} )
    content = response.json()

    print(f"\n3.6.1 Response content\n{content}") # envelope

    # Chewbacca the Wookiee
    chewie = content['results'][0]  # Get first element
    print(f"\n3.6.2 Chewbacca\n{chewie}")

    # Write to file
    # TODO Uncomment
    write_json("stu-chewie.json", chewie)

    # 4.1 SWAPI: REQUEST FUNCTION/METHOD CHAINING

    # Get the Empire Strikes Back (1980)
    url = f"{endpoint}/films/"
    params = {"search": "empire strikes back"}
    content = requests.get(url, params).json()  # TODO Call function, call method
    film = content['results'][0]  # Access film

    print(f"\n4.1.1: Film = {film['title']} ({film['release_date']})")

    # Write to file
    # TODO Implement
    write_json("./stu-swapi_film_empire.json", film)

    # Get Yoda
    url = f"{endpoint}/people/"
    params = {"search": "yoda"}
    yoda = requests.get(url, params).json()['results'][0]  # TODO Access Yoda (one line)

    print(f"\n4.1.2: Yoda = {yoda}")

    # Write to file
    # TODO Uncomment
    write_json("stu-stu-swapi_yoda.json", yoda)

    # 4.2 UTILITY FUNCTION

    # Search and retrieve the astromech droid R2-D2
    url = f"{endpoint}/people"
    params = {"search": "r2"}
    r2_d2 = get_swapi_resource(url, params)["results"][0]  # chain

    print(f"\n3.2 R2-D2 = {r2_d2}\n")

    # Write to file
    # TODO Uncomment
    write_json("stu-swapi_r2d_d2.json", r2_d2)

    # 4.3 CHALLENGE 02

    # Add homeworld
    # TODO Uncomment and implement
    chewie['homeworld'] = get_swapi_resource(url, {"search":"chewie"})['results'][0]["homeworld"] # Call function

    # Add species
    # TODO Uncomment and implement
    chewie['species'] = get_swapi_resource(url, {"search":"chewie"})['results'][0]["species"] # Call function

    print(f"\n4.3 Chewbacca enriched\n{chewie}")

    # Write to file
    # TODO Uncomment
    # write_json("stu-chewie_enriched.json", chewie)

    # 4.4 CREATE_*() FUNCTIONS

    # Get Leia Organa
    swapi_leia = None  # TODO Call function
    leia = None  # TODO Call function

    # Write to file
    # TODO Uncomment
    # write_json("./stu-leia.json", leia)

    # 4.5 ADDITIONAL RESPONSE ATTRIBUTES

    url = f"{endpoint}/people/"
    params = {"search": "chewbacca"}
    response = requests.get(url, params)

    # Status code
    # TODO Uncomment
    # print(f"\n4.5.1 Response status code = {response.status_code}")

    # Response headers
    # TODO Uncomment
    # print(f"\n4.5.2 Response headers = {response.headers}")

    # Encoding
    # TODO Uncomment
    # print(f"\n4.5.3 Response encoding = {response.encoding}")

    # Check for bad request
    # TODO Uncomment
    # if response.raise_for_status():
    #     print(f"\n4.5.4 Bad request")
    # else:
    #     print(f"\n4.5.4 Valid request")

    # Decode response
    # TODO Uncomment
    # name = response.json()["results"][0]["name"]
    # print(f"\n4.5.5 Resource name = {name}")

    # 5.0 SORTING

    planets = read_json("./data-swapi_planets.json")
    planet_names = [planet["name"] for planet in planets]

    # print(f"\n5.0 planet_names (len={len(planet_names)}) = {planet_names[:6]}")

    planet_names_sorted = None  # TODO slice (61 planets in total)

    # print(f"5.0.1 planet_names_sorted = {planet_names_sorted}")

    planet_names_sorted = None  # TODO slice

    # print(f"5.0.2 courses_sorted reversed = {planet_names_sorted}")

    # In-place sort
    # TODO Uncomment
    # planet_names.sort() # ascending

    # print(f"5.0.3 planet_names ascending = {planet_names[:6]}")

    # TODO Uncomment
    # planet_names.sort(reverse=True) # descending

    # print(f"5.0.4 planet_names descending = {planet_names[:6]}")

    # WARN: cannot sort non-compatible types
    mix = [1, 2, "One", "one", "ONE", 1.1, "1", "01", 506]
    # TODO Uncomment
    # mix_sorted = sorted(mix) # Triggers TypeError
    # mix.sort() # Triggers TypeError

    # WARN: Triggers TypeError: "<" not supported between instances of "dict" and "dict"
    # planets_sorted = sorted(planets)

    # Sort by population size (ascending order, smallest to largest)
    planets_sorted = None  # TODO Call sorted() pass key arg

    # Write to file
    # TODO Uncomment
    write_json("stu-planets_sorted.json", planets_sorted)

    # Sort by population size (descending order, largest to smallest)
    planets_sorted = None  # TODO Call sorted() pass key arg, reverse order

    # Write to file
    # TODO Uncomment
    # write_json("stu-planets_sorted_reversed.json", planets_sorted)

    # Sort in-place: list.sort() method

    # TODO planets in-place sort, reverse order

    # Write to file
    # TODO Uncomment
    # write_json("stu-planets_sorted_inplace.json", planets)

    # 5.1 CHALLENGE 03

    wookiee_starships = read_csv_to_dicts("data-wookieepedia_starships.csv")

    # TODO Sort list

    # print(f"\n5.1 function name = {sort_by_length.__name__}")

    # Write to file
    # TODO Uncomment
    # write_json("stu-wookiee_starships_sorted.json", wookiee_starships)

    # 6.0 CHALLENGES

    endpoint = "https://swapi.py4e.com/api"

    # 6.3 CHALLENGE 04

    swapi_x_wing = None  # Call function

    # print(f"\n6.3.1 T-65 X-wing\n{swapi_x_wing}")

    wookiee_x_wing = None
    for starship in wookiee_starships:
        pass  # TODO implement

    # TODO Combine dictionaries

    # print(f"\n6.3.2: T-65 X-wing enriched\n{swapi_x_wing}")

    # Write to file
    # TODO Uncomment
    # write_json("stu-x_wing_enriched.json", swapi_x_wing)

    # 6.4 CHALLENGE 05

    drop_keys = (
        "films",
        "created",
        "edited",
        "people",
        "residents",
        "species",
        "starships",
        "vehicles",
    )
    x_wing = None  # TODO Call function

    # print(f"\n6.4 cleaned T-65 X-wing\n{x_wing}")

    # Write to file
    # TODO Uncomment
    # write_json("stu-x_wing_cleaned.json", x_wing)

    # 6.5 CHALLENGE 06

    # TODO Implement loop

    # Write to file
    # TODO Uncomment
    # write_json("stu-x_wing_pilots.json", x_wing)

    # 6.6 CHALLENGE 07

    # Access Luke and then remove the pilots key-value pair
    luke = None  # TODO Access Luke
    x_wing = None  # TODO Call function

    # Get R2-D2 (Astromech droid)
    r2 = None  # TODO Call function
    r2 = None  # TODO Call function

    # Get R2-D2's home planet
    homeworld = None  # TODO Call function
    # TODO Uncomment and implement
    # r2[???] = None # TODO Call function

    # Add crew members
    # TODO Uncomment and implement
    # x_wing[???] = None # Add dictionary

    # Write to file
    # TODO
    # write_json("stu-x_wing_crew.json", x_wing)


if __name__ == "__main__":
    main()
