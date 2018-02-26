import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        ex = input("Did you mean %s instead? Enter Y if yes or N for no:" % get_close_matches(word,data.keys())[0])
        if ex == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ex == "N":
            return "Word not understand"
        else:
            return "Inelegible"
    else:
        return "word does'nt exists."

word =input("Enter word:")
output=(translate(word))

if type(output) ==list:
    for items in output:
        print(items)
else:
    print(output)        
