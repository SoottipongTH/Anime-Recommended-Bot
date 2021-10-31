import re
import pickle
from pathlib import Path
from sre_constants import AT_UNI_BOUNDARY
from mal import Anime
from matplotlib.pyplot import text
import pandas as pd
from mal import config

config.MAL_ENDPOINT = "https://myanimelist.net/"
config.TIMEOUT = 1
# from data.data import get_info,get_name

anime_path = Path("data/anime_final.pickle")

with open(anime_path, "rb") as f:
    df = pickle.load(f)

def random():
    anime_id = df.sample(1)
    i = 1
    text = ""
    for id in anime_id["MAL_ID"]:
        text += str(i) + ". " + Anime(id).title + "\n"
        i += 1 
    return text

def ranked():
    i = 1
    text = ""
    for id in df[df["Score"].astype('float') > 9.0 ].sort_values(by='Score')["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "อันดับ: " + str(Anime(id).rank) + "\n" 
        i += 1
    return text

def studio(user_input):
    studio_name = re.findall(r"[A-Za-z]+", user_input)[0]
    all_stu = ""
    all_stu += "".join(i for i in studio_name)
    i = 1
    text = ""
    studios = ""
    for id in df[df["Studios"].str.lower().str.contains(all_stu.lower())]["MAL_ID"].sample(1):
        studios += ','.join(i for i in Anime(id).studios)
        text += str(i) + ". " + Anime(id).title + "\n" + "สตูดิโอที่สร้าง: " + studios + "\n"
        i += 1
    return text


def genre(user_input):
    _input = re.findall(r"[A-Za-z]+", user_input)[0]
    genre = ""
    genre += "".join(i for i in _input)
    i = 1
    text = ""
    gens = ""
    for id in df[df["Genres"].str.lower().str.contains(genre.lower())]["MAL_ID"].sample(1):
        gens += ','.join(i for i in Anime(id).genres)
        text += str(i) + ". " + Anime(id).title + "\n" + "ประเภท: " + gens + "\n"
        i += 1
    return text

def year(user_input):
    year = str(re.findall(r"\d\d\d\d", user_input)[0])
    i = 1
    text = ""
    for id in df[df["Aired"].str.contains(year)].sort_values(by="Aired")["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "ออกอากาศ: " + Anime(id).aired + "\n"
        i += 1
    return text



def fall():
    season = "Fall"
    i = 1
    text = ""
    for id in df[df["Premiered"].str.contains(season)]["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "ฤดูที่ฉาย: " + Anime(id).premiered + "\n"
        i += 1
    return text

def summer():
    season = "Summer"
    i = 1
    text = ""
    for id in df[df["Premiered"].str.contains(season)]["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "ฤดูที่ฉาย: " + Anime(id).premiered + "\n"
        i += 1
    return text

def spring():
    season = "Spring"
    i = 1
    text = ""
    for id in df[df["Premiered"].str.contains(season)]["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "ฤดูที่ฉาย: " + Anime(id).premiered + "\n"
        i += 1
    return text

def winter():
    season = "Winter"
    i = 1
    text = ""
    for id in df[df["Premiered"].str.contains(season)]["MAL_ID"].sample(1):
        text += str(i) + ". " + Anime(id).title + "\n" + "ฤดูที่ฉาย: " + Anime(id).premiered + "\n"
        i += 1
    return text

def based_on_manga():
    i = 1
    text = ""
    for id in df[df["Source"] == "Manga"]["MAL_ID"].sample(1):
        text += str(i) + ". "+ Anime(id).title + "\n" + "อ้างอิงจาก: " + Anime(id).source + "\n"
        i += 1
    return text

def based_on_light_novel():
    i = 1
    text = ""
    for id in df[df["Source"] == "Light novel"]["MAL_ID"].sample(1):
        text += str(i) + ". "+ Anime(id).title + "\n" + "อ้างอิงจาก: " + Anime(id).source + "\n"
        i += 1
    return text



def based_on_visual_novel():
    i = 1
    text = ""
    for id in df[df["Source"] == "Visual novel"]["MAL_ID"].sample(1):
        text += str(i) + ". "+ Anime(id).title + "\n" + "อ้างอิงจาก: " + Anime(id).source + "\n"
        i += 1
    return text


def recommend(tag, response, inp):
    no_argm = {
        "rec_random": random,
        "rec_fall": fall,
        "rec_winter": winter,
        "rec_summer": summer,
        "rec_spring": spring,
        "rec_ranked": ranked,
        "rec_based_on_manga": based_on_manga,
        "rec_based_on_visual_novel": based_on_visual_novel,
        "rec_based_on_light_novel": based_on_light_novel
               }
    have_argm = {
        "rec_genre": genre,
        "rec_studio": studio,
        "rec_year": year, }
    if tag in no_argm:
        return response + "\n" + no_argm[tag]()

    txt = have_argm[tag](inp)
    return (response + "\n" + txt)

