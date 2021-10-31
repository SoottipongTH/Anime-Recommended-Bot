# Pytorch-Anime-Bot
Pytorch - Chatbot using NLP 
Creating a chatbot using Pytorch model based on Natural Language Processing and apply Thai language by using Pythainlp
## The Data Set
https://www.kaggle.com/hernan4444/anime-recommendation-database-2020?select=anime.csv
## Toolkits
PythaiNLP, Pandas, Json, Random, Pathlib, Matplotlib, Re, MyAnimeList API, torch
## Intents
    tag : a unique name
    patterns: sentence patterns for neural network text classifier
    responses: output text to user
```
"intents": [{
        "tag": "greeting",
        "patterns": ["ดี", "ไง","สวัสดี", "หวัดดี", "สวัสดีครับ", "สวัสดีค่ะ", "ว่าไง"],
        "responses": ["สวัสดี!!! ", "หวัดดีจ้า !!! ", "ส ~ ~ "]
      }]
```
## Model and Training
Pytorch Model using Neural Network training on 500 epoch with final loss around ~ 0.0001 
## How to use on local
1. Create training data by running train.py
    ```
    python .\models\train.py
    ```
2. Run App.py to type on GUI by running App.py
    ```
    python .\app.py
    ```