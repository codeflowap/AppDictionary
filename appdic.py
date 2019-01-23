import json
from difflib import get_close_matches

entries = json.load(open("entries.json"))

def findEntry(word):
    word = correctEntry(word)  
    if word in entries:
        return entries[word]
    elif len(get_close_matches(word, entries.keys()))>0:
        ans = input("Did you mean %s instead? [Y/N]" % get_close_matches(word, entries.keys())[0])
        if ans == "Y" or "y":
            return entries[get_close_matches(word, entries.keys())[0]]
        else:
            return "Your entry doesn't exist."
    else:
        return "The word does not exist"

def correctEntry(word):
    """Keep the first letter as it is and lowercase the rest"""
    firstletter = word[0]
    wordlower = word[1:].lower()
    correctOriginalWord = firstletter + wordlower
    return correctOriginalWord

word = input("Enter a word: ")
print (findEntry(word))


