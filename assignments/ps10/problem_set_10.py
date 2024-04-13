import json
import csv
import requests
import pprint

print("\nProblem Set 10")
print("\n20th Century Fox")
print("\nA LUCASFILM LIMITED Production")
print("\nA long time ago in a galaxy far, far away....")
print("\nSWAPI: The Star Wars API")

# SETUP CODE
ENDPOINT = "https://swapi.py4e.com/api"

dialogue = {
    "C-3PO": [
        "Did you hear that?",
        "They've shut down the main reactor.",
        "We'll be destroyed for sure. This is madness!",
        "We're doomed!",
        "There'll be no escape for the Princess this time.",
        "What's that?",
    ],
    "R2-D2": ["beep, beep, boop.", "boop, beep, beep.", "boop, beeeep!"],
    "Darth Vader": ["sound of evil mechanical breathing"],
}
# END SETUP


def board_starship(starship, people):
    """Loops over the passed in people list, which is a list of tuples each representing
    people/passengers on the starship. Each tuple contains a variable assigned to a decoded
    JSON representing a person (in the 0th index) and a boolean indicating their intruder
    status (True, if intruder; False, if just a passenger) (in the 1st index).

    Example:
    [(< person_variable > , < intruder_bool > ), (< person_variable > , < intruder_bool > )]

    Utilizes sequence unpacking to access the 'person' element and the 'intruder' status
    element from the passed in list of tuples.

    Utilizes an if-elif-else statement and compound conditionals to evaluate the truth value
    of the 'intruder' status and check the following conditions:

        (1) If the 'intruder' status element evaluates to True and 'intruder' is already a
            key in the starship dictionary, then it simply appends the 'person' to the
            'intruder' key-value pair.
        (2) If the 'intruder' status element evaluates to True and 'intruder' is not yet a key
            in the starship dictionary, then it assigns a list literal containing the 'person'
            to the new 'intruder' key.
        (3) Otherwise, it appends the 'person' to the 'passengers' key.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains
                         starship attributes.
        people (list): a list of tuples where, for each tuple, a variable assigned to
                       the decoded JSON representing a person is at the 0th index and a
                       bool value indicating whether they are an intruder is at the 1st index.

    Returns:
        dict: an updated dictionary of key-value pairs representing a starship.
    """

    pass


def capture_starship(attacker, prey):
    """Utilizes a conditional statement to check if the key 'primary_docking_bay'
    is not already present in the decoded JSON representing an attacking starship.                                                     .

    If the conditional statement evaluates to 'True', it assigns the new key
    'primary_docking_bay' with a dictionary literal as its value. The dictionary
    literal has a key of 'docked' and a list literal containing the < prey >
    as its value. Otherwise, it gets access to the value of the key 'primary_docking_bay'
    and appends the < prey > to the 'docked' key.

    Parameters:
        attacker (dict): a dictionary representation of the decoded JSON
        that contains attributes of an attacking starship.
        prey (dict): a dictionary representation of the decoded JSON
        that contains attributes of a starship that is being captured.

    Returns:
        dict: an updated dictionary representation of the decoded JSON
        representing the attacking starship.
    """

    pass


def create_person(person):
    """Returns a dictionary literal with the following keys:

    name, height, mass, birth_year, eye_color, homeworld, dialogue

    Leverages the < dict.get() > function to access the corresponding value
    for certain keys (indicated above) present in the passed in person dictionary,
    except for the 'dialogue' key. Assign an empty list to the 'dialogue' key instead
    of utilizing the < dict.get() > function.

    When assigning the "homeworld" value, leverage the < get_homeworld > function
    by passing to it both the return value from < dict.get() >.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a person.
    """

    pass


def create_starship(starship):
    """Returns a dictionary literal with the following keys:

       name, model, passengers, max_atmosphering_speed, length

    Leverages the < dict.get() > function to access the corresponding value
    for certain keys (indicated above) present in the passed in starship dictionary,
    except for the 'passengers' key. Assign an empty list to the 'passengers' key instead
    of utilizing the < dict.get() > function.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains
                         starship attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a starship.
    """

    pass


