####
# Reads reference grammar and training data to generate a file with valid pos sentences
#
#
# IMPORTANT
#
# This script is written bad
# Your output will contain noise in the beginning
#####
import csv
import re
import os
import collections
import sys
import xml.etree.ElementTree as ET
import nltk
from nltk import word_tokenize

test_utterances_csv = "scst1_testData_textTask.csv"
utterances_csv = "sc2abc_sc1.csv"
reference_grammar = "referenceGrammar_v3.0.0.xml"
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def read_grammar(reference_grammar):
    tree = ET.parse(reference_grammar)
    root = tree.getroot()
    dictionary = { get_prompt(unit): get_responses(unit) for unit in root.findall('prompt_unit') }
    return ( dictionary, dictionary.keys() )

def get_prompt(unit):
    prompt = unit.find('prompt').text
    return prompt

def get_responses(unit):
    return [ response.text for response in unit.findall('response') ]


# ---------------------------------------------------


def read_and_process_spreadsheet(input_csv, transcription_row, correctness_row):
    tokenized_all = set()

    with open(input_csv, 'r', encoding="utf-8") as csv_infile:
        reader = csv.reader(csv_infile, delimiter='\t', quotechar='"')
        for row in reader:
            # Skip header row
            if ( not is_header_row(row) ):
                process_spreadsheet_row(row, tokenized_all, transcription_row, correctness_row)

    return tokenized_all

def is_header_row(row):
    return ( row[0] == 'Id' )


def process_spreadsheet_row(row, tokenized_all, transcription_row, correctness_row):
    #"Id"   "Prompt"    "Wavfile"   "RecResult" "Transcription" "language"  "meaning"   "Trace"
    transcription = row[transcription_row]
    language_correct_gold_standard = row[correctness_row]

    if language_correct_gold_standard:
        tokenized_all.add(clean_and_tokenize(transcription))
   

def clean_and_tokenize(transcription):
    tuples = nltk.pos_tag(word_tokenize(clean_kaldi_tags(transcription)))
    if not tuples: return ""
    
    words, tags = zip(*tuples)
    return " ".join(tags)

def clean_kaldi_tags(rec_result):
    words = rec_result.split(" ")
    sentence = []
    for word in words:
        word = re.sub(r"([A-Za-zöäüÖÄÜ]+[*][v])", "", word)
        word = re.sub(r"([A-Za-zöäüÖÄÜ]+[*][a])", "", word)
        word = re.sub(r"([A-Za-zöäüÖÄÜ]+[*][x])", "", word)
        word = re.sub(r"([*][z])", "", word)
        word = re.sub(r"-xxx-", "", word)
        word = re.sub(r"-xxx", "", word)
        word = re.sub(r"xxx", "", word)
        word = re.sub(r"ggg", "", word)
        word = re.sub(r"ah", "" ,word)
        if word:
            sentence.append(word)
    return " ".join(sentence)


# ---------------------------------------------------


def create_tokenized_grammar(reference_grammar, grammar_dic, known_prompts):
    tokenized_all = set()

    for prompt in known_prompts:
        for response in grammar_dic[prompt]:
            words, tags = zip(*nltk.pos_tag(word_tokenize(response)))
            tokenized_all.add(" ".join(tags))
    return tokenized_all

def do_all_processing():
    ( grammar_dic, known_prompts ) = read_grammar(reference_grammar)
    tokenized_all = create_tokenized_grammar(reference_grammar, grammar_dic, known_prompts)
    tokenized_all.update(read_and_process_spreadsheet(utterances_csv, 4, 5))
    tokenized_all.update(read_and_process_spreadsheet(test_utterances_csv, 3, 4))

    for sentence in tokenized_all:
        print(sentence)
    
do_all_processing()
