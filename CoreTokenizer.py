import stanza
def ratio(paragraph):
    #creating a pipeline
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos')
    doc = nlp(paragraph)
    #counters for pronouns and nouns
    proCtr = 0.0
    nounCtr = 0.0
    #tags to tokenize with
    pronouns  = ['PRP', 'PRP$', 'WP', 'WP$']
    nouns = ['NN', 'NNS', 'NNP', 'NNPS']
    #accessing each sentence in pipeline
    doc_sentences = doc.sentences
    sent_word = None
    for sent in doc_sentences:
        #accessing each word in sentence
        sent_word = sent.words
        for word in sent_word:
            print(word.xpos)
            if word.xpos in pronouns:
                proCtr= proCtr + 1
            elif word.xpos in nouns:
                nounCtr = nounCtr + 1
    #checking for divide by zero error
    if nounCtr == 0:
        return -1
    return proCtr/nounCtr

#getting input sentences
paragraph = input("Enter sentences: ")
ratioSent = ratio(paragraph)
print(ratioSent)
