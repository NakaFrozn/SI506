# SI 506: Dictionaries

import csv
from datetime import datetime as dt
import pprint


def get_country_sites(sites, undp_code, categories):
    """Returns heritage sites filtered on the United Nations Development Programme
    (UNDP) country code and a tuple containing one or more heritage categories. For
    both the site's UNDP code and the category, a case-sensitive comparison of values
    is performed.

    While only one UNPD code is accepted, multiple categories may be passed by the
    caller, permitting one, some, or all a country's heritage sites to be returned.

    UNESCO Institute for Statistics categories: Cultural, Mixed, Natural

    Parameters:
        sites (list): list of heritage site dictionaries
        undp_code (str): three digit UNDP country code (e.g., 'USA')
        categories (tuple): one or more heritage categories

    Returns:
        list: list of site dictionaries that match the caller's filtering criteria

    """

    pass  # TODO Implement


def read_csv_to_dicts(filepath, encoding="utf-8", newline="", delimiter=","):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

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
            data.append(line)  # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict
        return data


def write_dicts_to_csv(filepath, data, fieldnames, encoding="utf-8", newline=""):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader()  # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # 1.0 DICTIONARY

    # A list
    site = [
        527,
        "Cultural",
        "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra",
        "Designed to rival Hagia Sophia in Constantinople . . . .",
        1990,
        0,
        30.51686,
        50.45258,
        28.52,
        "Europe and North America",
        "Ukraine",
        "UKR",
    ]

    # print("\n1.0 UNESCO heritage site (list)")
    # pp.pprint(site)

    # A dictionary
    site = {
        "id_no": 527,
        "category": "Cultural",
        "name_en": (
            "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra"
        ),
        "short_description_en": "Designed to rival Hagia Sophia in Constantinople . . . .",
        "date_inscribed": 1990,
        "endangered": 0,
        "longitude": 30.51686,
        "latitude": 50.45258,
        "area_hectares": 28.52,
        "region_en": "Europe and North America",
        "states_name_en": "Ukraine",
        "undp_code": "UKR",
    }

    # print("\n1.0 UNESCO heritage site (dict)")
    # pp.pprint(site)

    # Type
    site_type = type(site)  # <class 'dict'>

    # print(f"\n1.0 site obj type = {site_type}")

    # 2.0 CREATING A DICTIONARY

    # 2.1 EMPTY DICTIONARY

    site = {}
    site["id_no"] = 1330
    site["category"] = "Cultural"
    site["name_en"] = "Residence of Bukovinian and Dalmatian Metropolitans"
    site["short_description_en"] = (
        "[R]epresents a masterful synergy of architectural styles built by Czech architect Josef"
        " Hlavka from 1864 to 1882. . . ."
    )
    site["date_inscribed"] = 2011
    site["endangered"] = 0
    site["geo_coordinates"] = {}  # nested dict
    site["geo_coordinates"]["longitude"] = 25.9247222222
    site["geo_coordinates"]["latitude"] = 48.2966666667
    site["area_hectares"] = 8.0
    site["region_en"] = "Europe and North America"
    site["states_name_en"] = "Ukraine"
    site["undp_code"] = "UKR"

    # print("\n2.1 Key/value pair assignment\n")
    # pp.pprint(site)

    # 2.2 DICTIONARY LITERAL

    site = {
        "id_no": 865,
        "category": "Cultural",
        "name_en": "L'viv – the Ensemble of the Historic Centre",
        "short_description_en": (
            "The city of L'viv, founded in the late Middle Ages, was a flourishing administrative,"
            " religious and commercial centre for several centuries. The medieval urban topography"
            " has been preserved virtually intact . . . ."
        ),
        "date_inscribed": 1998,
        "endangered": 0,
        "geo_coordinates": {"longitude": 24.03198, "latitude": 49.84163},
        "area_hectares": 120.0,
        "region_en": "Europe and North America",
        "states_name_en": "Ukraine",
        "undp_code": "UKR",
    }

    # print("\n2.2 Dict literal\n")
    # pp.pprint(site)

    # 2.3 BUILT-IN DICT() FUNCTION

    # Pass in keyword arguments (note use of nested dict())
    site = dict(
        id_no=1411,
        category="Cultural",
        name_en="Ancient City of Tauric Chersonese and its Chora",
        short_description_en=(
            "The site features the remains of a city founded by Dorian Greeks in the 5th century BC"
            " on the northern shores of the Black Sea. . . ."
        ),
        date_inscribed=2013,
        endangered=0,
        geo_coordinates=dict(longitude=33.4913888889, latitude=44.6108333333),
        area_hectares=259.3752,
        region_en="Europe and North America",
        states_name_en="Ukraine",
        undp_code="UKR",
    )

    # print("\n2.3.1 Built-in dict() keyword args\n")
    # pp.pprint(site)

    # Pass in list of tuples (note used of nested dict())
    site = dict(
        [
            ("id_no", 1411),
            ("category", "Cultural"),
            ("name_en", "Ancient City of Tauric Chersonese and its Chora"),
            (
                "short_description_en",
                (
                    "The site features the remains of a city founded by Dorian Greeks in the 5th"
                    " century BC on the northern shores of the Black Sea. . . ."
                ),
            ),
            ("date_inscribed", 2013),
            ("endangered", 0),
            ("geo_coordinates", dict([("longitude", 33.4913888889), ("latitude", 44.6108333333)])),
            ("area_hectares", 259.3752),
            ("region_en", "Europe and North America"),
            ("states_name_en", "Ukraine"),
            ("undp_code", "UKR"),
        ]
    )

    # print("\n2.3.2 Built-in dict() list of tuples\n")
    # pp.pprint(site)

    # 3.0 WORKING WITH DICTIONARIES

    # 3.1 ACCESSING A VALUE

    site = {
        "id_no": 527,
        "category": "Cultural",
        "name_en": (
            "Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra"
        ),
        "short_description_en": "Designed to rival Hagia Sophia in Constantinople . . . .",
        "date_inscribed": 1990,
        "endangered": 0,
        "geo_coordinates": {"longitude": 24.03198, "latitude": 49.84163},
        "area_hectares": 28.52,
        "region_en": "Europe and North America",
        "states_name_en": "Ukraine",
        "undp_code": "UKR",
    }

    # Accessing a value
    site_name = None  # TODO Assign value

    # TODO Uncomment (KeyError)
    # site_name = site['name'] # raises KeyError: 'name'

    # print(f"\n3.1 Site name = {site_name}")

    ## 3.2 ACCESSING A NESTED VALUE

    # Accessing a nested dictionary value
    site_latitude = None  # TODO Assign value

    # print(f"\n3.2 Site latitude = {site_latitude}")

    # 3.3 ADD KEY-VALUE PAIR

    # TODO Add key-value pair

    # print("\n3.3.1 New key-value pair\n")
    # pp.pprint(site)

    # Add nested key-value pairs

    # TODO Add nested key-value paire

    # print("\n3.3.2 Street addresses\n")
    # pp.pprint(site)

    # https://en.wikipedia.org/wiki/Saint_Sophia_Cathedral,_Kyiv
    # cathedral_dimensions = {
    #     'length_m': 29.5,
    #     'width_m': 29.3,
    #     'dome_height_outer_m': 28.6
    # }

    # 3.4 MODIFY AN EXISTING VALUE

    # TODO Modify existing value

    # print("\n3.4 Modified key-value pair\n")
    # pp.pprint(site)

    # 3.5 DELETE KEY-VALUE PAIR

    # Delete key-value pair

    # TODO Delete existing value

    # print("\n3.5 Remove UNDP code\n")
    # pp.pprint(site)

    # 4.0 DICTIONARY METHODS

    # 4.1 DICT.GET()

    site_type = None  # TODO Get value

    # TODO Uncomment
    # site_type = site['type'] # triggers KeyError
    # site_type = site.get('type') # returns None
    # site_type = site.get('type', 'Undefined') # returns default value

    # print(f"\n4.1 Heritage site category = {site_type}")

    # 4.2 DICT.KEYS()

    # https://data.un.org/en/iso/ua.html

    country = {
        "name": "Ukraine",
        "region": "Eastern Europe",
        "population": "43467000",
        "urban_population_pct": "69.5",
        "surface_area_km2": "603500",
        "capital_city": "Kyiv",
        "un_membership_date": "1945-10-24",
    }

    # print(f"\n4.2.1 dict_keys object = {type(country.keys())}")  # dict_keys object

    # Loop over dict_keys object
    # print(f"\n4.2.2 Country keys")
    for key in country.keys():
        pass
        # print(key)

    # Convert dict_keys to a list
    country_keys = list(country.keys())

    # print(f"\n4.2.3 Country keys list\n{country_keys}")

    # Loop over list of keys; print associated values
    # print("\n4.2.4 Country values")
    for key in country_keys:
        pass
        # print(country[key])

    # 4.3 DICT.VALUES()

    # print(f"\n4.3.1 dict_values object = {type(country.values())}")  # dict_values object

    # Loop over dict_values object
    # print("\n4.3.1 Country values")
    for value in country.values():
        pass
        # print(value)

    # Convert to a list
    country_values = list(country.values())  # convert to a list

    # print(f"\n4.3.2 Country values list\n{country_values}")

    # Print value types
    # print("\n4.3.3 Country value types")
    for value in country.values():
        pass
        # print(type(value))

    # Unpacking

    # TODO Unpack values

    # print(f"\n4.3.4 Site Geo coordinates = {site_longitude}, {site_latitude}")

    # 4.4 DICT.ITEMS()

    # print(f"\n4.4 dict_items object = {type(country.items())}")

    # Looping over a dictionary's items
    for key, val in country.items():
        pass
        # print(f"key: {key}, val: {val}")

    # 4.5 CHALLENGE 01

    # Convert value types

    # TODO Loop over dictionary items

    # print("\n4.5 Country values converted\n")
    # pp.pprint(country)

    # 5.3 CHALLENGE 02

    # Get UNESCO World heritage sites
    sites = None  # TODO Call function

    # print(f"\n5.3 Sites list length = {len(sites)}")

    # Get Ukranian sites by undp_code 'ukr'
    ukrainian_sites = []

    # TODO Implement loop

    # Get fieldnames (retrieve keys from selected site)
    fieldnames = None  # TODO Assign fieldnames

    # Write to file
    # TODO Uncomment and assign arguments
    # write_dicts_to_csv(None, None, None)

    # 5.4 CHALLENGE 03

    usa_sites = None  # TODO Call function

    # Write to file
    # TODO Uncomment and assign arguments
    # write_dicts_to_csv(None, None, None)

    ind_sites = None  # TODO Call function

    # Write to file
    # TODO Uncomment and assign arguments
    # write_dicts_to_csv(None, None, None)

    # 6.1 ACCUMULATING VALUES FROM A DICTIONARY
    sites = read_csv_to_dicts("./data-whc-sites.csv")

    # print(f"\n6.1 Sites list length = {len(sites)}")

    china_sites = []
    year = dt.today().year  # Return current year
    # year = dt.now().year # Alternative
    for site in sites:
        date_inscribed = int(site["date_inscribed"])  # convert
        if site["states_name_en"].lower() == "china" and date_inscribed < year:
            year = date_inscribed
            china_sites.clear()  # reset
            china_sites.append(site)
        elif site["states_name_en"].lower() == "china" and date_inscribed == year:
            china_sites.append(site)

    # Write to file
    # TODO Uncomment
    # write_dicts_to_csv("./stu-china-earliest.csv", china_sites, china_sites[0].keys())

    # 6.2 STORING ACCUMULATED VALUES IN A DICTIONARY

    china_counts = {}
    for site in sites:
        if site["states_name_en"].lower() == "china":
            year = site["date_inscribed"]  # str
            if year not in china_counts.keys():
                china_counts[year] = 1  # seed value
            else:
                china_counts[year] += 1  # increment

    # print(f"\n6.2.1 China counts (unordered) = {china_counts}")

    # WARN: must pass a list of dictionaries

    # TODO Uncomment
    # write_dicts_to_csv("stu-china-counts.csv", [china_counts], china_counts.keys())

    # BONUS: reorder dictionary by keys (year)
    # TODO Uncomment
    # china_counts = dict(sorted(china_counts.items(), key=lambda x: x[0]))

    # BONUS: Alternative: dictionary comprehension (preferred)
    # china_counts = {k: v for k, v in sorted(china_counts.items(), key=lambda x: x[0])}

    # print(f"\n6.2.2 China counts sorted = {china_counts}")

    # WARN: must pass a list of dictionaries
    # TODO Uncomment
    # write_dicts_to_csv("./stu-china-counts_sorted.csv", [china_counts], china_counts.keys())

    # 6.3 CHALLENGE 04

    region_counts = {}

    # TODO Implement loop

    # print("\n6.3.1 Region counts\n")
    # pp.pprint(region_counts)

    # BONUS: sort by value
    # TODO Uncomment
    # region_counts = {k: v for k, v in sorted(region_counts.items(), key=lambda x: x[1], reverse=True)}

    # print("\n6.3.2. Region counts (sorted)\n")
    # pp.pprint(region_counts)

    # 7.1 CHALLENGE 05

    endangered_sites = []

    # TODO Implement loop

    # Write to file
    # TODO Uncomment and assign arguments
    # write_dicts_to_csv(None, None, None)

    # 7.2 CHALLENGE 06

    endangered_counts = {}

    # TODO Implement loop

    # print(f"\n7.2.1 Endangered site counts by region\n")
    # pp.pprint(endangered_counts)

    # BONUS: sort counts descending order
    # TODO Uncomment
    # endangered_counts = dict(sorted(endangered_counts.items(), key=lambda x: x[1], reverse=True))

    # print(f"\n7.2.2 Endangered site counts by region (sorted)\n")
    # pp.pprint(endangered_counts)

    # 7.3 Challenge 07

    # Add four (4) Ukrainian sites to the Europe and North America count

    # TODO Key-value assignment (add 4)

    # print(f"\n7.3.1 Endangered site counts by region + Ukraine\n")
    # pp.pprint(endangered_counts)

    # Total count of endangered sites.
    count = None  # TODO call built-in function

    # print(f"\n7.3.2. Endangered site count = {count}")

    # TODO Implement loop

    # print(f"\n7.3.3 Endangered site by region (percent)\n")
    # pp.pprint(endangered_counts)


if __name__ == "__main__":
    main()
