import json

entries = json.load(open("entries.json"))

def findEntry(word):
    return entries[word]

word = input("Enter a word: ")
print (findEntry(word))

