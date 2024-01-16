# SI 506 Week 02

# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

# Block comment
# A single line comment
# Yet another single line comment
# And yet another single line comment

# x = 5
# y = 2
# sum = x + y

url = "https://uniteagainstbookbans.org/"  # ALA initiative


# 2.0 VALUES AND TYPES


# 3.1 VARIABLE ASSIGNMENT

organization = "American Library Association"

year_founded = 1876

strategic_directions = [
    "Advocacy",
    "Information Policy",
    "Professional & Leadership Development.",
    "Equity, Diversity & Inclusion",
]

tweet = """82% of voters across the political spectrum support young people's ability
to access books that help them learn and grow. Join the movement:
http://UniteAgainstBookBans.org. #UniteAgainstBookBans"""


# 3.2 VARIABLE NAMING RULES AND CONVENTIONS

# 3.2.1 Good

# TODO examples


# 3.2.2 Bad

# TODO examples


# 3.2.3 Ugly (illegal)

# TODO examples


# 3.3 CHALLENGE 01

# TODO Create list

# TODO Uncomment
# print(f"\n3.3 Top 5 most challenged books = {titles}")


# 4.0 BUILT-IN FUNCTIONS (print(), type(), len())


# 4.1 print(): print passed in object to the screen

# Passing a hard-coded string.
# TODO Uncomment
# print("\n4.1.1 Libraries rock!") # \n = newline escape character

# Passing a variable name which points to a string.
# TODO Uncomment
# print(f"\n4.1.2 organization = {organization}")  # formatted string literal


# 4.2 type(): determine object's data type

data_type = None  # TODO Call function

# TODO Uncomment
# print(f"\n4.2.1 year_founded type = {data_type}")  # returns <class 'int'>

data_type = None  # TODO Call function

# TODO Uncomment
# print(f"\n4.2.2 tweet type = {data_type}")  # returns <class 'str'>

data_type = None  # TODO Call function

# TODO Uncomment
# print(f"\n4.2.3 strategic_directions type = {data_type}")  # returns <class 'list'>


# 4.3 len(): check length of sequence (i.e., number of elements)

# TODO Uncomment
# len = 10 # Shadowing built-in function name (avoid)
# Generates TypeError: 'int' object is not callable when len() is called below.

# Count characters in string (including whitespace).
char_count = None  # TODO Call function

# TODO Uncomment
# print(f"\n4.3.1 tweet length = {char_count}")

# Count number of elements in list.
element_count = None  # TODO Call function

# TODO Uncomment
# print(f"\n4.3.2 strategic_directions length = {element_count}")


# 4.4 CHALLENGE 02

# TODO Return type and print

# TODO Return length and print


# 5.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# 5.2 Challenge 03

# Counts
lecturer_count = 1
gsi_count = 3
ia_count = 3
student_count = 111
seat_count = 162

# 5.2.1 Addition (+ operator)
team_count = None  # TODO Implement expression

# TODO Uncomment
# print(f"\n5.2.1 team_count = {team_count}")

# 5.2.2 Subtraction (- operator)
open_seats = None  # TODO Implment expression

# TODO Uncomment
# print(f"\n5.2.2 Available seats = {open_seats}")

# 5.2.3 Multiplication (* operator)
max_enrollment = None  # TODO Implment expression

# TODO Uncomment
# print(f"\n5.2.3 max_enrollment = {max_enrollment}")

# 5.2.4 Floor division (// operator)
students_per_gsi = None  # TODO Implment expression

# TODO Uncomment
# print(f"\n5.2.4 Student:GSI ratio = {students_per_gsi}")

# 5.2.5 Max enrolled percentage
max_enrolled_pct = None  # TODO Implement expression

# TODO Uncomment
# print(f"\n5.2.5 Max enrolled percent = {max_enrolled_pct:.2f}")


# 6.0 STATEMENTS AND EXPRESSIONS

office = "ALA Office for Intellectual Freedom"  # statement

challenges = 377 + 156 + 729 + 1269  # arithmetical expression

# TODO Uncomment
# print(f"\n6.0 challenges 2019-2022 = {challenges}\n")  # expression (function call)


# 6.1 CHALLENGE 04

banned_title = None  # TODO Assign value
banned_author = None  # TODO Assign value
banned_publisher = None  # TODO Assign value

# TODO Call print()


# 6.3 CHALLENGE 05

banned_book = None  # TODO Concatenate

# TODO Call print()


# 7.0 OBJECT METHODS

event = "banned books week (18-24 September 2022)"
event_upper = event.upper()

# TODO Uncomment
# print(f"\n7.0 upper case = {event_upper}")

# 7.1 str.upper()/str.lower()

title = "Beyond Magenta"
lower_case = None  # Call str method
upper_case = None  # Call str method

# TODO Uncomment
# print(f"\n7.1 lower_case = {lower_case}")
# print(f"\n7.1 upper_case = {upper_case}")

# 7.2 str.startswith()/str.endswith()

title = "Out of Darkness"
starts_with_O = None  # Call str method
ends_with_S = None  # Call str method

# TODO Uncomment
# print(f"\n7.2 starts_with_O = {starts_with_O}")
# print(f"\n7.2 ends_with_S = {ends_with_S}")

# 7.3 str.count()

source = (
    'The Learning Network, "What Students Are Saying About Banning Books From School Libraries"'
    " (New York Times, 18 Feb 2022)."
)
char_a_count = None  # Call str method
char_ban_count = None  # Call str method

# TODO Uncomment
# print(f"\n7.3 char_a_count = {char_a_count}")
# print(f"\n7.3 char_ban_count = {char_ban_count}")

# 7.4 str.replace()

ala_statement = (
    "The American Library Association condemns censorship and works to ensure free access to"
    " information."
)
ala_statement = None  # Call str method

# TODO Uncomment
# print(f"\n7.4 ala_statement = {ala_statement}")


# 7.5 CHALLENGE 06

title = "Angie Thomas, The Hate You Give (Balzer + Bray, 2017)"  # contains a typo

# TODO Uncomment
# print(f"\n7.5 title (id={id(title)} = {title}")  # includes object id

hate_u_give = None  # Call str method

# TODO Uncomment
# print(f"\n7.5 title (id={id(title)} = {title}")  # includes object id


# 7.6 CHALLENGE 07

stamped = (
    "Ibram X. Kendi with Jason Reynolds, Stamped: Racism, Antiracism, and You (Little, Brown Books"
    " for Young Readers, 2020)."
)
i_count = None  # Call str method

# TODO Uncomment
# print(f"\n7.6 stamped 'i' count = {i_count}")


# 8.0 FORMATTED STRING LITERALS

author = "Toni Morrison"

# TODO Uncomment
# print(f"\n8.0 author = {author}")


# 8.1 CHALLENGE 08

bluest_eye = "Toni Morrison, The Bluest Eye (Holt, Rinehart and Winston, 1970)."

# TODO Call print() and pass f-string as the argument
