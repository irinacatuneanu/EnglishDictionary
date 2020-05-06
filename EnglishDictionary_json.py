import json
import difflib                          #for comparing texts
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))
print(type(data))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N':
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "word does not exist. Please, double check it."
output = translate(input("Enter word: "))
if type(output) == list:
    for answer in output:
        print (answer)
else:
    print(output)
#print(SequenceMatcher(None,"rainn","rain").ratio())        #ratio indicating similarity between strings
