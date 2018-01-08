import spacy
nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
   print(ent.text, ent.start_char, ent.end_char, ent.label_)

###Output

#Apple 0 5 ORG
#U.K. 27 31 GPE
#$1 billion 44 54 MONEY

for token in doc:
   print(token.text)

###Output

#Apple
#is
#looking
#at
#buying
#U.K.
#startup
#for
#$
#1
#billion
