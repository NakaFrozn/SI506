# SI 506 Week 03

from pprint import pprint  # import statement

# 1.0 SEQUENCES: STRINGS, LISTS, AND TUPLES

# 1.1 String basics

comedy_series = "Monty Python"

# The object's unique identifier in memory
comedy_series_id = id(comedy_series)  # TODO call function

print(f"\n1.1.1 comedy_series (id={comedy_series_id}) = {comedy_series}")

# Return the object's type
comedy_series_type = type(comedy_series)  # TODO call function

print(f"\n1.1.2 comedy_series type (id={comedy_series_id}) = {comedy_series_type}")

# Return the object's length
comedy_series_len = len(comedy_series)  # TODO call function

print(f"\n1.1.3 comedy_series length (id={comedy_series_id}) = {comedy_series_len}")

# UNCOMMENT: Immutability check
# comedy_series[0] = "m"
# TypeError: 'str' object does not support item assignment

# String concatenation
comedy_series = comedy_series + "'s Flying Circus"  # string concatenation (new object)

print(f"\n1.1.4 comedy_series (id={comedy_series_id}) = {comedy_series}")


# 1.2 LIST BASICS

pythons = ["Graham Chapman", "John Cleese", "Terry Jones", "Eric Idle", "Michael Palin"]

# The object's unique identifier in memory
pythons_id = id(pythons)

print(f"\n1.2.1 pythons (id={id(pythons)}) = {pythons}")

# Return the type
pythons_type = type(pythons)

print(f"\n1.2.2 pythons type (id={id(pythons)}) = {pythons_type}")

# Return the length
pythons_len = len(pythons)

print(f"\n1.2.3 pythons len (id={id(pythons)}) = {pythons_len}")

# In-place method call mutates the list.
pythons.append("Terry Gilliam")
# .insert & .extend also work.

# TODO call pythons in-place methods to add Terry Gilliam

print(f"\n1.2.4 pythons (id={id(pythons)}) = {pythons}")

# List concatenation
pythons = pythons + ['Neil Innes']  # TODO concatenate lists

print(f"\n1.2.5 pythons (id={id(pythons)}) = {pythons}") # new identity


# 1.3 Tuple basics

silly_walks = ("Monty Python", "Sketch", "The Ministry of Silly Walks", "15 September 1970")

# The object's unique identifier in memory
silly_walks_id = id(silly_walks)

print(f"\n1.3.1 silly_walks (id={id(silly_walks)}) = {silly_walks}")

# Return the type
silly_walks_type = type(silly_walks)

print(f"\n1.3.2 silly_walks type (id={id(silly_walks)}) = {silly_walks}")

# Return the length
silly_walks_len = len(silly_walks)

print(f"\n1.3.3 silly_walks len (id={id(silly_walks)}) = {silly_walks_len}")

# Single item tuple

python_theme_song = ('The Liberty Bell',)  # TODO Create single item tuple

print(f"\n1.3.4 Flying Circus theme song = {python_theme_song}")

python_theme_song = ('John Philip Sousa', 'Composer') + python_theme_song + (1893,)  # TODO Concatenate tuples

print(f"\n1.3.5 Flying Circus theme song composer = {python_theme_song}")

holy_grail = (
    "Monty Python and the Holy Grail",
    1975,
    [
        "Arthur, King of the Britons",
        "Sir Lancelot the Brave",
        "Sir Bedevere the Wise",
        "Sir Galahad the Pure",
    ],
)

# TODO Uncomment
# holy_grail[1] = "3 April 1975" # Illegal

# TODO Uncomment
holy_grail[2].append("Patsy") # Mutates tuple list item with a new element

print(f"\n1.3.6 Tuple mutable elements = {holy_grail}")


## 2.0 CREATE A LIST FROM A STRING

# 2.1 str.split()

sketch_comedy = "Monty Python's Flying Circus"
words = sketch_comedy.split()  # TODO Split string

print(f"\n2.1.1 Split title = {words}")

sketches = "Dead Parrot Sketch, The Spanish Inquisition, The Argument Clinic"
sketches = sketches.split(', ')  # TODO Split string

print(f"\n2.1.2 Split sketches = {sketches}")

# 2.2 str.splitlines()

