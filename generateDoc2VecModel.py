#Import all the dependencies
import gensim
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import sys
from gensim.models.deprecated.doc2vec import LabeledSentence

class LabeledLineSentence(object):

    def __init__(self, doc_list, labels_list):

        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):

        for idx, doc in enumerate(self.doc_list):
              yield gensim.models.deprecated.doc2vec.LabeledSentence(doc,[self.labels_list[idx]])

path = sys.argv[1]
tokenizer = RegexpTokenizer(r'\w+')
stopword_set = set(stopwords.words('english'))

def nlp_clean(data):

   new_data = []
   for d in data:
      new_str = d.lower()
      dlist = tokenizer.tokenize(new_str)
     # dlist = list(set(dlist).difference(stopword_set))
      new_data.append(dlist)
   return new_data


#now create a list that contains the name of all the text file in your data #folder
docLabels = []
docLabels = [f for f in listdir(path) if f.endswith('.txt')]

#create a list data that stores the content of all text files in order of their names in docLabels
data = []
for doc in docLabels:
  data.append(open(path + doc).read())

data = nlp_clean(data)

#iterator returned over all documents
it = LabeledLineSentence(data, docLabels)

model = gensim.models.Doc2Vec(vector_size=300, min_count=0, alpha=0.025, min_alpha=0.025)
model.build_vocab(it)

#training of model
for epoch in range(100):
 print('iteration ' +str(epoch+1))
 model.train(it, total_examples=model.corpus_count, epochs=100)
 model.alpha -= 0.002
 model.min_alpha = model.alpha

#saving the created model
model.save('doc2vec.model')
print('model saved')