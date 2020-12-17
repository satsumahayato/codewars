# CodeWars.com
# 7-kyu
# Testing 1-2-3
# December 16, 2020

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    length = len(lines) + 1
    new_list = []
    if lines == []:
        return []
    elif lines != []:
        for counter in range(1,length):
            letter_pos = counter - 1
            new_item = str(counter) + ': ' + lines[letter_pos]
            print(new_item)
            new_list.append(new_item)
        return new_list