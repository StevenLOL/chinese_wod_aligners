# -*- coding: UTF-8 -*-
from config import *
import codecs
from scipy import linalg, mat, dot
import numpy as np


w2v=None


################################################################################
def loadPPDB(ppdbFileName = 'Resources/ppdb-1.0-xxxl-lexical.extended.synonyms.uniquepairs'):

    global ppdbSim
    global ppdbDict

    count = 0

    ppdbFile = codecs.open(ppdbFileName,encoding='utf-8').readlines()
    ppdbFile=[s.strip() for s in ppdbFile]

    for line in ppdbFile:
        if not line.count(u'\t')==1:continue
        tokens = line.split(u'\t')
        tokens[1] = tokens[1].strip()
        ppdbDict[(tokens[0], tokens[1])] = ppdbSim
        count += 1

################################################################################

def consine_similarity(v1,v2):

    return dot(v1,v2.T)/np.linalg.norm(v1)/np.linalg.norm(v2)

################################################################################

def presentInPPDB(word1, word2):

    global ppdbDict
    #global w2v
    #TODO:
    #1) dict
    #2) word2vec
    #if cos > 0.8 return true
    if (word1.lower(), word2.lower()) in ppdbDict:
        return True
    if (word2.lower(), word1.lower()) in ppdbDict:
        return True


    
################################################################################


def canoicalWord(iWord):
    if len(iWord) > 1:
        canonicalWord1 = iWord.replace('.', '')
        canonicalWord1 = canonicalWord1.replace('-', '')
        canonicalWord1 = canonicalWord1.replace(',', '')
    else:
        canonicalWord1 = iWord
    return canonicalWord1

##############################################################################################################################

index=0
tdict={}
def wordRelatedness2(word1, pos1, word2, pos2):
    #using word2vec

    global stemmer
    global ppdbSim
    global punctuations
    global index


    canonicalWord1 = canoicalWord(word1)
    canonicalWord2 = canoicalWord(word2)
    
    
    if canonicalWord1.lower() == canonicalWord2.lower():
        return 1

    if stemmer.stem(word1).lower() == stemmer.stem(word2).lower():
        return 1

    if canonicalWord1.isdigit() and canonicalWord2.isdigit() and canonicalWord1 <> canonicalWord2:
        return 0

    if pos1.lower() == 'cd' and pos2.lower() == 'cd' and (not canonicalWord1.isdigit() and not canonicalWord2.isdigit()) and canonicalWord1 <> canonicalWord2:
        return 0

    # stopwords can be similar to only stopwords
    if (word1.lower() in stopwords and word2.lower() not in stopwords) or (word1.lower() not in stopwords and word2.lower() in stopwords):
        return 0

    # punctuations can only be either identical or totally dissimilar
    if word1 in punctuations or word2 in punctuations:
        return 0

    if presentInPPDB(word1.lower(), word2.lower()):
        return ppdbSim
    else:
        print index,word1, pos1, word2, pos2
        index+=1
        return 0
##############################################################################################################################

loadPPDB()

