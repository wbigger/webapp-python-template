import re
from Element import Element

java_file = open("input.txt")
keywords_file = open("keywords.txt")

java_input = []
for line in  java_file:
    checked_line = ""
    for letter in line:
        if re.search("[\{\}\[\]\,\=\(\)\;]", str(letter)):
            checked_line += " " + letter + " "
        else:
            checked_line += letter
    java_input += checked_line.split()

keywords = []
for line in  keywords_file:
    keywords += line.split()

elements = []

types = []
identificator = ""
for word in java_input:
    if word in keywords:
        types.append(word)
    elif word not in str(keywords) and len(types) > 0 and re.search("[A-Za-z]*", word):
        identificator = word
        elements.append(Element(identificator, types))
        types = []
        identificator = ""

def get_elements():
    return elements