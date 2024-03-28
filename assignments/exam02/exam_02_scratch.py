
from os import write
from pathlib import Path
import csv


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


def convert_player_numbers(player):
    """Converts numbers masquerading as string to integers. Delegates to the
    < to_int > function the task of converting individual values.

    Parameters:
        player (list): list of player data

    Returns:
        list: player list with numbers converted to integers
    """

    for i in range(len(player)):
        player[i] = to_int(player[i])
    return player
        


def to_int(value):
    """Converts a string to an integer. If the conversion fails, the original
    value is returned unchanged.

    Parameters:
        value (str): the value to convert

    Returns:
        int | any: the converted value or original value
    """

    try:
        return int(value)
    except:
        return value


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


def main():
    """Application entry point. Orchestrates workflow."""

    # 1.0 WARN: Fix csv issue

    # 2.0 Create Path object
    parent_path = Path("__file__").resolve().parent
    filepath = parent_path.joinpath("./data-players.csv")
    print(f"\nFilepath = {filepath}")

    # 3.0 Read CSV file
    data = read_csv(filepath)
    print(f"\nData length = {len(data)}")

    # 4.0 Get headers and players
    headers = data[0]
    print(f"\nHeaders = {headers}")
    players = data[1:]
    print(f"\nplayers = {players[524]}")

    # 5.0 Retrieve index of "player" column from headers
    player_idx = headers[1]
    print(f"\nplayer_idx = {player_idx}")

    # 6.0 Get player name (element 524)
    # CSV = 525,Wang Shuang,FW|MF,CN,China PR,28,1995,1.8,2,3,1
    name = players[524][1]
    print(f"\nname = {name}")

    # 7.0 Implement function to_int()

    assert to_int("123") == 123
    assert to_int("abc") == "abc"

    # 8.0 Implement function convert_player_numbers()

    assert convert_player_numbers(["123", "abc", "456"]) == [123, "abc", 456]

    # 9.0 Convert all player lists

    # TODO: Implement Loop
    for player in players:
        player = convert_player_numbers(player)
    # Wang Shuang (element 524)
    print(f"\nplayer = {players[524]}")

    # 10.0 Unpack Wang Shuang shooting numbers

    # TODO: Unpack
    goals, shots, shots_on_target  = players[524][-3:]
    print(f"\ngoals = {goals}, shots = {shots}, shots_on_target = {shots_on_target}")

    # 11.0 Get all goal scorers (illustrate truth value testing)
    goals_idx = 8
    goal_scorers = []

    # TODO: Implement loop
    for player in players:
        if player[goals_idx] > 0:
            goal_scorers.append(player)
    print(f"\nGoal scorers = {len(goal_scorers)}")

    # 12.0 Compute shot conversion rate (round to 2 decimal places)
    shots_idx = 9

    # WARN: 443 Yomira Pinzón,DF,PA,Panama,26,1996,3,1,0,0 (shots = 0?)
    # Triggers exception
    for player in goal_scorers:
        try:
            shot_conv_rate = round(player[goals_idx] / player[shots_idx], 2)
        except:
            player.append(0.00)
        player.append(shot_conv_rate)

    # TODO: Fix loop

    # 13.0 Sync headers list

    # TODO: Append header
    headers.append("Shot Conversion Rate")
    # 14.0 Write data to new CSV file
    filepath = "./data-goal_scorers.csv"

    # TODO: write CSV
    write_csv(filepath,  goal_scorers, headers)
    # 15.0 Convert player to a dictionary (use headers)
    wang_shuang = {}
    for i in range(len(players[524])):
        wang_shuang[headers[i]] = players[524][i]
    # TODO: Implement loop

    print(f"\nWang Shuang = {wang_shuang}")


if __name__ == "__main__":
    main()
