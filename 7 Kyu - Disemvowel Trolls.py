# 7 Kyu
# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the
# vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new
# string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become
# "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    string = string.replace("a","")
    string = string.replace("e","")
    string = string.replace("i","")
    string = string.replace("o","")
    string = string.replace("u","")
    string = string.replace("A","")
    string = string.replace("E","")
    string = string.replace("I","")
    string = string.replace("O","")
    string = string.replace("U","")
    print(string)
    return string
