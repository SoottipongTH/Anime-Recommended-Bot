from pathlib import Path
import pickle
import pandas as pd
import re
from mal import Anime
from mal import config
from mal import AnimeSearch, AnimeSearchResult

from data.recommend import based_on_visual_novel

config.MAL_ENDPOINT = "https://myanimelist.net/"
config.TIMEOUT = 1
anime_path = Path("data/anime_final.pickle")

with open(anime_path, "rb") as f:
    df = pickle.load(f)

# def genre(user_input):
#     _input = re.findall(r"[A-Za-z]+", user_input)[0]
#     genre = ""
#     genre += "".join(i for i in _input)
#     i = 1
#     text = ""
#     gens = ""
#     for id in df[df["Genres"].str.contains(genre)]["MAL_ID"].sample(1):
#         gens += ','.join(i for i in Anime(id).genres)
#         text += str(i) + ". " + Anime(id).title + "\n" + "Genres: " + gens + "\n"
#         i += 1
#     return text

# def fall():
#     season = "Fall"
#     i = 1
#     text = ""
#     for id in df[df["Premiered"].str.contains(season)]["MAL_ID"].sample(1):
#         text += str(i) + ". " + Anime(id).title + "\n" + "ฤดูที่ฉาย: " + Anime(id).premiered + "\n"
#         i += 1
#     return text



result = AnimeSearchResult("Kimi")
print(result)
# Kimi no na wa 32281