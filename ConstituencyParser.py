import json
import pandas as pd
import stanza
import CoreTokenizer as ct
from stanza.server import CoreNLPClient

f = open('dev-v2.0-own (1).json')
fw = open('temp1.txt', 'a')
fw.write('NP->DT NN Pairs/Tokens,Pronoun-Noun Ratio\n')
text = json.load(f)

#recursive function to parse tree
def reloop(temp, cnt):
    tempcntr = cnt
    #recurse until leaf node of tree is reached
    if len(temp.child) != 0:
        for children in temp.child:
            #check node and its children
            tempcntr = checker(children,tempcntr)
            #go deeper in tree once check is completed
            tempcntr = reloop(children, tempcntr)
    return tempcntr

#function that checks required constituent to count
def checker(parent, counter):
    if parent.value == 'NP':
        if len(parent.child) == 2:
            if parent.child[0].value == 'DT' and parent.child[1].value == 'NN':
                return counter + 1
    return counter

with CoreNLPClient(
        classpath = "C:/Users/udayr/ShoePicker/app/src/main/java/com/example/AusterweilLab/YOUR_CORENLP_FOLDER/*",
        annotators=['parse'],
        tokenize_no_ssplit=True,
        timeout=300000,
        memory='16G') as client:
        for index in text['data']:   
            #looping through each question in json file
            ann = client.annotate(index["question"])
            #counting pronoun/noun ratio
            ratioSent = ct.ratio(index["question"])
            #running algorithm to count constituent required
            root = ann.sentence[0].parseTree.child[0]
            cnt = 0
            cnt = checker(root, cnt) + reloop(root, cnt)
            #creating a pipeline for the question to tokenize it
            nlp = stanza.Pipeline(lang='en', processors='tokenize,pos')
            doc = nlp(index["question"])
            #writing result to a file
            fw.write(str(cnt/len(doc.sentences[0].tokens)) + ","+ str(ratioSent) +"\n")

#txt file from algorithm was converter to a csv file called out.csv
df = pd.read_csv("out.csv")
df.to_pickle("./out.pkl")
#closing files
f.close()
fw.close()