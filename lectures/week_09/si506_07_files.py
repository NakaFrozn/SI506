# SI 506: Files

import csv
from pathlib import Path


def clean_data(publication):
    """Mutates the passed in < publication > list by converting numbers masquerading as
    strings to an integer (int).

    Checks each string element in the < publication > list. Delegates to the function
    < convert_to_int > the task of attempting to convert the target string to an integer.
    Strings that cannot be converted are returned unchanged.

    Parameters:
      publication (list): represents a publication

    Returns:
        list: mutated publication list
    """

    pass  # TODO Implement


def convert_to_int(value):
    """Attempts to convert a string, number or boolean value to an int. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        int: if value successfully converted else returns value unchanged
    """

    try:
        return int(value)
    except ValueError:
        return value


def convert_to_float(value):
    """Attempts to convert a string, number or boolean value to a float. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        float: if value successfully converted else returns value unchanged
    """

    pass  # TODO Implement


def get_attribute(publication, headers, column_name):
    """Returns a < publication > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): provides header value used to look up the index value
                           of the target element

    Returns:
        str: element sourced from passed in publication list
    """

    pass  # TODO Implement


def get_citation_count_by_year(publications, headers, year):
    """Returns the annual citation count across all < publications > per
    the provided < year >. Delegates the task of accessing each publication's
    yearly citation count to the function < get_attribute >.

    Parameters:
        publications (list): nested list of publications
        headers (list): column names sourced from the CSV
        year (str): column name (e.g., '1995')

    Returns:
        int: citation count across all publications for a given year
    """

    pass  # TODO Implement


def has_umsi_faculty_author(umsi_faculty, coauthors, ignore="Resnick, Paul"):
    """Identifies whether or not a publication's < coauthors > includes at least
    one member of the UMSI faculty other than the faculty member flagged to
    < ignore >. If a match is obtained the function returns True; other False
    is returned.

    Comparing the names of faculty members and publication coauthors requires
    adoption of the following string format:

    `<last name>, <first name>`

    Parameters:
        umsi_faculty (list): nested list of UMSI faculty members
        coauthors (list): list of a publication's coauthors
        ignore (str): name of UMSI faculty member to ignore. Default = "Resnick, Paul"

    Returns:
        bool: True if a match is obtained; False otherwise
    """

    for member in umsi_faculty:
        name = ", ".join(member)

        # TODO Implement if statement

    return False


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


