from os import error
import pickle
from pathlib import Path
import re
from mal import Anime
from mal import config
import random
import json

config.MAL_ENDPOINT = "https://myanimelist.net/"
config.TIMEOUT = 5

anime_path = Path("data/anime_final.pickle")

with open(anime_path, "rb") as f:
    df = pickle.load(f)

with open('intents.json', 'r', encoding='utf-8') as f:
    fail = json.load(f)

def find_genres(id):
    gens = ""
    gens += ",".join(i for i in Anime(id).genres)
    if gens == "":
        gens = "ไม่ทราบ"
    return gens

def get_info(id):
    info = ""
    name = Anime(id).title
    genre = find_genres(id)
    link = Anime(id).url
    info = "\n" + "ชื่อ: " + name +  "\n" + "ประเภท: " + genre + "\n" + "ข้อมูลเพิ่มเติมดูใน Link " + link
    return info


def find_id(user_input):
    names = re.findall(r"[A-Za-z!\.\#:&'/,\*-?%+\(\)\_]+", user_input)
    names = "".join([i for i in names])
    series = df[df["Name"].str.lower().str.replace(' ','').str.contains(names.lower())]["MAL_ID"].head(1)
    if str(series) == "Series([], Name: MAL_ID, dtype: int64)":
        return 0
    return int(series)

def find(tag , responses , user_input):
    dict = {"get_info": get_info
    }
    id = find_id(user_input)
    if id == 0:
        responses = fail['error']["nodata"]
        response = random.choice(responses)
        return response

    txt = (responses + dict[tag](id))
    return txt

# print(find("get_info",":","ขอข้อมูล narutood"))