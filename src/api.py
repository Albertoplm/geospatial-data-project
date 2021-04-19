from pymongo import MongoClient
from pymongo import GEOSPHERE
import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os
from functools import reduce
import operator

def getFromDict(diccionario,mapa):
    
    return reduce(operator.getitem,mapa,diccionario)

def request_four(query):
    
    load_dotenv()
    
    tok1 = os.getenv("tok1")
    tok2 = os.getenv("tok2")
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    
    parametros = {
    "client_id": tok1,
    "client_secret": tok2,
    "v": "20200323",
    #"ll": f"{madrid.get('coordinates')[0]},{madrid.get('coordinates')[1]}",
    'near': 'Madrid',
    "query": f'{query}', 
    "limit": 100    
    }
    
    resp = requests.get(url= url_query, params = parametros).json()
    
    return resp


def decode(resp):

    data = resp.get("response")
    decode = data.get("groups")[0]
    decode_otravez = decode.get("items")

    mapa_nombre =  ["venue", "name"]
    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]

    lovemosclaro = []
    for dic in decode_otravez:
        paralista = {}
        paralista["name"] = getFromDict(dic, mapa_nombre)
        paralista["latitud"]= getFromDict(dic, mapa_latitud)
        paralista["longitud"] = getFromDict(dic,mapa_longitud)
        lovemosclaro.append(paralista)

    return lovemosclaro

def typepoint(lovemosclaro):
    
    documentos = []
    for diccionario in lovemosclaro:
        temporal = {
            "name": diccionario.get("name"),
            "location": {"type": "Point", "coordinates": [diccionario.get("latitud"), diccionario.get("longitud")]}

        }
        documentos.append(temporal)
        
    df_point = pd.DataFrame(documentos)
    return df_point

def mindistance(df):
    
    vegan = []
    club = []
    competency = []
    kindergarten = []
    starbucks = []
    basketball = []
    hairdresser = []
    
    for i, row in df.iterrows():
        if row["tipo"] == "vegan":
            vegan.append(row.dist)
        elif row["tipo"] == 'club':
            club.append(row.dist)
        elif row["tipo"] == 'competency':
            competency.append(row.dist)
        elif row["tipo"] == 'kindergarten':
            kindergarten.append(row.dist)
        elif row["tipo"] == 'starbucks':
            starbucks.append(row.dist)
        elif row["tipo"] == 'basketball':
            basketball.append(row.dist)
        elif row["tipo"] == 'hairdresser':
            hairdresser.append(row.dist)
    
    if len(vegan) > 0:
        vegan = min(vegan)
    if len(club) > 0:
        club = min(club)
    if len(competency) > 0:
        competency = min(competency)
    if len(kindergarten) > 0:
        kindergarten = min(kindergarten)
    if len(starbucks) > 0:
        starbucks = min(starbucks)
    if len(basketball) > 0:
        basketball = min(basketball)
    if len(hairdresser) > 0:
        hairdresser = min(hairdresser)
    
    interesting_venues = []
    distancias = {
            "vegan": vegan,
            "club": club,
            "competency": competency,
            "kindergarten": kindergarten,
            "starbucks": starbucks,
            "basketball": basketball,
            "hairdresser": hairdresser,
        }
    interesting_venues.append(distancias)
        
    df_interesting_venues = pd.DataFrame(interesting_venues)
    
    return df_interesting_venues