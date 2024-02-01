# SI 506 Week 04

from pprint import pprint  # import statement


# 1.1 NESTED LISTS

# EV attributes: make_model, vehicle_type, drivetrain, fuel_economy_mpge,
# range_mi, battery_capacity_kwh, seats, base_msrp

ev_vehicles = [
    "Cadillac Lyric, SUV, RWD, 89, 312, 119, , $61,795",
    "Chevrolet Bolt EUV, Sedan/Wagon, FWD, 115, 247, 75, 5, $27,200",
    "Chevrolet Bolt EV, Sedan/Wagon, FWD, 120, 259, 75, 5, $25,600",
    "Ford F150 Lightning 4WD, Pickup, AWD, 66-70, 240-320, 165, 5, $55,974",
]

model = None  # TODO Split strings and access Cadillac Lyric

# print(f"\n1.1.1 Model = {model}")

ev_vehicles = [
    ["Cadillac Lyric", "SUV", "RWD", "89", "312", "119", "", "$61,795"],
    ["Chevrolet Bolt EUV", "Sedan/Wagon", "FWD", "115", "247", "75", "5", "$27,200"],
    ["Chevrolet Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["Ford F150 Lightning 4WD", "Pickup", "AWD", "66-70", "240-320", "165", "5", "$55,974"],
]

model = None  # TODO Access Cadillac Lyric

# print(f"\n1.1.2 Model = {model}")


# 1.2 FOR LOOP

# print("\n1.2.1 Print elements")

# TODO Implement loop

# print("\n1.2.2 Print elements")

# TODO Implement loop

# 1.3 IF STATEMENT

# print("\n1.3.1 Find Ford and print")
# for vehicle in ev_vehicles:
#     if vehicle[0].find("Ford") > -1:
#         print(vehicle)

# print("\n1.3.2 Get all Chevrolet vehicles and print")
# for vehicle in ev_vehicles:
#     if "chevrolet" in vehicle[0].lower():
#         print(vehicle)

# print("\n1.3.3 Exclude all Chevrolet vehicles and print")
# for vehicle in ev_vehicles:
#     if "chevrolet" not in vehicle[0].lower():
#         print(vehicle)


# 1.4 CHALLENGE 01

# Range values have been simplified to a single value.

# fmt: off
ev_vehicles = [
    ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    ["Tesla Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
    ["Porsche Taycan GTS Sport Turismo", "Sedan/Wagon", "AWD", "80", "233", "109", "4", "$86,700"],
    ["Kia Niro Electric", "Sedan/Wagon", "FWD", "113", "253", "64", "5", "$39,900"],
    ["Lucid Air G Touring XR AWD", "Sedan/Wagon", "AWD", "131", "516", "120", "5", "$87,400"],
    ["Toyota bZ4X AWD", "SUV", "AWD", "104", "228", "72", "5", "$44,080"],
    ["BMW i4 M50 Gran Coupe", "Sedan/Wagon", "AWD", "96", "271", "83", "5", "$67,300"],
    ["Tesla Model X", "SUV", "AWD", "102", "348", "104", "7", "$120,990"],
    ["Volkswagen ID.4 AWD Pro/Pro S", "SUV", "AWD", "99", "255", "81", "5", "$41,230"],
    ["Genesis Electrified G80", "Sedan/Wagon", "AWD", "97", "282", "87", "", "$79,825"],
    ["Porsche Taycan AWD", "Sedan/Wagon", "AWD", "83", "246", "109", "4", "$86,700"],
    ["Mini Cooper SE Hardtop 2 door", "Sedan/Wagon", "FWD", "110", "114", "32", "4", "$29,900"],
    ["Genesis GV60 Performance", "Sedan/Wagon", "AWD", "90", "235", "77", "", "$67,890"],
    ["Rivian R1S", "SUV", "AWD", "71", "321", "144", "7", "$78,000"],
    ["Tesla Model Y AWD", "SUV", "AWD", "123", "330", "84", "7", "$65,990"],
    ["Audi e-tron Sportback/S Sportback", "SUV", "AWD", "78", "225", "95", "5", "$69,100"],
    ["Rivian R1T", "Pickup", "AWD", "73", "328", "144", "5", "$73,000"],
    ["Tesla Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"],
    ["Toyota bZ4X", "SUV", "FWD", "119", "252", "71", "5", "$42,000"],
    ["Polestar Automotive USA Polestar 2", "Sedan/Wagon", "FWD", "107", "270", "77", "5", "$48,400"],
    ["Audi e-tron quattro/S", "SUV", "AWD", "79", "226", "95", "5", "$65,900"],
    ["BMW i7 xDrive60 Sedan", "Sedan/Wagon", "AWD", "89", "318", "105", "5", "$119,300"],
    ["BMW iX xDrive50", "SUV", "AWD", "86", "324", "76", "5", "$83,200"],
    ["Chevrolet Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["BMW iX M60", "SUV", "AWD", "78", "288", "111", "5", "$108,900"],
    ["Tesla Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],
]
# fmt: on

# print("\n1.4.1 Tesla EVs (membership in)")
# TODO Implement loop


# 2.0 ACCUMULATOR PATTERN

# teslas = []
# for vehicle in ev_vehicles[1:]:
#     if vehicle[0].lower().find("tesla") > -1:
#         teslas.append(vehicle)

# print(f"\n2.0 Teslas = {teslas}")

# 2.0.1 Max range (does not handle ties)
# ev_max_range = None
# max_range = 0
# for vehicle in ev_vehicles[1:]:
#     vehicle_range = int(vehicle[4])  # cast str to int
#     if vehicle_range > max_range:
#         ev_max_range = vehicle[0]  # automaker model
#         max_range = vehicle_range

# print(f"\n2.0.1 Max range ({max_range} mi) = {ev_max_range}")


# 2.1 CHALLENGE 02

ev_types = []
# TODO Implement loop
for vehicle in ev_vehicles[1:]:
    if vehicle[1] not in ev_types:
        ev_types.append(vehicle[1])

print(f"\n2.1 EV types = {ev_types}")


# 2.2 CHALLENGE 03

# fmt: off
ev_vehicles = [
    ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    ["Tesla Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
    ["Porsche Taycan GTS Sport Turismo", "Sedan/Wagon", "AWD", "80", "233", "109", "4", "$86,700"],
    ["Kia Niro Electric", "Sedan/Wagon", "FWD", "113", "253", "64", "5", "$39,900"],
    ["Lucid Air G Touring XR AWD", "Sedan/Wagon", "AWD", "131", "516", "120", "5", "$87,400"],
    ["Toyota bZ4X AWD", "SUV", "AWD", "104", "228", "72", "5", "$44,080"],
    ["BMW i4 M50 Gran Coupe", "Sedan/Wagon", "AWD", "96", "271", "83", "5", "$67,300"],
    ["Tesla Model X", "SUV", "AWD", "102", "348", "104", "7", "$120,990"],
    ["Volkswagen ID.4 AWD Pro/Pro S", "SUV", "AWD", "99", "255", "81", "5", "$41,230"],
    ["Genesis Electrified G80", "Sedan/Wagon", "AWD", "97", "282", "87", "", "$79,825"],
    ["Porsche Taycan AWD", "Sedan/Wagon", "AWD", "83", "246", "109", "4", "$86,700"],
    ["Mini Cooper SE Hardtop 2 door", "Sedan/Wagon", "FWD", "110", "114", "32", "4", "$29,900"],
    ["Genesis GV60 Performance", "Sedan/Wagon", "AWD", "90", "235", "77", "", "$67,890"],
    ["Rivian R1S", "SUV", "AWD", "71", "321", "144", "7", "$78,000"],
    ["Tesla Model Y AWD", "SUV", "AWD", "123", "330", "84", "7", "$65,990"],
    ["Audi e-tron Sportback/S Sportback", "SUV", "AWD", "78", "225", "95", "5", "$69,100"],
    ["Rivian R1T", "Pickup", "AWD", "73", "328", "144", "5", "$73,000"],
    ["Tesla Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"],
    ["Toyota bZ4X", "SUV", "FWD", "119", "252", "71", "5", "$42,000"],
    ["Polestar Automotive USA Polestar 2", "Sedan/Wagon", "FWD", "107", "270", "77", "5", "$48,400"],
    ["Audi e-tron quattro/S", "SUV", "AWD", "79", "226", "95", "5", "$65,900"],
    ["BMW i7 xDrive60 Sedan", "Sedan/Wagon", "AWD", "89", "318", "105", "5", "$119,300"],
    ["BMW iX xDrive50", "SUV", "AWD", "86", "324", "76", "5", "$83,200"],
    ["Chevrolet Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["BMW iX M60", "SUV", "AWD", "78", "288", "111", "5", "$108,900"],
    ["Tesla Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],
]
# fmt: on

ev_min_range = None
min_range = None  # TODO Assign seed value

# TODO Implement loop

# print(f"\n2.2 Shortest range ({min_range} mi) = {ev_min_range}")


# 2.3 ACCUMULATING COUNTS

bmw_count = 0
# TODO Implement loop

# print(f"\n2.3 BMW count = {bmw_count}")


# 2.4 CHALLENGE 04

vehicle_count = 0
# TODO Implement loop

# print(f"\n2.4 mpge >= 250 mi = {vehicle_count}")


# 3.0 LOOPING WITH RANGE()

# 3.1 range() behaviors

seq = range(10)

# print(f"\n3.1.1 seq (type={type(seq)}) = {seq}")  # <class 'range'>

seq = list(range(10))  # convert range object to a list

# print(f"\n3.1.2 range seq = {seq}")

seq = list(range(5, 10))

# print(f"\n3.1.3 range seq start/stop = {seq}")

seq = list(range(5, 21, 5))

# print(f"\n3.1.4 range seq start/stop/step = {seq}")

seq = list(range(20, 4, -5))

# print(f"\n3.1.5 range seq start/stop/step reversed = {seq}")


# 3.2 The `for` loop and `range`

# print(f"\n3.2 for loop with range()\n")

# TODO Implement loop

automakers = [
    "Bayerische Motoren Werke AG",
    "Ford Motor Co.",
    "General Motors Co.",
    "Kandi Technologies Group",
    "Nissan Motor Co.",
    "Volkswagen AG",
    "Volvo Group",
    "Tesla, Inc.",
]

# print(f"\n3.2 access automakers with range()")
# TODO Implement loop

# WARN: Replace immutable string value fails
for automaker in automakers:
    automaker = automaker.upper()  # assigns new string to loop variable only


# 3.3 Employing `range` to replace list elements

# print("\n3.3.1 automaker to uppercase (fail)")
# pprint(automakers)

# Replace immutable element value (success)

# TODO Implement loop

# print("\n3.3.2 automaker to uppercase")
# pprint(automakers)

# Modify every third element commencing from index 0

# TODO Uncomment
# for i in range(0, len(automakers), 3):
#     automakers[i] = automakers[i].lower()  # assigns new string elements at positions 0, 3, 6

# print(f"\n3.3.3 to lowercase (sequence = {list(range(0, len(automakers), 3))})")
# pprint(automakers)


# 3.4 Subscript notation chaining

# ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
# ["Tesla Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],

tesla_3_range = None  # TODO Access Tesla Model 3 AWD

# print(f"\n3.4.1 Tesla Model 3 range (mpg) = {tesla_3_range}")

# ["Tesla Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"]

tesla_s_range = 0
for i in range(len(ev_vehicles)):
    if ev_vehicles[i][0].lower() == "tesla model s":
        tesla_s_range = ev_vehicles[i][4]

# print(f"\n3.4.2 Tesla Model S range (mpg) = {tesla_s_range}")


# 3.5 CHALLENGE 05

# fmt: off
ev_vehicles = [
    ["model", "type", "drivetrain", "fuel_ec_mpge", "range_mi", "battery_kwh", "seats", "base_msrp"],
    ["Tesla Model 3 RWD", "Sedan/Wagon", "RWD", "132", "272", "60", "5", "$46,990"],
    ["Porsche Taycan GTS Sport Turismo", "Sedan/Wagon", "AWD", "80", "233", "109", "4", "$86,700"],
    ["Kia Niro Electric", "Sedan/Wagon", "FWD", "113", "253", "64", "5", "$39,900"],
    ["Lucid Air G Touring XR AWD", "Sedan/Wagon", "AWD", "131", "516", "120", "5", "$87,400"],
    ["Toyota bZ4X AWD", "SUV", "AWD", "104", "228", "72", "5", "$44,080"],
    ["BMW i4 M50 Gran Coupe", "Sedan/Wagon", "AWD", "96", "271", "83", "5", "$67,300"],
    ["Tesla Model X", "SUV", "AWD", "102", "348", "104", "7", "$120,990"],
    ["Volkswagen ID.4 AWD Pro/Pro S", "SUV", "AWD", "99", "255", "81", "5", "$41,230"],
    ["Genesis Electrified G80", "Sedan/Wagon", "AWD", "97", "282", "87", "", "$79,825"],
    ["Porsche Taycan AWD", "Sedan/Wagon", "AWD", "83", "246", "109", "4", "$86,700"],
    ["Mini Cooper SE Hardtop 2 door", "Sedan/Wagon", "FWD", "110", "114", "32", "4", "$29,900"],
    ["Genesis GV60 Performance", "Sedan/Wagon", "AWD", "90", "235", "77", "", "$67,890"],
    ["Rivian R1S", "SUV", "AWD", "71", "321", "144", "7", "$78,000"],
    ["Tesla Model Y AWD", "SUV", "AWD", "123", "330", "84", "7", "$65,990"],
    ["Audi e-tron Sportback/S Sportback", "SUV", "AWD", "78", "225", "95", "5", "$69,100"],
    ["Rivian R1T", "Pickup", "AWD", "73", "328", "144", "5", "$73,000"],
    ["Tesla Model S", "Sedan/Wagon", "AWD", "120", "405", "104", "5", "$104,990"],
    ["Toyota bZ4X", "SUV", "FWD", "119", "252", "71", "5", "$42,000"],
    ["Polestar Automotive USA Polestar 2", "Sedan/Wagon", "FWD", "107", "270", "77", "5", "$48,400"],
    ["Audi e-tron quattro/S", "SUV", "AWD", "79", "226", "95", "5", "$65,900"],
    ["BMW i7 xDrive60 Sedan", "Sedan/Wagon", "AWD", "89", "318", "105", "5", "$119,300"],
    ["BMW iX xDrive50", "SUV", "AWD", "86", "324", "76", "5", "$83,200"],
    ["Chevrolet Bolt EV", "Sedan/Wagon", "FWD", "120", "259", "75", "5", "$25,600"],
    ["BMW iX M60", "SUV", "AWD", "78", "288", "111", "5", "$108,900"],
    ["Tesla Model 3 AWD", "Sedan/Wagon", "AWD", "131", "358", "84", "5", "$46,990"],
]
# fmt: on

# TODO Implement loop

# print(f"\n3.5 ev_vehicles modified (last 5) = {ev_vehicles[-5:]}")


# 4.0 IF-ELSE

sedan_wagon = []
suv_pickup = []
for vehicle in ev_vehicles[1:]:
    string = f"{vehicle[0]} ({vehicle[1]})"

    # TODO Implement if-else


# print(f"\n4.0.1 Sedan/Wagon (n={len(sedan_wagon)})")
# pprint(sedan_wagon)

# print(f"\n4.0.2 SUV/Pickup (n={len(suv_pickup)})")
# pprint(suv_pickup)

standard_ranges = []
outlier_ranges = []
for vehicle in ev_vehicles[1:]:
    string = f"{vehicle[0]} (range = {vehicle[4]} mi)"

    # TODO Implement if-else

# print(f"\n4.0.3 Standard ranges (n={len(standard_ranges)})")
# pprint(standard_ranges)

# print(f"\n4.0.4 Outlier ranges (n={len(outlier_ranges)})")
# pprint(outlier_ranges)


# 4.1 Challenge 06

us_automakers = [
    "Cadillac",
    "Chevrolet",
    "Ford",
    "Lucid",
    "Polestar Automotive USA",
    "Rivian",
    "Tesla",
]

ev_vehicles = [
    ["model", "make", "type", "range_mi", "base_msrp"],
    ["Tesla", "Model 3 RWD", "Sedan/Wagon", "272", "$46,990"],
    ["Porsche", "Taycan GTS Sport Turismo", "Sedan/Wagon", "233", "$86,700"],
    ["Kia", "Niro Electric", "Sedan/Wagon", "253", "$39,900"],
    ["Lucid", "Air G Touring XR AWD", "131", "516", "$87,400"],
    ["Toyota", "bZ4X AWD", "SUV", "228", "$44,080"],
    ["BMW", "i4 M50 Gran Coupe", "Sedan/Wagon", "271", "$67,300"],
    ["Tesla", "Model X", "SUV", "348", "$120,990"],
    ["Volkswagen", " ID.4 AWD Pro/Pro S", "SUV", "255", "$41,230"],
    ["Genesis", "Electrified G80", "Sedan/Wagon", "282", "$79,825"],
    ["Porsche", "Taycan AWD", "Sedan/Wagon", "246", "$86,700"],
    ["Mini Cooper", "SE Hardtop 2 door", "Sedan/Wagon", "114", "$29,900"],
    ["Genesis", "GV60 Performance", "Sedan/Wagon", "235", "$67,890"],
    ["Rivian", "R1S", "SUV", "321", "$78,000"],
    ["Tesla", "Model Y AWD", "SUV", "330", "$65,990"],
    ["Audi", "e-tron Sportback/S Sportback", "SUV", "225", "$69,100"],
    ["Rivian", "R1T", "Pickup", "328", "$73,000"],
    ["Tesla", "Model S", "Sedan/Wagon", "405", "$104,990"],
    ["Toyota", "bZ4X", "SUV", "252", "$42,000"],
    ["Polestar Automotive USA", "Polestar 2", "Sedan/Wagon", "270", "$48,400"],
    ["Audi", "e-tron quattro/S", "SUV", "226", "$65,900"],
    ["BMW", "i7 xDrive60 Sedan", "Sedan/Wagon", "318", "$119,300"],
    ["BMW", "iX xDrive50", "SUV", "324", "$83,200"],
    ["Chevrolet", "Bolt EV", "Sedan/Wagon", "259", "$25,600"],
    ["BMW", "iX M60", "SUV", "288", "$108,900"],
    ["Tesla", "Model 3 AWD", "Sedan/Wagon", "358", "$46,990"],
]

domestic_count = 0
foreign_count = 0

# TODO Implement loop

# print(f"\n4.1 Domestic-designed EV count = {domestic_count}")
# print(f"\n4.1 Foreign-designed EV count = {foreign_count}")


# 4.2 Challenge 07

affordable = []
unaffordable = []

# TODO Implement loop

# Alphanumeric sort
affordable.sort()
unaffordable.sort()

# print(f"\n4.2 Affordable EVs (len={len(affordable)}) = {affordable}")
# print(f"\n4.2 Unaffordable EVs (len={len(unaffordable)}) = {unaffordable}")
