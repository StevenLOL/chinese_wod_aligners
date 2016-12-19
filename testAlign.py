# -*- coding: UTF-8 -*-
from aligner import *
import coreNlpUtil
import gensim
import wordSim
# import nltk
#
# nltk.download()

# aligning strings (output indexes start at 1)
# sentence1 = "Four men died in an accident."
# sentence2 = "4 people are dead from a collision."
sentence1 = u"他于乡里无恶不作，穷凶极恶，这次慈善捐款不过是作秀"
sentence2 = u"他平日里在乡里作威作福，十恶不赦，如今搞慈善，弄捐款，这是做秀"

fname='/home/steven/douban_lenovo_skip_word_cwe3.space'

global w2v

#w2v=gensim.models.Word2Vec.load_word2vec_format(fname)
#wordSim.w2v=w2v





# nlp = coreNlpUtil.StanfordNLP()
# print nlp.parse(u'你好，你叫什么名字？')

alignments,al2,tk1,tk2 = align(sentence1, sentence2)

alength=0
for al in al2:
    print al[0],al[1]
    alength+=len(al[0])+len(al[1])

for s in tk1:
    print s[2]

for s in tk2:
    print s[2]


print len(alignments)*2.0/(len(tk1)+len(tk2))

print alength*1.0/(len(sentence1)+len(sentence2))

# print alignments[0]
# print alignments[1]


# # aligning sets of tokens (output indexes start at 1)
# sentence1 = ['Four', 'men', 'died', 'in', 'an', 'accident', '.']
# sentence2 = ['4', 'people', 'are', 'dead', 'from', 'a', 'collision', '.']
#
# alignments = align(sentence1, sentence2)
#
# print alignments[0]
# print alignments[1]

