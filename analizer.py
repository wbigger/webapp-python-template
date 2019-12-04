import re
from Element import Element

input = open("input.java")

informations = [Element("undefined", ["import"])]

for line in input:
    if re.search("^import .*;$", line):
        print(str(re.findall(" .*;$", line)[0]))
        informations.append(Element(str(re.findall(" .*;$", line)[0]), ["import"]))

def get_elements():
    return informations