#Import all the dependencies
import gensim
import sys

with open(sys.argv[1]) as dataFile:
    sentences = dataFile.readline()
    model = gensim.models.Word2Vec(sentences , min_count=0, workers=10 , size=200)
    model.save('word2vec.model')
    print ('model saved.')
