import re
from Element import Element
from keywords import keywords, data_types, access_modifiers, special_characters

input_file = open("input.txt")

input = ""
for line in input_file:
    for letter in line:
        if letter in special_characters:
            input += " "
        else:
            input += letter

elements = []
identifier = ""
data_type = ""
access_modifier = ""
keyword = ""

words = input.split()
for word in words:
    if word in access_modifiers and access_modifier == "":
        access_modifier = word
    elif word in data_types and data_type == "":
        data_type = word
    elif word in keywords and keyword == "":
        keyword = word
    elif not(data_type == "" and keyword == ""):
        identifier = word
        elements.append(Element(identifier,data_type, access_modifier, keyword))
        identifier = ""
        data_type = ""
        access_modifier = ""
        keyword = ""