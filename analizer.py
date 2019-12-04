import re
from Element import Element

input = open("input.java")

informations = [Element("undefined", ["import"])]

for line in input:
    if re.search("^import .*;$", line):
        informations.append(Element(re.search(" .*;$", line), ["import"]))

def get_elements():
    return informations