excerpt = """Nobody expects the Spanish Inquisition.
Our chief weapon is surprise.
Surprise and fear. Fear and surprise.
Our two weapons are fear and surprise ...
and ruthless efficieny.
Our three weapons are fear and surprise and ruthless efficiency ...
and an almost fanatical devotion to the pope.
Uh! Four. No.
Amongst our weapons ....
Amongst our weaponry are such elements as fear, su -- I'll come in again.
"""

lines = excerpt.splitlines()  # TODO Split multiline string

print(f"\n2.2 Excerpt splitlines = {lines}")


## 2.3 CHALLENGE 01

arthur = (
    "The Lady of the Lake, "
    "her arm clad in the purest shimmering samite, "
    "held aloft Excalibur from the bosom of the water "
    "signifying by Divine Providence that "
    "I, Arthur, was to carry Excalibur. "
    "That is why I am your king."
)

dennis = (
    "Listen, strange women lying in ponds distributing swords "
    "is no basis for a system of government. "
    "Supreme executive power derives from a mandate from the masses, "
    "not from some farcical aquatic ceremony."
)

# TODO Implement
# I need to concatenate the two strings

excalibur = arthur + " " + dennis
print(f"\n2.3 Arthur and Dennis = {excalibur}")

excalibur = excalibur.split(". ")  # TODO Split string

# Assert equality
assert excalibur == [
     (
         "The Lady of the Lake, her arm clad in the purest shimmering samite, held aloft Excalibur"
         " from the bosom of the water signifying by Divine Providence that I, Arthur, was to carry"
         " Excalibur"
     ),
     "That is why I am your king",
     (
         "Listen, strange women lying in ponds distributing swords is no basis for a system of"
         " government"
     ),
     (
         "Supreme executive power derives from a mandate from the masses, not from some farcical"
         " aquatic ceremony."
     ),
]


# 3.0 INDEXING

# 3.1 Accessing a character by position

name = "Monty Python"
letter = name[0]  # TODO First letter (zero-based index)

print(f"\n3.1.1 Letter = {letter}")

letter = name[4]  # TODO Fifth letter

print(f"\n3.1.2 Letter = {letter}")

letter = name[-1]  # TODO Last letter

print(f"\n3.1.3 Letter = {letter}")


# 3.2 Index operator (list)

menu = [
    "Egg and bacon",
    "Egg, sausage and bacon",
    "Egg and Spam",
    "Egg, bacon and Spam",
    "Egg, bacon, sausage and Spam",
    "Spam, bacon, sausage and Spam",
    "Spam, egg, Spam, Spam, bacon and Spam",
    "Spam, Spam, Spam, egg and Spam",
    "Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam",
    (
        "Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy"
        " and a fried egg on top and Spam"
    ),
]

menu_item = menu[1]  # TODO Second element (zero-based index)

print(f"\n3.2.1 Menu item = {menu_item}")

menu_item = menu[-2]  # TODO Second to last element

print(f"\n3.2.2 Menu item = {menu_item}")


# 3.3 Mutating a list element using indexing

menu[3] = "Scrambled eggs, bacon and Spam"

print(f"\n3.3 Scrambled eggs added to menu = {menu}")

# Trigger an IndexError exception
# menu_item = menu[10] # IndexError: list index out of range#


# 3.4 CHALLENGE 02
import re
order = [i for i in menu if len(re.findall(r'Spam|spam',i))>1]  # TODO Index to access 2 helpings of spam
order = order[0]
print(f"\n3.5 Menu order = {order}")

# Assert equality
assert order == "Spam, bacon, sausage and Spam"


# 4.0 SLICING

cast = [
    "Terry Jones, Waitress",
    "Eric Idle, Mr Bun",
    "Graham Chapman, Mrs Bun",
    "John Cleese, The Hungarian",
    "Michael Palin, Historian",
    "Extra, Viking 01",
    "Extra, Viking 02",
    "Extra, Viking 03",
    "Extra, Viking 04",
    "Extra, Viking 05",
    "Extra, Viking 06",
    "Extra, Police Constable",
]

# 4.1 slice from index 0 to index n (stride = 1)

# Return Mr and Mrs Bun
cast_members = None  # TODO Slice

# print(f"\n4.1.1 The Buns = {cast_members}")

# Return Mr and Mrs Bun (negative slice)
named_cast_members = None  # TODO Slice

