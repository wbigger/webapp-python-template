keywords_file = open("information/keywords.txt")
data_types_file = open("information/data_types.txt")
access_modifiers_file = open("information/access_modifiers.txt")

keywords = []
for line in  keywords_file:
    keywords += line.split()

data_types = []
for line in  data_types_file:
    data_types += line.split()

access_modifiers = []
for line in  access_modifiers_file:
    access_modifiers += line.split()

special_characters = ["{", "}", "[", "]", "(", ")", ";", "=", ",", "*", "\\", "/"]