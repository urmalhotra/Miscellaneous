import nltk
def ratio(sentence):
    tokenSent = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenSent)
    #counters for pronouns and nouns
    proCtr = 0.0
    nounCtr = 0.0
    #tags to tokenize with
    print(tagged)
    pronouns  = ['PRP', 'PRP$', 'WP', 'WP$']
    nouns = ['NN', 'NNS', 'NNP', 'NNPS']
    #checking for tags
    for val in tagged:
        if val[1] in pronouns:
            proCtr = proCtr + 1
        elif val[1] in nouns:
            nounCtr = nounCtr + 1
    #checking for divide by zero error
    if nounCtr == 0:
        return -1
    return proCtr/nounCtr
#getting input sentences
sentence = input("Enter sentences: ")
ratioSent = ratio(sentence)
print(ratioSent)