# print(f"\n4.1.2 The Buns (negative slice) = {named_cast_members}")

# Slice from index 0 to index n (stride = 1)
named_cast_members = None  # TODO Slice

# print(f"\n4.1.3 Named cast members = {named_cast_members}")

# Slice from index -n to end of list inclusive (stride = 1)
unnamed_cast_members = None  # TODO Slice WARN: not the same as cast[-7:-1]

# print(f"\n4.1.4 Extras = {unnamed_cast_members}")


# 4.2 CHALLENGE 03

cleese_palin =   # TODO Slice

# print(f"\n4.2 Cleese and Palin = {cleese_palin}")

# Assert equality
# assert cleese_palin == ["John Cleese, The Hungarian", "Michael Palin, Historian"]


# 4.3 CHALLENGE 04

vikings = None  # TODO Slice

# print(f"\n4.3 Vikings = {vikings}")

# assert vikings == [
#     "Extra, Viking 01",
#     "Extra, Viking 02",
#     "Extra, Viking 03",
#     "Extra, Viking 04",
#     "Extra, Viking 05",
#     "Extra, Viking 06",
# ]


# 4.4 SLICING STRIDE VALUES

cast = [
    "Terry Jones, Waitress",
    "Eric Idle, Mr Bun",
    "Graham Chapman, Mrs Bun",
    "John Cleese, The Hungarian",
    "Michael Palin, Historian",
    "Extra, Viking 01",
    "Extra, Viking 02",
    "Extra, Viking 03",
    "Extra, Viking 04",
    "Extra, Viking 05",
    "Extra, Viking 06",
    "Extra, Police Constable",
]

# Retrieve the late Terry Jones and Graham Chapman
cast_members = None  # TODO Slice

# print("\n4.4 Deceased cast members\n")
# pprint(cast_members)  # Pretty print

# Return cast members in reverse order
cast_members = None  # TODO Slice

# print("\n4.4 Cast members reverse order\n")
# pprint(cast_members)  # Pretty print

# Return every other cast member starting from the first element
cast_members = None  # TODO Slice

# print("\n4.4 Every other cast member\n")
# pprint(cast_members)  # Pretty print


# 4.5 CHALLENGE 05

# Return every other cast member starting from the last element (negative stride)
cast_members = None  # TODO Slice

# print("\n4.5 Every other cast member (negative stride)\n")
# pprint(cast_members)  # Pretty print

# assert cast_members == [
#     "Extra, Police Constable",
#     "Extra, Viking 05",
#     "Extra, Viking 03",
#     "Extra, Viking 01",
#     "John Cleese, The Hungarian",
#     "Eric Idle, Mr Bun",
# ]


# 4.6 CHALLENGE 06

# Return every other Viking starting with Viking 01.
cast_members = None  # TODO Slice

# print("\n4.6.1 Every other Viking\n")
# pprint(cast_members) # Pretty print

# BONUS. Return every other Viking starting with Viking 01 in reverse order.
cast_members = None  # TODO Slice Fails: empty list returned

# print("\n4.6.2 Every other Viking reverse order \n")
# pprint(cast_members) # Pretty print

# Workaround
cast_members = None  # TODO Slice chaining

# print("\n4.6.3 Every other Viking reverse order workaround\n")
# pprint(cast_members)  # Pretty print

# assert cast_members == ["Extra, Viking 06", "Extra, Viking 04", "Extra, Viking 02"]


# 5.0 OTHER SLICING OPERATIONS

# 5.1 Slice Assignment

cast[4] = "Michael Palin, The Historian"  # Adds the definite article "The"

mounties = [
    "Extra, Canadian Mountie 01",
    "Extra, Canadian Mountie 02",
    "Extra, Canadian Mountie 03",
    "Extra, Canadian Mountie 04",
    "Extra, Canadian Mountie 05",
    "Extra, Canadian Mountie 06",
]

# 5.1.1 Replace part of a list (length unchanged)

# TODO Uncomment
# cast[5:11] = None  # TODO Slice replace Vikings with Mounties

# print("\n5.1.1 Replace Vikings with Canadian Mounties\n")
# pprint(cast) # Pretty print

# 5.1.2 Replace part of a list (length changes)

