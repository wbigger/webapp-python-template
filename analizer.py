import re
from Element import Element

input = open("input.java")

informations = [Element("undefined", ["import"])]

# for line in input:
#     if re.search("^import .*;$", line):
#         informations.append(Element("undefined", ["import"]))
#     elif re.search("[^//]int|float|String|char|static|public|private|protected .*;$", line):
#         informations.append(Element("undefined", re.search("int|float|String|char|static|public|private|protected", line)))