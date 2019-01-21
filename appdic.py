import json

entries = json.load(open("entries.json"))

def findEntry(word):
    word = word.lower()
    if word in entries:
        return entries[word]
    else:
        return "The word does not exist"

word = input("Enter a word: ")
print (findEntry(word))