# TODO Uncomment
# cast[5:11] = None  # TODO Slice replace Vikings with mounties 02-04 (negative slice)

# print("\n5.1.2 Replace Vikings with mounties 02-04\n")
# pprint(cast) # Pretty print


# 5.2 del statement and slicing

# Delete a slice with the del statement

# Delete the Mounties (retain the Police Constable)

# TODO add del statement

# print("\n5.2 Delete Mounties\n")
# pprint(cast)  # Pretty print


# 5.3 Built-in slice() function

# slice([start, ]end[, step]) object
s = slice(1, 4, 2)  # Returns Idle and Cleese
cast_members = cast[s]

# print("\n5.3 slice() example\n")
# pprint(cast_members)  # Pretty print


## 6.0 OBJECT METHODS AND METHOD CHAINING

menu_item = "Spam, egg, Spam, Spam, bacon and Spam"

# str.lower() -- no argument method
menu_item_lower = menu_item.lower()

# print(f"\n6.0.1 lower case = {menu_item_lower}")

# str.count(value, start=0, end=len(str) - 1) -- start and end are optional
spam_count = menu_item.count("Spam")

# print(f"\n6.0.2 Spam count = {spam_count}")

# str.split(sep=" ", maxsplit=-1) -- sep and maxsplit are optional
items = None  # TODO call method return list

# print("\n6.0.3\n")
# pprint(items) # Pretty print

# TODO Call method in-place and remove "egg"

# print("\n6.0.4\n")
# pprint(items) # Pretty print

# Do not do this: items variable no longer points to a list object
# TODO Uncomment
# items = items.remove("bacon and Spam") # None is returned

# print("\n6.0.5\n")
# pprint(items) # Pretty print

# Chained method calls
menu_item = "Egg, bacon, sausage and Spam"

# Good. Replace, convert to lower case, and split.
items = None  # TODO Chain method calls

# print("\n6.0.6 Menu reformatted\n")
# pprint(items)  # Pretty print

# Bad. The trailing list.append() returns None (oops!)
# TODO Uncomment
# items = menu_item.replace(" and", ",").lower().split(", ").append("pancakes")

# print("\n6.0.7 Bad chaining order\n")
# pprint(items)  # Pretty print

# Ugly. Premature split. Calling lower on a list object raises a runtime error
# AttributeError: 'list' object has no attribute 'lower'

# TODO UNCOMMENT (WARN: RAISES EXCEPTION)
# items = menu_item.replace(" and", ",").split(", ").lower()

# print("\n6.0.8\n")
# pprint(items) # Pretty print


# 6.1 SELECT STR METHODS

# 6.1.1 str.strip()
monty_python = " Monty Python's Flying Circus \n"  # note apostrophe

# print(f"\n6.1.1.1 Monty Python (unstripped) = {monty_python}")

monty_python = None  # TODO Strip (note reassignment)

# print(f"\n6.1.1.2 Monty Python (stripped) = {monty_python}")


# 6.1.2 str.find()
menu_item = "Spam, Spam, Spam, egg and Spam"
position = menu_item.find("Spam")

# print(f"\n6.1.2.1 Index position = {position}")

menu_item = "Spam, Spam, Spam, egg and Spam"
position = menu_item.find("ham")

# print(f"\n6.1.2.2 Index position = {position}")


# 6.1.3 str.index()
menu_item = "Spam, Spam, Spam, egg and Spam"
position = menu_item.index("egg and Spam")

# print(f"\n6.1.3.1 Index position = {position}")

# TODO UNCOMMENT (WARN: RAISES RUNTIME EXCEPTION)
# position = menu_item.index("ham")

# # print(f"\n6.1.3.2 Index position = {position}")


# 6.1.4 str.join()
items = ["Oatmeal", "Fruit", "Spam"]  # a list
menu_item = "".join(items)  # join to blank or empty string (not so good in this case)

# print(f"\n6.1.4.1 Menu item = {menu_item}")

menu_item = ", ".join(items)  # better

# print(f"\n6.1.4.2 Menu item = {menu_item}")


# 6.2 CHALLENGE 07

