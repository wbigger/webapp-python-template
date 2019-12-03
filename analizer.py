import re

input = open("input.java")

informations = []

for line in input:
    if re.search("^import .*;$", line):
        informations.append(Data("undefined", ["import"]))
    elif re.search("[^//]int|float|String|char|static|public|private|protected .*;$", line):
        informations.append(Data("undefined", re.search("int|float|String|char|static|public|private|protected")))