# This is a sample Python script.
from curses.ascii import isdigit


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
one_string = "one"
two_string = "two"
three_string = "three"
four_string = "four"
five_string = "five"
six_string = "six"
seven_string = "seven"
eight_string = "eight"
nine_string = "nine"
zero_string = "zero"

one_string_reversed = one_string[::-1]
two_string_reversed = two_string[::-1]
three_string_reversed = three_string[::-1]
four_string_reversed = four_string[::-1]
five_string_reversed = five_string[::-1]
six_string_reversed = six_string[::-1]
seven_string_reversed = seven_string[::-1]
eight_string_reversed = eight_string[::-1]
nine_string_reversed = nine_string[::-1]
zero_string_reversed = zero_string[::-1]


def get_numbers_line(line):
    first_number = 0
    last_number = 0
    reversed_line = line[::-1]
    for i in range(len(line)):
        if isdigit(line[i]):
            first_number = int(line[i])
            break
        elif line[i:i+3] == "one":
            first_number = 1
            break
        elif line[i:i+3] == "two":
            first_number = 2
            break
        elif line[i:i + 5] == "three":
            first_number = 3
            break
        elif line[i:i + 4] == "four":
            first_number = 4
            break
        elif line[i:i + 4] == "five":
            first_number = 5
            break
        elif line[i:i + 3] == "six":
            first_number = 6
            break
        elif line[i:i + 5] == "seven":
            first_number = 7
            break
        elif line[i:i + 5] == "eight":
            first_number = 8
            break
        elif line[i:i + 4] == "nine":
            first_number = 9
            break
        elif line[i:i + 4] == "zero":
            first_number = 0
            break
    for i in range(len(line)):
        if isdigit(reversed_line[i]):
            last_number = int(reversed_line[i])
            break
        elif reversed_line[i:i+3] == "one"[::-1]:
            last_number = 1
            break
        elif reversed_line[i:i+3] == "two"[::-1]:
            last_number = 2
            break
        elif reversed_line[i:i + 5] == "three"[::-1]:
            last_number = 3
            break
        elif reversed_line[i:i + 4] == "four"[::-1]:
            last_number = 4
            break
        elif reversed_line[i:i + 4] == "five"[::-1]:
            last_number = 5
            break
        elif reversed_line[i:i + 3] == "six"[::-1]:
            last_number = 6
            break
        elif reversed_line[i:i + 5] == "seven"[::-1]:
            last_number = 7
            break
        elif reversed_line[i:i + 5] == "eight"[::-1]:
            last_number = 8
            break
        elif reversed_line[i:i + 4] == "nine"[::-1]:
            last_number = 9
            break
        elif reversed_line[i:i + 4] == "zero"[::-1]:
            last_number = 0
            break
    return first_number * 10 + last_number
# Press the green button in the gutter to run the script.
total = 0
with open('C:\\Users\\fabok\Desktop\Coding Advent 2023\coding_advent_1st_star.txt') as f:
    lines = f.readlines()
    for line in lines:
        total += get_numbers_line(line)
print(total)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
