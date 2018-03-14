import sys
import gensim
import time
from gensim.models import KeyedVectors
import xml.etree.ElementTree as ET
import numpy as np
import codecs
import csv
import multiprocessing
from joblib import Parallel, delayed

# [1] -> model
# [2] -> reference_grammar
# [3] -> input_file
parameters = sys.argv

word2vec_model = parameters[1]
inputCsv = parameters[2]
grammar = parameters[3]
# dimension of features, the number of distances you want to keep
num_feats = 10
similarities = []

def read_grammar():
    tree = ET.parse(grammar)
    root = tree.getroot()
    dictionary = {get_prompt(unit): get_responses(unit) for unit in root.findall('prompt_unit')}
    return (dictionary, dictionary.keys())

def get_prompt(unit):
    prompt = unit.find('prompt').text
    return prompt

def get_responses(unit):
    return [response.text for response in unit.findall('response')]

def get_label(language, meaning): 
    #1 means correct language and correct meaning# 2 means incorrect language and correct meaning# 3 means incorrect language and incorrect meaning
    if language == 'correct':
        return 1
    elif meaning == 'correct':
        return 2
    else:
        return 3

def check_prompt(grammar_dic, known_prompts, num_feats):
    for prompt in known_prompts:
        if np.size(grammar_dic[prompt]) < num_feats:
            print(str(np.size(grammar_dic[prompt])) + prompt)
    return True

def get_sim(prompt, rec_result, grammar_dic, known_prompts, model):
    distances = []
    if prompt in known_prompts:
        valid_responses = grammar_dic[prompt]
        distances = [model.wmdistance(rec_result, response) for response in valid_responses]
    else:
        distances = [100,100,100,100,100,100,100,100,100,100]
        print("*** Error: prompt not in XML dictionary: '" + prompt + "'")
    return distances

# calculate the similarities
def calc_similarities(row):
    global grammar_dic, known_prompts, model

    x = np.array([]).reshape(0, num_feats)
    y = np.array([]).reshape(0, 1)
    
    if row:
        line = ''
        prompt = row[1]
        rec_result = row[3]
        language = row[4]
        meaning = row[5]
        distances = get_sim(prompt, rec_result, grammar_dic, known_prompts, model)
        if np.size(distances) < num_feats:
            distances = distances + [(min(distances) + max(distances)) / 2] * (num_feats - np.size(distances))
        distances = sorted(distances)[: num_feats]

        x = np.vstack((x, distances))
        y = np.vstack((y, (get_label(language, meaning))))

        line = row[0].replace('.wav', '') + ','
        i = 1
        for item in distances:
            if np.isinf(item):
                mean = sum(distances)/len(distances)
                if np.isinf(mean):
                    line += '100'
                else:
                    print(str(sum(distances)/len(distances)))
                    line += str(sum(distances)/len(distances))
            else:
                line += str(item)
            if i < len(distances):
                line += ','

            i += 1
        line += '\n'
    else:
        line = ""
        
    return line

# read referenceGrammar
print("Read XML grammar: " + grammar)
grammar_dic, known_prompts = read_grammar()
# load trained model
print("Read model: " + word2vec_model)
# model which is used for calculating the similarities
model = gensim.models.doc2vec.Doc2Vec.load(word2vec_model)
model.init_sims(replace = True)
print("Read model done!")

with open(inputCsv, 'r', encoding = "utf-8") as input_csv_file:
    reader = csv.reader(input_csv_file, delimiter = '\t', quotechar = '"')

    # parallelized generation of the vectors 
    #similarities.append(Parallel(n_jobs=20)(delayed(calc_similarities)(i) for i in input_lines))
    similarities.append(Parallel(n_jobs=20)(delayed(calc_similarities)(i) for i in reader))

with open("similarities.csv", 'w+') as similrities_file:
    # write the vectors in new file
    for entries in similarities:
        for entry in entries:
            similrities_file.write(entry)