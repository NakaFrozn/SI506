# SI 506: Accumulator dictionary

import csv
import pprint


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


def get_sites_by_key(sites, key):
    """Returns a dictionary containing site counts by region. The passed in < key > corresponds to
    a column name in the sites data and is used as a dictionary key. Counts are accumulated by
    iterating over < sites > and counting the occurrences of the key's value.

    If a key is not present in the < counts > dictionary it is added and assigned a value of 1.
    If the key has been previously added to the dictionary the associated value is incremented by 1.

    Parameters:
        sites (list): list of dictionaries
        key (str): column name

    Returns:
        dict: key-value pairs structed as < key: count >
    """

    counts = {}

    for site in sites:
        value = site.get(key)
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # TODO: Read file
    sites = read_csv_to_dicts("data-sites.csv")

    # TODO: Compute site counts by region
    region_counts = get_sites_by_key(sites, "region_en")

    #Uncomment and test
    assert region_counts == {
        "Asia and the Pacific": 273,
        "Europe and North America": 516,
        "Arab States": 88,
        "Africa": 92,
        "Latin America and the Caribbean": 143,
    }


    # UNCOMMENT: sort counts descending order
    region_counts_sorted = dict(sorted(region_counts.items(), key=lambda x: x[1], reverse=True))

    print("\nSite counts by region (sorted)\n")
    pp.pprint(region_counts_sorted)

    #Uncomment and test
    assert region_counts_sorted == {
        "Europe and North America": 516,
        "Asia and the Pacific": 273,
        "Latin America and the Caribbean": 143,
        "Africa": 92,
        "Arab States": 88,
    }


if __name__ == "__main__":
    main()
