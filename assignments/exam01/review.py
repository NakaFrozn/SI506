# SI 506

# Lines of code per challenge
challenges = [
    "CH01: 1",
    "CH02: 1",
    "CH03: 1",
    "CH04: 1",
    "CH05: 0",
    "CH06: 2",
    "CH07: 0",
    "CH08: 1",
    "CH09: 0",
    "CH10: 3",
    "CH11: 4",
    "CH12: 4",
    "CH13: 3",
    "CH14: 1",
    "CH15: 2",
    "CH16 BONUS: 5",
]

# 1.0 Total challenges
total_challenges = len(challenges)  # TODO ...

print(f"\n1.0 total challenges = {total_challenges}")

# 2.0 Access element by index
bonus = challenges[-1]  # TODO ...
char = challenges[-1][-1]

print(f"\n2.0 last element = {bonus}")

# 3.0 Convert string to list and access points
bonus_points = bonus.split(": ")  # TODO ...

print(f"\n3.0 bonus points = {bonus_points}")

# 4.0 Return new list comprising even challenges (CH02, CH04, ...) using slicing
even_challenges = challenges[1::2]  # TODO ...

print(f"\n4.0 even challenges = {even_challenges}")

# 5.0 Replace substrings (BONUS->(Bonus); CH->Challenge)

# TODO Implement loop
for i in range(len(challenges)):
    challenges[i] = challenges[i].replace("BONUS", "Bonus")
    challenges[i] = challenges[i].replace("CH", "Challenge ")

print(f"\n5.1 Challenges renamed (FAILS) = {challenges}")


# 6.0 code line count: regular challenges (non-bonus only)
line_count = 0

# TODO Implement loop
for challenge in challenges[:-1]:
    if "bonus" not in challenge.lower():
        line_count += int(challenge.split(": ")[1])
print(f"\n6.0 line count (regular challenges) = {line_count}")


# 7.0 Avg number of lines (non-bonus challenges)
avg_lines = line_count / len(challenges) - 1  # TODO ...

print(
    f"\n7.0 average number of code lines (non bonus) = {avg_lines:.2f}"
)  # 2 decimal places

# 8.0 Max code lines per challenge
max_lines = []
lines = 0  # TODO ...

for challenge in challenges[:-1]:
    line = int(challenge.split(": ")[1])
    if line > lines:
        max_lines.clear()
        max_lines.append(challenge)
        lines = line
    elif line == lines:
        max_lines.append(challenge)

print(f"\n8.0 max lines = {max_lines}")

# 9.0 Min code lines per challenge
min_lines = []
lines = 100 # TODO ...
for challenge in challenges[:-1]:
    line = int(challenge.split(": ")[1])
    if line < lines:
        min_lines.clear()
        min_lines.append(challenge)
        lines = line
    elif line == lines:
        min_lines.append(challenge)

# Implement loop

print(f"\n9.0 min lines = {min_lines}")


# 10.0 Between 1 and 4 lines (exclusive)
some_lines = []
for challenge in challenges[:-1]:
    line = int(challenge.split(": ")[1])
    if line >1 and line < 4:
        some_lines.append(challenge)
# Implement loop


print(f"\n10.0 between 1 and 4 lines = {some_lines}")
