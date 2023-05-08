import spacy
nlp = spacy.load("en_core_web_sm")

with open("data/wiki-nlp.txt",'r') as file:
    text = file.read()

print(text)