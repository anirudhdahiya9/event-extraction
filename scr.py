import nltk
from nltk.corpus import wordnet as wn

events = []
f=open('data.txt')
sentences=f.readlines()
for sentence in sentences:
    sentence=sentence.strip('\n')
    tokens = nltk.word_tokenize(sentence)
    print tokens
    tagged = nltk.pos_tag(tokens)
    print tagged
    for i in tagged:
        print i[0]
        for syn in wn.synsets(i[0]):
            for path in syn.hypernym_paths():
                for bla in path:
                    if bla.name().startswith('act') or bla.name().startswith('event'):
                        events+=[i[0]]

    print events
