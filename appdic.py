import json
from difflib import get_close_matches
entries = json.load(open("entries.json"))

def findEntry(wordEntered):
    word = checkForDouble(wordEntered)
    if word in entries.keys():
        return entries[word]
    elif word[0].upper()+word[1:] in entries.keys():
        print("You have entered **",word,"** while it's correct form is **",word[0].upper()+word[1:],"**:")
        return entries[word[0].upper()+word[1:]]
    elif word[0].lower()+word[1:] in entries.keys():
        print("You have entered **",word,"** while it's correct form is **",word[0].lower()+word[1:],"**:")
        return entries[word[0].lower()+word[1:]]
    elif len(get_close_matches(word, entries.keys(), cutoff=0.7))>0:
        ans = input("Did you mean %s instead? [Y/N]" % get_close_matches(word, entries.keys())[0])
        if ans == "Y" or ans == "y":
            return entries[get_close_matches(word, entries.keys())[0]]
        else:
            return "Your entry doesn't exist."
    else:
        return "The word does not exist"


def checkForDouble(w):
    """ Checks if a word with both uppercase AND lowercase first letter has entries"""
    ww = correctEntry(w)
    wordFirstUpper = ww[0].upper()+ww[1:]
    wordFirstLower = ww[0].lower()+ww[1:]
    if wordFirstUpper in entries.keys() and wordFirstLower in entries.keys():
        print("We found two entries for **",ww,"** as",wordFirstUpper,"and",wordFirstLower)
        print("Which one do you mean?","[1] for",wordFirstUpper,"/ [2] for",wordFirstLower,":")
        answer = input()
        if int(answer) == 1:
            return wordFirstUpper
        else:
            return wordFirstLower
    else:
        return ww

    
def correctEntry(wrodIn):
    """Keep the first letter as it is and make the rest lowercase"""
    firstletter = wrodIn[0]
    wordlower = wrodIn[1:].lower()
    correctOriginalWord = firstletter + wordlower
    return correctOriginalWord


word = input("Enter a word: ")
print (findEntry(word))

    



