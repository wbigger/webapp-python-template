import re

java_file = open("input.txt")
keywords_file = open("keywords.txt")

java = []
for line in  java_file:
    java += line.split()

keywords = []
for line in  keywords_file:
    keywords += line.split()

print(keywords)

informations = []


def get_elements():
    return informations