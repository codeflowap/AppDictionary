import json
from difflib import get_close_matches

entries = json.load(open("entries.json"))

def findEntry(wordEntered):
    word = correctEntry(wordEntered)
    if word in entries:
        return entries[word]
    elif word[0].upper()+word[1:] in entries:
        print("You have entered **",word,"** while it's correct form is **",word[0].upper()+word[1:],"**:")
        return entries[word[0].upper()+word[1:]]
    elif len(get_close_matches(word, entries.keys()))>0:
        ans = input("Did you mean %s instead? [Y/N]" % get_close_matches(word, entries.keys())[0])
        if ans == "Y" or "y":
            return entries[get_close_matches(word, entries.keys())[0]]
        else:
            return "Your entry doesn't exist."
    else:
        return "The word does not exist"

def correctEntry(word):
    """Keep the first letter as it is and make the rest lowercase"""
    firstletter = word[0]
    wordlower = word[1:].lower()
    correctOriginalWord = firstletter + wordlower
    return correctOriginalWord

def checkForDouble(word):
    """ Checks if a word with both uppercase AND lowercase first letter has entries"""
    word = correctEntry(word)
    wordFirstUpper = word[0].upper()+word[1:]
    wordFirstLower = word[0].lower()+word[1:]
    if wordFirstUpper and wordFirstLower in entries:
        print("We found two entries for **",word,"** as",wordFirstUpper,"and",wordFirstLower)
        print("Which one do you mean?","[1] for",wordFirstUpper,"/ [2] for",wordFirstLower,":")
        answer = input()
        if int(answer) == 1:
            return wordFirstUpper
        else:
            return wordFirstLower
    

word = input("Enter a word: ")


    
    
print (findEntry(word))