def read_file(filepath, encoding="utf-8", strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file.
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        if strip:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip())  # strip leading/trailing whitespace including '\n'
            return data
        else:
            return file_obj.readlines()  # list


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def write_file(filepath, data, encoding="utf-8", newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence of strings comprising the content to be written to the
                             target file
        encoding (str): name of encoding used to encode the file.
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n")  # add newline
        else:
            file_obj.writelines(data)  # write sequence to file


def main():
    """Program entry point. Orchestrates execution flow.

    Parameters:
        None

    Returns:
        None
    """

    # 2.0 FILE SYSTEM PATHS

    # 2.4.1 CURRENT WORKING DIRECTORY (CWD)
    cwd = Path.cwd() # TODO method call
    print(f"\n2.4.1.1 pathlib.path cwd = {cwd}")

    # 2.4.2 PARENT DIR PATH
    parent_path = Path(__file__).resolve().parent  # TODO instantiate Path() instance
    print(f"\n2.4.2.1 Path(__file__).resolve().parent = {parent_path}")
    # OR
    parent_path = Path().absolute()
    print(f"\n2.4.2.2 Path.absolute() = {parent_path}")
    #OR
    parent_path = Path().resolve()
    print(f"\n2.4.2.3 Path.resolve() = {parent_path}")

    # 2.4.3 THIS FILE ABSOLUTE (ABS) PATH
    abs_path = None  # TODO instantiate Path() instance
    # print(f"\n2.4.3.1 Path(__file__).absolute() = {abs_path}")
    # OR
    abs_path = None  # TODO instantiate Path() instance
    # print(f"\n2.4.3.2 Path(__file__).resolve() = {abs_path}")
    # OR
    # TODO UNCOMMENT
    # abs_path = Path("si506_week_07.py").resolve()
    # print(f"\n2.4.3.3 Path('si506_week_07.py').resolve() = {abs_path}")

    # 2.4.4 JOIN PATHS
    parent_path = Path(__file__).resolve().parent  # parent directory

    faculty_path = None  # TODO instantiate Path() instance
    # print(f"\n2.4.4.1 Path.joinpath() data-umsi-faculty.csv path = {faculty_path}")

    resnick_path = parent_path.joinpath("data-resnick-citations.csv")
    # print(f"\n2.4.4.2 Path.joinpath() data-resnick-citations.csv path = {resnick_path}")
    # print(f"\n2.4.4.3 resnick_path type = {type(resnick_path)}")

    # 2.4.5 PATH SEGMENTS
    # print(
    #     "\n2.4.5.1 Path parts",
    #     f"\nname = {resnick_path.name}",
    #     f"\nstem = {resnick_path.stem}",
    #     f"\nsuffix = {resnick_path.suffix}",
    #     f"\nparent dir = {resnick_path.parent}",
    #     f"\nparent.parent dir = {resnick_path.parent.parent}",
    # )

    # 3.0 FILES

    # Relative path
    filepath = "./data-umsi-faculty.txt"  # relative path
    # filepath = 'data-umsi-faculty.txt' # alternative
    filepath = Path("data-umsi-faculty.txt")  # relative
    # print(f"\n3.0.1 Relative filepath (type={type(filepath)}) = {filepath}")

    # Absolute path (safe)
    filepath = Path("data-umsi-faculty.txt").resolve()
    filepath = Path().cwd().joinpath("data-umsi-faculty.txt") # alternative
    print(f"\n3.0.2 ABS Path() filepath (type={type(filepath)}) = {filepath}")

    # 3.1.1 WITH STATEMENT AND OPEN()

    # TODO Implement with open() statement
    with open(filepath,'r') as file_obj:
        data = file_obj.read()
    print(f"\n3.1.1 with open() file_obj.read()\n{data}")

    # 3.1.2 YE OLDE WAY: AVOID

    # TODO Uncomment
    # file_obj = open(filepath)  # open
    # data = file_obj.read()  # returns a single string
    # file_obj.close()  # close (REQUIRED)

    # print(f"\n3.1.2 file_obj.close()\n{data}")

    # 3.2 FILE OPENING MODES

    # TODO Uncomment
    # with open(filepath, "r") as file_obj:  # open in read mode
    #     data = file_obj.read()

    # print(f"\n3.2 file_obj.read() data (type = {type(data)})")

    # TODO Write out files with names converted to upper case
    # with open("./stu-umsi-faculty-v1.txt", "w") as file_obj:  # open in write mode
    #     file_obj.write(data.upper())  # writes string to file

    # 3.3 READ METHODS (READLINE(), READLINES())

    # 3.3.1 READLINE()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readline()
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient

    # print(f"\n3.3.1 file_obj.readline()\n{data}")

    # 3.3.2 READLINES()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns list; elements include trailing '\n'

    # print(f"\n3.3.2.1 file_obj.readlines() (type={type(data)}\n{data[-8:]}")
    # print(f"\n3.3.2.2 file_obj.readlines(), .join()\n{''.join(data)}")  # print string (pretty)

    # 3.3.3 GOTCHA: READ(), READLINES() LIMITED TO ONE CALL ONLY

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.read()
        data_lines = file_obj.readlines()  # WARN: does not execute

    # print(f"\n3.3.3 data_lines list is empty = {data_lines}\n")

    # 3.5 WRITE METHODS (WRITE(), WRITELINES())

    # 3.5.1 WRITE STR TO FILE WITH WRITE()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.read()  # returns a single multiline string

    # TODO Write out files with names converted to upper case
    # with open("./stu-umsi-faculty-v2.txt", "w") as file_obj:  # open in write mode
    #     file_obj.write(data.lower())

    # 3.5.2 WRITE SEQUENCE TO FILE WITH WRITELINES()

    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a list

    # Reverse names: last, first -> first, last
    for i in range(len(data)):
        name = data[i].strip().split(", ")  # strip \n
        data[i] = f"{name[1]} {name[0]}\n"  # restore \n

    # TODO Write to file
    # with open("./stu-umsi-faculty-v3.txt", "w") as file_obj:  # open in write mode
    #     file_obj.writelines(data)

    # ALTERNATIVE (reverse name order without mutating original data)
    with open(filepath, "r") as file_obj:  # open in read mode
        data = file_obj.readlines()  # returns a single multiline string

    with open("./stu-umsi-faculty-v4.txt", "w") as file_obj:  # open in write mode
        for row in data:
            name = row.strip().split(", ")
            # file_obj.write(f"{name[1]} {name[0]}") # WARN: lose trailing `n`
            file_obj.write(f"{name[1]} {name[0]}\n")  # restore `\n`

    # 3.7 CHALLENGE 01

    # Get data
    data = None  # Call function

    # Access surnames first before calling write_file()
    surnames = []

    # TODO Implement loop

    # TODO Write surnames to file in reverse order
    # write_file("./stu-umsi-faculty-v5.txt", None) # replace None

    # TODO Uncomment
    # data_v5 = read_file("./stu-umsi-faculty-v5.txt")
    # assert data_v5[::-1] == surnames  # Reverse to match
    # assert data_v5 == surnames  # Triggers AssertionError

    # 4.0 CSV FILES

    # 4.4 CHALLENGE 02

    # Read CSV file and retrieve data
    filepath = Path("data-resnick-citations.csv").resolve()  # absolute
    publications = None  # TODO Call function

    # print(f"\n4.4.1: Total publications (rows) = {len(publications)}")

    # TODO Uncomment
    # headers = publications[0]  # header row

    # print(f"\n4.4.2: headers (n={len(headers)}) = {headers}")

    # TODO Uncomment. Filter title on "recommender"; accumulate results
    # recommender_publications = []
    # for publication in publications[1:]:
    #     pass  # TODO Add if statement

    # Write CSV file
    filepath = "./stu-resnick-recommender_pubs.csv"

    # TODO call function write_csv()

    # 5.0 TRY/EXCEPT

    # 5.1 CHALLENGE 03

    # print(f"\n5.1.0 All strings = {publications[-7]}")  # Recommender systems article

    # TODO Uncomment
    # for publication in publications[1:]:
    #     pass  # TODO Call function and assign return value

    # print(f"\n5.1.1 Integers converted = {publications[-7]}")  # Recommender systems article

    # 6.0 ADDITIONAL CHALLENGES

    # 6.1 CHALLENGE 04

    # TODO Uncomment
    # idx = headers.index("Average per Year")  # look up once
    # for publication in publications[1:]:
    #     pass  # TODO Implement loop block (2 lines of code)

    # print(f"\n6.1 Float converted = {publications[-7]}")  # Recommender systems article

    # 6.2 CHALLENGE 05

    # TODO Uncomment
    # umsi_faculty = read_csv(faculty_path)  # includes header row
    umsi_coauthored_publications = []

    # TODO Uncomment loop
    # for publication in publications[1:]:
    #     authors = None  # Call function, return authors, split string (delimiter = "; ")
    #     if None:
    #         umsi_coauthored_publications.append(publication)

    # Write to file
    filepath = "./stu-resnick-citations-umsi_coauthored.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-umsi_coauthors.csv")

    # TODO Uncomment
    # write_csv(filepath, umsi_coauthored_publications, headers)

    # 6.3 CHALLENGE 06

    max_citations = None  # TODO Replace start value
    max_count = None  # TODO Replace start value

    # TODO Implement loop

    # Write to file
    filepath = "./stu-resnick-citations-max_citations.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-max_citations.csv")

    # TODO Call write_csv()

    # 6.4 CHALLENGE 07 (BONUS)

    # idx = headers.index("1995") # TODO Uncomment
    years = None  # TODO Assign slice
    annual_counts = []

    # TODO Implement loop

    # Write to file
    filepath = "./stu-resnick-citations-annual_counts.csv"
    # filepath = Path(__file__).resolve().parent.joinpath("resnick-citations-annual_counts.csv")

    # TODO call write_csv()


if __name__ == "__main__":
    main()
