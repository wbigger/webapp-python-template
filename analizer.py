import re
from Element import Element

input = open("input.java")

informations = [Element("undefined", ["import"])]

for line in input:
    if re.search("^import .*;$", line) != None:
        informations.append(Element(str(re.findall(" .*;$", line)[0]), ["import"]))
    if re.search("public .*;$", line):
        informations.append(Element(str(re.findall("c .*;$", line)[0]), ["public"]))
    if re.search("private .*;$", line):
        informations.append(Element(str(re.findall("e .*;$", line)[0]), ["private"]))

def get_elements():
    return informations