def get_homeworld(url):
    """Attempts to retrieve a SWAPI representation of a home planet using the provided
    < url >. The < url > is assumed to be a SWAPI planet URL
    (e.g., https://swapi.py4e.com/api/planets/5/). The < url > is passed to the
    function < get_swapi_resource() > as its < url > argument.

    The return value is a "thinned" dictionary literal with the following keys:

    name, diameter, climate, terrain, population


    Parameters:
        url (str): the URL pattern for a resource category

    Returns:
        dict: "thinned" dictionary literal representation of a planet
    """

    pass


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
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


def insert_dialogue(person, dialogue):
    """Loops over the < dialogue > dictionary key-value pairs accessing the dictionary's
    items leveraging the dictionary method `dict.items()`. Utilizes a conditional statement
    to check if the value corresponding to the 'name' key in the < person > dictionary
    matches a key in the < dialogue > dictionary.

    If the conditional statement evaluates to 'True', a list method that adds the
    elements of a list to the end of the current list is leveraged to update the
    'dialogue' key-value pair in the < person > dictionary.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.
        dialogue (dict): a dictionary whose key-value pairs each represent a person
                         and their dialogue.

    Returns:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.
    """

    pass


def read_csv_to_dicts(filepath, encoding="utf-8-sig", newline="", delimiter=","):
    """
    Accepts a file path for a .csv file to be read, creates a file object,
    and uses csv.DictReader() to return a list of dictionaries
    that represent the row values from the file.

    Parameters:
        filepath (str): path to csv file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
    """

    with open(filepath, "r", newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:  # take out for loop and have students finish
            data.append(line)
        return data


def write_json(filepath, data, encoding="utf-8", indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)


def main():
    """
    This function serves as the point of entry and controls the flow of this Python script.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter()

    # Problem 01
    print("\nProblem 01:")

    # TODO 1.1
    SWAPI_FILMS = None
    SWAPI_STARSHIPS = None
    SWAPI_PEOPLE = None

    # TODO 1.2
    swapi_new_hope = None

    # Problem 02
    print("\nProblem 02:")

    # TODO 2.1
    new_hope = None

    # TODO 2.2

    # Problem 03
    print("\nProblem 03:")

    # TODO 3.3
    params = None
    swapi_corvette = None
    corvette = None

    params = None
    swapi_stardestroyer = None
    stardestroyer = None

    # TODO 3.4

    # Problem 04
    print("\nProblem 04:")

    # TODO 4.3
    params = None
    swapi_r2d2 = None
    r2d2 = None

    params = None
    swapi_c3po = None
    c3p0 = None

    params = None
    swapi_leia = None
    leia = None

    # TODO 4.4
    # assert get_homeworld(swapi_r2d2["homeworld"], SWAPI_PEOPLE) == {
    #     "name": "Naboo",
    #     "diameter": "12120",
    #     "climate": "temperate",
    #     "terrain": "grassy hills, swamps, forests, mountains",
    #     "population": "4500000000",
    # }
    # assert get_homeworld(swapi_c3po["homeworld"], SWAPI_PEOPLE) == {
    #     "name": "Tatooine",
    #     "diameter": "10465",
    #     "climate": "arid",
    #     "terrain": "desert",
    #     "population": "200000",
    # }

    # Problem 05
    print("\nProblem 05:")

    # TODO 5.3
    people = None

    # TODO 5.4
    # assert corvette["passengers"][0]["name"] == "R2-D2"

    # Problem 06
    print("\nProblem 06:")

    # TODO 6.1

    # TODO 6.2

    # TODO 6.3

    # Problem 07
    print("\nProblem 07:")

    # TODO 7.2

    # Problem 08
    print("\nProblem 08:")

    # TODO 8.2

    # Problem 09
    print("\nProblem 09:")

    # TODO 9.1.1

    # TODO 9.1.2

    # TODO 9.1.3

    # TODO 9.1.4

    # Problem 10
    print("\nProblem 10:")

    # TODO 10.1

    # TODO 10.2
    # droids = [r2d2,c3po]

    # TODO 10.3

    # TODO 10.4


if __name__ == "__main__":
    main()