# Current menu
menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam
"""

healthy_choice = "Oatmeal"

# Multiline expression expressed across multiple lines
menu_v2 = None  # TODO Chain method calls

# print("\n6.2 menu_v2")
# pprint(menu_v2, width=125) # Pretty print

# assert menu_v2 == [
#     "egg and bacon",
#     "egg, toast and bacon",
#     "egg and spam",
#     "egg, bacon and spam",
#     "egg, bacon, toast and spam",
#     "spam, bacon, toast and spam",
#     "spam, egg, spam, spam, bacon and spam",
#     "spam, spam, oatmeal, egg and spam",
#     "spam, spam, oatmeal, spam, spam, oatmeal, baked beans, spam, spam, oatmeal and spam",
#     (
#         "lobster thermidor aux crevettes with a mornay sauce, garnished with truffle pâté, brandy"
#         " and a fried egg on top and spam"
#     ),
# ]


# 6.3 LIST METHODS

# 6.3.1 list.append() (in-place)

# TODO Uncomment
# menu_v2.append("red beans and rice") # modify in-place (no variable assignment)

# print("\n6.3.1 New menu item\n")
# pprint(menu_v2, width=125) # Pretty print


# 6.3.2 list.remove() (in-place)
# TODO Uncomment
# item = menu_v2[-2] # Lobster Thermidor
# menu_v2.remove(item)

# print("\n6.3.2 Lobster Thermidor removed\n")
# pprint(menu_v2, width=125) # Pretty print


# 6.3.3 list.extend() (in-place)
healthy_items = ["cereal, yogurt, and spam", "oatmeal, fruit plate, and spam"]
# TODO Uncomment
# menu_v2.extend(healthy_items)

# print("\n6.3.3 new menu extended\n")
# pprint(menu_v2, width=125) # Pretty print

# 6.3.4 list.index()

# TODO Uncomment
# index = menu_v2.index("egg, bacon and spam")

# print(f"\n6.3.4 Index postion = {index}")


# 6.3.5 list.insert() (in-place)
# TODO Uncomment
# menu_v2.insert(1, "belgian waffle, strawberries, and spam")

# print("\n6.3.5 Belgian waffle added to the menu\n")
# pprint(menu_v2, width=125) # Pretty print


# 6.3.6 list.sort() (in-place)
# TODO Uncomment
# menu_v2.sort()  # default alpha sort

# print("\n6.3.6 New menu sorted\n")
# pprint(menu_v2, width=125)  # Pretty print


# 6.4 CHALLENGE 08

menu_v3 = None  # TODO Slice

# print(f"\n6.4.1 Menu_v2 (id={id(menu_v2)}, len={len(menu_v3)})\n")
# pprint(menu_v2, width=125)

# print(f"\n6.4.2 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
# pprint(menu_v3, width=125)

# Eliminate "egg and spam" menu item

# TODO Call method in-place

# print(f"\n6.4.3 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
# pprint(menu_v3, width=125)

# TODO Call method in-place

# print(f"\n6.4.4 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
# pprint(menu_v3, width=125)


# 6.5 CHALLENGE 09

# Retrieve
idx = None  # Call method and return index value

# print(f"\n6.5.1 Index value = {idx}")

# Calculate length
length = None  # Call function

# print(f"\n6.5.2 menu_v3 len = {length}")

# Egg first dishes
# WARN: indexes are zero-based.
egg_first_dishes = None  # TODO Slice

# print("\n6.5.3 Egg first dishes\n")
# pprint(egg_first_dishes)

# assert egg_first_dishes == [
#     "egg, toast and bacon",
#     "egg, bacon, toast and spam",
#     "egg, bacon and spam",
#     "egg and bacon",
# ]


# 7.0 STRING FORMATTING

# Formatted string literal (f-string)
special_item = "egg, bacon, spam and sausage"
question = f"Why can't she have {special_item}?"

# print(f"\n7.1 f-string = {question}") # embedded variable

# str.format()s
question = "Could I have {}, {}, {} and {}, without the spam?".format(
    "egg", "bacon", "spam", "sausage"
)

# print(f"\n7.2 str.format() = {question}")

# 7.3 C-style or simple provisional formatting
question = "No, it wouldn't be %s, %s, %s and %s, would it?" % ("egg", "bacon", "spam", "sausage")

# print(f"\n7.3.1 C-style = {question}")

string = "%s %i %c" % ("Spam Sketch (", 1970, ")")

# print(f"\n7.3.2 C-style = {string}")
