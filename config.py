# -*- coding: UTF-8 -*-

ppdbDict = {}
ppdbSim = 0.9
theta1 = 0.9


import nltk
from nltk.corpus import stopwords

from nltk import SnowballStemmer
stemmer = SnowballStemmer('english')

punctuations = [u'(',u'-lrb-',u'.',u',',u'-',u'?',u'!',u';',u'_',u':',u'{',u'}',u'[',u'/',u']',u'...',u'"',u'\'',u')', u'-rrb-', u'，', u'。', u'！', u'？', u'；', u'：']
# stopwords = stopwords.words('english')
stopwords = stopwords.words('english')

SENTENCES_INFO_URL= 'http://xx.xx.xx.xx./corpus-manager/sentence_new/info.show'
SENTENCES_INFO_SERVER= 'xx.xx.xx.xx'
