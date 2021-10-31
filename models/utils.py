import numpy as np
from pythainlp import word_tokenize

def tokenize(sentence):
    return word_tokenize(sentence, engine='deepcut')

def bag_of_words(tokenized_sentence, words):
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in tokenized_sentence: 
            bag[idx] = 1
    return bag