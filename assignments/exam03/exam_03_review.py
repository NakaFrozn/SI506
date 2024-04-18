import csv
import json

from pathlib import Path


def planet_mass(planet, mass_idx):
    """Returns the mass of the provided < planet >. If the mass value is not a valid number,
    the function returns None.

    Parameters:
        planet (dict): a dictionary representing a planet
        mass_idx (str): the key for the mass value

    Returns:
        float: the mass of the planet or None if unknown
    """

    try:
        return float(planet[mass_idx])
    except:
        return None


def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, "r", encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


def read_csv_to_dicts(filepath, encoding="utf-8", newline="", delimiter=","):
    """Accepts a file path, creates a file object, and returns a list of dictionaries that
    represent the row values using the cvs.DictReader().

    WARN: This function must be implemented using a list comprehension in order to earn points.

    Parameters:
        filepath (str): path to file
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
        for line in reader:
            data.append(line)  # OrderedDict() | alternative: data.append(dict(line))
        return data


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
    """Entry point. Orchestrates the execution of the program.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    orbital = "International Space Station"

    words = orbital.split()
    print(f"\nCH01 words (len={len(words)}): {words}")

    acronym = ""
    for word in orbital.split():
        acronym += word[0]
    # TODO Implement loop

    print(f"\nCH01 acronym: {acronym}")

    assert acronym == "ISS"

    # CHALLENGE 02

    data = read_csv("data-nasa-planets.csv")
    print(f"\nCH02 planets (len={len(data)}): {data[:2]}")

    headers = data[0]
    print(f"\nCH02 headers (len={len(headers)}): {headers}")

    name_idx = headers.index("name")
    len_day_idx = headers.index("length_of_day_hours")

    planets = []
    # TODO Implement loop
    for planet in data[1:]:
        if 8.0<float(planet[len_day_idx])<32.0:
            planets.append(planet[name_idx])
    print(f"\nCH02 planets (len={len(planets)}): {planets}")

    # CHALLENGE 03
    planets = []
    planets = [
        planet[name_idx]
        for planet in data[1:]
        if 8.0<float(planet[len_day_idx])<32.0
    ]

    print(f"\nCH03 planets (len={len(planets)}): {planets}")

    # CHALLENGE 04

    # Global magnetic field but no ring system

    planets = []
    print(bool(data[2][-2]))
    # TODO Implement loop
    for planet in data[1:]:
        has_rings, has_mag_field = planet[-2:]
        if has_rings == "False" and has_mag_field == "True":
            planets.append(planet[name_idx])
    print(f"\nCH04 planets (len={len(planets)}): {planets}")

    # CHALLENGE 05
    planets = []
    # TODO Implement loop
    for i in range(1,len(data)):
        if not data[i][-1]:   # this is different from is not True
            planets.append(data[i][name_idx])
    print(f"\nCH05 planets (len={len(planets)}): {planets}")

    # CHALLENGE 06

    parent_path = Path(__file__).absolute().parent
    print(f"\nCH06 parent_path = {parent_path}")
    filepath = parent_path.joinpath("data-nasa-planets.csv")
    print(f"\nCH06 filepath = {filepath}")

    data = read_csv_to_dicts(filepath)
    # print(f"\nCH06 planets (len={len(data)}): {data[:2]}")

    # CHALLENGE 07

    planets = sorted(data, key=lambda x:(-planet_mass(x, "mass_1024kg")))
    print(f"\nCH06 planets (len={len(planets)}): {planets[0]['name']} to {planets[-1]['name']}")

    assert planets[0]["name"] == "Jupiter" and planets[-1]["name"] == "Pluto"

    # CHALLENGE 08

    data = read_json("data-nasa-planets.json")
    print(f"\nCH08 planets (len={len(data)}): {data[0]}")

    jupiter_num_moons = data[4]["number_of_moons"]
    print(f"\nCH09 jupiter_num_moons: {jupiter_num_moons}")

    neptune_orbit_period_days = data[-2]["orbit"]["orbital_period_days"]
    print(f"\nCH09 neptune: {neptune_orbit_period_days}")

    # CHALLENGE 09

    planets = [
        {
            "name":planet.get("name"),
            "moon_count": planet.get("number_of_moons")
        }
        for planet in planets
    ]

    write_json("stu-data-nasa-moon_counts.json", planets)

    # CHALLENGE 10

    planets = {}
    # TODO Implement nested loop
    for planet in data:
        name = planet['name']
        planets[name] = {}
        for key, value in planet.items():
            if key != "name":
                planets[name][key] = value
    write_json("stu-data-nasa-planet-dict-v1p0.json", planets)

    # CHALLENGE 11

    planets = None

    # write_json("stu-data-nasa-planet-dict-v1p1.json", planets)

    # CHALLENGE 12

    cold_planets = {}
    # TODO Implement loop

    # print(f"\nCH13 cold planets (len={len(cold_planets)}) = {cold_planets}")

    cold_planets = None

    # print(f"\nCH13 cold planets (len={len(cold_planets)}) = {cold_planets}")

    # Write to file
    # write_json("stu-data-nasa-cold_planets.json", cold_planets)


if __name__ == "__main__":
    main()
