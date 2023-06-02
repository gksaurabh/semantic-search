from curses import raw
import spacy
import json
from collections import OrderedDict
import numpy as np

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




# print((researchInterests))
for key,val in researchInterests.items():
    researchInterests[key] = nlp(val)
    

query = input("what would you like to search for?\n")

query_doc = nlp(query)
i = 0


print(researchInterests)
matchesFound = {}
for val in researchInterests.values():
    
    if(val.vector_norm):
        simalrityRating = query_doc.similarity(val)
        # print(i,": ",type(simalrityRating), type(val))
        if(simalrityRating >= 0.50):
            key = get_keys_from_value(researchInterests, val)[0]
            matchesFound.update({key: simalrityRating})
            # print(key," ", simalrityRating, " ")
    i += 1

unsortedKeys = list(matchesFound.keys())
unsortedValues = list(matchesFound.values())
sorted_value_index = np.argsort(unsortedValues)
sortedMatches = {unsortedKeys[i]: unsortedValues[i] for i in sorted_value_index}
res = dict(reversed(list(sortedMatches.items())[5:]))
print(res)