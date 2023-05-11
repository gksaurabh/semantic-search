from curses import raw
import spacy
import json
nlp = spacy.load("en_core_web_lg")


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

file = open("data/cie-air-default-rtdb-export.json", 'r')
raw_data = []
raw_data.append(file)


for element in raw_data:
    data = json.load(element)

researchInterests = {}
for item in data:
    for interest in item["research"].values():
        researchInterests.update({item["name"]: interest})

print(len(researchInterests))
for val in researchInterests.values():
    
    if(type(val) == list):
        print(get_keys_from_value(researchInterests,val)[0])
        del researchInterests[get_keys_from_value(researchInterests,val)[0]]
        
print(len(researchInterests))


