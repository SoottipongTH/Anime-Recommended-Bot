from pathlib import Path
import random
import json

import torch
import re

from models.model import NeuralNet
from models.utils import bag_of_words, tokenize
from data.data import find
from data.recommend import recommend

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

intent_path = Path('intents.json')

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)


FILE = "models/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()



bot_name = 'HIKARI'
def get_response(sentence):
    user_input = sentence
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    #softmax 
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                response = random.choice(intent['responses'])
                if re.match(r"^get", tag):
                    response = find(tag, response, user_input)
                    return response
                elif re.match(r"^rec",tag):
                    response = recommend(tag, response, user_input)
                    return response
                return response
    else: 
        fail = intents['error']['dontunderstand']
        print(fail)
        return random.choice(fail)
